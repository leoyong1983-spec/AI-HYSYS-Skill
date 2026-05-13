"""Created on the 25 Feb 2024
@author: Maetee Lorprajuksiri
@author contact: may3rd@gmail.com


API for controlling the Aspen Python Interface automatically

This module contains interface of Aspen HYSYS V14.

.. contents:: :local:

HYSYS Interface Class
---------------------

"""

import os
import win32com.client as win32
import time
from pywintypes import com_error
from typing import Union
import cosmo.hysys_typelib as hytlb

__all__ = ['simulation',
           ]

OPERATION_CLASSIFICATION = ['All', 'Vessels', 'HeatTransfer', 'Rotating', 'Piping', 'SolidHandling', 'Reactor',
                            'Column', 'ShortCutColumn', 'SubFlowsheet', 'Logical']


def normalize_values(data: list):
    """
    Normalizes a list of values

    Args:
        data: A list of floats to be normalized.

    Returns:
        A new list with the normalized values.
    """
    # determine the total summation of list data
    total_sum = sum(data)

    if total_sum == 0:
        # Handle the case where the sum of all elements is zero
        return [0.0] * len(data)

    return [x / total_sum for x in data]


class simulation:
    """
    Skeleton class for HYSYS interface
    """

    hysys_app = win32.gencache.EnsureDispatch('HYSYS.Application')

    def __init__(self, filename: str = None, working_path: str = None, visibility: bool = True):
        print('The current Directory is : ')
        print(os.getcwd())

        if working_path:
            os.chdir(working_path)
            print('The new Directory where you should have your simulation file is : ')
            print(os.getcwd())
        else:
            working_path = os.getcwd()

        if not filename:
            # if not input filename, just use the current open simulation case
            self.hysys_case = self.hysys_app.ActiveDocument
        else:
            # extract the filename and extension (if any)
            file_name, extension = os.path.splitext(filename)

            # add '.hsc' extension if none exists
            if not extension:
                filename = file_name + '.hsc'

            print(f"The simulation case to be open is {filename}")

            # try opening the file and return None if file cannot be opened
            try:
                self.hysys_case = self.hysys_app.SimulationCases.Open(os.path.join(working_path, filename))
            except FileNotFoundError:
                print(f"Error: File '{filename}' not found.")
                return
            except com_error as e:
                print(f"Error open simulation case '{filename}' : {e}")
                return

        print('The Aspen HYSYS in active now.')

        # set simulation case visibility, default is True
        self.hysys_case.Visible = visibility

        self.component_list = []

        # get the fluid package and components list
        for i in range(self.hysys_case.BasisManager.FluidPackages.Count):
            # add each detail of fluid package
            self.component_list.append({"fluid package": self.hysys_case.BasisManager.FluidPackages(i).name,
                                        "property package": self.hysys_case.BasisManager.FluidPackages(
                                            i).PropertyPackage.name,
                                        "components": list(self.Components(i).Names)})

        # end of __init__
        return

    @property
    def Solver(self):
        return self.hysys_case.Solver

    @property
    def Operations(self):
        return self.hysys_case.Flowsheet.Operations

    @property
    def Streams(self):
        return self.hysys_case.Flowsheet.Streams

    def Components(self, name: Union[int, str] = 0):
        return self.hysys_case.BasisManager.FluidPackages.Item(name).Components

    ########################################################################################################################

    #   Utility functions

    ########################################################################################################################
    def close_case(self) -> bool:
        activeCase = self.hysys_app.ActiveDocument
        activeCase.Close(False)
        return True

    def turn_off_solver(self):
        """turn off the solving mode"""
        self.Solver.CanSolve = False

    def turn_on_solver(self):
        """turn on the solving mode"""
        self.Solver.CanSolve = True

    def is_solver_running(self) -> bool:
        """return solving status, True = still solving, False = finish solving"""
        return self.Solver.IsSolving

    def save(self):
        """
        save current simulation (.hsc)
        """
        self.hysys_case.Save()

    def is_stream_valid(self, name: Union[int, str] = 0) -> bool:
        """
        Check if stream called name is valid.

        Args:
            name: either int or string

        Returns:
            True or False
        """
        try:
            self.Streams.Item(name)
        except com_error:
            print(f'Stream : {name} is not valid.')
            return False

        return True

    def is_operation_valid(self, name: Union[int, str] = 0) -> bool:
        """
        Check if unit operation called name is valid.

        Args:
            name: either int or string

        Returns:
            True or False
        """
        try:
            self.Operations.Item(name)
        except com_error:
            print(f'Operation : {name} is not valid.')
            return False

        return True

    def operating_class(self, name: Union[int, str]) -> str:
        return self.Operations(name).ClassificationName

    def list_all_streams(self):
        """
        Lists all the streams in current simulation case.
        """
        if self.Streams.Count > 0:
            print(f'List of Streams in {self.hysys_case.name} is:')
            for i in range(self.Streams.Count):
                stream = self.Streams(i)
                AttOps = []
                for j in range(stream.AttachedOpers.Count):
                    name = stream.AttachedOpers(j).name
                    if name != "":
                        AttOps.append(f'"{name}"')

                print(f'{i}: "{stream.name}" is connecting to: {', '.join(AttOps)}')
        else:
            print('No streams in current simulation case.')

    def list_all_operations(self):
        """
        Lists all the unit operations, including logic op, in current simulation case.
        """
        if self.Operations.Count > 0:
            print(f'List of Unit Operations in {self.hysys_case.name} is:')
            for i in range(self.Operations.Count):
                print(
                    f'{i}: {self.Operations(i).name} with operation class of "{self.Operations(i).ClassificationName}"')
        else:
            print('No unit operation in current simulation case.')

    ########################################################################################################################

    #   Method for modify stream parameters

    ########################################################################################################################

    def stream_set_vapour_fraction(self, name: Union[int, str], value: float) -> bool:
        return self.stream_set_value(name, self.Streams(name).VapourFration, 'Vapour Fraction', value)

    def stream_set_temperature(self, name: Union[int, str], value: float, unit: str = 'C') -> bool:
        if unit not in self.hysys_app.UnitConversionSetManager.GetUnitConversionSet(
                hytlb.constants.uctTemperature).Names:
            print('Error: Wrong unit')
            return False

        return self.stream_set_value(name, self.Streams(name).Temperature, 'Temperature', value, unit)

    def stream_set_pressure(self, name: Union[int, str], value: float, unit: str = 'kPa') -> bool:
        if unit not in self.hysys_app.UnitConversionSetManager.GetUnitConversionSet(hytlb.constants.uctPressure).Names:
            print('Error: Wrong unit')
            return False

        return self.stream_set_value(name, self.Streams(name).Pressure, 'Pressure', value, unit)

    def stream_set_molar_flow(self, name: Union[int, str], value: float, unit: str = 'kgmole/h') -> bool:
        if unit not in self.hysys_app.UnitConversionSetManager.GetUnitConversionSet(hytlb.constants.uctMolarFlow).Names:
            print('Error: Wrong unit')
            return False

        return self.stream_set_value(name, self.Streams(name).MolarFlow, 'Molar flow', value, unit)

    def stream_set_mass_flow(self, name: Union[int, str], value: float, unit: str = 'kg/h') -> bool:
        if unit not in self.hysys_app.UnitConversionSetManager.GetUnitConversionSet(hytlb.constants.uctMassFlow).Names:
            print('Error: Wrong unit')
            return False

        return self.stream_set_value(name, self.Streams(name).MassFlow, 'Mass flow', value, unit)

    def stream_set_value(self, name: Union[int, str], var_obj: object, var_name: str, value: float,
                         unit: str = "") -> bool:
        """
        set value of variable of stream.

        Args:
            name: name of stream to be set value
            var_obj: the variable to be set
            var_name: variable's name for displaying message
            value: value to set
            unit: unit of measurement

        Returns:
            status of setting
        """
        # Check if stream name is correct
        if not self.is_stream_valid(name):
            print(f'Error: No stream {name}.')
            return False

        # Check if variable can be modified
        if not var_obj.CanModify:
            print(f'Error: {var_name} of {name} cannot be modified.')
            return False

        self.turn_off_solver()
        var_obj.SetValue(value, unit)
        self.turn_on_solver()

        # wait for solver to run
        while self.is_solver_running():
            time.sleep(0.001)

        return True

########################################################################################################################

#   Method for modify unit operation parameters    

########################################################################################################################
