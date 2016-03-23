# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clients.ui'
#
# Created: Tue Mar 22 02:26:21 2016
#      by: PyQt4 UI code generator 4.11.3
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
        Form.resize(355, 141)
        self.roomLabel = QtGui.QLabel(Form)
        self.roomLabel.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.roomLabel.setObjectName(_fromUtf8("roomLabel"))
        self.responseLabel = QtGui.QLabel(Form)
        self.responseLabel.setGeometry(QtCore.QRect(10, 60, 46, 13))
        self.responseLabel.setObjectName(_fromUtf8("responseLabel"))
        self.dateLabel = QtGui.QLabel(Form)
        self.dateLabel.setGeometry(QtCore.QRect(180, 20, 46, 13))
        self.dateLabel.setObjectName(_fromUtf8("dateLabel"))
        self.roomEdit = QtGui.QLineEdit(Form)
        self.roomEdit.setGeometry(QtCore.QRect(50, 20, 113, 20))
        self.roomEdit.setObjectName(_fromUtf8("roomEdit"))
        self.dateEdit = QtGui.QLineEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(230, 20, 113, 20))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.bookButton = QtGui.QPushButton(Form)
        self.bookButton.setGeometry(QtCore.QRect(20, 110, 75, 23))
        self.bookButton.setObjectName(_fromUtf8("bookButton"))
        self.unBookButton = QtGui.QPushButton(Form)
        self.unBookButton.setGeometry(QtCore.QRect(140, 110, 75, 23))
        self.unBookButton.setObjectName(_fromUtf8("unBookButton"))
        self.quitButton = QtGui.QPushButton(Form)
        self.quitButton.setGeometry(QtCore.QRect(250, 110, 75, 23))
        self.quitButton.setObjectName(_fromUtf8("quitButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Building Services", None))
        self.roomLabel.setText(_translate("Form", "Room", None))
        self.responseLabel.setText(_translate("Form", "Response", None))
        self.dateLabel.setText(_translate("Form", "Date", None))
        self.bookButton.setText(_translate("Form", "Book", None))
        self.unBookButton.setText(_translate("Form", "Unbook", None))
        self.quitButton.setText(_translate("Form", "Quit", None))

