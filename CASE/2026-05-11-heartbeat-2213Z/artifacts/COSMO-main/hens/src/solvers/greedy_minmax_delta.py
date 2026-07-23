# Greedy Min Delta
"""
Greedy proposed algorithm:

It selects matches between hot stream "h" and cold stream "c"
iteratively util it ends up with a feasible set of M matches
exchanging sum(hi) units of heat. 

In each iteration, the heuristic (given a feasible heat exchange qmax)
chooses a match that minimizes max(hi - qmax, ci - qmax).
"""
import sys
from time import time
from .greedy_max_heat import greedy_heat_2
from ..classes.network import Network
from ..classes.stream import Stream
from ..classes.temperatureinterval import TemperatureInterval


def greedy_min_delta(network: Network) -> None:
    
    H: list[Stream] = network.H
    C: list[Stream] = network.C
    T: list[TemperatureInterval] = network.T
    sigma: dict[tuple[Stream, TemperatureInterval], float] = network.sigmas
    delta: dict[tuple[Stream, TemperatureInterval], float] = network.deltas
    heats: dict[Stream, float] = network.heats
    demands: dict[Stream, float] = network.demands

    M: list[tuple[Stream, Stream]] = []
    total_heat: float = sum(heats[hot_stream] for hot_stream in H)
    q = {}

    # Tolerance
    tolerance: float = 10**(-7)

    # Starting time
    starting_time: float = time()
    n_iterations: int = 1

    while total_heat > tolerance:
        
        print("Remaining heat in iteration {}: {}".format(n_iterations, total_heat))
        n_iterations += 1
        # if (n_iterations > 11):
        #     break

        matched_heat: float = 0
        matched_h: Stream = Stream()
        matched_c: Stream = Stream()
        min_delta: float = float(sys.maxint)
        matched_q: dict[tuple[Stream, TemperatureInterval, Stream, TemperatureInterval], float] = {}

        for h in H:
            for c in C:
                if (h, c) not in M:
                    (itr_heat, itr_q) = greedy_heat_2(T, h, c, sigma, delta)
                    itr_delta = max(heats[h] - itr_heat, demands[c] - itr_heat)

                    if itr_delta - min_delta < tolerance:
                        matched_h = h
                        matched_c = c
                        matched_heat = itr_heat
                        matched_q = itr_q
                        min_delta = itr_delta

        print(matched_heat)
        total_heat -= matched_heat
        q.update(matched_q)
        M.append((matched_h, matched_c))

    # ending time
    ending_time = time()
    elapsed_time = round(ending_time - starting_time, 3)
    print(len(M))
    print(M)
    print(elapsed_time)

    for match in M:
        h = match[0]
        c = match[1]

        for s in T:
            for t in T:
                heat = q.get((h, s, c, t))
                if heat is None or heat == 0:
                    continue
                print("{} in {} to {} in {} -------------- {}".format(h, s, c, t, q[h, s, c, t]))
