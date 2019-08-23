# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from add import Ui_addClass
import qtmodern.styles
import qtmodern.windows
import classList

# UI for main GUI window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ClassNotify")
        MainWindow.resize(632, 522)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(120, 400, 371, 31))
        self.startButton.setObjectName("startButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 30, 371, 271))
        self.listWidget.setObjectName("listWidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(420, 40, 181, 41))
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(420, 110, 181, 41))
        self.removeButton.setObjectName("removeButton")
        self.twilioButton = QtWidgets.QPushButton(self.centralwidget)
        self.twilioButton.setGeometry(QtCore.QRect(120, 350, 371, 31))
        self.twilioButton.setObjectName("twilioButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(120, 450, 371, 31))
        self.stopButton.setObjectName("stopButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.addButton.setText(_translate("MainWindow", "ADD"))
        self.removeButton.setText(_translate("MainWindow", "REMOVE"))
        self.twilioButton.setText(_translate("MainWindow","Twilio Info"))
        self.stopButton.setText(_translate("MainWindow","STOP"))
