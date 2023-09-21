import inspect
import math
from collections import defaultdict, namedtuple

from . import util
from .morphemes import AnkiDeck
from .preferences import get_preference as cfg
from .util import mw

COL_YOUNG = "#7c7"
COL_CARD = "#282"
COL_K = "#4a4"
COL_V = "#7c7"
DEFAULT_COLOR = "#2F2"

_NUM_GRAPHS = 0

# an individual review of a card with a bucket_index representing the time period the review
# occurred in (e.g. which day, month, etc.)
CardReview = namedtuple(
    "CardReview",
    ["id", "nid", "did", "bucket_index", "cid", "ease", "ivl", "lastIvl", "type"],
)

# all the reviews for a particular card and length of time (e.g. day, week, etc.)
CardReviewsForBucket = namedtuple(
    "CardReviewsForBucket", ["bucket_index", "cid", "reviews"]
)

CardIdNoteId = namedtuple("CardIdNoteId", ["cid", "nid"])


class MorphStats:
    def __init__(self):
        self.a_morphs = 0
        self.u_morphs = 0


class ProgressStats:
    """Tracks stats for a particular length of time (e.g. day, week, etc.).

    learned_cards: The number of morphs that began in the learning phase and later exited this phase.
    """

    def __init__(self):
        self.learned_cards = 0
        self.learned = MorphStats()
        self.matured = MorphStats()


# all the stats for a particular length of time (e.g. day, week, etc.)
BucketStats = namedtuple("BucketStats", ["bucket_index", "stats"])


def _fix_ivl(ivl):
    if ivl < 0:
        return 0.5
    return ivl


def _has_lost_learned(card_reviews, last_ivl):
    "Check if the card has lost maturity for the current length of time."

    last_review = card_reviews.reviews[-1]
    new_ivl = last_review.ivl

    # return last_ivl > 0 and new_ivl <= 0
    if last_ivl > 0 >= new_ivl:
        return True
    return False


def _has_learned(card_reviews, last_ivl):
    "Check if the card was learned at some point during the length of time."

    last_review = card_reviews.reviews[-1]
    new_ivl = last_review.ivl

    if last_ivl <= 0 < new_ivl:
        return True
    return False


def _has_lost_matured(card_reviews, last_ivl, threshold):
    "Check if the card has lost maturity for the current length of time."

    last_review = card_reviews.reviews[-1]
    new_ivl = last_review.ivl

    last_ivl = _fix_ivl(last_ivl)
    new_ivl = _fix_ivl(new_ivl)

    if last_ivl >= threshold > new_ivl:
        return True
    return False


def _has_matured(card_reviews, last_ivl, threshold):
    "Check if the card was learned at some point during the length of time."

    last_review = card_reviews.reviews[-1]
    new_ivl = last_review.ivl

    last_ivl = _fix_ivl(last_ivl)
    new_ivl = _fix_ivl(new_ivl)

    if last_ivl < threshold <= new_ivl:
        return True
    return False


def _new_bucket_stats(bucket_index):
    return BucketStats(bucket_index=bucket_index, stats=ProgressStats())


def _get_reviews(  # pylint:disable=too-many-locals
    db_table, bucket_size_days, day_cutoff_seconds, num_buckets=None
):
    """Fetches all the reviews over a period of time and buckets them by (bucket_index, cid), where
    cid is the card ID and bucket_index where 0 is today, -1 is yesterday, etc.

    bucket_size_days represents the size of each bucket measusured in days.  So a value of 1 buckets per day,
    a value of 7 buckets per week, etc.

    day_cutoff_seconds is the cutoff measured in seconds since epoch for the start of the next day.  So, for example,
    if the cutoff is 4 am then this should be tomorrow at 4 am.

    num_buckets is the (optional) number of buckets, which indicates how many reviews to fetch.  Enough reviews are
    fetched to fill all the buckets.  So, for example, if bucket_size_days is 1 and num_buckets is 30 this fetches
    the last month of reviews.

    db_table is the table used to fetch from the review logs.

    additional_filter is an (optiona) filter added to the SQL WHERE clause that limits which reviews to fetch.
    This can be used to limit the reviews to a particular deck, for example.
    """

    # Set up the overall WHERE clause for the query, which filters out reviews older than the desired time window
    # and includes whatever other additional filters where provided (e.g. filter on cards belonging to a particular
    # deck).

    # The earlier time that will be used for graphing.  Any reviews earlier than this are only used to determine
    # when each card was first learned.
    id_cutoff = None

    filters = ["(cards.ivl != 0 or cards.type=1)"]

    # Exclude cards that are currently in new state.

    if num_buckets:
        id_cutoff = (
            day_cutoff_seconds - (bucket_size_days * num_buckets * 86400)
        ) * 1000
        # Get all recent reviews and any earlier reviews where the card was learned.  We need to query
        # earlier reviews because Anki's type does not appear to be reliable.  That is, you can't assume
        # that if the type is learning (type = 0) and the ivl becomes positive that this means the card
        # was learned for the first time.

        # filters.append("""(rl.id >= %d OR
        #                    (rl.id < %d AND
        #                      (rl.ivl > 0 AND rl.lastIvl <= 0)
        #                    )
        #                  )
        #               """ % (id_cutoff, id_cutoff))
    where_clause = "WHERE %s" % (" AND ".join(filters)) if filters else ""

    # id - The time at which the review was conducted, in epoch time (milliseconds)
    # nid - The ID of the note that was reviewed.  Also equals card creation time (milliseconds).
    # cid - The ID of the card that was reviewed.  Also equals card creation time (milliseconds).
    # ivl - The new interval that the card was pushed to after the review.
    #       Positive values are in days; negative values are in seconds (for learning cards).
    # lastIvl - The interval the card had before the review. Cards introduced for the first time
    #          have a last interval equal to the Again delay.
    # ease - 1 for Again, 4 for Easy
    # type - This is 0 = learning cards, 1 = review cards, 2 = relearn cards, and 3 = "cram"
    #        cards (cards being studied in a filtered deck when they are not due).

    # Convert the time to the day, where 0 is today (i.e. after the cutoff for today), -1 is yesterday, etc.
    # We add 0.5 and round in order to round up.

    query = """\
      SELECT cards.id,
             cards.nid,
             cards.did,
             cards.type,
             rl.id,
             CAST(round(( (rl.id/1000.0 - %d) / 86400.0 / %d ) + 0.5) as int)
               as bucket_index,
             rl.ease, rl.ivl, rl.lastIvl, cards.ivl, rl.type
      FROM revlog rl
      INNER JOIN cards ON rl.cid = cards.id
      %s
      ORDER BY rl.cid ASC, rl.id ASC;
      """ % (
        day_cutoff_seconds,
        bucket_size_days,
        where_clause,
    )

    result = db_table.all(query)

    prior_learned_cards_ivl = {}

    all_reviews_for_bucket = {}

    for i, (
        cid,
        nid,
        did,
        card_type,
        rl_id,
        bucket_index,
        ease,
        ivl,
        last_ivl,
        card_ivl,
        _type,
    ) in enumerate(result):
        # For the last review for a card, use the last card interval unless card is in the learning queue.
        if (i + 1 == len(result) or result[i + 1][0] != cid) and card_type != 1:
            ivl = card_ivl

        # Any ids earlier than the cutoff will not be graphed.  We only queried them to determine the
        # first time each card was learned.
        if id_cutoff and rl_id < id_cutoff:
            prior_learned_cards_ivl[CardIdNoteId(cid=cid, nid=nid)] = ivl
            continue

        key = (bucket_index, cid, nid, did)
        review = CardReview(
            id=rl_id,
            nid=nid,
            did=did,
            bucket_index=bucket_index,
            cid=cid,
            ease=ease,
            ivl=ivl,
            lastIvl=last_ivl,
            type=_type,
        )
        card_reviews = all_reviews_for_bucket.get(key)
        if not card_reviews:
            card_reviews = CardReviewsForBucket(
                bucket_index=bucket_index, cid=cid, reviews=[]
            )
            all_reviews_for_bucket[key] = card_reviews
        card_reviews.reviews.append(review)

    return all_reviews_for_bucket, prior_learned_cards_ivl


def get_stats(  # pylint:disable=too-many-branches,too-many-statements,too-many-locals
    self, db_table, bucket_size_days, day_cutoff_seconds, num_buckets=None
):
    stats_by_name = defaultdict(list)

    min_bucket_index = 0
    if num_buckets:
        min_bucket_index = -1 * num_buckets + 1
    max_bucket_index = 0

    all_reviews_for_bucket, prior_learned_cards_ivl = _get_reviews(
        db_table, bucket_size_days, day_cutoff_seconds, num_buckets
    )

    # print('all_reviews_for_bucket', len(all_reviews_for_bucket))
    # print('prior_learned_cards_ivl', len(prior_learned_cards_ivl))

    # If there is no review data then return empty dictionary. No graphs should be plotted.
    if not all_reviews_for_bucket:
        return stats_by_name

    all_db = util.get_all_db()
    nid_to_morphs = defaultdict(set)

    for morph, locations in all_db.db.items():
        for loc in locations:
            if isinstance(loc, AnkiDeck):
                nid_to_morphs[loc.note_id].add(morph)

    # print('nid_to_morphs', len(nid_to_morphs))

    all_deck_stats = defaultdict(ProgressStats)

    known_v_morph_times = defaultdict(int)
    known_k_morph_times = defaultdict(int)
    mature_v_morph_times = defaultdict(int)
    mature_k_morph_times = defaultdict(int)

    # stats_by_name['marked_known_cards'] = in_range_known_cards
    # print('marked_known_cards', stats_by_name['marked_known_cards'])

    # mature_v_morph_times = known_v_morph_times.copy()
    # mature_k_morph_times = known_k_morph_times.copy()

    threshold_known = cfg("threshold_known")
    threshold_mature = cfg("threshold_mature")

    last_ivl_by_cid = defaultdict(int)

    # Get morphs from cards learned prior to the cutoff
    for card, ivl in prior_learned_cards_ivl.items():
        for morph in nid_to_morphs[card.nid]:
            group_key = morph.get_group_key()
            if ivl >= threshold_known:
                known_v_morph_times[morph] += 1
                known_k_morph_times[group_key] += 1

            if ivl >= threshold_mature:
                mature_v_morph_times[morph] += 1
                mature_k_morph_times[group_key] += 1

        last_ivl_by_cid[card.cid] = ivl

    # k_already_known_morphs = len(known_k_morph_times)
    # v_already_known_morphs = len(known_v_morph_times)
    # k_already_mature_morphs = len(mature_k_morph_times)
    # v_already_mature_morphs = len(mature_v_morph_times)
    # print('k_already_known_morphs', k_already_known_morphs)
    # print('v_already_known_morphs', v_already_known_morphs)
    # print('k_already_mature_morphs', k_already_mature_morphs)
    # print('v_already_mature_morphs', v_already_mature_morphs)

    if self.wholeCollection:
        active_decks = None
    else:
        active_decks = set(self.col.decks.active())

    stats_by_bucket = {}

    # sort by bucket
    for key in sorted(all_reviews_for_bucket, key=lambda k: k[0]):
        card_reviews = all_reviews_for_bucket[key]

        bucket_index, cid, nid, did = key

        last_ivl = last_ivl_by_cid[cid]

        if bucket_index < min_bucket_index:
            min_bucket_index = bucket_index

        if bucket_index > max_bucket_index:
            max_bucket_index = bucket_index

        deck_stats = all_deck_stats[did]
        bucket_stats = stats_by_bucket.get(bucket_index)

        if not bucket_stats:
            bucket_stats = _new_bucket_stats(bucket_index)
            stats_by_bucket[bucket_index] = bucket_stats

        if _has_learned(card_reviews, last_ivl):
            if active_decks is None or (did in active_decks):
                deck_stats.learned_cards += 1
        if _has_lost_learned(card_reviews, last_ivl):
            if active_decks is None or (did in active_decks):
                deck_stats.learned_cards -= 1

        if _has_matured(card_reviews, last_ivl, threshold_known):
            update_morph_stats(
                nid,
                did,
                known_v_morph_times,
                known_k_morph_times,
                bucket_stats.stats.learned,
                deck_stats.learned,
                1,
                nid_to_morphs,
                active_decks,
            )
        if _has_lost_matured(card_reviews, last_ivl, threshold_known):
            update_morph_stats(
                nid,
                did,
                known_v_morph_times,
                known_k_morph_times,
                bucket_stats.stats.learned,
                deck_stats.learned,
                -1,
                nid_to_morphs,
                active_decks,
            )

        if _has_matured(card_reviews, last_ivl, threshold_mature):
            update_morph_stats(
                nid,
                did,
                mature_v_morph_times,
                mature_k_morph_times,
                bucket_stats.stats.matured,
                deck_stats.matured,
                1,
                nid_to_morphs,
                active_decks,
            )
        if _has_lost_matured(card_reviews, last_ivl, threshold_mature):
            update_morph_stats(
                nid,
                did,
                mature_v_morph_times,
                mature_k_morph_times,
                bucket_stats.stats.matured,
                deck_stats.matured,
                -1,
                nid_to_morphs,
                active_decks,
            )

        last_ivl_by_cid[cid] = card_reviews.reviews[-1].ivl

    # print('k_morphs_marked_known', len(known_k_morph_times))
    # print('v_morphs_marked_known', len(known_v_morph_times))

    # Return deck stats for decks with learned morphs
    stats_by_name["all_deck_stats"] = {}
    for did, deck_stats in all_deck_stats.items():
        if (
            deck_stats.learned.a_morphs
            or deck_stats.learned.u_morphs
            or deck_stats.matured.a_morphs
            or deck_stats.matured.u_morphs
        ):
            dname = mw.col.decks.name_if_exists(did)
            stats_by_name["all_deck_stats"][dname] = deck_stats

    added_a_bucket = False
    for bucket_index in range(min_bucket_index, max_bucket_index + 1):
        # Fill in days missing reviews with zero values
        if bucket_index not in stats_by_bucket:
            stats_by_bucket[bucket_index] = _new_bucket_stats(bucket_index)

        stats = stats_by_bucket[bucket_index]

        if (
            added_a_bucket
            or stats.stats.learned.a_morphs != 0
            or stats.stats.learned.u_morphs != 0
        ):
            stats_by_name["learned_v_morphs"].append(
                (bucket_index, stats.stats.learned.a_morphs)
            )
            stats_by_name["learned_k_morphs"].append(
                (bucket_index, stats.stats.learned.u_morphs)
            )
            added_a_bucket = True

    # k_final_known_morphs = len(known_k_morph_times)
    # v_final_known_morphs = len(known_v_morph_times)
    # k_final_mature_morphs = len(mature_k_morph_times)
    # v_final_mature_morphs = len(mature_v_morph_times)
    # print('k_final_known_morphs', k_final_known_morphs)
    # print('v_final_known_morphs', v_final_known_morphs)
    # print('k_final_mature_morphs', k_final_mature_morphs)
    # print('v_final_mature_morphs', v_final_mature_morphs)

    return stats_by_name


def update_morph_stats(  # pylint:disable=too-many-arguments
    nid,
    did,
    v_morph_times,
    k_morph_times,
    bucket_morph_stats,
    deck_morph_stats,
    delta,
    nid_to_morphs=None,
    active_decks=None,
):
    for _morph in nid_to_morphs[nid]:
        _group_key = _morph.get_group_key()

        if active_decks is None or (did in active_decks):
            if (delta == 1 and v_morph_times[_morph] == 0) or (
                delta == -1 and v_morph_times[_morph] == 1
            ):
                bucket_morph_stats.a_morphs += delta
                deck_morph_stats.a_morphs += delta

            if (delta == 1 and k_morph_times[_group_key] == 0) or (
                delta == -1 and k_morph_times[_group_key] == 1
            ):
                bucket_morph_stats.u_morphs += delta
                deck_morph_stats.u_morphs += delta

        v_morph_times[_morph] += delta
        k_morph_times[_group_key] += delta


def morph_graphs(args, kwargs):
    self = args[0]
    old = kwargs["_old"]

    # Try to use get_start_end_chunk if it exists to get the bucketing parameters
    # so the plugin graphs are consistent with Anki's other graphs.  This function only
    # exists for recent versions of Anki.
    if hasattr(self, "get_start_end_chunk"):
        (
            start_not_used,  # pylint:disable=unused-variable
            num_buckets,
            bucket_size_days,
        ) = self.get_start_end_chunk()

    # Fallback for older versions of Anki without this method.  Backporting the newer logic is
    # a bit complicated.  Note that the fallback values for type 2 don't work well for decks where
    # the deck life is very short (e.g. one or two months), but we'll just have to live with this.
    # The best option is for users to use Anki 2.1.
    else:
        if self.type == 0:
            # type 0 = past month
            num_buckets = 31
            bucket_size_days = 1
        elif self.type == 1:
            # type 1 = past year
            num_buckets = 52
            bucket_size_days = 7
        else:
            # type 2 = deck life
            num_buckets = None
            bucket_size_days = 31

    stats = get_stats(
        self,
        db_table=self.col.db,
        bucket_size_days=bucket_size_days,
        num_buckets=num_buckets,
        day_cutoff_seconds=self.col.sched.day_cutoff,
    )

    morph_result = ""

    morph_result += _plot(
        self,
        stats["learned_k_morphs"],
        "Unique Morphs",
        "Number of known unique morphemes learned from cards",
        bucket_size_days,
        include_cumulative=True,
        color=COL_K,
    )

    morph_result += _plot(
        self,
        stats["learned_v_morphs"],
        "All Morphs",
        "Number of known morphemes learned from cards",
        bucket_size_days,
        include_cumulative=True,
        color=COL_V,
    )

    morph_result += self._title(
        "Net Learned Cards & Morphs",
        "Summary of net learned cards and morphemes by deck",
    )
    morph_result += """
        <style>
            td.morph_trl { border: 1px solid; text-align: left; padding: 5px; }
            td.morph_trr { border: 1px solid; text-align: right; padding: 5px; }
            td.morph_trc { border: 1px solid; text-align: center; padding: 5px;}
            span.morph_c { color: %(c_color)s }
            span.morph_k { color: %(k_color)s }
            span.morph_v { color: %(v_color)s }
        </style>
        <br /><br />
        <table style="border-collapse: collapse;" cellspacing="0" cellpadding="2">
            <tr>
                <td class="morph_trl" rowspan=2><b>Deck</b></td>
                <td class="morph_trc" rowspan=2><span class="morph_c"><b>Cards<br />Learned</b></span></td>
                <td class="morph_trc" colspan=2><span class="morph_k"><b>Unique Morphs</b></span></td>
                <td class="morph_trc" colspan=2><span class="morph_v"><b>All Morphs</b></span></td>
            </tr>
            <tr>
                <td class="morph_trc"><span class="morph_k"><b>Learned</b></span></td>
                <td class="morph_trc"><span class="morph_k"><b>Matured</b></span></td>
                <td class="morph_trc"><span class="morph_v"><b>Learned</b></span></td>
                <td class="morph_trc"><span class="morph_v"><b>Matured</b></span></td>
            </tr>
            """ % {
        "c_color": COL_CARD,
        "k_color": COL_K,
        "v_color": COL_V,
    }
    total = ProgressStats()
    for deck in sorted(stats["all_deck_stats"].keys()):
        deck_stats = stats["all_deck_stats"][deck]
        morph_result += (
            """
            <tr>
                 <td class="morph_trl">"""
            + deck
            + """</td>
                 <td class="morph_trc"><span class="morph_c">"""
            + str(deck_stats.learned_cards)
            + """</span></td>
                 <td class="morph_trc"><span class="morph_k">"""
            + str(deck_stats.learned.u_morphs)
            + """</span></td>
                 <td class="morph_trc"><span class="morph_k">"""
            + str(deck_stats.matured.u_morphs)
            + """</span></td>
                 <td class="morph_trc"><span class="morph_v">"""
            + str(deck_stats.learned.a_morphs)
            + """</span></td>
                 <td class="morph_trc"><span class="morph_v">"""
            + str(deck_stats.matured.a_morphs)
            + """</span></td>
            </tr>"""
        )
        total.learned_cards += deck_stats.learned_cards
        total.learned.u_morphs += deck_stats.learned.u_morphs
        total.learned.a_morphs += deck_stats.learned.a_morphs
        total.matured.u_morphs += deck_stats.matured.u_morphs
        total.matured.a_morphs += deck_stats.matured.a_morphs
    morph_result += (
        """
            <tr>
                 <td class="morph_trl"><b>Total</b></td>
                 <td class="morph_trc"><b><span class="morph_c">"""
        + str(total.learned_cards)
        + """</span></b></td>
                 <td class="morph_trc"><b><span class="morph_k">"""
        + str(total.learned.u_morphs)
        + """</span></b></td>
                 <td class="morph_trc"><b><span class="morph_k">"""
        + str(total.matured.u_morphs)
        + """</span></b></td>
                 <td class="morph_trc"><b><span class="morph_v">"""
        + str(total.learned.a_morphs)
        + """</span></b></td>
                 <td class="morph_trc"><b><span class="morph_v">"""
        + str(total.matured.a_morphs)
        + """</span></b></td>
            </tr>"""
    )
    morph_result += "</table>"

    return morph_result + old(self)


def _round_up_max(max_val):
    """Rounds up a maximum value."""

    # Prevent zero values raising an error.  Rounds up to 10 at a minimum.
    max_val = max(10, max_val)

    exponent = int(math.log10(max_val))
    if exponent >= 2:
        exponent -= 1
    _min = 10**exponent
    return math.ceil(float(max_val) / _min) * _min


def _round_down_min(min_val):
    """Rounds down a minimum value."""

    # Minimum should not be positive
    min_val = min(0, min_val)

    if not min_val:
        return 0

    return -1 * _round_up_max(-1 * min_val)


def _plot(  # pylint:disable=too-many-locals,too-many-arguments
    self,
    data,
    title,
    subtitle,
    bucket_size_days,
    include_cumulative=False,
    color=DEFAULT_COLOR,
):
    global _NUM_GRAPHS  # pylint:disable=global-statement
    if not data:
        return ""
    cumulative_total = 0
    cumulative_data = []
    for x_value, y_value in data:
        cumulative_total += y_value
        cumulative_data.append((x_value, cumulative_total))

    txt = self._title(title, subtitle)

    graph_data = [{"data": data, "color": color}]

    if include_cumulative:
        graph_data.append(
            {
                "data": cumulative_data,
                "color": color,
                "label": "Cumulative",
                "yaxis": 2,
                "bars": {"show": False},
                "lines": {"show": True},
                "stack": False,
            }
        )

    y_axes = [
        {
            "min": _round_down_min(min((y for (x, y) in data))),
            "max": _round_up_max(max((y for (x, y) in data))),
        }
    ]

    if include_cumulative:
        y_axes.append(
            {
                "min": _round_down_min(min((y for (x, y) in cumulative_data))),
                "max": _round_up_max(max((y for (x, y) in cumulative_data))),
                "position": "right",
            }
        )

    graph_kwargs = {
        "id": f"morphs-{_NUM_GRAPHS}",
        "data": graph_data,
        "conf": {"max": 0.5, "tickDecimals": 0},
    }

    # In recent versions of Anki, an xunit arg was added to _graph to control the tick
    # labelling.  The old version picked the tick labels based on the graph type (last month, last year,
    # or deck life).  Now for deck life it picks the appropriate bucket size based on the age of the deck.
    try:
        if "xunit" in inspect.signature(self._graph).parameters:
            graph_kwargs["xunit"] = bucket_size_days
        if "ylabel" in inspect.signature(self._graph).parameters:
            graph_kwargs["ylabel"] = "Morphemes"
        if "ylabel2" in inspect.signature(self._graph).parameters:
            graph_kwargs["ylabel2"] = "Cumulative Morphemes"
    except Exception:  # TODO: Catch too broad!
        pass

    txt += self._graph(**graph_kwargs)

    _NUM_GRAPHS += 1
    text_lines = []
    average_cards = cumulative_total / float(len(data) * bucket_size_days)

    self._line(
        text_lines,
        "Average",
        f"{average_cards:.1f} morphs/day",
    )

    if include_cumulative:
        self._line(text_lines, "Total", f"{cumulative_total} morphs")

    txt += self._lineTbl(text_lines)

    return txt
