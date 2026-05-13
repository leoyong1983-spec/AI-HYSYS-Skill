# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(597, 473)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 101, 31))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 16, 341, 20))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 110, 101, 22))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 101, 31))
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(10, 170, 101, 22))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 140, 61, 31))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 210, 121, 31))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 250, 61, 20))
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 46, 101, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Abrir archivo Hysys", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Default", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Corriente de proceso", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Propiedades", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Mostrar propiedad ", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Default", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Mostrar al abrir", None))
    # retranslateUi

