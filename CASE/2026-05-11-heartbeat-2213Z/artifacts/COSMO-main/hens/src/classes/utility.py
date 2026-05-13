# Utility Class
# A utility in the problems of interest is defined by:
# 1. An inlet temperature Tin
# 2. An outlet temperature Tout
# 3. A unitary cost per unit of heat
from .processstream import ProcessStream


class Utility(ProcessStream):

    def __init__(self, name: str = '', t_in: float = 0, t_out: float = 0, cost: float = 0) -> None:
        super().__init__(name, t_in, t_out)
        self.cost: float = cost

    def __str__(self) -> str:
        return f'{self.name} {self.t_in:.2f} {self.t_out:.2f} {self.cost:.2f}'

    def __repr__(self) -> str:
        if self.t_in > self.t_out:
            return_str = f'Hot Utility {self.name} {self.t_in:.2f} {self.t_out:.2f} {self.cost:.2f}'
        else:
            return_str = f'Cold Utility {self.name} {self.t_in:.2f} {self.t_out:.2f} {self.cost:.2f}'
        return return_str
