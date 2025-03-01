# Form implementation generated from reading ui file 'ankimorphs/ui/frequency_file_generator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FrequencyFileGeneratorWindow(object):
    def setupUi(self, FrequencyFileGeneratorWindow):
        FrequencyFileGeneratorWindow.setObjectName("FrequencyFileGeneratorWindow")
        FrequencyFileGeneratorWindow.resize(533, 437)
        FrequencyFileGeneratorWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        FrequencyFileGeneratorWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(parent=FrequencyFileGeneratorWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 437))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.inputButton.setObjectName("inputButton")
        self.verticalLayout.addWidget(self.inputButton)
        self.outputButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.outputButton.setObjectName("outputButton")
        self.verticalLayout.addWidget(self.outputButton)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inputDirLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.inputDirLineEdit.setObjectName("inputDirLineEdit")
        self.verticalLayout_2.addWidget(self.inputDirLineEdit)
        self.outputFileLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.outputFileLineEdit.setObjectName("outputFileLineEdit")
        self.verticalLayout_2.addWidget(self.outputFileLineEdit)
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txtFilesCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.txtFilesCheckBox.setObjectName("txtFilesCheckBox")
        self.horizontalLayout_3.addWidget(self.txtFilesCheckBox)
        self.srtFilesCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.srtFilesCheckBox.setObjectName("srtFilesCheckBox")
        self.horizontalLayout_3.addWidget(self.srtFilesCheckBox)
        self.vttFilesCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.vttFilesCheckBox.setObjectName("vttFilesCheckBox")
        self.horizontalLayout_3.addWidget(self.vttFilesCheckBox)
        self.mdFilesCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
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
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.minOccurrenceSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.minOccurrenceSpinBox.setMinimum(1)
        self.minOccurrenceSpinBox.setMaximum(1000)
        self.minOccurrenceSpinBox.setObjectName("minOccurrenceSpinBox")
        self.horizontalLayout_2.addWidget(self.minOccurrenceSpinBox, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 10, -1, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.squareBracketsCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.squareBracketsCheckBox.setObjectName("squareBracketsCheckBox")
        self.verticalLayout_5.addWidget(self.squareBracketsCheckBox)
        self.roundBracketsCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.roundBracketsCheckBox.setObjectName("roundBracketsCheckBox")
        self.verticalLayout_5.addWidget(self.roundBracketsCheckBox)
        self.slimRoundBracketsCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.slimRoundBracketsCheckBox.setObjectName("slimRoundBracketsCheckBox")
        self.verticalLayout_5.addWidget(self.slimRoundBracketsCheckBox)
        self.namesMorphemizerCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.namesMorphemizerCheckBox.setObjectName("namesMorphemizerCheckBox")
        self.verticalLayout_5.addWidget(self.namesMorphemizerCheckBox)
        self.namesFileCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.namesFileCheckBox.setObjectName("namesFileCheckBox")
        self.verticalLayout_5.addWidget(self.namesFileCheckBox)
        self.numbersCheckBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.numbersCheckBox.setObjectName("numbersCheckBox")
        self.verticalLayout_5.addWidget(self.numbersCheckBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.createFrequencyFileButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.createFrequencyFileButton.setStyleSheet("margin-top: 10px;\n"
"margin-bottom: 10px;\n"
"padding: 5px;")
        self.createFrequencyFileButton.setObjectName("createFrequencyFileButton")
        self.verticalLayout_3.addWidget(self.createFrequencyFileButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        FrequencyFileGeneratorWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrequencyFileGeneratorWindow)
        QtCore.QMetaObject.connectSlotsByName(FrequencyFileGeneratorWindow)

    def retranslateUi(self, FrequencyFileGeneratorWindow):
        _translate = QtCore.QCoreApplication.translate
        FrequencyFileGeneratorWindow.setWindowTitle(_translate("FrequencyFileGeneratorWindow", "Frequency File Generator"))
        self.inputButton.setText(_translate("FrequencyFileGeneratorWindow", "Select input"))
        self.outputButton.setText(_translate("FrequencyFileGeneratorWindow", "Select output"))
        self.label.setText(_translate("FrequencyFileGeneratorWindow", "Morphemizer"))
        self.label_3.setText(_translate("FrequencyFileGeneratorWindow", "File formats:"))
        self.txtFilesCheckBox.setText(_translate("FrequencyFileGeneratorWindow", ".txt"))
        self.srtFilesCheckBox.setText(_translate("FrequencyFileGeneratorWindow", ".srt"))
        self.vttFilesCheckBox.setText(_translate("FrequencyFileGeneratorWindow", ".vtt"))
        self.mdFilesCheckBox.setText(_translate("FrequencyFileGeneratorWindow", ".md"))
        self.label_2.setText(_translate("FrequencyFileGeneratorWindow", "Minimum occurrence:"))
        self.label_4.setText(_translate("FrequencyFileGeneratorWindow", "Preprocess:"))
        self.squareBracketsCheckBox.setText(_translate("FrequencyFileGeneratorWindow", "Ignore content in square brackets []"))
        self.roundBracketsCheckBox.setText(_translate("FrequencyFileGeneratorWindow", "ignore content in round brackets（）"))
        self.slimRoundBracketsCheckBox.setText(_translate("FrequencyFileGeneratorWindow", "ignore content in slim round brackets ()"))
        self.namesMorphemizerCheckBox.setText(_translate("FrequencyFileGeneratorWindow", "Ignore names found by morphemizer"))
        self.namesFileCheckBox.setText(_translate("FrequencyFileGeneratorWindow", "Ignore names found in names.txt"))
        self.numbersCheckBox.setText(_translate("FrequencyFileGeneratorWindow", "Ignore numbers"))
        self.createFrequencyFileButton.setText(_translate("FrequencyFileGeneratorWindow", "Create Frequency File"))
