# heat exchanger matching class

from .temperatureinterval import TemperatureInterval
from .stream import Stream
from .utility import Utility
from typing import Union


class MatchingHEX:

    def __init__(self, hot: Union[Stream, Utility], cold: Union[Stream, Utility], hot_interval: TemperatureInterval,
                 cold_interval: TemperatureInterval, duty: float = 0.0, name: str = ""):
        self.name: str = name
        self.duty: float = duty
        self.hot: Union[Stream, Utility] = hot
        self.cold: Union[Stream, Utility] = cold
        self.hot_interval: TemperatureInterval = hot_interval
        self.cold_interval: TemperatureInterval = cold_interval

    def __str__(self) -> str:
        return_str: str = f"{self.hot.name} <-> {self.cold.name} , duty = {self.duty:.3f}"
        # return_str: str = f"{self.name} {self.hot.name} - {self.cold.name}, duty = {self.duty:.3f}"
        # return_str += f"\nhot temp = {self.hot_interval.t_max} - {self.hot_interval.t_min}\ncold temp = {self.cold_interval.t_min} - {self.cold_interval.t_max}"
        return return_str

    def __repr__(self) -> str:
        return_str = f"MatchingHEX({self.name}, {self.hot.name}{self.hot_interval}, {self.cold.name}{self.cold_interval} duty={self.duty})"
        return return_str
