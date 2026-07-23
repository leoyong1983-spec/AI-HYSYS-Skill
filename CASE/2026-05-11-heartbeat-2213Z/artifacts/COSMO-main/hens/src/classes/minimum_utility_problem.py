# Minimum Utility Problem Class
# It encapsulates all the necessary elements of a minimum utility cost problem
# This class is defined by:
# 1. A set of streams
# 3. A set of utilities
# 5. A minimum approach heat
#
# -----------------------------------------------------------------
# Modified by Maetee L. in 2024
#

from .temperatureinterval import TemperatureInterval
from .stream import Stream
from .utility import Utility
from typing import Any, Union
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

class MinUtilityProblem:
    """
    Basic class to contain the pinch analysis problem, includes hot stream, cold
    stream, hot utility, cold utility, minimum temperature difference, heat supply
    by hot stream, heat demanded by cold stream, etc.
    """

    def __init__(self, streams: list[Stream], utilities: list[Utility], diff_t_min: float) -> None:
        self.hot_streams: list[Stream] = []
        self.cold_streams: list[Stream] = []
        self.hot_utilities: list[Utility] = []
        self.cold_utilities: list[Utility] = []
        self.temperatures: list[float] = []
        self.intervals: list[TemperatureInterval] = []
        self.sigmas: dict[tuple[Stream, TemperatureInterval], float] = {}
        self.deltas: dict[tuple[Stream, TemperatureInterval], float] = {}
        self.accepted_hu_sigmas: dict[tuple[Utility, TemperatureInterval], bool] = {}
        self.accepted_cu_deltas: dict[tuple[Utility, TemperatureInterval], bool] = {}
        self.diff_t_min: float = diff_t_min

        # ---------------------------------------------------------
        # appended by Maetee to display composite curve
        # ---------------------------------------------------------
        # heat exchanger match between hot stream h and cold stream c is permitted
        self.accepted_h_c: dict[tuple[Union[Stream, Utility], Union[Stream, Utility]], int] = {}
        self.accepted_h_c_k: dict[tuple[Union[Stream, Utility], Union[Stream, Utility], TemperatureInterval], int] = {}
        # properties for determination of pinch temperature and composite diagram
        self.problem_table: dict[TemperatureInterval, float] = {}
        self.hot_composite_h: list[float] = []
        self.hot_composite_t: list[float] = []
        self.cold_composite_h: list[float] = []
        self.cold_composite_t: list[float] = []
        self.grand_composite_h: list[float] = []
        self.grand_composite_t: list[float] = []
        self.unfeasible_heat_cascade: list[dict[str, float]] = []
        self.heat_cascade: list[dict[str, float]] = []
        self.optimal_hot_utility: float = 0
        self.optimal_cold_utility: float = 0
        self.pinch_temperature: float = 0
        # ---------------------------------------------------------
        # Original methods
        # ---------------------------------------------------------
        self.__init_streams(streams)
        self.__init_utilities(utilities)
        self.__init_temperatures(streams, utilities)
        self.__init_heats()
        self.__init_accepted_u_intervals()
        # ---------------------------------------------------------
        # Additional method
        # ---------------------------------------------------------
        self.__init_accepted_h_c()
        self.__init_accepted_h_c_k()
        self.__init_heat_cascade()
        self.__init_composite_diagram()
        self.__init_grand_composite_curve()

    def __init_streams(self, streams: list[Stream]) -> None:
        """
        This method helps in the initialization of the streams.
        It receives a set of streams and initializes the hot 
        and cold streams lists.
        """
        for stream in streams:
            if stream.is_hot:
                self.hot_streams.append(stream)
            else:
                self.cold_streams.append(stream)

    def __init_utilities(self, utilities: list[Utility]) -> None:
        """
        This method helps in the initialization of the utilities.
        It receives a set of streams and initializes the hot and 
        cold streams lists.
        """
        for utility in utilities:
            if utility.is_hot:
                self.hot_utilities.append(utility)
            else:
                self.cold_utilities.append(utility)

    def __init_temperatures(self, streams: list[Stream], utilities: list[Utility]) -> None:
        """
        This method initialized a list of unique temperature
        values affected by diff_t_min.
        """
        process_streams: list[Union[Stream, Utility]] = streams + utilities
        for process_stream in process_streams:
            t_in: float = process_stream.t_in
            t_out: float = process_stream.t_out
            if not process_stream.is_hot:
                t_in += self.diff_t_min
                t_out += self.diff_t_min
            if t_in not in self.temperatures:
                self.temperatures.append(t_in)
            if t_out not in self.temperatures:
                self.temperatures.append(t_out)
        self.temperatures.sort(reverse=True)
        # creating intervals
        for i in range(len(self.temperatures) - 1):
            new_interval = TemperatureInterval(self.temperatures[i], self.temperatures[i + 1])
            self.intervals.append(new_interval)

    def __init_heats(self) -> None:
        for interval in self.intervals:
            total_h_interval: float = 0.0
            # initializing sigmas
            for hot_stream in self.hot_streams:
                if hot_stream.interval.passes_through_interval(interval):
                    self.sigmas[(hot_stream, interval)] = float(TemperatureInterval.common_interval(interval, hot_stream.interval).diff_temp * hot_stream.FCp)
                else:
                    self.sigmas[(hot_stream, interval)] = 0
                total_h_interval += self.sigmas[(hot_stream, interval)]
            # initializing deltas. This one is tricky because intervals were constructed 
            # by adding minimum diff temp to each CS interval, but CS intervals were nos modified
            for cold_stream in self.cold_streams:
                if cold_stream.interval.shifted(self.diff_t_min).passes_through_interval(interval):
                    self.deltas[(cold_stream, interval)] = float(TemperatureInterval.common_interval(interval, cold_stream.interval.shifted(self.diff_t_min)).diff_temp * cold_stream.FCp)
                else:
                    self.deltas[(cold_stream, interval)] = 0
                total_h_interval -= self.deltas[(cold_stream, interval)]
            # initializing problem table
            self.problem_table[interval] = total_h_interval

    def __init_accepted_u_intervals(self) -> None:
        for interval in self.intervals:
            # accepted sigmas
            for hot_utility in self.hot_utilities:
                if hot_utility.interval.passes_through_interval(interval):
                    self.accepted_hu_sigmas[(hot_utility, interval)] = True
                else:
                    self.accepted_hu_sigmas[(hot_utility, interval)] = False
            # accepted deltas
            for cold_utility in self.cold_utilities:
                if cold_utility.interval.shifted(self.diff_t_min).passes_through_interval(interval):
                    self.accepted_cu_deltas[(cold_utility, interval)] = True
                else:
                    self.accepted_cu_deltas[(cold_utility, interval)] = False

    def __init_accepted_h_c(self) -> None:
        for hot_stream in self.hot_streams + self.hot_utilities:
            for cold_stream in self.cold_streams + self.cold_utilities:
                self.accepted_h_c[(hot_stream, cold_stream)] = 1
        # not transfer hot utility to cold utility
        for H in self.hot_utilities:
            for C in self.cold_utilities:
                self.accepted_h_c[H, C] = 0

    def __init_accepted_h_c_k(self) -> None:
        for i in self.hot_streams + self.hot_utilities:
            for j in self.cold_streams + self.cold_utilities:
                for k in self.intervals:
                    if i.interval.passes_through_interval(k) and j.interval.shifted(self.diff_t_min).passes_through_interval(k):
                        self.accepted_h_c_k[(i, j, k)] = True
                    else:
                        self.accepted_h_c_k[(i, j, k)] = False

    def __init_heat_cascade(self) -> None:
        """_summary_
        This method initializes the heat cascade table and the unfeasible heat cascade table.
        The heat cascade table contains the enthalpy change for each interval, and the exit enthalpy.
        The unfeasible heat cascade table contains the enthalpy change for each interval, and the exit enthalpy.
        The exit enthalpy is the minimum exit enthalpy for each interval.
        The optimal hot and cold utilities are also calculated.
        The pinch temperature is also calculated.
        """
        exit_h: float = 0
        lowest_exit_h: float = 0
        i: int = 0
        pinch_interval: int = i
        for interval in self.intervals:
            row: dict[str, float] = {'deltaH': self.problem_table[interval]}
            exit_h += row['deltaH']
            row['exitH'] = exit_h
            if exit_h < lowest_exit_h:
                lowest_exit_h = exit_h
                pinch_interval = i
            self.unfeasible_heat_cascade.append(row)
            i += 1
        self.optimal_hot_utility = -lowest_exit_h
        exit_h = self.optimal_hot_utility
        for interval in self.intervals:
            row = {'deltaH': self.problem_table[interval]}
            exit_h += row['deltaH']
            row['exitH'] = exit_h
            self.heat_cascade.append(row)
        self.optimal_cold_utility = exit_h
        if pinch_interval > 0:
            self.pinch_temperature = self.intervals[pinch_interval].t_min

    def __init_composite_diagram(self) -> None:
        """_summary_
        This method initializes the composite diagram.
        The composite diagram is a plot of the enthalpy change for each interval, and the exit enthalpy.
        The exit enthalpy is the minimum exit enthalpy for each interval.
        """
        # need temperatures and enthalpies in ascending order
        temperatures: list[float] = self.temperatures[::-1]
        delta_h_hot: list[float] = []
        delta_h_cold: list[float] = []
        # find enthalpies change for hot and cold composite streams
        for interval in self.intervals[::-1]:
            total_h: float = 0.0
            for H in self.hot_streams:
                total_h += self.sigmas[(H, interval)]
            delta_h_hot.append(total_h)
            total_h: float = 0.0
            for C in self.cold_streams:
                total_h += self.deltas[(C, interval)]
            delta_h_cold.append(total_h)
        total_h_hot: float = 0
        self.hot_composite_h.append(total_h_hot)
        self.hot_composite_t.append(temperatures[0])
        for i in range(1, len(temperatures)):
            if delta_h_hot[i - 1] != 0:
                total_h_hot += delta_h_hot[i - 1]
                self.hot_composite_h.append(total_h_hot)
                self.hot_composite_t.append(temperatures[i])
        total_h_cold: float = self.optimal_cold_utility
        self.cold_composite_h.append(total_h_cold)
        self.cold_composite_t.append(temperatures[0])
        for i in range(1, len(temperatures)):
            if delta_h_cold[i - 1] != 0:
                total_h_cold += delta_h_cold[i - 1]
                self.cold_composite_h.append(total_h_cold)
                self.cold_composite_t.append(temperatures[i])

    def __init_grand_composite_curve(self) -> None:
        self.grand_composite_h.append(self.optimal_hot_utility)
        self.grand_composite_t.append(self.temperatures[0])
        for i in range(1, len(self.temperatures)):
            self.grand_composite_h.append(self.heat_cascade[i - 1]['exitH'])
            self.grand_composite_t.append(self.temperatures[i])

    def change_diff_t_min(self, diff_t_min: float) -> None:
        self.diff_t_min = diff_t_min
        # clear all related parameters
        self.temperatures = []
        self.intervals = []
        self.sigmas = {}
        self.deltas = {}
        self.accepted_hu_sigmas = {}
        self.accepted_cu_deltas = {}
        self.accepted_h_c_k = {}
        self.problem_table = {}
        self.hot_composite_h = []
        self.hot_composite_t = []
        self.cold_composite_h = []
        self.cold_composite_t = []
        self.grand_composite_h = []
        self.grand_composite_t = []
        self.unfeasible_heat_cascade = []
        self.heat_cascade = []
        self.optimal_hot_utility = 0
        self.optimal_cold_utility = 0
        self.pinch_temperature = 0
        self.__init_temperatures(self.hot_streams + self.cold_streams, self.hot_utilities + self.cold_utilities)
        self.__init_heats()
        self.__init_accepted_u_intervals()
        self.__init_accepted_h_c_k()
        self.__init_heat_cascade()
        self.__init_composite_diagram()
        self.__init_grand_composite_curve()

    def plot_composite_diagram(self, save: bool = False, filename: str = 'composite.svg') -> None:
        # Create a new figure and axes
        fig, ax = plt.subplots()

        # Plot hot and cold composite curves
        ax.plot(self.hot_composite_h, self.hot_composite_t, 'tab:red', label='Hot Composite')
        ax.plot(self.cold_composite_h, self.cold_composite_t, 'tab:blue', label='Cold Composite')
        ax.plot(self.hot_composite_h, self.hot_composite_t, 'ro')
        ax.plot(self.cold_composite_h, self.cold_composite_t, 'bo')

        # Initialize variables for filled areas
        left_hot_h_index: int = 0
        right_cold_h_index: int = 0
        left_hot_h: list[float] = []
        left_hot_t: list[float] = []
        left_cold_h: list[float] = []
        right_hot_h: list[float] = []
        right_cold_h: list[float] = []
        right_cold_t: list[float] = []

        # Find left point of hot composite curve
        for i in range(len(self.hot_composite_h)):
            if self.hot_composite_h[i] >= self.cold_composite_h[0]:
                left_hot_h_index = i
                break

        # Find right point of cold composite curve
        for i in range(len(self.cold_composite_h) - 1, -1, -1):
            if self.cold_composite_h[i] <= self.hot_composite_h[-1]:
                right_cold_h_index = i
                break

        # Calculate temperatures for left and right points
        if left_hot_h_index == 0:
            left_hot_h.append(self.hot_composite_h[0])
            left_hot_t.append(self.hot_composite_t[0])
        else:
            for i in range(left_hot_h_index):
                left_hot_h.append(self.hot_composite_h[i])
                left_hot_t.append(self.hot_composite_t[i])
            i = left_hot_h_index
            m = ((self.hot_composite_t[i] - self.hot_composite_t[i - 1]) / 
                (self.hot_composite_h[i] - self.hot_composite_h[i - 1]))
            left_hot_h.append(self.cold_composite_h[0])
            h_diff = (self.cold_composite_h[0] - self.hot_composite_h[i - 1])
            left_hot_t.append(self.hot_composite_t[i - 1] + h_diff * m)

        if left_hot_h_index == 0:
            right_cold_h = self.hot_composite_h
        else:
            right_hot_h.append(left_hot_h[-1])
            for r in self.hot_composite_h[left_hot_h_index:]:
                right_hot_h.append(r)

        if right_cold_h_index == len(self.cold_composite_h) - 1:
            right_cold_h.append(self.cold_composite_h[-1])
            right_cold_t.append(self.cold_composite_t[-1])
        else:
            for i in range(len(self.cold_composite_h) - 1, right_cold_h_index, -1):
                right_cold_h.append(self.cold_composite_h[i])
                right_cold_t.append(self.cold_composite_t[i])
            i = right_cold_h_index
            m = ((self.cold_composite_t[i + 1] - self.cold_composite_t[i]) / 
                (self.cold_composite_h[i + 1] - self.cold_composite_h[i]))
            right_cold_h.append(self.hot_composite_h[-1])
            right_cold_t.append(self.cold_composite_t[i] + 
                                (self.hot_composite_h[-1] - self.cold_composite_h[i]) * m)

        # Correct order of right_cold_h and right_cold_t
        right_cold_h.reverse()
        right_cold_t.reverse()

        for x in self.cold_composite_h[:right_cold_h_index]:
            left_cold_h.append(x)
        if right_cold_h_index < len(self.cold_composite_h) - 1:
            left_cold_h.append(right_cold_h[0])

        # Calculate combined enthalpy and interpolated temperatures
        combined_h = sorted(list(set(right_hot_h) | set(left_cold_h)))
        hot_t = np.interp(combined_h, self.hot_composite_h, self.hot_composite_t)
        cold_t = np.interp(combined_h, self.cold_composite_h, self.cold_composite_t)

        # Fill areas
        ax.fill_between(combined_h, hot_t, cold_t, color='g', alpha=0.3)
        ax.fill_between(left_hot_h, 0, left_hot_t, color='b', alpha=0.5)
        ax.fill_between(right_cold_h, 0, right_cold_t, color='r', alpha=0.5)

        # Add pinch line if applicable
        try:
            pinch_index = self.cold_composite_t.index(self.pinch_temperature)
            pinch_h = self.cold_composite_h[pinch_index]
            ax.plot([pinch_h, pinch_h], [self.temperatures[0], self.temperatures[-1]], ':', 
                    label='Pinch Line')
        except ValueError:
            pass

        # Customize the plot
        ax.grid(True)
        ax.set_title('Temperature-Enthalpy Composite Diagram')
        ax.set_xlabel('Enthalpy')
        ax.set_ylabel('Temperature')
        ax.legend()

        # Save or display the plot
        if save:
            print(f'Save composite diagram to {filename}')
            fig.savefig(filename)
            plt.close(fig)  # Close the figure to prevent overlap
        else:
            plt.show()  # Show the plot and close it afterward

    def plot_grand_composite_curve(self, save: bool = False, filename: str = 'grand_composite.png') -> None:
        """
        Plots the Grand Composite Curve with hot and cold utility areas and pinch temperature.
        
        Parameters:
        - save (bool): If True, saves the plot to a file; if False, displays it.
        - filename (str): Name of the file to save the plot (used when save=True).
        """
        # Create a new figure and axes
        fig, ax = plt.subplots()

        # Plot the grand composite curve line and points
        ax.plot(self.grand_composite_h, self.grand_composite_t, 'tab:blue', label='Grand Composite Curve')
        ax.plot(self.grand_composite_h, self.grand_composite_t, 'bo')  # Blue dots at data points

        # Fill areas for hot and cold utilities
        ax.fill_between([0, self.grand_composite_h[0]], 0, self.temperatures[0], 
                    color='r', alpha=0.5, label='Hot Utility')
        ax.fill_between([0, self.grand_composite_h[-1]], 0, self.temperatures[-1], 
                    color='b', alpha=0.5, label='Cold Utility')

        # Add pinch temperature line
        ax.plot([0, self.grand_composite_h[-1]], [self.pinch_temperature, self.pinch_temperature], 
            ':', label='Pinch Temperature')

        # Customize the plot
        ax.grid(True)
        ax.set_title('Grand Composite Curve')
        ax.set_xlabel('Net Enthalpy Change')
        ax.set_ylabel('Temperature')
        ax.legend()

        # Handle saving or displaying the plot
        if save:
            print(f'Save grand composite curve to {filename}')
            fig.savefig(filename)
            plt.close(fig)  # Close the figure to prevent overlap
        else:
            plt.show()  # Display the plot and close it afterward

    def __str__(self) -> str:
        return "Hot Stream: {} \nCold Stream: {}\nHot Utility: {}\nCold Utility: {}\nDiff Tmin: {}".format(
            len(self.hot_streams), len(self.cold_streams),
            len(self.hot_utilities), len(self.cold_utilities),
            self.diff_t_min)

    def __repr__(self) -> str:
        return self.__str__()

    def print_temperature_interval(self) -> None:
        for k in self.intervals:
            print(f'{k}, {self.problem_table[k]:.2f}')

    def print_minimum_demanded_utility(self) -> None:
        print(f'Pinch temperature (hot) is {self.pinch_temperature:.2f}')
        print(f'Optimal Hot Utility is {self.optimal_hot_utility:.2f}')
        print(f'Optimal Cold Utility is {self.optimal_cold_utility:.2f}')

    def get_hot_stream(self, name: str) -> Union[Stream, None]:
        for h in self.hot_streams:
            if h.name == name:
                return h
        return None

    def get_cold_stream(self, name: str) -> Union[Stream, None]:
        for c in self.cold_streams:
            if c.name == name:
                return c
        return None

    @staticmethod
    def generate_from_data(data_id: str) -> Any:
        path = 'data/original_problems/' + data_id + '.dat'
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        elements = [line.split() for line in lines]
        diff_t_min = float(elements[3][1])
        elements = elements[4:]
        streams = [Stream(name=str(e[0]), t_in=float(e[1]), t_out=float(e[2]),
                          f_cp=float(e[3])) for e in elements if e[0][1] != 'U']
        utilities = [Utility(name=str(e[0]), t_in=float(e[1]), t_out=float(e[2]),
                             cost=float(e[3])) for e in elements if e[0][1] == 'U']
        return MinUtilityProblem(streams, utilities, diff_t_min)

    @staticmethod
    def generate_from_csv(filename: str) -> Any:
        elements = []
        # open the csv file in read mode
        with open(filename, 'r') as csv_file:
            # create a CSV reader object
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                trimmed_row = [element.strip() for element in row]
                elements.append(trimmed_row)
        if len(elements[0]) == 2:  # first line is number of stream and number of utility
            stream_count = int(elements[0][0])
            utility_count = int(elements[0][1])
            diff_t_min = float(elements[1][1])
            elements_streams = elements[2:stream_count + 2]
            elements_utilities = elements[stream_count + 2:utility_count + stream_count + 2]
            streams = [Stream(name=str(e[0]), t_in=float(e[1]), t_out=float(e[2]), f_cp=float(e[3])) for e in elements_streams]
            utilities = [Utility(name=str(e[0]), t_in=float(e[1]), t_out=float(e[2]), cost=float(e[3])) for e in elements_utilities]
            return_obj = MinUtilityProblem(streams, utilities, diff_t_min)
            if stream_count + utility_count + 2 < len(elements):
                elements_permit = elements[stream_count + utility_count + 2:]
                if len(elements_permit) > 0:
                    for e in elements_permit:
                        hot_stream = return_obj.get_hot_stream(e[0])
                        cold_stream = return_obj.get_cold_stream(e[1])
                        return_obj.accepted_h_c[(hot_stream, cold_stream)] = int(e[2])
            return return_obj
        return None

    @classmethod
    def generate_from_excel_sheet(cls, xls: pd.ExcelFile, sheet_name: str) -> 'MinUtilityProblem':
        """
        Generate a MinUtilityProblem instance from an Excel sheet.

        Args:
            xls (pd.ExcelFile): The Excel file object.
            sheet_name (str): The name of the sheet to read from.

        Returns:
            MinUtilityProblem: An instance of the class initialized with the parsed data.
        """
        # Read DTmin from cell AH1
        dtmin = pd.read_excel(xls, sheet_name=sheet_name, usecols="AH", skiprows=1, nrows=1, header=None).iloc[0, 0]

        # Read cold streams (A3:F100, headers in A2:F2)
        cold_streams_df = pd.read_excel(xls, sheet_name=sheet_name, usecols="A:F", header=1)
        cold_streams_df = cold_streams_df[cold_streams_df["Cold Stream"].notna()]

        # Read hot streams (H3:M100, headers in H2:M2)
        hot_streams_df = pd.read_excel(xls, sheet_name=sheet_name, usecols="H:M", header=1)
        hot_streams_df = hot_streams_df[hot_streams_df["Hot Stream"].notna()]

        # Read cold utilities (O3:T100, headers in O2:T2)
        cold_utilities_df = pd.read_excel(xls, sheet_name=sheet_name, usecols="O:T", header=1)
        cold_utilities_df = cold_utilities_df[cold_utilities_df["Cold Utility"].notna()]

        # Read hot utilities (V3:AA100, headers in V2:AA2)
        hot_utilities_df = pd.read_excel(xls, sheet_name=sheet_name, usecols="V:AA", header=1)
        hot_utilities_df = hot_utilities_df[hot_utilities_df["Hot Utility"].notna()]

        # Create streams
        cold_streams = [
            Stream(name=row["Cold Stream"], t_in=row["cold supply temp"], t_out=row["cold target temp"], f_cp=row["cold MCp"])
            for _, row in cold_streams_df.iterrows()
        ]
        hot_streams = [
            Stream(name=row["Hot Stream"], t_in=row["hot supply temp"], t_out=row["hot target temp"], f_cp=row["hot MCp"])
            for _, row in hot_streams_df.iterrows()
        ]

        # Create utilities
        cold_utilities = [
            Utility(name=row["Cold Utility"], t_in=row["cu supply temp"], t_out=row["cu target temp"], cost=row["cu cost"])
            for _, row in cold_utilities_df.iterrows()
        ]
        hot_utilities = [
            Utility(name=row["Hot Utility"], t_in=row["hu supply temp"], t_out=row["hu target temp"], cost=row["hu cost"])
            for _, row in hot_utilities_df.iterrows()
        ]

        # Combine streams and utilities
        streams = hot_streams + cold_streams
        utilities = hot_utilities + cold_utilities

        # Create the problem instance
        problem = cls(streams, utilities, dtmin)

        # Read constraints (AC3:AE100, headers in AC2:AE2)
        constraints_df = pd.read_excel(xls, sheet_name=sheet_name, usecols="AC:AE", header=1)
        constraints_df = constraints_df[constraints_df["Hot"].notna() & constraints_df["Cold"].notna()]

        # Create dictionaries for quick lookup
        hot_dict = {s.name: s for s in problem.hot_streams + problem.hot_utilities}
        cold_dict = {s.name: s for s in problem.cold_streams + problem.cold_utilities}

        # Apply constraints
        for _, row in constraints_df.iterrows():
            hot_name = row["Hot"]
            cold_name = row["Cold"]
            flag = int(row["Flag"])
            if hot_name in hot_dict and cold_name in cold_dict:
                hot_stream = hot_dict[hot_name]
                cold_stream = cold_dict[cold_name]
                problem.accepted_h_c[(hot_stream, cold_stream)] = flag
            else:
                print(f"Warning: Constraint for {hot_name} and {cold_name} not applied, streams not found.")

        return problem