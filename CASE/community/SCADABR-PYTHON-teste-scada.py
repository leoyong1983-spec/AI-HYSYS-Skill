# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:06:50 2021

@author: lizst
"""
# Importação das Bibliotecas
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
import numpy as np
from scipy.optimize import fsolve
import time


# Classe incial para escrita e leitura
class FloatModbusClient(ModbusClient):
    def read_float(self, address, number=1):
        reg_l = self.read_holding_registers(address, number * 2)
        if reg_l:
            return [utils.decode_ieee(f) for f in utils.word_list_to_long(reg_l)]
        else:
            return None

    def write_float(self, address, floats_list):
        b32_l = [utils.encode_ieee(f) for f in floats_list]
        b16_l = utils.long_list_to_word(b32_l)
        return self.write_multiple_registers(address, b16_l)



# TCP auto connect on first modbus request
# c = ModbusClient() # Objeto de conecção do Modbus
c = FloatModbusClient(host='localhost', port=5028, auto_open=True)

while 1<2:
    # teste de escrita
    if c.write_float(0, [10,20,30]):
        print("write ok")
    else:
        print("write error")

# teste de leitura
regs = c.read_holding_registers(0, 2)
if regs:
    print(regs)
    print("read ok")
else:
    print("read error")
