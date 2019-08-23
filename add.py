# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

#  UI for window that takes in class information
from PyQt5 import QtCore, QtGui, QtWidgets
import qtmodern.styles
import qtmodern.windows
import classList
class Ui_addClass(object):
    def setupUi(self, addClass):
        addClass.setObjectName("addClass")
        addClass.resize(495, 200)
        self.centralwidget = QtWidgets.QWidget(addClass)
        self.centralwidget.setObjectName("centralwidget")
        self.courseBox = QtWidgets.QComboBox(self.centralwidget)
        self.courseBox.setGeometry(QtCore.QRect(20, 50, 171, 21))
        self.courseBox.setObjectName("courseBox")
        self.courseBox.addItems(["ACCT","ADDM","AEGD","AERO","AERS","AFST","AGCJ","AGEC","AGLS","AGSC","AGSM","ALEC","ALED","ANSC","ANTH","ARAB","ARCH","ARTS","ASIA","ASTR","ATMO","ATTR","BAEN","BEFB","BESC","BICH","BIED","BIMS","BIOL","BIOT","BMEN","BUAD","BUSH","BUSN","CARC","CEHD","CHEM","CHEN","CHIN","CLAS","COMM","COSC","CPSY","CSCE","CVEN","DASC","DCED","DDHS","DPHS","ECEN","ECMT","ECON","EDAD","EDCI","EDHP","EDTC","EEBL","EHRD","ELIC","ELID","ELIG","ELIL","ELIO","ELIR","ELIT","ELIV","ENDG","ENDO","ENDS","ENGL","ENGR","ENTC","ENTO","EPFB","EPSY","ESET","ESSM","EURO","FILM","FINC","FIVS","FREN","FSTC","GENE","GEOG","GEOL","GEOP","GEOS","GERM","GS01","GS04","GS11","GS14","GS21","GSMV","GSPY","HCPI","HEFB","HISP","HIST","HLTH","HORT","HPCH","HPED","HUMA","IBST","IBUS","ICPE","IDIS","INST","INTA","INTS","ISEN","ISYS","ITAL","JAPN","JOUR","KINE","KNFB","LAND","LAW","LBAR","LCSE","LDEV","LING","LMAS","MASC","MATH","MCMD","MEEN","MEFB","MEMA","MEPS","MGMT","MKTG","MLSC","MMET","MODL","MPHY","MPIM","MSCI","MSEN","MUSC","NEXT","NRSC","NUEN","NURS","NUTR","NVSC","OCEN","OCNG","OMFP","OMFR","OMSF","ORTH","PEDD","PERF","PERI","PETE","PHAR","PHEB","PHEO","PHIL","PHLT","PHPM","PHYS","PLAN","PLPA","POLS","POSC","PROS","PSAA","PSYC","RDNG","RELS","RENR","RPTS","RUSS","SABR","SCEN","SCMT","SCSC","SEFB","SENG","SLCX","SOCI","SOMS","SOPH","SPAN","SPED","SPMT","SPSY","STAT","STLC","TAMU","TCMG","TEED","TEFB","THAR","UGST","URPN","URSC","VIBS","VIST","VIZA","VLCS","VMID","VPAR","VPAT","VSCS","VTMI","VTPB","VTPP","WFSC","WGST","WMHS"])
        self.courseLine = QtWidgets.QLineEdit(self.centralwidget)
        self.courseLine.setGeometry(QtCore.QRect(210, 50, 131, 21))
        self.courseLine.setObjectName("courseLine")
        self.sectionLine = QtWidgets.QLineEdit(self.centralwidget)
        self.sectionLine.setGeometry(QtCore.QRect(360, 50, 91, 21))
        self.sectionLine.setObjectName("sectionLine")
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(210, 90, 93, 28))
        self.confirmButton.setObjectName("confirmButton")
        addClass.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(addClass)
        self.statusbar.setObjectName("statusbar")
        addClass.setStatusBar(self.statusbar)

        self.retranslateUi(addClass)
        QtCore.QMetaObject.connectSlotsByName(addClass)

    def retranslateUi(self, addClass):
        _translate = QtCore.QCoreApplication.translate
        addClass.setWindowTitle(_translate("addClass", "Add Class"))
        self.courseLine.setText(_translate("addClass", "Course Number"))
        self.sectionLine.setText(_translate("addClass", "Section"))
        self.confirmButton.setText(_translate("addClass", "Confirm"))



