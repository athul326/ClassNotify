# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'twilio.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

#  UI for the dialog window that takes in Twilio API info
class Ui_twilioWindow(object):
    def setupUi(self, twilioWindow):
        twilioWindow.setObjectName("twilioWindow")
        twilioWindow.resize(637, 250)
        self.accountId = QtWidgets.QLineEdit(twilioWindow)
        self.accountId.setGeometry(QtCore.QRect(40, 20, 561, 21))
        self.accountId.setObjectName("accountId")
        self.authKey = QtWidgets.QLineEdit(twilioWindow)
        self.authKey.setGeometry(QtCore.QRect(40, 70, 561, 21))
        self.authKey.setObjectName("authKey")
        self.twilioNum = QtWidgets.QLineEdit(twilioWindow)
        self.twilioNum.setGeometry(QtCore.QRect(40, 120, 561, 21))
        self.twilioNum.setObjectName("twilioNum")
        self.yourNum = QtWidgets.QLineEdit(twilioWindow)
        self.yourNum.setGeometry(QtCore.QRect(40, 170, 561, 21))
        self.yourNum.setObjectName("yourNum")
        self.confirmButton = QtWidgets.QPushButton(twilioWindow)
        self.confirmButton.setGeometry(QtCore.QRect(270, 210, 93, 28))
        self.confirmButton.setObjectName("confirmButton")

        self.retranslateUi(twilioWindow)
        QtCore.QMetaObject.connectSlotsByName(twilioWindow)

    def retranslateUi(self, twilioWindow):
        _translate = QtCore.QCoreApplication.translate
        twilioWindow.setWindowTitle(_translate("twilioWindow", "Dialog"))
        self.accountId.setText(_translate("twilioWindow", "Twilio Account ID"))
        self.authKey.setText(_translate("twilioWindow", "Twilio Authentication Key"))
        self.twilioNum.setText(_translate("twilioWindow", "Twilio Phone Number (Include +1)"))
        self.yourNum.setText(_translate("twilioWindow", "Your Phone Number (Include +1)"))
        self.confirmButton.setText(_translate("twilioWindow", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    twilioWindow = QtWidgets.QDialog()
    ui = Ui_twilioWindow()
    ui.setupUi(twilioWindow)
    twilioWindow.show()
    sys.exit(app.exec_())
