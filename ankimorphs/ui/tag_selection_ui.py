# Form implementation generated from reading ui file 'ankimorphs/ui/tag_selection.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TagSelectionDialog:
    def setupUi(self, TagSelectionDialog):
        TagSelectionDialog.setObjectName("TagSelectionDialog")
        TagSelectionDialog.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(TagSelectionDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(parent=TagSelectionDialog)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.unselectAllButton = QtWidgets.QPushButton(parent=TagSelectionDialog)
        self.unselectAllButton.setStyleSheet("")
        self.unselectAllButton.setObjectName("unselectAllButton")
        self.verticalLayout.addWidget(self.unselectAllButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.applyButton = QtWidgets.QPushButton(parent=TagSelectionDialog)
        self.applyButton.setObjectName("applyButton")
        self.verticalLayout.addWidget(self.applyButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(TagSelectionDialog)
        QtCore.QMetaObject.connectSlotsByName(TagSelectionDialog)

    def retranslateUi(self, TagSelectionDialog):
        _translate = QtCore.QCoreApplication.translate
        TagSelectionDialog.setWindowTitle(_translate("TagSelectionDialog", "Tag Selector"))
        self.unselectAllButton.setText(_translate("TagSelectionDialog", "Unselect All"))
        self.applyButton.setText(_translate("TagSelectionDialog", " Apply"))
