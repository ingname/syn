# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.autores = QtWidgets.QPushButton(Dialog)
        self.autores.setGeometry(QtCore.QRect(170, 180, 75, 23))
        self.autores.setObjectName("autores")
        self.login = QtWidgets.QLineEdit(Dialog)
        self.login.setGeometry(QtCore.QRect(150, 80, 113, 20))
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(150, 120, 113, 20))
        self.password.setObjectName("password")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.autores.setText(_translate("Dialog", "Авто"))
