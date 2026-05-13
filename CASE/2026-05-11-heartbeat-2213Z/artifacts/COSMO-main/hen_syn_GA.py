import numpy as np
from collections import namedtuple
import pandas as pd

# Define data structure
Stream = namedtuple('Stream', ['type', 'Tin', 'Tout', 'CP'])
Utility = namedtuple('Utility', ['type', 'Tin', 'Tout', 'cost'])

# Function to load data from CSV files
def load_streams(streams_csv, utilities_csv):
    streams_df = pd.read_csv(streams_csv)
    utilities_df = pd.read_csv(utilities_csv)

    streams = [Stream(row['Type'], row['TIN_spec'], row['TOUT_spec'], row['Fcp'])
               for _, row in streams_df.iterrows()]

    utilities = {row['Type'].lower(): Utility(row['Type'], row['TIN_utility'], row['TOUT_utility'], row['Unit_Cost_Energy'])
                 for _, row in utilities_df.iterrows()}

    hot_streams = [s for s in streams if s.type.lower() == 'hot']
    cold_streams = [s for s in streams if s.type.lower() == 'cold']

    hot_utilities = [s for s in utilities.values() if s.type.lower() == 'hot_utility']
    cold_utilities = [s for s in utilities.values() if s.type.lower() == 'cold_utility']

    num1 = len(hot_streams)# + len(hot_utilities)
    num2 = len(cold_streams)# + len(cold_utilities)
    stage_num = max(num1, num2)

    return hot_streams, cold_streams, hot_utilities, cold_utilities, stage_num

# Example data (replace with actual streams)
hot_streams = [Stream('hot', 443, 333, 30.0), Stream('hot', 423, 303, 15.0)]
cold_streams = [Stream('cold', 293, 408, 20.0), Stream('cold', 353, 413, 40.0)]
U = 1.0  # overall heat transfer coefficient (assumed constant for simplicity)
stage_num = max(len(hot_streams), len(cold_streams))

# Genetic Algorithm Class
class GeneticAlgorithm:
    def __init__(self, hot_streams, cold_streams, hot_utilities, cold_utilities, stages, pop_size=20, gen=50):
        self.hot_streams = hot_streams
        self.cold_streams = cold_streams
        self.hot_utilities = hot_utilities
        self.cold_utilities = cold_utilities
        self.stages = stages
        self.pop_size = pop_size
        self.gen = gen

        self.n_hot = len(hot_streams)
        self.n_cold = len(cold_streams)
        self.n_hot_util = len(hot_utilities)
        self.n_cold_util = len(cold_utilities)

        # Chromosome parts sizes
        self.proc_proc_size = stages * self.n_hot * self.n_cold
        self.hot_util_cold_size = self.n_hot_util * self.n_cold
        self.cold_util_hot_size = self.n_hot * self.n_cold_util

        self.chromosome_length = self.proc_proc_size + self.hot_util_cold_size + self.cold_util_hot_size
        self.population = [self.random_chromosome() for _ in range(pop_size)]

    def random_chromosome(self):
        proc_proc_part = np.random.randint(0, 2, self.proc_proc_size)
        hot_util_cold_part = np.zeros(self.hot_util_cold_size, dtype=int)
        cold_util_hot_part = np.zeros(self.cold_util_hot_size, dtype=int)

        # Assign at most one hot utility per cold stream
        for j in range(self.n_cold):
            assigned = False
            for u in range(self.n_hot_util):
                if not assigned and np.random.rand() < 0.5:
                    idx = u * self.n_cold + j
                    hot_util_cold_part[idx] = 1
                    assigned = True

        # Assign at most one cold utility per hot stream
        for i in range(self.n_hot):
            assigned = False
            for v in range(self.n_cold_util):
                if not assigned and np.random.rand() < 0.5:
                    idx = i * self.n_cold_util + v
                    cold_util_hot_part[idx] = 1
                    assigned = True

        return np.concatenate((proc_proc_part, hot_util_cold_part, cold_util_hot_part))

    def decode_chromosome(self, chromosome):
        proc_proc = chromosome[:self.proc_proc_size].reshape(self.stages, self.n_hot, self.n_cold)
        start = self.proc_proc_size
        hot_util_cold = chromosome[start:start+self.hot_util_cold_size].reshape(self.n_hot_util, self.n_cold)
        start += self.hot_util_cold_size
        cold_util_hot = chromosome[start:start+self.cold_util_hot_size].reshape(self.n_hot, self.n_cold_util)
        return proc_proc, hot_util_cold, cold_util_hot

    def fitness(self, chromosome):
        proc_proc, hot_util_cold, cold_util_hot = self.decode_chromosome(chromosome)
        total_cost = self.calculate_TAC(proc_proc, hot_util_cold, cold_util_hot)
        return total_cost

    def calculate_TAC(self, proc_proc, hot_util_cold, cold_util_hot):
        """
        Calculate Total Annual Cost (TAC) for a given network configuration.
        Includes area cost (Yee 1990: C_area = C * (area ** B)) and a fixed cost per match.
        Coefficients for each match type are set at the start for easy adjustment.
        """
        # --- Cost coefficients for each match type (easy to adjust here) ---
        # Process-process matches
        process_U, process_C, process_B, process_CF = 1.0, 1000, 0.6, 5000
        # Hot utility-cold matches
        hotutil_U, hotutil_C, hotutil_B, hotutil_CF = 1.2, 1200, 0.6, 7000
        # Cold utility-hot matches
        coldu_U, coldu_C, coldu_B, coldu_CF = 1.0, 1200, 0.6, 7000

        total_area_cost = 0.0
        total_fixed_cost = 0.0
        total_utility_cost = 0.0
        penalty = 0
        deltaT_min = 10  # Minimum approach temperature

        hot_temps = [hs.Tin for hs in self.hot_streams]
        cold_temps = [cs.Tin for cs in self.cold_streams]

        used_hot_utils = np.zeros(self.n_hot_util)
        used_cold_utils = np.zeros(self.n_cold_util)

        # --- Stagewise process-process matches ---
        for k in range(self.stages):
            for i, hs in enumerate(self.hot_streams):
                for j, cs in enumerate(self.cold_streams):
                    if proc_proc[k, i, j] == 1:
                        hot_available = hs.CP * (hot_temps[i] - hs.Tout)
                        cold_needed = cs.CP * (cs.Tout - cold_temps[j])
                        Q = min(hot_available, cold_needed)
                        if Q <= 0:
                            penalty += 1e6
                            continue
                        hot_out_temp = hot_temps[i] - Q / hs.CP
                        cold_out_temp = cold_temps[j] + Q / cs.CP
                        dt1 = hot_temps[i] - cold_out_temp
                        dt2 = hot_out_temp - cold_temps[j]
                        if dt1 < deltaT_min or dt2 < deltaT_min:
                            penalty += 1e6
                            continue
                        # Log-mean temperature difference (LMTD)
                        try:
                            LMTD = (dt1 - dt2) / np.log((dt1 + 1e-6) / (dt2 + 1e-6))
                        except Exception:
                            penalty += 1e6
                            continue
                        U = process_U
                        area = Q / (U * LMTD)
                        area_cost = process_C * (area ** process_B)
                        total_area_cost += area_cost
                        total_fixed_cost += process_CF
                        hot_temps[i] = hot_out_temp
                        cold_temps[j] = cold_out_temp

        # --- Utility assignments from chromosome ---
        # For cold streams: hot utility to cold stream matches
        for j in range(self.n_cold):
            assigned_util = None
            for u in range(self.n_hot_util):
                if hot_util_cold[u, j] == 1:
                    assigned_util = u
                    break
            if assigned_util is not None:
                cs = self.cold_streams[j]
                cu = self.hot_utilities[assigned_util]
                deltaT = cs.Tout - cold_temps[j]
                if deltaT > 1e-6:
                    Q_needed = cs.CP * deltaT
                    if cu.Tout <= cold_temps[j]:
                        penalty += 1e8
                    else:
                        # Area and cost for hot utility-cold match
                        # Assume utility temperature is cu.Tin (inlet), cs.Tout (target)
                        dt1 = cu.Tin - cs.Tout
                        dt2 = cu.Tout - cold_temps[j]
                        if dt1 < deltaT_min or dt2 < deltaT_min:
                            penalty += 1e8
                        else:
                            try:
                                LMTD = (dt1 - dt2) / np.log((dt1 + 1e-6) / (dt2 + 1e-6))
                            except Exception:
                                penalty += 1e8
                                continue
                            U = hotutil_U
                            area = Q_needed / (U * LMTD)
                            area_cost = hotutil_C * (area ** hotutil_B)
                            total_area_cost += area_cost
                            total_fixed_cost += hotutil_CF
                        utility_cost = Q_needed * cu.cost
                        total_utility_cost += utility_cost
                        cold_temps[j] = cs.Tout
                        used_hot_utils[assigned_util] += Q_needed
                else:
                    # Already satisfied
                    pass
            else:
                # No utility assigned, check if satisfied
                cs = self.cold_streams[j]
                deltaT = cs.Tout - cold_temps[j]
                if deltaT > 1e-6:
                    penalty += 1e8

        # For hot streams: cold utility to hot stream matches
        for i in range(self.n_hot):
            assigned_util = None
            for v in range(self.n_cold_util):
                if cold_util_hot[i, v] == 1:
                    assigned_util = v
                    break
            if assigned_util is not None:
                hs = self.hot_streams[i]
                cu = self.cold_utilities[assigned_util]
                deltaT = hot_temps[i] - hs.Tout
                if deltaT > 1e-6:
                    Q_needed = hs.CP * deltaT
                    if cu.Tin >= hot_temps[i]:
                        penalty += 1e8
                    else:
                        # Area and cost for cold utility-hot match
                        # Assume utility temperature is cu.Tin (inlet), hs.Tout (target)
                        dt1 = hot_temps[i] - cu.Tout
                        dt2 = hs.Tout - cu.Tin
                        if dt1 < deltaT_min or dt2 < deltaT_min:
                            penalty += 1e8
                        else:
                            try:
                                LMTD = (dt1 - dt2) / np.log((dt1 + 1e-6) / (dt2 + 1e-6))
                            except Exception:
                                penalty += 1e8
                                continue
                            U = coldu_U
                            area = Q_needed / (U * LMTD)
                            area_cost = coldu_C * (area ** coldu_B)
                            total_area_cost += area_cost
                            total_fixed_cost += coldu_CF
                        utility_cost = Q_needed * cu.cost
                        total_utility_cost += utility_cost
                        hot_temps[i] = hs.Tout
                        used_cold_utils[assigned_util] += Q_needed
                else:
                    # Already satisfied
                    pass
            else:
                # No utility assigned, check if satisfied
                hs = self.hot_streams[i]
                deltaT = hot_temps[i] - hs.Tout
                if deltaT > 1e-6:
                    penalty += 1e8

        total_cost = total_area_cost + total_fixed_cost + total_utility_cost + penalty
        return total_cost

    def run(self):
        for generation in range(self.gen):
            fitness_scores = [self.fitness(ch) for ch in self.population]
            best_idx = np.argmin(fitness_scores)
            best_fitness = fitness_scores[best_idx]

            new_pop = [self.population[best_idx]]  # elitism

            while len(new_pop) < self.pop_size:
                parents_indices = np.random.choice(len(self.population), 2, replace=False)
                parents = [self.population[idx] for idx in parents_indices]

                child = self.crossover(parents[0], parents[1])
                child = self.mutate(child)
                new_pop.append(child)

            self.population = new_pop
            print(f'Generation {generation+1}, Best Fitness: {best_fitness}')

        best_chromosome = self.population[np.argmin([self.fitness(ch) for ch in self.population])]
        return best_chromosome, self.fitness(best_chromosome)

    def crossover(self, p1, p2):
        point = np.random.randint(1, len(p1))
        return np.concatenate((p1[:point], p2[point:]))

    def mutate(self, chromosome, rate=0.01):
        for idx in range(len(chromosome)):
            if np.random.rand() < rate:
                chromosome[idx] = 1 - chromosome[idx]
        return chromosome

# Execution example
if __name__ == "__main__":
    # Load streams and utilities from CSV files
    hot_streams, cold_streams, hot_utilities, cold_utilities, stage_num = load_streams('streams.csv', 'utilities.csv')
    ga = GeneticAlgorithm(hot_streams, cold_streams, hot_utilities, cold_utilities, stage_num, pop_size=100, gen=100)
    best_solution, best_cost = ga.run()
    proc_proc, hot_util_cold, cold_util_hot = ga.decode_chromosome(best_solution)

    print("\nOptimal Heat Exchanger Network Solution:\n")

    hot_temps = [hs.Tin for hs in hot_streams]
    cold_temps = [cs.Tin for cs in cold_streams]
    deltaT_min = 10
    used_hot_utils = [0.0 for _ in hot_utilities]
    used_cold_utils = [0.0 for _ in cold_utilities]

    # ---- Stagewise reporting: process-process matches only ----
    for k in range(stage_num):
        print(f"Stage {k+1}:")
        for i, hs in enumerate(hot_streams):
            for j, cs in enumerate(cold_streams):
                if proc_proc[k, i, j] == 1:
                    hot_available = hs.CP * (hot_temps[i] - hs.Tout)
                    cold_available = cs.CP * (cs.Tout - cold_temps[j])
                    Q = min(hot_available, cold_available)
                    if Q <= 0:
                        continue
                    hot_out_temp = hot_temps[i] - Q / hs.CP
                    cold_out_temp = cold_temps[j] + Q / cs.CP
                    dt1 = hot_temps[i] - cold_out_temp
                    dt2 = hot_out_temp - cold_temps[j]
                    if dt1 < deltaT_min or dt2 < deltaT_min:
                        continue
                    print(f"  Process Exchanger: H{i+1} - C{j+1}")
                    print(f"    - Heat transferred (Q): {Q:.2f} kW")
                    print(f"    - Hot stream inlet temperature (H{i+1}): {hot_temps[i]:.2f}°C")
                    print(f"    - Hot stream outlet temperature (H{i+1}): {hot_out_temp:.2f}°C")
                    print(f"    - Cold stream inlet temperature (C{j+1}): {cold_temps[j]:.2f}°C")
                    print(f"    - Cold stream outlet temperature (C{j+1}): {cold_out_temp:.2f}°C\n")
                    hot_temps[i] = hot_out_temp
                    cold_temps[j] = cold_out_temp

    # ---- Utility matches from chromosome ----
    print("Utility Matches after all stages:\n")
    # For each cold stream: hot utility assigned
    for j, cs in enumerate(cold_streams):
        assigned_util = None
        for u in range(len(hot_utilities)):
            if hot_util_cold[u, j] == 1:
                assigned_util = u
                break
        if assigned_util is not None:
            cu = hot_utilities[assigned_util]
            deltaT = cs.Tout - cold_temps[j]
            if deltaT > 1e-6:
                Q_needed = cs.CP * deltaT
                if cu.Tout <= cold_temps[j]:
                    print(f"  ERROR: Hot Utility HU{assigned_util+1} temperature too low for C{j+1} (T={cold_temps[j]:.2f}°C)")
                else:
                    print(f"  Hot Utility Exchanger: HU{assigned_util+1} ({cu.Tin:.1f}-{cu.Tout:.1f}°C) - C{j+1}")
                    print(f"    - Heat supplied by HU{assigned_util+1}: {Q_needed:.2f} kW")
                    print(f"    - Utility (HU{assigned_util+1}) temperature: {cu.Tin:.2f} to {cu.Tout:.2f}°C")
                    print(f"    - Cold stream inlet temperature (C{j+1}): {cold_temps[j]:.2f}°C")
                    print(f"    - Cold stream outlet temperature (C{j+1}): {cs.Tout:.2f}°C\n")
                    used_hot_utils[assigned_util] += Q_needed
                    cold_temps[j] = cs.Tout
            else:
                print(f"  Hot Utility HU{assigned_util+1} assigned to C{j+1} but stream already satisfied.")
        else:
            deltaT = cs.Tout - cold_temps[j]
            if deltaT > 1e-6:
                print(f"  ERROR: No hot utility assigned to C{j+1} and stream not heated to target (T={cold_temps[j]:.2f}°C)")

    # For each hot stream: cold utility assigned
    for i, hs in enumerate(hot_streams):
        assigned_util = None
        for v in range(len(cold_utilities)):
            if cold_util_hot[i, v] == 1:
                assigned_util = v
                break
        if assigned_util is not None:
            cu = cold_utilities[assigned_util]
            deltaT = hot_temps[i] - hs.Tout
            if deltaT > 1e-6:
                Q_needed = hs.CP * deltaT
                if cu.Tin >= hot_temps[i]:
                    print(f"  ERROR: Cold Utility CU{assigned_util+1} temperature too high for H{i+1} (T={hot_temps[i]:.2f}°C)")
                else:
                    print(f"  Cold Utility Exchanger: H{i+1} - CU{assigned_util+1} ({cu.Tin:.1f}-{cu.Tout:.1f}°C)")
                    print(f"    - Heat removed by CU{assigned_util+1}: {Q_needed:.2f} kW")
                    print(f"    - Utility (CU{assigned_util+1}) temperature: {cu.Tin:.2f} to {cu.Tout:.2f}°C")
                    print(f"    - Hot stream inlet temperature (H{i+1}): {hot_temps[i]:.2f}°C")
                    print(f"    - Hot stream outlet temperature (H{i+1}): {hs.Tout:.2f}°C\n")
                    used_cold_utils[assigned_util] += Q_needed
                    hot_temps[i] = hs.Tout
            else:
                print(f"  Cold Utility CU{assigned_util+1} assigned to H{i+1} but stream already satisfied.")
        else:
            deltaT = hot_temps[i] - hs.Tout
            if deltaT > 1e-6:
                print(f"  ERROR: No cold utility assigned to H{i+1} and stream not cooled to target (T={hot_temps[i]:.2f}°C)")

    print("Utility Requirements after Heat Recovery:\n")
    for idx, hu in enumerate(hot_utilities):
        print(f"  - Hot Utility HU{idx+1} ({hu.Tin:.1f}-{hu.Tout:.1f}°C) supplied: {used_hot_utils[idx]:.2f} kW")
    for idx, cu in enumerate(cold_utilities):
        print(f"  - Cold Utility CU{idx+1} ({cu.Tin:.1f}-{cu.Tout:.1f}°C) used: {used_cold_utils[idx]:.2f} kW")

    print(f"\nOptimal Total Annual Cost (TAC): {best_cost:.2f}")
