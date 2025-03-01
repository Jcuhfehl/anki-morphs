import csv
import datetime
import os
from pathlib import Path
from typing import Any, Callable, Union

import aqt
from anki.collection import Collection
from aqt import mw
from aqt.operations import QueryOp
from aqt.qt import QDialog, QDir, QFileDialog  # pylint:disable=no-name-in-module
from aqt.utils import tooltip

from . import ankimorphs_globals
from .ankimorphs_db import AnkiMorphsDB
from .exceptions import CancelledOperationException, EmptyFileSelectionException
from .ui.known_morphs_exporter_ui import Ui_KnownMorphsExporterDialog


class KnownMorphsExporterDialog(QDialog):
    def __init__(
        self,
    ) -> None:
        super().__init__(parent=None)  # no parent makes the dialog modeless
        self.ui = Ui_KnownMorphsExporterDialog()  # pylint:disable=invalid-name
        self.ui.setupUi(self)  # type: ignore[no-untyped-call]

        self.ui.knownIntervalSpinBox.setValue(21)  # usually considered known

        self._setup_output_path()
        self._setup_buttons()

        self.show()

    def _setup_output_path(self) -> None:
        assert mw is not None

        _output_dir = os.path.join(mw.pm.profileFolder(), "known-morphs")
        # create the parent directories if they don't exist
        Path(_output_dir).parent.mkdir(parents=True, exist_ok=True)
        self.ui.outputLineEdit.setText(_output_dir)

    def _setup_buttons(self) -> None:
        self.ui.selectOutputPushButton.setAutoDefault(False)
        self.ui.exportKnownMorphsPushButton.setAutoDefault(False)

        self.ui.selectOutputPushButton.clicked.connect(self._on_output_button_clicked)
        self.ui.exportKnownMorphsPushButton.clicked.connect(self._export_known_morphs)

    def _on_output_button_clicked(self) -> None:
        output_dir: str = QFileDialog.getExistingDirectory(
            caption="Directory to place file",
            directory=QDir().homePath(),
        )
        self.ui.outputLineEdit.setText(output_dir)

    def _export_known_morphs(self) -> None:
        assert mw is not None

        mw.progress.start(label="Exporting Known Morphs")
        operation = QueryOp(
            parent=mw,
            op=self._background_export_known_morphs,
            success=self._on_success,
        )
        operation.failure(self._on_failure)
        operation.with_progress().run_in_background()

    def _background_export_known_morphs(self, col: Collection) -> None:
        del col  # unused
        assert mw is not None

        if self.ui.outputLineEdit.text() == "":
            raise EmptyFileSelectionException

        _output_dir = self.ui.outputLineEdit.text()
        _datetime = datetime.datetime.now().strftime("%Y-%m-%d@%H-%M-%S")
        _output_file = os.path.join(_output_dir, f"known_morphs-{_datetime}.csv")

        # create the parent directories if they don't exist
        Path(_output_file).parent.mkdir(parents=True, exist_ok=True)

        with open(_output_file, mode="w+", encoding="utf-8", newline="") as csvfile:
            morph_writer = csv.writer(csvfile)
            morph_writer.writerow(["Morph-lemma", "Morph-inflection"])

            highest_learning_interval: int = self.ui.knownIntervalSpinBox.value()
            known_morphs: list[tuple[str, str]] = AnkiMorphsDB.get_known_morphs(
                highest_learning_interval
            )

            for known_morphs_tuple in known_morphs:
                # lemma, inflection
                morph_writer.writerow([known_morphs_tuple[0], known_morphs_tuple[1]])

    def closeWithCallback(  # pylint:disable=invalid-name
        self, callback: Callable[[], None]
    ) -> None:
        # This is used by the Anki dialog manager
        self.close()
        aqt.dialogs.markClosed(ankimorphs_globals.KNOWN_MORPHS_EXPORTER_DIALOG_NAME)
        callback()

    def reopen(self) -> None:
        # This is used by the Anki dialog manager
        self.show()

    def _on_success(self, result: Any) -> None:
        # This function runs on the main thread.
        del result  # unused
        assert mw is not None
        assert mw.progress is not None

        mw.toolbar.draw()  # updates stats
        mw.progress.finish()

        tooltip("Known morphs file created", parent=self)

    def _on_failure(
        self,
        error: Union[
            Exception,
            CancelledOperationException,
            EmptyFileSelectionException,
        ],
    ) -> None:
        # This function runs on the main thread.
        assert mw is not None
        assert mw.progress is not None
        mw.progress.finish()

        if isinstance(error, CancelledOperationException):
            tooltip("Cancelled Known Morphs Export", parent=self)
        elif isinstance(error, EmptyFileSelectionException):
            tooltip("No file/folder selected", parent=self)
        else:
            raise error
