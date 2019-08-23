import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QProcess, QObject, QThread
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget,QListWidget
import qtmodern.styles
import qtmodern.windows
import classList
import apikeys
import main
import time
from test import Ui_MainWindow
from add import Ui_addClass
from twilioDialog import Ui_twilioWindow

# handles main GUI window
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.openAdd)
        self.removeButton.clicked.connect(self.openDelete)
        self.twilioButton.clicked.connect(self.openTwilio)
        self.stopButton.clicked.connect(self.stopProg)
        self.thread = QThread()  # new thread that starts backend search function when start button is clicked
        self.worker = worker()
        self.worker.moveToThread(self.thread)
        self.startButton.clicked.connect(self.thread.start)
        self.thread.started.connect(self.worker.work)
    # opens add window when add button is clicked
    def openAdd(self):
        self.addWindow = addClass()
        self.addWindow.show()
        self.addWindow.listAdd.connect(self.addList)
    # adds information received from addClass window to main GUI listwidget
    def addList(self, string):
        self.listWidget.addItem(string)
    # deletes class info from backend dictionary and from GUI listwidget
    def openDelete(self):
        classList.userClasses.pop(str(self.listWidget.currentItem().text()[0:8]))
        listItems = self.listWidget.selectedItems()
        for item in listItems:
            self.listWidget.takeItem(self.listWidget.row(item))
        print(classList.classString)
    # opens twilio info dialog box
    def openTwilio(self):
        self.twilioWindow = twilioClass()
        self.twilioWindow.show()
    # stops search function
    def stopProg(self):
        self.worker.run = False

# handles dialog box for taking in class information
class addClass(QtWidgets.QMainWindow, Ui_addClass):
    listAdd = QtCore.pyqtSignal(str)
    def __init__(self):
        super(addClass, self).__init__()
        self.setupUi(self)
        self.confirmButton.clicked.connect(self.confirm)
    def confirm(self):
        sectionList = self.sectionLine.text().split(',')
        classList.userClasses[self.courseBox.currentText()+' '+self.courseLine.text()] = sectionList
        string = str(self.courseBox.currentText() + ' ' + self.courseLine.text() + ' - ' + self.sectionLine.text())
        self.listAdd.emit(string)
        self.close()

# handles twilio dialog box
class twilioClass(QtWidgets.QDialog,Ui_twilioWindow):
    def __init__(self):
        super(twilioClass, self).__init__()
        self.setupUi(self)
        self.confirmButton.clicked.connect(self.confirm)
    def confirm(self):
        apikeys.accountID = self.accountId.text()
        apikeys.authKey = self.authKey.text()
        apikeys.fromNumber = self.twilioNum.text()
        apikeys.toNumber = self.yourNum.text()
        self.close()

# worker object that runs backend search function
class worker(QObject):
    def __init__(self):
        super(worker,self).__init__()
        self.run = True
    def work(self):
        while self.run:
            main.search(main.main())
            time.sleep(300)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
qtmodern.styles.dark(app)
mw = qtmodern.windows.ModernWindow(window)
mw.show()
app.exec_()
