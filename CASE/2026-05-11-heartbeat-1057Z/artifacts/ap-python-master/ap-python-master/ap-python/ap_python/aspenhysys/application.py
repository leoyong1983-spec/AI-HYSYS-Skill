# type 'pip install pypiwin32' to install if missing
import win32com.client
from enum import Enum


class Version(Enum):
    Default = ''
    V88 = '.V8.8'
    V9 = '.V9.0'
    V10 = '.V10.0'

class UnitConversionType_enum(Enum):
    uctUnitless = 0x41


FEMPTY = -32767.0

class Application(object):
    def __init__(self, version=Version.Default):
        self.__hyApp = win32com.client.Dispatch(
            'HYSYS.Application' + version.value)
        self.__hyApp.ChangePreferencesToMinimizePopupWindows(True)
        self.visible = False

    def open_file(self, path):
        self.__hyCase = self.__hyApp.SimulationCases.Open(path)
        self.__hyCase.Activate()

    def close(self):
        '''close application.'''
        self.__hyApp.Quit()

    def save(self):
        '''save file.'''
        self.__hyCase.Save()

    def saveas(self, path):
        '''save file.'''
        self.__hyCase.SaveAs2(path, True)

    def find_node(self, path):
        '''get backdoor variable.'''
        backdoor = win32com.client.CastTo(self.__hyCase, 'BackDoor')
        return backdoor.BackDoorRealVariable(path).Variable

    def print_streams(self):
        '''print stream list.'''
        raise NotImplementedError

    def print_blocks(self):
        '''print block list.'''
        raise NotImplementedError

    def get_value(self, node, unit=None):
        '''get backdoor variable value.'''
        if unit is None:
            unit = self.__hyApp.UnitConversionSetManager.GetUnitConversionSet(
                node.UnitConversionType).CurrentDisplayUnit.name
        else:
            units = self.get_units(node)
            if unit not in units:
                raise Exception(f"Unit {unit} isn't in the available list {units}.")
        value = node.GetValue(unit)
        return (value, unit)

    def set_value(self, node, value, unit=None):
        '''set backdoor variable value.'''
        if not node.CanModify:
            raise Exception('Variable is not editable.')
        elif value == FEMPTY:
            node.Erase()
        else:
            if unit is None:
                if node.UnitConversionType == UnitConversionType_enum.uctUnitless.value:
                    node.Value = value
                else:
                    node.SetValue(value, self.__hyApp.UnitConversionSetManager.GetUnitConversionSet(node.UnitConversionType).CurrentDisplayUnit)
            else:
                units = self.get_units(node)
                if unit not in units:
                    raise Exception(f"Unit {unit} isn't in the available list {units}.")
                node.SetValue(value, unit)

    def get_units(self, node):
        '''get backdorr variable units.'''
        units = []
        for unit in self.__hyApp.UnitConversionSetManager.GetUnitConversionSet(node.UnitConversionType).Names:
            units.append(unit)
        return tuple(units)

    @property
    def visible(self):
        return self.__hyApp.Visible

    @visible.setter
    def visible(self, value):
        self.__hyApp.Visible = value


if __name__ == '__main__':
    pass
