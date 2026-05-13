import os
import win32com.client as win32
import logging

class AspenHysys:
    def __init__(self):
        self.hysys = win32.Dispatch("HYSYS.Application")
        self.hy_case = self.hysys.Application.ActiveDocument

    def abrir(self,direccion,mostrar):
        try:
            hy_case = self.hysys.Application.ActiveDocument
            if hy_case == None:
                self.hy_case = self.hysys.SimulationCases.Open(direccion)
                self.hy_case.Visible = mostrar
                return 1
        except:
            #me fijo el formato cual es:
            formato=direccion.split(".")[1]
            if formato=="hsc":
                print("Surgió un problema al abrir el ")
            elif formato!="hsc":
                print("Formato no soportado")
            elif formato=="":
                print("Archivo no seleccionado!")
            else:
                print("error desconocido, suerte!")
            return 0
    def mostrarCorrientes(self):
        self.hysys_ms = self.hy_case.Flowsheet.MaterialStreams
        self.hysys_es = self.hy_case.Flowsheet.EnergyStreams
        if self.hysys_ms.Count > 0:
            self.mass_streams = [self.hysys_ms.Item(i).Name for i in range(0, self.hysys_ms.Count)]
        else:
            self.mass_streams = None
        if self.hysys_es.Count > 0:
            self.energy_streams = [self.hysys_es.Item(i).Name for i in range(0, self.hysys_es.Count)]
        else:
            self.energy_streams = None
        #obtengo la temperatura de la corriente
        #print(self.hysys_ms[self.mass_streams[0]].Temperature.GetValue("C"))
        return self.mass_streams,self.hysys_ms, self.energy_streams,self.hysys_es

'''
stream_mf = hysys_ms.Item("101").MolarFlow.getValue("kgmole/h")
stream_p = hysys_ms.Item("101").Pressure.getValue("bar")
print(hysys_ms.Item(0).Name)
energy_streams = [hysys_es.Item(i).Name for i in range(1, hysys_es.Count + 1)]
print("Energy Streams:", energy_streams)'''


