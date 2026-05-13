# Greedy Max Heat
"""
Proposed greedy algorithm  to calculate the maximum
amount of heat that can be possibly exchanged between
two stream h and c in T temperature intervals.
"""
from ..classes.temperatureinterval import TemperatureInterval
from ..classes.stream import Stream


def greedy_heat(temperature_intervals: list[TemperatureInterval],
                h: Stream,
                c: Stream,
                sigma: dict[tuple[Stream, TemperatureInterval], float],
                delta: dict[tuple[Stream, TemperatureInterval], float]) -> (
        tuple)[float, dict[tuple[Stream, TemperatureInterval, Stream, TemperatureInterval], float]]:
    """
    Greedily computes the maximum amount of heat
    exchange between hot stream h and cold stream
    c in intervals T.

    It does not modify the network sigmas and deltas.
    """

    heat = 0
    q = {}
    residual = {}

    # Calculating the amount of heat exchanged in same interval
    for t in temperature_intervals:
        exchanged_heat = min(sigma[h, t], delta[c, t])
        heat += exchanged_heat
        q[h, t, c, t] = exchanged_heat
        residual[h, t] = sigma[h, t] - exchanged_heat
        residual[c, t] = delta[c, t] - exchanged_heat

    for s in temperature_intervals:
        if residual[h, s] != 0:
            s_index = temperature_intervals.index(s)
            for t in temperature_intervals[(s_index + 1):]:
                if residual[c, t] != 0:
                    exchanged_heat = min(residual[h, s], residual[c, t])
                    heat += exchanged_heat
                    q[h, s, c, t] = exchanged_heat
                    residual[h, s] -= exchanged_heat
                    residual[c, t] -= exchanged_heat
                    if residual[h, s] == 0:
                        break
    
    return heat, q


# TODO: This method will be useful for a heuristic to complete greedy_minmax_delta
def greedy_heat_2(temperature_intervals: list[TemperatureInterval],
                  h: Stream,
                  c: Stream,
                  sigmas: dict[tuple[Stream, TemperatureInterval], float],
                  deltas: dict[tuple[Stream, TemperatureInterval], float]) -> (
        tuple)[float, dict[tuple[Stream, TemperatureInterval, Stream, TemperatureInterval], float]]:
    """
    Greedily computes the maximum amount of heat
    exchange between hot stream h and cold stream
    c in intervals T.

    It modifies the network sigmas and deltas.
    """

    heat = 0
    q = {}
    sigma = dict(sigmas)
    delta = dict(deltas)

    for s in temperature_intervals:
        if sigma[h, s] != 0:
            s_index = temperature_intervals.index(s)
            for t in temperature_intervals[s_index:]:
                if delta[c, t] != 0:
                    exchanged_heat = min(sigma[h, s], delta[c, t])
                    heat += exchanged_heat
                    q[h, s, c, t] = exchanged_heat
                    sigma[h, s] -= exchanged_heat
                    delta[c, t] -= exchanged_heat
                    if sigma[h, s] == 0:
                        break
    
    return heat, q
