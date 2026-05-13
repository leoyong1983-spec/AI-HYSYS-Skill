# Process Stream Class
# A process stream in the problems of interest is defined by:
# 1. An inlet temperature Tin
# 2. An outlet temperature Tout
from .temperatureinterval import TemperatureInterval


class ProcessStream:

    # Static Variable
    hot_stream_id: int = 0
    cold_stream_id: int = 0

    def __init__(self, name: str = '', t_in: float = 0, t_out: float = 0) -> None:
        self.name: str = name
        self.t_in: float = t_in
        self.t_out: float = t_out
        self.is_hot: bool = t_in > t_out
        self.interval: TemperatureInterval = TemperatureInterval(t_in, t_out)
        self.__set_id()

    def __set_id(self) -> None:
        if self.is_hot:
            self.id: str = "H{}".format(ProcessStream.hot_stream_id)
            self.__class__.hot_stream_id += 1
        else:
            self.id: str = "C{}".format(ProcessStream.cold_stream_id)
            self.__class__.cold_stream_id += 1

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return_str = ""
        if self.is_hot:
            return_str += f"Hot Stream: {self.name} ({self.t_in:.2f} to {self.t_out:.2f})"
        else:
            return_str += f"Cold Stream: {self.name} ({self.t_in:.2f} to {self.t_out:.2f})"
        return return_str
