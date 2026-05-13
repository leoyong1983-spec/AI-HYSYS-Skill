
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSignal
import sys
import os
import json
from hysys2Python import AspenHysys 
hsc=AspenHysys()

class modelo:
    def __init__(self):
        #creo una señalpara vincularme con la UI
        #defino una señal del tipo pyqsignalque 
        self.apertura = pyqtSignal()

    def abrirCase_m(self,dirCase):
        #en función de la dirección seleccionada en la GUI (guardado en un json) abro el case
        #leo jsonHysys.json y lo llego a un diccionario
        self.jsonModel = json.load(open("json/jsonHysys.json"))
        self.jsonModel["ConfigCase"]["direccionCase"]=dirCase
        self.abrir=self.jsonModel["ConfigCase"]["abrirCase"]
        self.aperturaHsc=hsc.abrir(dirCase,self.abrir)
        if self.aperturaHsc==1:
            self.mStreams,self.hysysM,self.eStreams,self.hysysE=hsc.mostrarCorrientes() #me devuelve las corrientes
            #las guardo en el json
            print(self.hysysM[self.mStreams[0]].Temperature.GetValue("C"))
            self.jsonModel["corrientes"]=self.mStreams
            #guardo el json
            with open("json/jsonHysys.json","w") as file:
                json.dump(self.jsonModel,file)
        else:
            print("case no abierto")
        return self.mStreams,self.eStreams

    def mostrarPropiedades(self):
        print("mostrar propiedad")
'''
if __name__ == "__main__":
    app = QApplication()
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    #aplico las modificaciones de modelo gui
    modelo=modelo()
    sys.exit(app.exec_())'''