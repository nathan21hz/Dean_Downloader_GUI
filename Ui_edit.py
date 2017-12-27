# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Coding\CFile_new\edit.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(225, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(225, 200))
        Dialog.setMaximumSize(QtCore.QSize(225, 200))
        Dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.code_edit = QtWidgets.QLineEdit(Dialog)
        self.code_edit.setGeometry(QtCore.QRect(20, 40, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.code_edit.setFont(font)
        self.code_edit.setObjectName("code_edit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.teacher_edit = QtWidgets.QLineEdit(Dialog)
        self.teacher_edit.setGeometry(QtCore.QRect(20, 100, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.teacher_edit.setFont(font)
        self.teacher_edit.setObjectName("teacher_edit")
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setGeometry(QtCore.QRect(40, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.ok_button.setFont(font)
        self.ok_button.setObjectName("ok_button")

        self.retranslateUi(Dialog)
        self.ok_button.clicked.connect(self.doEdit)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加/修改课程"))
        self.label.setText(_translate("Dialog", "课程代码："))
        self.label_2.setText(_translate("Dialog", "授课教师："))
        self.ok_button.setText(_translate("Dialog", "确定"))
