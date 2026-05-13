# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIcjCyCN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import json
import sys
#importo el metodo abrirCase desde model.py
from model import modelo
m= modelo()
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(597, 473)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.abrirCase)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 16, 341, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 110, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 101, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 170, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 61, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 250, 61, 20))
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(10, 46, 101, 21))
        self.checkBox.setObjectName("checkBox")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def abrirCase(self):
        #abro una widget para seleccionar un archivo y extraer si direccion para abrirlo
        self.dialog = QFileDialog()
        self.dirCase=self.dialog.getOpenFileName()[0] #direccion del case que voy a abrir.
        self.label.setText(self.dirCase)
        #guardo la direccion del case en un json
        #si el checkbutton efsta clickeado guardo en el json guardo 1 sino 0
        #guardo la direccion del case en un json
        self.mStreams,self.eStreams=m.abrirCase_m(self.dirCase)
        self.comboBox.addItems(self.mStreams)


    def updateUI(self):
        self.jsonGUI=json.load(open("json/jsonHysys.json"))
        self.jsonGUI["ConfigCase"]["direccionCase"]=self.dirCase
        if self.checkBox.isChecked():
            self.jsonGUI["ConfigCase"]["abrirCase"]=1
        else:
            self.jsonGUI["ConfigCase"]["abrirCase"]=0
        with open("json/jsonHysys.json","w") as file:
            json.dump(self.jsonGUI,file)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Abrir archivo Hysys"))
        self.label.setText(_translate("Dialog", "Default"))
        self.label_2.setText(_translate("Dialog", "Corriente de proceso"))
        self.label_3.setText(_translate("Dialog", "Propiedades"))
        self.pushButton_2.setText(_translate("Dialog", "Mostrar propiedad "))
        self.label_4.setText(_translate("Dialog", "Default"))
        self.checkBox.setText(_translate("Dialog", "Mostrar al abrir"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

