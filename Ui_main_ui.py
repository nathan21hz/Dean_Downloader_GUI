# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Coding\CFile_new\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 566)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(487, 566))
        MainWindow.setMaximumSize(QtCore.QSize(487, 566))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 54, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.no_edit = QtWidgets.QLineEdit(self.centralWidget)
        self.no_edit.setGeometry(QtCore.QRect(20, 40, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.no_edit.setFont(font)
        self.no_edit.setText("")
        self.no_edit.setObjectName("no_edit")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 54, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pw_edit = QtWidgets.QLineEdit(self.centralWidget)
        self.pw_edit.setGeometry(QtCore.QRect(20, 100, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.pw_edit.setFont(font)
        self.pw_edit.setText("")
        self.pw_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_edit.setObjectName("pw_edit")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 54, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.check_edit = QtWidgets.QLineEdit(self.centralWidget)
        self.check_edit.setGeometry(QtCore.QRect(20, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.check_edit.setFont(font)
        self.check_edit.setText("")
        self.check_edit.setObjectName("check_edit")
        self.pic_label = QtWidgets.QLabel(self.centralWidget)
        self.pic_label.setGeometry(QtCore.QRect(100, 160, 71, 31))
        self.pic_label.setFrameShape(QtWidgets.QFrame.Box)
        self.pic_label.setMidLineWidth(0)
        self.pic_label.setText("")
        self.pic_label.setWordWrap(False)
        self.pic_label.setObjectName("pic_label")
        self.refpic_button = QtWidgets.QPushButton(self.centralWidget)
        self.refpic_button.setGeometry(QtCore.QRect(170, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.refpic_button.setFont(font)
        self.refpic_button.setObjectName("refpic_button")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(250, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.list = QtWidgets.QListWidget(self.centralWidget)
        self.list.setGeometry(QtCore.QRect(240, 40, 231, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.list.setFont(font)
        self.list.setObjectName("list")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(20, 255, 191, 1))
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.login_button = QtWidgets.QPushButton(self.centralWidget)
        self.login_button.setGeometry(QtCore.QRect(30, 210, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.route_edit = QtWidgets.QLineEdit(self.centralWidget)
        self.route_edit.setGeometry(QtCore.QRect(20, 290, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.route_edit.setFont(font)
        self.route_edit.setText("")
        self.route_edit.setObjectName("route_edit")
        self.route_button = QtWidgets.QPushButton(self.centralWidget)
        self.route_button.setGeometry(QtCore.QRect(180, 290, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.route_button.setFont(font)
        self.route_button.setObjectName("route_button")
        self.down_button = QtWidgets.QPushButton(self.centralWidget)
        self.down_button.setGeometry(QtCore.QRect(30, 340, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.down_button.setFont(font)
        self.down_button.setObjectName("down_button")
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 390, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(20, 440, 451, 1))
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 470, 451, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setGeometry(QtCore.QRect(20, 450, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.edit_button = QtWidgets.QPushButton(self.centralWidget)
        self.edit_button.setGeometry(QtCore.QRect(240, 340, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.edit_button.setFont(font)
        self.edit_button.setObjectName("edit_button")
        self.add_button = QtWidgets.QPushButton(self.centralWidget)
        self.add_button.setGeometry(QtCore.QRect(320, 340, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.del_button = QtWidgets.QPushButton(self.centralWidget)
        self.del_button.setGeometry(QtCore.QRect(390, 340, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.del_button.setFont(font)
        self.del_button.setObjectName("del_button")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.refpic_button.clicked.connect(self.refresh)
        self.login_button.clicked.connect(self.login)
        self.route_button.clicked.connect(self.sel_route)
        self.down_button.clicked.connect(self.start_down)
        self.edit_button.clicked.connect(self.list_edit)
        self.add_button.clicked.connect(self.list_add)
        self.del_button.clicked.connect(self.list_del)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "自动课件下载器 V2.1 By Nathan_21hz"))
        self.label.setText(_translate("MainWindow", "学号："))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.label_3.setText(_translate("MainWindow", "验证码："))
        self.refpic_button.setText(_translate("MainWindow", "刷新"))
        self.label_4.setText(_translate("MainWindow", "课程列表："))
        self.login_button.setText(_translate("MainWindow", "登陆"))
        self.label_6.setText(_translate("MainWindow", "下载位置："))
        self.route_button.setText(_translate("MainWindow", "..."))
        self.down_button.setText(_translate("MainWindow", "开始下载"))
        self.label_8.setText(_translate("MainWindow", "运行日志："))
        self.edit_button.setText(_translate("MainWindow", "修改"))
        self.add_button.setText(_translate("MainWindow", "添加"))
        self.del_button.setText(_translate("MainWindow", "删除"))
