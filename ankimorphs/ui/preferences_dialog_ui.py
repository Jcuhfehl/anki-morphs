# Form implementation generated from reading ui file 'ankimorphs/ui/preferences_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog:
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(793, 358)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.note_filters_tab = QtWidgets.QWidget()
        self.note_filters_tab.setObjectName("note_filters_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.note_filters_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.note_filters_table = QtWidgets.QTableWidget(parent=self.note_filters_tab)
        self.note_filters_table.setObjectName("note_filters_table")
        self.note_filters_table.setColumnCount(6)
        self.note_filters_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.note_filters_table.setHorizontalHeaderItem(5, item)
        self.verticalLayout_3.addWidget(self.note_filters_table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.delete_row_button = QtWidgets.QPushButton(parent=self.note_filters_tab)
        self.delete_row_button.setObjectName("delete_row_button")
        self.horizontalLayout_2.addWidget(self.delete_row_button)
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem)
        self.add_new_row_button = QtWidgets.QPushButton(parent=self.note_filters_tab)
        self.add_new_row_button.setObjectName("add_new_row_button")
        self.horizontalLayout_2.addWidget(self.add_new_row_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.note_filters_tab, "")
        self.extra_fields_tab = QtWidgets.QWidget()
        self.extra_fields_tab.setObjectName("extra_fields_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.extra_fields_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.extra_fields_table = QtWidgets.QTableWidget(parent=self.extra_fields_tab)
        self.extra_fields_table.setObjectName("extra_fields_table")
        self.extra_fields_table.setColumnCount(4)
        self.extra_fields_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.extra_fields_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.extra_fields_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.extra_fields_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.extra_fields_table.setHorizontalHeaderItem(3, item)
        self.verticalLayout_5.addWidget(self.extra_fields_table)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.extra_fields_tab, "")
        self.tags_tab = QtWidgets.QWidget()
        self.tags_tab.setObjectName("tags_tab")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tags_tab)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(parent=self.tags_tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.tags_tab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.tags_tab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.ripe_tag_input = QtWidgets.QLineEdit(parent=self.tags_tab)
        self.ripe_tag_input.setObjectName("ripe_tag_input")
        self.verticalLayout_7.addWidget(self.ripe_tag_input)
        self.budding_tag_input = QtWidgets.QLineEdit(parent=self.tags_tab)
        self.budding_tag_input.setObjectName("budding_tag_input")
        self.verticalLayout_7.addWidget(self.budding_tag_input)
        self.stale_tag_input = QtWidgets.QLineEdit(parent=self.tags_tab)
        self.stale_tag_input.setObjectName("stale_tag_input")
        self.verticalLayout_7.addWidget(self.stale_tag_input)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.verticalLayout_12.addLayout(self.verticalLayout_10)
        spacerItem2 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_12.addItem(spacerItem2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.restore_tags_defaults_button = QtWidgets.QPushButton(parent=self.tags_tab)
        self.restore_tags_defaults_button.setObjectName("restore_tags_defaults_button")
        self.horizontalLayout_7.addWidget(self.restore_tags_defaults_button)
        spacerItem3 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tags_tab, "")
        self.parse_tab = QtWidgets.QWidget()
        self.parse_tab.setObjectName("parse_tab")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.parse_tab)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.parse_ignore_bracket_contents_input = QtWidgets.QCheckBox(
            parent=self.parse_tab
        )
        self.parse_ignore_bracket_contents_input.setObjectName(
            "parse_ignore_bracket_contents_input"
        )
        self.verticalLayout_9.addWidget(self.parse_ignore_bracket_contents_input)
        self.parse_ignore_round_bracket_contents_input = QtWidgets.QCheckBox(
            parent=self.parse_tab
        )
        self.parse_ignore_round_bracket_contents_input.setObjectName(
            "parse_ignore_round_bracket_contents_input"
        )
        self.verticalLayout_9.addWidget(self.parse_ignore_round_bracket_contents_input)
        self.parse_ignore_slim_round_bracket_contents_input = QtWidgets.QCheckBox(
            parent=self.parse_tab
        )
        self.parse_ignore_slim_round_bracket_contents_input.setObjectName(
            "parse_ignore_slim_round_bracket_contents_input"
        )
        self.verticalLayout_9.addWidget(
            self.parse_ignore_slim_round_bracket_contents_input
        )
        self.parse_ignore_proper_nouns_input = QtWidgets.QCheckBox(
            parent=self.parse_tab
        )
        self.parse_ignore_proper_nouns_input.setObjectName(
            "parse_ignore_proper_nouns_input"
        )
        self.verticalLayout_9.addWidget(self.parse_ignore_proper_nouns_input)
        self.parse_ignore_suspended_cards_content_input = QtWidgets.QCheckBox(
            parent=self.parse_tab
        )
        self.parse_ignore_suspended_cards_content_input.setObjectName(
            "parse_ignore_suspended_cards_content_input"
        )
        self.verticalLayout_9.addWidget(self.parse_ignore_suspended_cards_content_input)
        self.verticalLayout_13.addLayout(self.verticalLayout_9)
        spacerItem4 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_13.addItem(spacerItem4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.restore_parse_defaults_button = QtWidgets.QPushButton(
            parent=self.parse_tab
        )
        self.restore_parse_defaults_button.setObjectName(
            "restore_parse_defaults_button"
        )
        self.horizontalLayout_8.addWidget(self.restore_parse_defaults_button)
        spacerItem5 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.parse_tab, "")
        self.skip_tab = QtWidgets.QWidget()
        self.skip_tab.setObjectName("skip_tab")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.skip_tab)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.skip_stale_cards_input = QtWidgets.QCheckBox(parent=self.skip_tab)
        self.skip_stale_cards_input.setObjectName("skip_stale_cards_input")
        self.verticalLayout_11.addWidget(self.skip_stale_cards_input)
        self.skip_unknown_morph_seen_today_cards_input = QtWidgets.QCheckBox(
            parent=self.skip_tab
        )
        self.skip_unknown_morph_seen_today_cards_input.setObjectName(
            "skip_unknown_morph_seen_today_cards_input"
        )
        self.verticalLayout_11.addWidget(self.skip_unknown_morph_seen_today_cards_input)
        self.skip_show_num_of_skipped_cards_input = QtWidgets.QCheckBox(
            parent=self.skip_tab
        )
        self.skip_show_num_of_skipped_cards_input.setObjectName(
            "skip_show_num_of_skipped_cards_input"
        )
        self.verticalLayout_11.addWidget(self.skip_show_num_of_skipped_cards_input)
        self.verticalLayout_20.addLayout(self.verticalLayout_11)
        spacerItem6 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_20.addItem(spacerItem6)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.restore_skip_defaults_button = QtWidgets.QPushButton(parent=self.skip_tab)
        self.restore_skip_defaults_button.setObjectName("restore_skip_defaults_button")
        self.horizontalLayout_11.addWidget(self.restore_skip_defaults_button)
        spacerItem7 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_11.addItem(spacerItem7)
        self.verticalLayout_20.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.skip_tab, "")
        self.recalc_tab = QtWidgets.QWidget()
        self.recalc_tab.setObjectName("recalc_tab")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.recalc_tab)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(parent=self.recalc_tab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.preferred_sentence_length_input = QtWidgets.QSpinBox(
            parent=self.recalc_tab
        )
        self.preferred_sentence_length_input.setObjectName(
            "preferred_sentence_length_input"
        )
        self.horizontalLayout_6.addWidget(self.preferred_sentence_length_input)
        spacerItem8 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_18.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(parent=self.recalc_tab)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.recalc_unknown_morphs_count_input = QtWidgets.QSpinBox(
            parent=self.recalc_tab
        )
        self.recalc_unknown_morphs_count_input.setObjectName(
            "recalc_unknown_morphs_count_input"
        )
        self.horizontalLayout_4.addWidget(self.recalc_unknown_morphs_count_input)
        self.label = QtWidgets.QLabel(parent=self.recalc_tab)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem9 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_18.addLayout(self.horizontalLayout_4)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.recalc_before_sync_input = QtWidgets.QCheckBox(parent=self.recalc_tab)
        self.recalc_before_sync_input.setObjectName("recalc_before_sync_input")
        self.verticalLayout_17.addWidget(self.recalc_before_sync_input)
        self.verticalLayout_18.addLayout(self.verticalLayout_17)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_5 = QtWidgets.QLabel(parent=self.recalc_tab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_14.addWidget(self.label_5)
        self.recalc_prioritize_collection_input = QtWidgets.QRadioButton(
            parent=self.recalc_tab
        )
        self.recalc_prioritize_collection_input.setObjectName(
            "recalc_prioritize_collection_input"
        )
        self.verticalLayout_14.addWidget(self.recalc_prioritize_collection_input)
        self.recalc_prioritize_textfile_input = QtWidgets.QRadioButton(
            parent=self.recalc_tab
        )
        self.recalc_prioritize_textfile_input.setObjectName(
            "recalc_prioritize_textfile_input"
        )
        self.verticalLayout_14.addWidget(self.recalc_prioritize_textfile_input)
        self.verticalLayout_18.addLayout(self.verticalLayout_14)
        spacerItem10 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_18.addItem(spacerItem10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.restore_recalc_defaults_button = QtWidgets.QPushButton(
            parent=self.recalc_tab
        )
        self.restore_recalc_defaults_button.setObjectName(
            "restore_recalc_defaults_button"
        )
        self.horizontalLayout_9.addWidget(self.restore_recalc_defaults_button)
        spacerItem11 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_9.addItem(spacerItem11)
        self.verticalLayout_18.addLayout(self.horizontalLayout_9)
        self.tabWidget.addTab(self.recalc_tab, "")
        self.shortcuts_tab = QtWidgets.QWidget()
        self.shortcuts_tab.setObjectName("shortcuts_tab")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.shortcuts_tab)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_8 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_16.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_16.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_16.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_16.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(parent=self.shortcuts_tab)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_16.addWidget(self.label_12)
        self.horizontalLayout_5.addLayout(self.verticalLayout_16)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.shortcut_browse_same_ripe_input = QtWidgets.QLineEdit(
            parent=self.shortcuts_tab
        )
        self.shortcut_browse_same_ripe_input.setObjectName(
            "shortcut_browse_same_ripe_input"
        )
        self.verticalLayout_15.addWidget(self.shortcut_browse_same_ripe_input)
        self.shortcut_browse_same_ripe_budding_input = QtWidgets.QLineEdit(
            parent=self.shortcuts_tab
        )
        self.shortcut_browse_same_ripe_budding_input.setObjectName(
            "shortcut_browse_same_ripe_budding_input"
        )
        self.verticalLayout_15.addWidget(self.shortcut_browse_same_ripe_budding_input)
        self.shortcut_known_and_skip_input = QtWidgets.QLineEdit(
            parent=self.shortcuts_tab
        )
        self.shortcut_known_and_skip_input.setObjectName(
            "shortcut_known_and_skip_input"
        )
        self.verticalLayout_15.addWidget(self.shortcut_known_and_skip_input)
        self.shortcut_learn_now_input = QtWidgets.QLineEdit(parent=self.shortcuts_tab)
        self.shortcut_learn_now_input.setObjectName("shortcut_learn_now_input")
        self.verticalLayout_15.addWidget(self.shortcut_learn_now_input)
        self.shortcut_view_morphs_input = QtWidgets.QLineEdit(parent=self.shortcuts_tab)
        self.shortcut_view_morphs_input.setObjectName("shortcut_view_morphs_input")
        self.verticalLayout_15.addWidget(self.shortcut_view_morphs_input)
        self.horizontalLayout_5.addLayout(self.verticalLayout_15)
        spacerItem12 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_5.addItem(spacerItem12)
        self.verticalLayout_19.addLayout(self.horizontalLayout_5)
        spacerItem13 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_19.addItem(spacerItem13)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.restore_shortcut_defaults_button = QtWidgets.QPushButton(
            parent=self.shortcuts_tab
        )
        self.restore_shortcut_defaults_button.setObjectName(
            "restore_shortcut_defaults_button"
        )
        self.horizontalLayout_10.addWidget(self.restore_shortcut_defaults_button)
        spacerItem14 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_10.addItem(spacerItem14)
        self.verticalLayout_19.addLayout(self.horizontalLayout_10)
        self.tabWidget.addTab(self.shortcuts_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem15 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem15)
        self.ankimorphs_version_label = QtWidgets.QLabel(parent=Dialog)
        self.ankimorphs_version_label.setObjectName("ankimorphs_version_label")
        self.horizontalLayout.addWidget(self.ankimorphs_version_label)
        spacerItem16 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout.addItem(spacerItem16)
        self.cancel_button = QtWidgets.QPushButton(parent=Dialog)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.save_button = QtWidgets.QPushButton(parent=Dialog)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AnkiMorph Settings"))
        item = self.note_filters_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Note Type"))
        item = self.note_filters_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tags"))
        item = self.note_filters_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Field"))
        item = self.note_filters_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Morphemizer"))
        item = self.note_filters_table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Read"))
        item = self.note_filters_table.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Modify"))
        self.delete_row_button.setText(_translate("Dialog", "Delete Selected Row"))
        self.add_new_row_button.setText(_translate("Dialog", "Add New Row"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.note_filters_tab),
            _translate("Dialog", "Note Filters"),
        )
        item = self.extra_fields_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Note Type"))
        item = self.extra_fields_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Focus Morph"))
        item = self.extra_fields_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Highlighted"))
        item = self.extra_fields_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Difficulty"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.extra_fields_tab),
            _translate("Dialog", "Extra Fields"),
        )
        self.label_2.setText(_translate("Dialog", "One unknown morph"))
        self.label_3.setText(_translate("Dialog", "Multiple Unknown morphs"))
        self.label_4.setText(_translate("Dialog", "All morphs known"))
        self.restore_tags_defaults_button.setText(
            _translate("Dialog", "Restore Default Tags Settings")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tags_tab), _translate("Dialog", "Tags")
        )
        self.parse_ignore_bracket_contents_input.setText(
            _translate("Dialog", "ignore content in brackets")
        )
        self.parse_ignore_round_bracket_contents_input.setText(
            _translate("Dialog", "ignore content in round brackets")
        )
        self.parse_ignore_slim_round_bracket_contents_input.setText(
            _translate("Dialog", "ignore content in slim round brackets")
        )
        self.parse_ignore_proper_nouns_input.setText(
            _translate("Dialog", "Ignore proper nouns")
        )
        self.parse_ignore_suspended_cards_content_input.setText(
            _translate("Dialog", "Ignore content in suspended cards")
        )
        self.restore_parse_defaults_button.setText(
            _translate("Dialog", "Restore Default Parse Settings")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.parse_tab), _translate("Dialog", "Parse")
        )
        self.skip_stale_cards_input.setText(_translate("Dialog", "Skip stale cards"))
        self.skip_unknown_morph_seen_today_cards_input.setText(
            _translate(
                "Dialog", "Skip cards that have unknown morphs already seen today"
            )
        )
        self.skip_show_num_of_skipped_cards_input.setText(
            _translate("Dialog", 'Show "skipped x cards" notifications')
        )
        self.restore_skip_defaults_button.setText(
            _translate("Dialog", "Restore Default Skip Settings")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.skip_tab), _translate("Dialog", "Skip")
        )
        self.label_6.setText(_translate("Dialog", "Preferred sentence length (morphs)"))
        self.label_7.setText(
            _translate("Dialog", "Only Recalc cards that have less than")
        )
        self.label.setText(_translate("Dialog", "unknown morphs"))
        self.recalc_before_sync_input.setText(
            _translate("Dialog", "Automatically Recalc before Sync")
        )
        self.label_5.setText(_translate("Dialog", "Prioritize morphs based on:"))
        self.recalc_prioritize_collection_input.setText(
            _translate("Dialog", "Frequency in card collection")
        )
        self.recalc_prioritize_textfile_input.setText(
            _translate("Dialog", "frequency.txt")
        )
        self.restore_recalc_defaults_button.setText(
            _translate("Dialog", "Restore Default Recalc Settings")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.recalc_tab), _translate("Dialog", "Recalc")
        )
        self.label_8.setText(
            _translate("Dialog", "Browse ripe cards with same unknown morph")
        )
        self.label_9.setText(
            _translate(
                "Dialog", "Browse ripe and budding cards with same unknown morph"
            )
        )
        self.label_10.setText(_translate("Dialog", "Set card as known and skip"))
        self.label_11.setText(_translate("Dialog", "Learn card now"))
        self.label_12.setText(_translate("Dialog", "View card morphemes"))
        self.restore_shortcut_defaults_button.setText(
            _translate("Dialog", "Restore Default Shortcut Settings")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.shortcuts_tab),
            _translate("Dialog", "Shortcuts"),
        )
        self.pushButton_3.setText(_translate("Dialog", "Restore All Default Settings"))
        self.ankimorphs_version_label.setText(
            _translate("Dialog", "AnkiMorphs version: x")
        )
        self.cancel_button.setText(_translate("Dialog", "Cancel"))
        self.save_button.setText(_translate("Dialog", "Save"))
