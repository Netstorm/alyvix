# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alyvix_code_properties_view.ui'
#
# Created: Fri Sep 25 10:12:57 2015
#      by: PyQt4 UI code generator 4.11
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
        Form.resize(563, 292)
        self.namelineedit = QtGui.QLineEdit(Form)
        self.namelineedit.setGeometry(QtCore.QRect(200, 10, 350, 20))
        self.namelineedit.setObjectName(_fromUtf8("namelineedit"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 178, 275))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.tab_7)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 131, 33))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.pushButtonSend = QtGui.QPushButton(self.verticalLayoutWidget_6)
        self.pushButtonSend.setObjectName(_fromUtf8("pushButtonSend"))
        self.verticalLayout_6.addWidget(self.pushButtonSend)
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.verticalLayoutWidget_7 = QtGui.QWidget(self.tab_8)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 10, 131, 174))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.pushButtonMouseClick = QtGui.QPushButton(self.verticalLayoutWidget_7)
        self.pushButtonMouseClick.setObjectName(_fromUtf8("pushButtonMouseClick"))
        self.verticalLayout_7.addWidget(self.pushButtonMouseClick)
        self.pushButtonMouseDoubleClick = QtGui.QPushButton(self.verticalLayoutWidget_7)
        self.pushButtonMouseDoubleClick.setObjectName(_fromUtf8("pushButtonMouseDoubleClick"))
        self.verticalLayout_7.addWidget(self.pushButtonMouseDoubleClick)
        self.pushButtonMouseRightClick = QtGui.QPushButton(self.verticalLayoutWidget_7)
        self.pushButtonMouseRightClick.setObjectName(_fromUtf8("pushButtonMouseRightClick"))
        self.verticalLayout_7.addWidget(self.pushButtonMouseRightClick)
        self.pushButtonMouseMove = QtGui.QPushButton(self.verticalLayoutWidget_7)
        self.pushButtonMouseMove.setObjectName(_fromUtf8("pushButtonMouseMove"))
        self.verticalLayout_7.addWidget(self.pushButtonMouseMove)
        self.pushButtonMouseScroll = QtGui.QPushButton(self.verticalLayoutWidget_7)
        self.pushButtonMouseScroll.setObjectName(_fromUtf8("pushButtonMouseScroll"))
        self.verticalLayout_7.addWidget(self.pushButtonMouseScroll)
        self.pushButtonMouseDrag = QtGui.QPushButton(self.verticalLayoutWidget_7)
        self.pushButtonMouseDrag.setObjectName(_fromUtf8("pushButtonMouseDrag"))
        self.verticalLayout_7.addWidget(self.pushButtonMouseDrag)
        self.tabWidget.addTab(self.tab_8, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 131, 61))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButtonProcCreate = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonProcCreate.setObjectName(_fromUtf8("pushButtonProcCreate"))
        self.verticalLayout_2.addWidget(self.pushButtonProcCreate)
        self.pushButtonProcKill = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonProcKill.setObjectName(_fromUtf8("pushButtonProcKill"))
        self.verticalLayout_2.addWidget(self.pushButtonProcKill)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 131, 121))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButtonWinShow = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonWinShow.setObjectName(_fromUtf8("pushButtonWinShow"))
        self.verticalLayout.addWidget(self.pushButtonWinShow)
        self.pushButtonWinMaximize = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonWinMaximize.setObjectName(_fromUtf8("pushButtonWinMaximize"))
        self.verticalLayout.addWidget(self.pushButtonWinMaximize)
        self.pushButtonWinCheck = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonWinCheck.setObjectName(_fromUtf8("pushButtonWinCheck"))
        self.verticalLayout.addWidget(self.pushButtonWinCheck)
        self.pushButtonWinClose = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButtonWinClose.setObjectName(_fromUtf8("pushButtonWinClose"))
        self.verticalLayout.addWidget(self.pushButtonWinClose)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.labelArgs = QtGui.QLabel(Form)
        self.labelArgs.setGeometry(QtCore.QRect(200, 263, 46, 13))
        self.labelArgs.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelArgs.setObjectName(_fromUtf8("labelArgs"))
        self.spinBoxArgs = QtGui.QSpinBox(Form)
        self.spinBoxArgs.setGeometry(QtCore.QRect(258, 258, 60, 22))
        self.spinBoxArgs.setObjectName(_fromUtf8("spinBoxArgs"))
        self.textEdit = QtGui.QPlainTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(201, 40, 349, 210))
        self.textEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Alyvix - Custom Code", None))
        self.namelineedit.setText(_translate("Form", "Type here the name of the object", None))
        self.pushButtonSend.setText(_translate("Form", "Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "Keyboard", None))
        self.pushButtonMouseClick.setText(_translate("Form", "Click", None))
        self.pushButtonMouseDoubleClick.setText(_translate("Form", "Double Click", None))
        self.pushButtonMouseRightClick.setText(_translate("Form", "Right Click", None))
        self.pushButtonMouseMove.setText(_translate("Form", "Move", None))
        self.pushButtonMouseScroll.setText(_translate("Form", "Scroll", None))
        self.pushButtonMouseDrag.setText(_translate("Form", "Drag", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("Form", "Mouse", None))
        self.pushButtonProcCreate.setText(_translate("Form", "Create Process", None))
        self.pushButtonProcKill.setText(_translate("Form", "Kill Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Porocess", None))
        self.pushButtonWinShow.setText(_translate("Form", "Show Window", None))
        self.pushButtonWinMaximize.setText(_translate("Form", "Maximize Window", None))
        self.pushButtonWinCheck.setText(_translate("Form", "Check if Exists", None))
        self.pushButtonWinClose.setText(_translate("Form", "Close Window", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Windows", None))
        self.labelArgs.setText(_translate("Form", "Args", None))

