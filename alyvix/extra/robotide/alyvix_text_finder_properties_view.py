# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alyvix_text_finder_properties_view.ui'
#
# Created: Thu May 10 00:17:13 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(561, 504)
        self.pushButtonCancel = QtGui.QPushButton(Form)
        self.pushButtonCancel.setGeometry(QtCore.QRect(478, 457, 75, 23))
        self.pushButtonCancel.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.pushButtonOk = QtGui.QPushButton(Form)
        self.pushButtonOk.setGeometry(QtCore.QRect(395, 457, 75, 23))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.label_line = QtGui.QLabel(Form)
        self.label_line.setGeometry(QtCore.QRect(70, 10110, 61, 21))
        self.label_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_line.setObjectName(_fromUtf8("label_line"))
        self.spinBoxLine = QtGui.QSpinBox(Form)
        self.spinBoxLine.setGeometry(QtCore.QRect(141, 10109, 121, 22))
        self.spinBoxLine.setMinimum(1)
        self.spinBoxLine.setMaximum(99999)
        self.spinBoxLine.setObjectName(_fromUtf8("spinBoxLine"))
        self.pushButtonAddBlock = QtGui.QPushButton(Form)
        self.pushButtonAddBlock.setGeometry(QtCore.QRect(271, 10109, 71, 23))
        self.pushButtonAddBlock.setObjectName(_fromUtf8("pushButtonAddBlock"))
        self.listWidgetBlocks = QtGui.QListWidget(Form)
        self.listWidgetBlocks.setGeometry(QtCore.QRect(484, 9835, 81, 302))
        self.listWidgetBlocks.setObjectName(_fromUtf8("listWidgetBlocks"))
        self.textEditCustomLines = QtGui.QTextEdit(Form)
        self.textEditCustomLines.setGeometry(QtCore.QRect(19, 9836, 457, 261))
        self.textEditCustomLines.setTabStopWidth(80)
        self.textEditCustomLines.setAcceptRichText(False)
        self.textEditCustomLines.setObjectName(_fromUtf8("textEditCustomLines"))
        self.pushButtonRemoveBlock = QtGui.QPushButton(Form)
        self.pushButtonRemoveBlock.setGeometry(QtCore.QRect(351, 10109, 91, 23))
        self.pushButtonRemoveBlock.setObjectName(_fromUtf8("pushButtonRemoveBlock"))
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(171, 9000, 381, 348))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.widget_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 380, 333))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.dontclickRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.dontclickRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dontclickRadio_2.setChecked(True)
        self.dontclickRadio_2.setObjectName(_fromUtf8("dontclickRadio_2"))
        self.buttonGroup_4 = QtGui.QButtonGroup(Form)
        self.buttonGroup_4.setObjectName(_fromUtf8("buttonGroup_4"))
        self.buttonGroup_4.addButton(self.dontclickRadio_2)
        self.gridLayout_2.addWidget(self.dontclickRadio_2, 5, 3, 1, 1)
        self.labelClickNumber_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.labelClickNumber_2.setEnabled(False)
        self.labelClickNumber_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelClickNumber_2.setObjectName(_fromUtf8("labelClickNumber_2"))
        self.gridLayout_2.addWidget(self.labelClickNumber_2, 6, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.add_quotes_ocr_2 = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.add_quotes_ocr_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.add_quotes_ocr_2.setChecked(True)
        self.add_quotes_ocr_2.setObjectName(_fromUtf8("add_quotes_ocr_2"))
        self.gridLayout_2.addWidget(self.add_quotes_ocr_2, 0, 3, 1, 1)
        self.lineEditWhiteList_2 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditWhiteList_2.setObjectName(_fromUtf8("lineEditWhiteList_2"))
        self.gridLayout_2.addWidget(self.lineEditWhiteList_2, 2, 1, 1, 3)
        self.clicknumber_spinbox_2 = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.clicknumber_spinbox_2.setEnabled(False)
        self.clicknumber_spinbox_2.setMinimum(1)
        self.clicknumber_spinbox_2.setObjectName(_fromUtf8("clicknumber_spinbox_2"))
        self.gridLayout_2.addWidget(self.clicknumber_spinbox_2, 6, 3, 1, 1)
        self.holdreleaseSpinBox_2 = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.holdreleaseSpinBox_2.setEnabled(False)
        self.holdreleaseSpinBox_2.setMinimum(1)
        self.holdreleaseSpinBox_2.setMaximum(9999)
        self.holdreleaseSpinBox_2.setObjectName(_fromUtf8("holdreleaseSpinBox_2"))
        self.gridLayout_2.addWidget(self.holdreleaseSpinBox_2, 8, 3, 1, 1)
        self.pushButtonXYoffset_2 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButtonXYoffset_2.setEnabled(False)
        self.pushButtonXYoffset_2.setObjectName(_fromUtf8("pushButtonXYoffset_2"))
        self.gridLayout_2.addWidget(self.pushButtonXYoffset_2, 6, 1, 2, 1)
        self.rightclickRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.rightclickRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.rightclickRadio_2.setObjectName(_fromUtf8("rightclickRadio_2"))
        self.buttonGroup_4.addButton(self.rightclickRadio_2)
        self.gridLayout_2.addWidget(self.rightclickRadio_2, 5, 1, 1, 1)
        self.text_encrypted_2 = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.text_encrypted_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.text_encrypted_2.setChecked(False)
        self.text_encrypted_2.setObjectName(_fromUtf8("text_encrypted_2"))
        self.gridLayout_2.addWidget(self.text_encrypted_2, 11, 3, 1, 1)
        self.lineEditText_2 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditText_2.setObjectName(_fromUtf8("lineEditText_2"))
        self.gridLayout_2.addWidget(self.lineEditText_2, 0, 1, 1, 2)
        self.clickdelay_spinbox_2 = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.clickdelay_spinbox_2.setEnabled(False)
        self.clickdelay_spinbox_2.setMinimum(1)
        self.clickdelay_spinbox_2.setMaximum(60000)
        self.clickdelay_spinbox_2.setProperty("value", 10)
        self.clickdelay_spinbox_2.setObjectName(_fromUtf8("clickdelay_spinbox_2"))
        self.gridLayout_2.addWidget(self.clickdelay_spinbox_2, 7, 3, 1, 1)
        self.line_5 = QtGui.QFrame(self.gridLayoutWidget_2)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_2.addWidget(self.line_5, 4, 0, 1, 4)
        self.labelClickDelay_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.labelClickDelay_2.setEnabled(False)
        self.labelClickDelay_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelClickDelay_2.setObjectName(_fromUtf8("labelClickDelay_2"))
        self.gridLayout_2.addWidget(self.labelClickDelay_2, 7, 2, 1, 1)
        self.inserttext_2 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.inserttext_2.setObjectName(_fromUtf8("inserttext_2"))
        self.gridLayout_2.addWidget(self.inserttext_2, 9, 0, 1, 4)
        self.text_label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.text_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text_label_2.setObjectName(_fromUtf8("text_label_2"))
        self.gridLayout_2.addWidget(self.text_label_2, 0, 0, 1, 1)
        self.clickRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.clickRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.clickRadio_2.setObjectName(_fromUtf8("clickRadio_2"))
        self.buttonGroup_4.addButton(self.clickRadio_2)
        self.gridLayout_2.addWidget(self.clickRadio_2, 5, 0, 1, 1)
        self.pushButtonCheck_2 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButtonCheck_2.setObjectName(_fromUtf8("pushButtonCheck_2"))
        self.gridLayout_2.addWidget(self.pushButtonCheck_2, 3, 1, 1, 1)
        self.add_quotes_2 = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.add_quotes_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.add_quotes_2.setChecked(True)
        self.add_quotes_2.setObjectName(_fromUtf8("add_quotes_2"))
        self.gridLayout_2.addWidget(self.add_quotes_2, 11, 2, 1, 1)
        self.lang_label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.lang_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lang_label_2.setObjectName(_fromUtf8("lang_label_2"))
        self.gridLayout_2.addWidget(self.lang_label_2, 1, 0, 1, 1)
        self.movemouseRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.movemouseRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.movemouseRadio_2.setChecked(False)
        self.movemouseRadio_2.setObjectName(_fromUtf8("movemouseRadio_2"))
        self.buttonGroup_4.addButton(self.movemouseRadio_2)
        self.gridLayout_2.addWidget(self.movemouseRadio_2, 5, 2, 1, 1)
        self.labelSendKeysDelay_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.labelSendKeysDelay_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSendKeysDelay_2.setObjectName(_fromUtf8("labelSendKeysDelay_2"))
        self.gridLayout_2.addWidget(self.labelSendKeysDelay_2, 10, 0, 1, 1)
        self.spinBoxSendKeysDelay_2 = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.spinBoxSendKeysDelay_2.setMaximum(60000)
        self.spinBoxSendKeysDelay_2.setProperty("value", 15)
        self.spinBoxSendKeysDelay_2.setObjectName(_fromUtf8("spinBoxSendKeysDelay_2"))
        self.gridLayout_2.addWidget(self.spinBoxSendKeysDelay_2, 10, 1, 1, 1)
        self.spinBoxSendKeysDuration_2 = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.spinBoxSendKeysDuration_2.setMaximum(60000)
        self.spinBoxSendKeysDuration_2.setProperty("value", 15)
        self.spinBoxSendKeysDuration_2.setObjectName(_fromUtf8("spinBoxSendKeysDuration_2"))
        self.gridLayout_2.addWidget(self.spinBoxSendKeysDuration_2, 10, 3, 1, 1)
        self.labelSendKeysDuration_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.labelSendKeysDuration_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSendKeysDuration_2.setObjectName(_fromUtf8("labelSendKeysDuration_2"))
        self.gridLayout_2.addWidget(self.labelSendKeysDuration_2, 10, 2, 1, 1)
        self.comboBoxLang_2 = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.comboBoxLang_2.setObjectName(_fromUtf8("comboBoxLang_2"))
        self.gridLayout_2.addWidget(self.comboBoxLang_2, 1, 1, 1, 2)
        self.holdreleaseRadio_2 = QtGui.QRadioButton(self.gridLayoutWidget_2)
        self.holdreleaseRadio_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.holdreleaseRadio_2.setObjectName(_fromUtf8("holdreleaseRadio_2"))
        self.buttonGroup_4.addButton(self.holdreleaseRadio_2)
        self.gridLayout_2.addWidget(self.holdreleaseRadio_2, 8, 0, 1, 1)
        self.holdreleaseComboBox_2 = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.holdreleaseComboBox_2.setEnabled(False)
        self.holdreleaseComboBox_2.setObjectName(_fromUtf8("holdreleaseComboBox_2"))
        self.holdreleaseComboBox_2.addItem(_fromUtf8(""))
        self.holdreleaseComboBox_2.addItem(_fromUtf8(""))
        self.holdreleaseComboBox_2.addItem(_fromUtf8(""))
        self.holdreleaseComboBox_2.addItem(_fromUtf8(""))
        self.holdreleaseComboBox_2.addItem(_fromUtf8(""))
        self.holdreleaseComboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.holdreleaseComboBox_2, 8, 1, 1, 1)
        self.labelPixels_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.labelPixels_2.setEnabled(False)
        self.labelPixels_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPixels_2.setObjectName(_fromUtf8("labelPixels_2"))
        self.gridLayout_2.addWidget(self.labelPixels_2, 8, 2, 1, 1)
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(9, 9, 157, 421))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidget.addItem(item)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(173, 9, 381, 431))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayoutWidget = QtGui.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 380, 421))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.rightclickRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.rightclickRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.rightclickRadio.setObjectName(_fromUtf8("rightclickRadio"))
        self.buttonGroup_2 = QtGui.QButtonGroup(Form)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.rightclickRadio)
        self.gridLayout.addWidget(self.rightclickRadio, 9, 1, 1, 1)
        self.add_quotes = QtGui.QCheckBox(self.gridLayoutWidget)
        self.add_quotes.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.add_quotes.setChecked(True)
        self.add_quotes.setObjectName(_fromUtf8("add_quotes"))
        self.gridLayout.addWidget(self.add_quotes, 15, 2, 1, 1)
        self.labelClickDelay = QtGui.QLabel(self.gridLayoutWidget)
        self.labelClickDelay.setEnabled(False)
        self.labelClickDelay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelClickDelay.setObjectName(_fromUtf8("labelClickDelay"))
        self.gridLayout.addWidget(self.labelClickDelay, 11, 2, 1, 1)
        self.pushButtonXYoffset = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButtonXYoffset.setEnabled(False)
        self.pushButtonXYoffset.setObjectName(_fromUtf8("pushButtonXYoffset"))
        self.gridLayout.addWidget(self.pushButtonXYoffset, 10, 1, 2, 1)
        self.clickdelay_spinbox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.clickdelay_spinbox.setEnabled(False)
        self.clickdelay_spinbox.setMinimum(1)
        self.clickdelay_spinbox.setMaximum(60000)
        self.clickdelay_spinbox.setProperty("value", 10)
        self.clickdelay_spinbox.setObjectName(_fromUtf8("clickdelay_spinbox"))
        self.gridLayout.addWidget(self.clickdelay_spinbox, 11, 3, 1, 1)
        self.dontclickRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.dontclickRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dontclickRadio.setChecked(True)
        self.dontclickRadio.setObjectName(_fromUtf8("dontclickRadio"))
        self.buttonGroup_2.addButton(self.dontclickRadio)
        self.gridLayout.addWidget(self.dontclickRadio, 9, 3, 1, 1)
        self.add_quotes_ocr = QtGui.QCheckBox(self.gridLayoutWidget)
        self.add_quotes_ocr.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.add_quotes_ocr.setChecked(True)
        self.add_quotes_ocr.setObjectName(_fromUtf8("add_quotes_ocr"))
        self.gridLayout.addWidget(self.add_quotes_ocr, 3, 3, 1, 1)
        self.lang_label = QtGui.QLabel(self.gridLayoutWidget)
        self.lang_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lang_label.setObjectName(_fromUtf8("lang_label"))
        self.gridLayout.addWidget(self.lang_label, 5, 0, 1, 1)
        self.clicknumber_spinbox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.clicknumber_spinbox.setEnabled(False)
        self.clicknumber_spinbox.setMinimum(1)
        self.clicknumber_spinbox.setObjectName(_fromUtf8("clicknumber_spinbox"))
        self.gridLayout.addWidget(self.clicknumber_spinbox, 10, 3, 1, 1)
        self.pushButtonCheck = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButtonCheck.setObjectName(_fromUtf8("pushButtonCheck"))
        self.gridLayout.addWidget(self.pushButtonCheck, 7, 1, 1, 1)
        self.text_encrypted = QtGui.QCheckBox(self.gridLayoutWidget)
        self.text_encrypted.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.text_encrypted.setChecked(False)
        self.text_encrypted.setObjectName(_fromUtf8("text_encrypted"))
        self.gridLayout.addWidget(self.text_encrypted, 15, 3, 1, 1)
        self.movemouseRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.movemouseRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.movemouseRadio.setChecked(False)
        self.movemouseRadio.setObjectName(_fromUtf8("movemouseRadio"))
        self.buttonGroup_2.addButton(self.movemouseRadio)
        self.gridLayout.addWidget(self.movemouseRadio, 9, 2, 1, 1)
        self.line_8 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout.addWidget(self.line_8, 8, 0, 1, 4)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)
        self.lineEditWhiteList = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEditWhiteList.setObjectName(_fromUtf8("lineEditWhiteList"))
        self.gridLayout.addWidget(self.lineEditWhiteList, 6, 1, 1, 3)
        self.inserttext = QtGui.QLineEdit(self.gridLayoutWidget)
        self.inserttext.setObjectName(_fromUtf8("inserttext"))
        self.gridLayout.addWidget(self.inserttext, 13, 0, 1, 4)
        self.labelClickNumber = QtGui.QLabel(self.gridLayoutWidget)
        self.labelClickNumber.setEnabled(False)
        self.labelClickNumber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelClickNumber.setObjectName(_fromUtf8("labelClickNumber"))
        self.gridLayout.addWidget(self.labelClickNumber, 10, 2, 1, 1)
        self.text_label = QtGui.QLabel(self.gridLayoutWidget)
        self.text_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text_label.setObjectName(_fromUtf8("text_label"))
        self.gridLayout.addWidget(self.text_label, 3, 0, 1, 1)
        self.clickRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.clickRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.clickRadio.setObjectName(_fromUtf8("clickRadio"))
        self.buttonGroup_2.addButton(self.clickRadio)
        self.gridLayout.addWidget(self.clickRadio, 9, 0, 1, 1)
        self.spinBoxSendKeysDelay = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBoxSendKeysDelay.setMaximum(60000)
        self.spinBoxSendKeysDelay.setProperty("value", 15)
        self.spinBoxSendKeysDelay.setObjectName(_fromUtf8("spinBoxSendKeysDelay"))
        self.gridLayout.addWidget(self.spinBoxSendKeysDelay, 14, 1, 1, 1)
        self.labelSendKeysDuration = QtGui.QLabel(self.gridLayoutWidget)
        self.labelSendKeysDuration.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSendKeysDuration.setObjectName(_fromUtf8("labelSendKeysDuration"))
        self.gridLayout.addWidget(self.labelSendKeysDuration, 14, 2, 1, 1)
        self.labelSendKeysDelay = QtGui.QLabel(self.gridLayoutWidget)
        self.labelSendKeysDelay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSendKeysDelay.setObjectName(_fromUtf8("labelSendKeysDelay"))
        self.gridLayout.addWidget(self.labelSendKeysDelay, 14, 0, 1, 1)
        self.labelName = QtGui.QLabel(self.gridLayoutWidget)
        self.labelName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)
        self.holdreleaseSpinBox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.holdreleaseSpinBox.setEnabled(False)
        self.holdreleaseSpinBox.setMinimum(1)
        self.holdreleaseSpinBox.setMaximum(9999)
        self.holdreleaseSpinBox.setObjectName(_fromUtf8("holdreleaseSpinBox"))
        self.gridLayout.addWidget(self.holdreleaseSpinBox, 12, 3, 1, 1)
        self.enable_scraper = QtGui.QCheckBox(self.gridLayoutWidget)
        self.enable_scraper.setEnabled(True)
        self.enable_scraper.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.enable_scraper.setChecked(False)
        self.enable_scraper.setObjectName(_fromUtf8("enable_scraper"))
        self.gridLayout.addWidget(self.enable_scraper, 5, 3, 1, 1)
        self.line_3 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 2, 0, 1, 4)
        self.namelineedit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.namelineedit.setObjectName(_fromUtf8("namelineedit"))
        self.gridLayout.addWidget(self.namelineedit, 0, 1, 1, 3)
        self.spinBoxSendKeysDuration = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBoxSendKeysDuration.setMaximum(60000)
        self.spinBoxSendKeysDuration.setProperty("value", 15)
        self.spinBoxSendKeysDuration.setObjectName(_fromUtf8("spinBoxSendKeysDuration"))
        self.gridLayout.addWidget(self.spinBoxSendKeysDuration, 14, 3, 1, 1)
        self.lineEditText = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEditText.setObjectName(_fromUtf8("lineEditText"))
        self.gridLayout.addWidget(self.lineEditText, 3, 1, 1, 2)
        self.labelArgs = QtGui.QLabel(self.gridLayoutWidget)
        self.labelArgs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelArgs.setObjectName(_fromUtf8("labelArgs"))
        self.gridLayout.addWidget(self.labelArgs, 1, 2, 1, 1)
        self.spinBoxArgs = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBoxArgs.setObjectName(_fromUtf8("spinBoxArgs"))
        self.gridLayout.addWidget(self.spinBoxArgs, 1, 3, 1, 1)
        self.comboBoxLang = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBoxLang.setObjectName(_fromUtf8("comboBoxLang"))
        self.gridLayout.addWidget(self.comboBoxLang, 5, 1, 1, 2)
        self.holdreleaseRadio = QtGui.QRadioButton(self.gridLayoutWidget)
        self.holdreleaseRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.holdreleaseRadio.setObjectName(_fromUtf8("holdreleaseRadio"))
        self.buttonGroup_2.addButton(self.holdreleaseRadio)
        self.gridLayout.addWidget(self.holdreleaseRadio, 12, 0, 1, 1)
        self.holdreleaseComboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.holdreleaseComboBox.setEnabled(False)
        self.holdreleaseComboBox.setObjectName(_fromUtf8("holdreleaseComboBox"))
        self.holdreleaseComboBox.addItem(_fromUtf8(""))
        self.holdreleaseComboBox.addItem(_fromUtf8(""))
        self.holdreleaseComboBox.addItem(_fromUtf8(""))
        self.holdreleaseComboBox.addItem(_fromUtf8(""))
        self.holdreleaseComboBox.addItem(_fromUtf8(""))
        self.holdreleaseComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.holdreleaseComboBox, 12, 1, 1, 1)
        self.labelPixels = QtGui.QLabel(self.gridLayoutWidget)
        self.labelPixels.setEnabled(False)
        self.labelPixels.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPixels.setObjectName(_fromUtf8("labelPixels"))
        self.gridLayout.addWidget(self.labelPixels, 12, 2, 1, 1)
        self.roi_width_label = QtGui.QLabel(Form)
        self.roi_width_label.setGeometry(QtCore.QRect(45, 9799, 89, 20))
        self.roi_width_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_width_label.setObjectName(_fromUtf8("roi_width_label"))
        self.roi_height_label = QtGui.QLabel(Form)
        self.roi_height_label.setGeometry(QtCore.QRect(234, 9799, 94, 20))
        self.roi_height_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_height_label.setObjectName(_fromUtf8("roi_height_label"))
        self.roi_y_spinbox = QtGui.QSpinBox(Form)
        self.roi_y_spinbox.setGeometry(QtCore.QRect(334, 9771, 89, 20))
        self.roi_y_spinbox.setMinimum(-9999)
        self.roi_y_spinbox.setMaximum(9999)
        self.roi_y_spinbox.setObjectName(_fromUtf8("roi_y_spinbox"))
        self.roi_x_label = QtGui.QLabel(Form)
        self.roi_x_label.setGeometry(QtCore.QRect(45, 9771, 89, 20))
        self.roi_x_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_x_label.setObjectName(_fromUtf8("roi_x_label"))
        self.roi_y_label = QtGui.QLabel(Form)
        self.roi_y_label.setGeometry(QtCore.QRect(234, 9771, 94, 20))
        self.roi_y_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roi_y_label.setObjectName(_fromUtf8("roi_y_label"))
        self.roi_x_spinbox = QtGui.QSpinBox(Form)
        self.roi_x_spinbox.setGeometry(QtCore.QRect(140, 9771, 88, 20))
        self.roi_x_spinbox.setMinimum(-9999)
        self.roi_x_spinbox.setMaximum(9999)
        self.roi_x_spinbox.setObjectName(_fromUtf8("roi_x_spinbox"))
        self.roi_height_spinbox = QtGui.QSpinBox(Form)
        self.roi_height_spinbox.setGeometry(QtCore.QRect(334, 9799, 89, 20))
        self.roi_height_spinbox.setMaximum(9999)
        self.roi_height_spinbox.setObjectName(_fromUtf8("roi_height_spinbox"))
        self.line_9 = QtGui.QFrame(Form)
        self.line_9.setGeometry(QtCore.QRect(45, 9827, 378, 3))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.roi_width_spinbox = QtGui.QSpinBox(Form)
        self.roi_width_spinbox.setGeometry(QtCore.QRect(140, 9799, 88, 20))
        self.roi_width_spinbox.setMaximum(9999)
        self.roi_width_spinbox.setObjectName(_fromUtf8("roi_width_spinbox"))
        self.find_radio = QtGui.QRadioButton(Form)
        self.find_radio.setGeometry(QtCore.QRect(66, 8000, 88, 17))
        self.find_radio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.find_radio.setObjectName(_fromUtf8("find_radio"))
        self.buttonGroup_5 = QtGui.QButtonGroup(Form)
        self.buttonGroup_5.setObjectName(_fromUtf8("buttonGroup_5"))
        self.buttonGroup_5.addButton(self.find_radio)
        self.doubleSpinBoxWarning = QtGui.QDoubleSpinBox(Form)
        self.doubleSpinBoxWarning.setGeometry(QtCore.QRect(160, 6000, 88, 20))
        self.doubleSpinBoxWarning.setMaximum(9999.99)
        self.doubleSpinBoxWarning.setSingleStep(1.0)
        self.doubleSpinBoxWarning.setObjectName(_fromUtf8("doubleSpinBoxWarning"))
        self.wait_disapp_radio = QtGui.QRadioButton(Form)
        self.wait_disapp_radio.setGeometry(QtCore.QRect(354, 6000, 89, 17))
        self.wait_disapp_radio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.wait_disapp_radio.setChecked(False)
        self.wait_disapp_radio.setObjectName(_fromUtf8("wait_disapp_radio"))
        self.buttonGroup_5.addButton(self.wait_disapp_radio)
        self.timeout_spinbox = QtGui.QSpinBox(Form)
        self.timeout_spinbox.setGeometry(QtCore.QRect(354, 6000, 89, 20))
        self.timeout_spinbox.setMaximum(999999)
        self.timeout_spinbox.setObjectName(_fromUtf8("timeout_spinbox"))
        self.doubleSpinBoxCritical = QtGui.QDoubleSpinBox(Form)
        self.doubleSpinBoxCritical.setGeometry(QtCore.QRect(354, 6000, 89, 20))
        self.doubleSpinBoxCritical.setMaximum(9999.99)
        self.doubleSpinBoxCritical.setSingleStep(1.0)
        self.doubleSpinBoxCritical.setObjectName(_fromUtf8("doubleSpinBoxCritical"))
        self.timeout_label = QtGui.QLabel(Form)
        self.timeout_label.setGeometry(QtCore.QRect(254, 6000, 94, 20))
        self.timeout_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timeout_label.setObjectName(_fromUtf8("timeout_label"))
        self.labelCritical = QtGui.QLabel(Form)
        self.labelCritical.setGeometry(QtCore.QRect(254, 6000, 94, 20))
        self.labelCritical.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCritical.setObjectName(_fromUtf8("labelCritical"))
        self.wait_radio = QtGui.QRadioButton(Form)
        self.wait_radio.setGeometry(QtCore.QRect(65, 6000, 283, 17))
        self.wait_radio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.wait_radio.setChecked(True)
        self.wait_radio.setObjectName(_fromUtf8("wait_radio"))
        self.buttonGroup_5.addButton(self.wait_radio)
        self.timeout_exception = QtGui.QCheckBox(Form)
        self.timeout_exception.setGeometry(QtCore.QRect(65, 6000, 183, 17))
        self.timeout_exception.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.timeout_exception.setChecked(True)
        self.timeout_exception.setObjectName(_fromUtf8("timeout_exception"))
        self.checkBoxEnablePerformance = QtGui.QCheckBox(Form)
        self.checkBoxEnablePerformance.setGeometry(QtCore.QRect(254, 6000, 189, 17))
        self.checkBoxEnablePerformance.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBoxEnablePerformance.setChecked(True)
        self.checkBoxEnablePerformance.setObjectName(_fromUtf8("checkBoxEnablePerformance"))
        self.labelWarning = QtGui.QLabel(Form)
        self.labelWarning.setGeometry(QtCore.QRect(160, 6000, 89, 137))
        self.labelWarning.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelWarning.setObjectName(_fromUtf8("labelWarning"))
        self.gridLayoutWidget_3 = QtGui.QWidget(Form)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 440, 158, 54))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButtonSelAll = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButtonSelAll.setObjectName(_fromUtf8("pushButtonSelAll"))
        self.gridLayout_3.addWidget(self.pushButtonSelAll, 0, 0, 1, 1)
        self.pushButtonDesAll = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButtonDesAll.setObjectName(_fromUtf8("pushButtonDesAll"))
        self.gridLayout_3.addWidget(self.pushButtonDesAll, 0, 1, 1, 1)
        self.pushButtonDelete = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButtonDelete.setObjectName(_fromUtf8("pushButtonDelete"))
        self.gridLayout_3.addWidget(self.pushButtonDelete, 1, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Alyvix - Text Finder", None))
        self.pushButtonCancel.setText(_translate("Form", "Cancel", None))
        self.pushButtonOk.setText(_translate("Form", "Ok", None))
        self.label_line.setText(_translate("Form", "Begin Line", None))
        self.pushButtonAddBlock.setText(_translate("Form", "Add Block", None))
        self.pushButtonRemoveBlock.setText(_translate("Form", "Remove Block", None))
        self.dontclickRadio_2.setText(_translate("Form", "None", None))
        self.labelClickNumber_2.setText(_translate("Form", "Clicks", None))
        self.label_2.setText(_translate("Form", "WhiteList", None))
        self.add_quotes_ocr_2.setText(_translate("Form", "Quotes", None))
        self.pushButtonXYoffset_2.setText(_translate("Form", "Interaction\n"
"Point", None))
        self.rightclickRadio_2.setText(_translate("Form", "Right Click", None))
        self.text_encrypted_2.setText(_translate("Form", "Encrypted", None))
        self.lineEditText_2.setText(_translate("Form", "Type here the Text to find", None))
        self.labelClickDelay_2.setText(_translate("Form", "Delays [ms]", None))
        self.inserttext_2.setText(_translate("Form", "Type text strings and shortcuts", None))
        self.text_label_2.setText(_translate("Form", "Text", None))
        self.clickRadio_2.setText(_translate("Form", "Click", None))
        self.pushButtonCheck_2.setText(_translate("Form", "Check", None))
        self.add_quotes_2.setText(_translate("Form", "Quotes", None))
        self.lang_label_2.setText(_translate("Form", "Lang", None))
        self.movemouseRadio_2.setText(_translate("Form", "Move", None))
        self.labelSendKeysDelay_2.setText(_translate("Form", "Delays [ms] ", None))
        self.labelSendKeysDuration_2.setText(_translate("Form", "Duration [ms] ", None))
        self.holdreleaseRadio_2.setText(_translate("Form", "Hold\'n\'Release", None))
        self.holdreleaseComboBox_2.setItemText(0, _translate("Form", "Hold", None))
        self.holdreleaseComboBox_2.setItemText(1, _translate("Form", "Release", None))
        self.holdreleaseComboBox_2.setItemText(2, _translate("Form", "Release Up", None))
        self.holdreleaseComboBox_2.setItemText(3, _translate("Form", "Release Down", None))
        self.holdreleaseComboBox_2.setItemText(4, _translate("Form", "Release Left", None))
        self.holdreleaseComboBox_2.setItemText(5, _translate("Form", "Release Right", None))
        self.labelPixels_2.setText(_translate("Form", "Pixels [px]", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "main_component", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.rightclickRadio.setText(_translate("Form", "Right Click", None))
        self.add_quotes.setText(_translate("Form", "Quotes", None))
        self.labelClickDelay.setText(_translate("Form", "Delays [ms]", None))
        self.pushButtonXYoffset.setText(_translate("Form", "Interaction\n"
"Point", None))
        self.dontclickRadio.setText(_translate("Form", "None", None))
        self.add_quotes_ocr.setText(_translate("Form", "Quotes", None))
        self.lang_label.setText(_translate("Form", "Lang", None))
        self.pushButtonCheck.setText(_translate("Form", "Check", None))
        self.text_encrypted.setText(_translate("Form", "Encrypted", None))
        self.movemouseRadio.setText(_translate("Form", "Move", None))
        self.label.setText(_translate("Form", "WhiteList", None))
        self.inserttext.setText(_translate("Form", "Type text strings and shortcuts", None))
        self.labelClickNumber.setText(_translate("Form", "Clicks", None))
        self.text_label.setText(_translate("Form", "Text", None))
        self.clickRadio.setText(_translate("Form", "Click", None))
        self.labelSendKeysDuration.setText(_translate("Form", "Duration [ms] ", None))
        self.labelSendKeysDelay.setText(_translate("Form", "Delays [ms] ", None))
        self.labelName.setText(_translate("Form", "Name", None))
        self.enable_scraper.setText(_translate("Form", "Scraper", None))
        self.namelineedit.setText(_translate("Form", "Type the keyword name", None))
        self.lineEditText.setText(_translate("Form", "Type here the Text to find", None))
        self.labelArgs.setText(_translate("Form", "Arguments", None))
        self.holdreleaseRadio.setText(_translate("Form", "Hold\'n\'Release", None))
        self.holdreleaseComboBox.setItemText(0, _translate("Form", "Hold", None))
        self.holdreleaseComboBox.setItemText(1, _translate("Form", "Release", None))
        self.holdreleaseComboBox.setItemText(2, _translate("Form", "Release Up", None))
        self.holdreleaseComboBox.setItemText(3, _translate("Form", "Release Down", None))
        self.holdreleaseComboBox.setItemText(4, _translate("Form", "Release Left", None))
        self.holdreleaseComboBox.setItemText(5, _translate("Form", "Release Right", None))
        self.labelPixels.setText(_translate("Form", "Pixels [px]", None))
        self.roi_width_label.setText(_translate("Form", "Roi Width", None))
        self.roi_height_label.setText(_translate("Form", "Roi Height", None))
        self.roi_x_label.setText(_translate("Form", "Roi X", None))
        self.roi_y_label.setText(_translate("Form", "Roi Y", None))
        self.find_radio.setText(_translate("Form", "Find", None))
        self.wait_disapp_radio.setText(_translate("Form", "Disappeared", None))
        self.timeout_label.setText(_translate("Form", "Timeout", None))
        self.labelCritical.setText(_translate("Form", "Critical", None))
        self.wait_radio.setText(_translate("Form", "Appeared", None))
        self.timeout_exception.setText(_translate("Form", "Break", None))
        self.checkBoxEnablePerformance.setText(_translate("Form", "Performance", None))
        self.labelWarning.setText(_translate("Form", "Warning", None))
        self.pushButtonSelAll.setText(_translate("Form", "Select All", None))
        self.pushButtonDesAll.setText(_translate("Form", "Deselect All", None))
        self.pushButtonDelete.setText(_translate("Form", "Remove", None))

