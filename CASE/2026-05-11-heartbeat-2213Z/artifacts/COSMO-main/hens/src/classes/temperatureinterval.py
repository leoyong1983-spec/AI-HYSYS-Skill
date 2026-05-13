# Temperature Interval Class
# Abstracts the idea of a temperature interval 
# going from T1 to T2

from typing import Any


class TemperatureInterval:

    def __init__(self, T1: float = 0, T2: float = 0) -> None:
        self.t_max: float = max(T1, T2)
        self.t_min: float = min(T1, T2)
        self.diff_temp: float = self.t_max - self.t_min

    def __str__(self) -> str:
        return f"[{self.t_max}, {self.t_min}]"

    def __repr__(self) -> str:
        return self.__str__()

    def passes_through_interval(self, other: Any) -> bool:
        """
        This method checks if self temperature 
        interval passes through other temperature
        interval. 
        Returns True if it does.
        """
        # self interval is to the left of other interval
        if self.t_min >= other.t_max:
            return False
        
        # self interval is to the right of other interval
        if self.t_max <= other.t_min:
            return False

        # otherwise it is contained
        return True

    def shifted(self, shifted_temperature) -> Any:
        return TemperatureInterval(self.t_max + shifted_temperature, self.t_min + shifted_temperature)

    @staticmethod
    def common_interval(interval_1, interval_2) -> Any:

        assert interval_1.passes_through_interval(interval_2), "Intervals do not have common ground."

        t_max = min(interval_1.t_max, interval_2.t_max)
        t_min = max(interval_1.t_min, interval_2.t_min)

        return TemperatureInterval(t_max, t_min)
