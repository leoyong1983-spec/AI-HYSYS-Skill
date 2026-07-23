# Network Class
# This class abstracts the necessary items for a
# Min Number of Matches Problem. It provides:
# 1. A set of hot streams (hot utilities included)
# 2. A set of cold streams (cold utilities included)
# 3. A set of temperature intervals
# 4. A big-M parameter Ui,j that bounds the heat exchanged
#    between a hot stream i and a cold stream j
# 5. A dictionary with info of heat supply for each hot stream 
#    at each temperature interval
# 6. A dictionary with info of heat demand for each cold stream 
#    at each temperature interval
from .temperatureinterval import TemperatureInterval
from .stream import Stream
from .utility import Utility
from .minimum_utility_problem import MinUtilityProblem
from ..solvers.greedy_max_heat import greedy_heat
from ..solvers.min_utility_solver import solve_min_utility
from typing import Any, Union


class Network:

    def __init__(self,
                 min_utility_instance: MinUtilityProblem,
                 utility_sigmas: dict[tuple[Union[Stream, Utility], TemperatureInterval], float],
                 utility_deltas: dict[tuple[Union[Stream, Utility], TemperatureInterval], float],
                 pinch_interval: int = 0, below_pinch: bool = False) -> None:
        self.H: list[Union[Stream, Utility]] = min_utility_instance.hot_streams + min_utility_instance.hot_utilities
        self.C: list[Union[Stream, Utility]] = min_utility_instance.cold_streams + min_utility_instance.cold_utilities
        self.T: list[TemperatureInterval] = min_utility_instance.intervals
        self.PinchInterval: int = pinch_interval  # index of pinch interval, default is 0
        self.below_pinch: bool = below_pinch
        self.P: dict[tuple[Union[Stream, Utility], Union[Stream, Utility]], int] = min_utility_instance.accepted_h_c
        self.Pk: dict[tuple[Union[Stream, Utility], Union[Stream, Utility], TemperatureInterval], int] = min_utility_instance.accepted_h_c_k
        self.diff_t_min: float = min_utility_instance.diff_t_min
        self.sigmas: dict[tuple[Union[Stream, Utility], TemperatureInterval], float] = min_utility_instance.sigmas
        self.deltas: dict[tuple[Union[Stream, Utility], TemperatureInterval], float] = min_utility_instance.deltas
        self.heats: dict[Union[Stream, Utility], float] = {}   # hi
        self.demands: dict[Union[Stream, Utility], float] = {}  # cj
        self.U: dict[tuple[Union[Stream, Utility], Union[Stream, Utility]], float] = {}
        self.U_greedy: dict[tuple[Union[Stream, Utility], Union[Stream, Utility]], float] = {}
        self.u_ijk: dict[tuple[Union[Stream, Utility], Union[Stream, Utility], TemperatureInterval], float] = {}
        self.u_ijkl: dict[tuple[Union[Stream, Utility], TemperatureInterval, Union[Stream, Utility], TemperatureInterval], float] = {}
        self.model: str = ''
        self.__update_sigmas(utility_sigmas)
        self.__update_deltas(utility_deltas)
        self.__init_heats()
        self.__init_demands()
        self.__init_u_ij()
        self.__init_u_ij_greedy()
        self.__init_u_ijk()
        self.__init_u_ijkl()
        self.__update_intervals()

    def __update_intervals(self):
        if self.PinchInterval > 0:
            if self.below_pinch:
                self.T = self.T[self.PinchInterval:]
            else:
                self.T = self.T[0:self.PinchInterval]

    def __update_sigmas(self, new_sigmas: dict[tuple[Union[Stream, Utility], TemperatureInterval], float]) -> None:
        for key in new_sigmas.keys():
            self.sigmas[key] = new_sigmas[key]
    
    def __update_deltas(self, new_deltas: dict[tuple[Union[Stream, Utility], TemperatureInterval], float]) -> None:
        for key in new_deltas.keys():
            self.deltas[key] = new_deltas[key]

    def __init_heats(self) -> None:
        for hot_stream in self.H:
            stream_heat = 0
            for interval in self.T:
                stream_heat += self.sigmas[(hot_stream, interval)]
            self.heats[hot_stream] = stream_heat

    def __init_demands(self) -> None:
        for cold_stream in self.C:
            stream_demand = 0
            for interval in self.T:
                stream_demand += self.deltas[cold_stream, interval]
            self.demands[cold_stream] = stream_demand

    def __init_u_ij(self) -> None:
        """
        Computes Uij as min{hi, cj}
        Where hi is the total heat supply of hot stream i
        and ci is the total heat demand of cold stream j
        """
        for hot_stream in self.H:
            for cold_stream in self.C:
                self.U[(hot_stream, cold_stream)] = min(self.heats[hot_stream], self.demands[cold_stream])

    def __init_u_ijk(self) -> None:
        for hot_stream in self.H:
            for cold_stream in self.C:
                for interval in self.T:
                    k_index = self.T.index(interval)
                    sum_q_il: float = sum(self.sigmas[(hot_stream, s)] for s in self.T[:k_index+1])
                    self.u_ijk[(hot_stream, cold_stream, interval)] = min(sum_q_il, self.deltas[(cold_stream, interval)])

    def __init_u_ijkl(self) -> None:
        for i in self.H:
            for k in self.T:
                for j in self.C:
                    for l in self.T:
                        self.u_ijkl[(i, k, j, l)] = min(self.sigmas[(i, k)], self.deltas[(j, l)])

    def __init_u_ij_greedy(self) -> None:
        for hot_stream in self.H:
            for cold_stream in self.C:
                self.U_greedy[(hot_stream, cold_stream)] = greedy_heat(self.T, hot_stream, cold_stream, self.sigmas, self.deltas)[0]

    def __str__(self) -> str:
        return "H: {} {}\nC: {} {}\nT: {}".format(len(self.H), self.H, len(self.C), self.C, self.T)

    def __repr__(self) -> str:
        return self.__str__()

    def print_heats(self):
        for hot_stream in self.H:
            print(f'{hot_stream.name} - {self.heats[hot_stream]:.2f}')

    def print_demands(self):
        for cold_stream in self.C:
            print(f'{cold_stream.name} - {self.demands[cold_stream]:.2f}')

    @staticmethod
    def generate_from_csv(csv_path: str,
                          create_with_subnetwork: bool = False,
                          plot_composite: bool = False,
                          plot_grand_composite: bool = False,
                          debug: bool = False) -> Any:
        """
        Generate a network from a csv file and return it as a Network object.

        :param csv_path: csv file path
        :param create_with_subnetwork: create with subnetwork flag
        :param plot_composite: plot composite flag
        :param plot_grand_composite: plot grand composite flag
        :param debug: debug flag
        """
        # create the min utility problem from the csv file
        min_obj: MinUtilityProblem = MinUtilityProblem.generate_from_csv(csv_path)

        # plot the composite diagram
        if plot_composite:
            min_obj.plot_composite_diagram()
        # plot the grand composite curve
        if plot_grand_composite:
            min_obj.plot_grand_composite_curve()
        # solve for the min utility demand and pinch interval location
        sigma_hu, delta_hu, pinch_interval = solve_min_utility(min_obj, debug=debug)
        # create the networks and return them
        if create_with_subnetwork and pinch_interval > 0:
            return Network(min_obj, sigma_hu, delta_hu, pinch_interval, below_pinch=False), Network(min_obj, sigma_hu, delta_hu, pinch_interval, below_pinch=True)
        else:
            return Network(min_obj, sigma_hu, delta_hu), Network(min_obj, sigma_hu, delta_hu)
