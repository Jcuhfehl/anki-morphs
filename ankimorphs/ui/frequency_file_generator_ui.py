# Form implementation generated from reading ui file 'ankimorphs/ui/frequency_file_generator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FrequencyFileGeneratorDialog:
    def setupUi(self, FrequencyFileGeneratorDialog):
        FrequencyFileGeneratorDialog.setObjectName("FrequencyFileGeneratorDialog")
        FrequencyFileGeneratorDialog.resize(459, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FrequencyFileGeneratorDialog.sizePolicy().hasHeightForWidth())
        FrequencyFileGeneratorDialog.setSizePolicy(sizePolicy)
        FrequencyFileGeneratorDialog.setMinimumSize(QtCore.QSize(0, 450))
        FrequencyFileGeneratorDialog.setMaximumSize(QtCore.QSize(16777215, 450))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(FrequencyFileGeneratorDialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputButton = QtWidgets.QPushButton(parent=FrequencyFileGeneratorDialog)
        self.inputButton.setObjectName("inputButton")
        self.verticalLayout.addWidget(self.inputButton)
        self.outputButton = QtWidgets.QPushButton(parent=FrequencyFileGeneratorDialog)
        self.outputButton.setObjectName("outputButton")
        self.verticalLayout.addWidget(self.outputButton)
        self.label = QtWidgets.QLabel(parent=FrequencyFileGeneratorDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(parent=FrequencyFileGeneratorDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inputDirLineEdit = QtWidgets.QLineEdit(parent=FrequencyFileGeneratorDialog)
        self.inputDirLineEdit.setObjectName("inputDirLineEdit")
        self.verticalLayout_2.addWidget(self.inputDirLineEdit)
        self.outputFileLineEdit = QtWidgets.QLineEdit(parent=FrequencyFileGeneratorDialog)
        self.outputFileLineEdit.setObjectName("outputFileLineEdit")
        self.verticalLayout_2.addWidget(self.outputFileLineEdit)
        self.comboBox = QtWidgets.QComboBox(parent=FrequencyFileGeneratorDialog)
        self.comboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txtFilesCheckBox = QtWidgets.QCheckBox(parent=FrequencyFileGeneratorDialog)
        self.txtFilesCheckBox.setObjectName("txtFilesCheckBox")
        self.horizontalLayout_3.addWidget(self.txtFilesCheckBox)
        self.srtFilesCheckBox = QtWidgets.QCheckBox(parent=FrequencyFileGeneratorDialog)
        self.srtFilesCheckBox.setObjectName("srtFilesCheckBox")
        self.horizontalLayout_3.addWidget(self.srtFilesCheckBox)
        self.vttFilesCheckBox = QtWidgets.QCheckBox(parent=FrequencyFileGeneratorDialog)
        self.vttFilesCheckBox.setObjectName("vttFilesCheckBox")
        self.horizontalLayout_3.addWidget(self.vttFilesCheckBox)
        self.mdFilesCheckBox = QtWidgets.QCheckBox(parent=FrequencyFileGeneratorDialog)
        self.mdFilesCheckBox.setObjectName("mdFilesCheckBox")
        self.horizontalLayout_3.addWidget(self.mdFilesCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=FrequencyFileGeneratorDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.minOccurrenceSpinBox = QtWidgets.QSpinBox(parent=FrequencyFileGeneratorDialog)
        self.minOccurrenceSpinBox.setMinimum(1)
        self.minOccurrenceSpinBox.setMaximum(1000)
        self.minOccurrenceSpinBox.setObjectName("minOccurrenceSpinBox")
        self.horizontalLayout_2.addWidget(self.minOccurrenceSpinBox, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(parent=FrequencyFileGeneratorDialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.squareBracketsCheckBox = QtWidgets.QCheckBox(parent=FrequencyFileGeneratorDialog)
        self.squareBracketsCheckBox.setObjectName("squareBracketsCheckBox")
        self.verticalLayout_5.addWidget(self.squareBracketsCheckBox)
        self.roundBracketsCheckBox = QtWidgets.QCheckBox(parent=FrequencyFileGeneratorDialog)
        self.roundBracketsCheckBox.setObjectName("roundBracketsCheckBox")
        self.verticalLayout_5.addWidget(self.roundBracketsCheckBox)
        self.slimRoundBracketsCheckBox = QtWidgets.QCheckBox(parent=FrequencyFileGeneratorDialog)
        self.slimRoundBracketsCheckBox.setObjectName("slimRoundBracketsCheckBox")
        self.verticalLayout_5.addWidget(self.slimRoundBracketsCheckBox)
        self.namesMorphemizerCheckBox = QtWidgets.QCheckBox(parent=FrequencyFileGeneratorDialog)
        self.namesMorphemizerCheckBox.setObjectName("namesMorphemizerCheckBox")
        self.verticalLayout_5.addWidget(self.namesMorphemizerCheckBox)
        self.namesFileCheckBox = QtWidgets.QCheckBox(parent=FrequencyFileGeneratorDialog)
        self.namesFileCheckBox.setObjectName("namesFileCheckBox")
        self.verticalLayout_5.addWidget(self.namesFileCheckBox)
        self.numbersCheckBox = QtWidgets.QCheckBox(parent=FrequencyFileGeneratorDialog)
        self.numbersCheckBox.setObjectName("numbersCheckBox")
        self.verticalLayout_5.addWidget(self.numbersCheckBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.createFrequencyFileButton = QtWidgets.QPushButton(parent=FrequencyFileGeneratorDialog)
        self.createFrequencyFileButton.setStyleSheet("margin-top: 10px;\n"
"margin-bottom: 10px;\n"
"padding: 5px;")
        self.createFrequencyFileButton.setObjectName("createFrequencyFileButton")
        self.verticalLayout_3.addWidget(self.createFrequencyFileButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(FrequencyFileGeneratorDialog)
        QtCore.QMetaObject.connectSlotsByName(FrequencyFileGeneratorDialog)

    def retranslateUi(self, FrequencyFileGeneratorDialog):
        _translate = QtCore.QCoreApplication.translate
        FrequencyFileGeneratorDialog.setWindowTitle(_translate("FrequencyFileGeneratorDialog", "Frequency File Generator"))
        self.inputButton.setText(_translate("FrequencyFileGeneratorDialog", "Select input"))
        self.outputButton.setText(_translate("FrequencyFileGeneratorDialog", "Select output"))
        self.label.setText(_translate("FrequencyFileGeneratorDialog", "Morphemizer:"))
        self.label_3.setText(_translate("FrequencyFileGeneratorDialog", "File formats:"))
        self.txtFilesCheckBox.setText(_translate("FrequencyFileGeneratorDialog", ".txt"))
        self.srtFilesCheckBox.setText(_translate("FrequencyFileGeneratorDialog", ".srt"))
        self.vttFilesCheckBox.setText(_translate("FrequencyFileGeneratorDialog", ".vtt"))
        self.mdFilesCheckBox.setText(_translate("FrequencyFileGeneratorDialog", ".md"))
        self.label_2.setText(_translate("FrequencyFileGeneratorDialog", "Minimum occurrence:"))
        self.label_4.setText(_translate("FrequencyFileGeneratorDialog", "Parsing:"))
        self.squareBracketsCheckBox.setText(_translate("FrequencyFileGeneratorDialog", "Ignore content in square brackets []"))
        self.roundBracketsCheckBox.setText(_translate("FrequencyFileGeneratorDialog", "ignore content in round brackets（）"))
        self.slimRoundBracketsCheckBox.setText(_translate("FrequencyFileGeneratorDialog", "ignore content in slim round brackets ()"))
        self.namesMorphemizerCheckBox.setText(_translate("FrequencyFileGeneratorDialog", "Ignore names found by morphemizer"))
        self.namesFileCheckBox.setText(_translate("FrequencyFileGeneratorDialog", "Ignore names found in \"names.txt\""))
        self.numbersCheckBox.setText(_translate("FrequencyFileGeneratorDialog", "Ignore numbers"))
        self.createFrequencyFileButton.setText(_translate("FrequencyFileGeneratorDialog", "Create Frequency File"))