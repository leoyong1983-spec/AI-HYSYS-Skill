# Stream Class
# A stream in the problems of interest is defined by:
# 1. An inlet temperature Tin
# 2. An outlet temperature Tout
# 3. A flow rate - heat capacity product FCp
from .processstream import ProcessStream


class Stream(ProcessStream):

    def __init__(self, name: str = '', t_in: float = 0.0, t_out: float = 0.0, f_cp: float = 0.0) -> None:
        super().__init__(name, t_in, t_out)
        self.FCp: float = f_cp
        self.heat: float = abs((t_out - t_in) * f_cp)

    def __str__(self) -> str:
        return f'{self.name} {self.t_in:.2f} {self.t_out:.2f} {self.FCp:.2f} {self.heat:.2f}'

    def __repr__(self) -> str:
        return str(self)
