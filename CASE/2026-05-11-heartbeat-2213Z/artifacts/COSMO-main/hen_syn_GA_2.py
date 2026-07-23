# --- Major Refactor: Yee 1990 MINLP-style GA with temperature-split chromosome and multi-utility/multi-stage logic ---
import numpy as np
from collections import namedtuple
import pandas as pd
import os # For checking/creating CSVs

Stream = namedtuple('Stream', ['type', 'Tin', 'Tout', 'CP'])
Utility = namedtuple('Utility', ['type', 'Tin', 'Tout', 'cost'])

def load_streams(streams_csv, utilities_csv):
    streams_df = pd.read_csv(streams_csv)
    utilities_df = pd.read_csv(utilities_csv)
    streams = [Stream(row['Type'], row['TIN_spec'], row['TOUT_spec'], row['Fcp'])
               for _, row in streams_df.iterrows()]
    utilities = [Utility(row['Type'], row['TIN_utility'], row['TOUT_utility'], row['Unit_Cost_Energy'])
                 for _, row in utilities_df.iterrows()]
    hot_streams = [s for s in streams if s.type.lower() == 'hot']
    cold_streams = [s for s in streams if s.type.lower() == 'cold']
    hot_utilities = [u for u in utilities if u.type.lower() == 'hot_utility']
    cold_utilities = [u for u in utilities if u.type.lower() == 'cold_utility']
    
    stage_num = max(len(hot_streams), len(cold_streams)) if (len(hot_streams) + len(cold_streams)) > 0 else 1
    return hot_streams, cold_streams, hot_utilities, cold_utilities, stage_num

def pinch_analysis(hot_streams, cold_streams, deltaTmin=10):
    # Step 1: Build all shifted stream temperature endpoints
    # It's good practice to store the shifted Tin/Tout with the stream CP for clarity.
    shifted_hot_streams = [
        {'CP': hs.CP, 'Tin_shifted': hs.Tin - deltaTmin/2, 'Tout_shifted': hs.Tout - deltaTmin/2}
        for hs in hot_streams
    ]
    shifted_cold_streams = [
        {'CP': cs.CP, 'Tin_shifted': cs.Tin + deltaTmin/2, 'Tout_shifted': cs.Tout + deltaTmin/2}
        for cs in cold_streams
    ]

    # Collect all unique shifted temperatures to define intervals
    temps = set()
    for s in shifted_hot_streams:
        temps.add(s['Tin_shifted'])
        temps.add(s['Tout_shifted'])
    for s in shifted_cold_streams:
        temps.add(s['Tin_shifted'])
        temps.add(s['Tout_shifted'])
    
    # Sort in descending order
    temps = sorted(list(temps), reverse=True)
    
    if len(temps) < 2:
        return 0.0, 0.0 # No streams or invalid temperatures for pinch analysis

    # Step 2: For each interval, compute net CP and dT
    intervals = []
    for i in range(len(temps)-1):
        T_high_interval, T_low_interval = temps[i], temps[i+1] # Boundaries of the current interval
        dT_interval = T_high_interval - T_low_interval

        # Sum CPs for hot streams active in interval
        CP_hot_active = sum(
            s['CP']
            for s in shifted_hot_streams
            # A hot stream is active if its shifted temperature range encompasses the interval
            # i.e., it starts at or above T_high_interval AND ends at or below T_low_interval
            if s['Tin_shifted'] >= T_high_interval and s['Tout_shifted'] <= T_low_interval
        )
        
        # Sum CPs for cold streams active in interval
        CP_cold_active = sum(
            s['CP']
            for s in shifted_cold_streams
            # A cold stream is active if its shifted temperature range encompasses the interval
            # i.e., it starts at or below T_low_interval AND ends at or above T_high_interval
            if s['Tin_shifted'] <= T_low_interval and s['Tout_shifted'] >= T_high_interval
        )
        
        net_CP = CP_hot_active - CP_cold_active
        intervals.append({'T_high': T_high_interval, 'T_low': T_low_interval, 'dT': dT_interval, 'net_CP': net_CP})

    # Step 3: Cascade
    enthalpy_cascade = [0.0]
    for iv in intervals:
        enthalpy_cascade.append(enthalpy_cascade[-1] + iv['net_CP'] * iv['dT'])
    
    # Step 4 & 5: Compute minimum utilities
    # The most negative point in the cascade curve is the deficit that needs hot utility
    min_heating_utility = max(0, -min(enthalpy_cascade))
    # The last point of the cascade curve, adjusted by the hot utility, gives the cold utility
    min_cooling_utility = enthalpy_cascade[-1] + min_heating_utility

    return min_heating_utility, min_cooling_utility

class YeeHEN_GA:
    def __init__(self, hot_streams, cold_streams, hot_utilities, cold_utilities, stage_num,
                 pop_size=50, gen=100, Q_HU_min=0, Q_CU_min=0):
        self.hot_streams = hot_streams
        self.cold_streams = cold_streams
        self.hot_utilities = hot_utilities
        self.cold_utilities = cold_utilities
        self.n_hot = len(hot_streams)
        self.n_cold = len(cold_streams)
        self.n_hot_util = len(hot_utilities)
        self.n_cold_util = len(cold_utilities)
        self.stage_num = stage_num
        self.pop_size = pop_size
        self.gen = gen
        self.Q_HU_min = Q_HU_min 
        self.Q_CU_min = Q_CU_min 

        # Chromosome segment lengths - MODIFIED UTILITY SEGMENT LENGTHS
        self.dt_split_len = (self.n_hot + self.n_cold) * self.stage_num
        self.qfrac_hot_len = self.n_hot * self.n_cold * self.stage_num
        self.qfrac_cold_len = self.n_cold * self.n_hot * self.stage_num
        # Utility assignment lengths are now independent of stages
        self.hot_util_len = self.n_hot * self.n_cold_util if self.n_cold_util > 0 else 0
        self.cold_util_len = self.n_cold * self.n_hot_util if self.n_hot_util > 0 else 0
        
        self.chromosome_length = (
            self.dt_split_len
            + self.qfrac_hot_len
            + self.qfrac_cold_len
            + self.hot_util_len
            + self.cold_util_len
        )
        
        # Seed initial population: first 20% process-to-process favored, rest random
        n_favored = int(np.ceil(0.2 * self.pop_size))
        self.population = []
        for idx in range(self.pop_size):
            if idx < n_favored:
                self.population.append(self.favored_chromosome())
            else:
                self.population.append(self.random_chromosome())

        self.utility_penalty_factor = 100 

    def random_chromosome(self):
        dt_splits = []
        for s in range(self.n_hot + self.n_cold):
            if self.stage_num == 0: splits = np.array([])
            else: splits = np.random.dirichlet(np.ones(self.stage_num))
            dt_splits.extend(splits)

        qfrac_hot = np.zeros((self.n_hot, self.n_cold, self.stage_num))
        if self.n_cold > 0 and self.stage_num > 0:
            for i in range(self.n_hot):
                for k in range(self.stage_num):
                    qfrac = np.random.dirichlet(np.ones(self.n_cold))
                    qfrac_hot[i, :, k] = qfrac

        qfrac_cold = np.zeros((self.n_cold, self.n_hot, self.stage_num))
        if self.n_hot > 0 and self.stage_num > 0:
            for j in range(self.n_cold):
                for k in range(self.stage_num):
                    qfrac = np.random.dirichlet(np.ones(self.n_hot))
                    qfrac_cold[j, :, k] = qfrac

        # Utility assignment: one-hot for each stream, random assignment - MODIFIED
        hot_util_assign = np.zeros((self.n_hot, self.n_cold_util))
        if self.n_cold_util > 0:
            for i in range(self.n_hot):
                idx = np.random.choice(self.n_cold_util)
                hot_util_assign[i, idx] = 1

        cold_util_assign = np.zeros((self.n_cold, self.n_hot_util))
        if self.n_hot_util > 0:
            for j in range(self.n_cold):
                idx = np.random.choice(self.n_hot_util)
                cold_util_assign[j, idx] = 1

        chrom = np.concatenate([
            np.array(dt_splits),
            qfrac_hot.flatten(),
            qfrac_cold.flatten(),
            hot_util_assign.flatten(), # No longer multiplied by stage_num
            cold_util_assign.flatten()  # No longer multiplied by stage_num
        ])
        return chrom

    def favored_chromosome(self):
        dt_splits = []
        for s in range(self.n_hot + self.n_cold):
            splits = np.zeros(self.stage_num)
            if self.stage_num > 0:
                splits[-1] = 1.0 
            dt_splits.extend(splits)

        qfrac_hot = np.zeros((self.n_hot, self.n_cold, self.stage_num))
        qfrac_cold = np.zeros((self.n_cold, self.n_hot, self.stage_num))

        if self.stage_num > 0:
            last_stage_k = self.stage_num - 1
            if self.n_cold > 0:
                for i in range(self.n_hot):
                    j_match = i if self.n_hot == self.n_cold else i % self.n_cold
                    qfrac_hot[i, j_match, last_stage_k] = 1.0
            if self.n_hot > 0:
                for j in range(self.n_cold):
                    i_match = j if self.n_hot == self.n_cold else j % self.n_hot
                    qfrac_cold[j, i_match, last_stage_k] = 1.0

        # Utility assignment: initially, attempt no utility (all zeros) to promote process-process. - MODIFIED
        hot_util_assign = np.zeros((self.n_hot, self.n_cold_util))
        cold_util_assign = np.zeros((self.n_cold, self.n_hot_util))
        
        chrom = np.concatenate([
            np.array(dt_splits),
            qfrac_hot.flatten(),
            qfrac_cold.flatten(),
            hot_util_assign.flatten(), # No longer multiplied by stage_num
            cold_util_assign.flatten()  # No longer multiplied by stage_num
        ])
        return chrom

    def decode_chromosome(self, chromosome):
        dt_splits = chromosome[:self.dt_split_len].reshape((self.n_hot + self.n_cold, self.stage_num))
        start = self.dt_split_len
        qfrac_hot = chromosome[start:start + self.qfrac_hot_len].reshape((self.n_hot, self.n_cold, self.stage_num))
        start += self.qfrac_hot_len
        qfrac_cold = chromosome[start:start + self.qfrac_cold_len].reshape((self.n_cold, self.n_hot, self.stage_num))
        start += self.qfrac_cold_len
        # MODIFIED SLICING FOR UTILITY ASSIGNMENTS
        hot_assign = chromosome[start:start + self.hot_util_len].reshape((self.n_hot, self.n_cold_util))
        start += self.hot_util_len
        cold_assign = chromosome[start:start + self.cold_util_len].reshape((self.n_cold, self.n_hot_util))
        return dt_splits, qfrac_hot, qfrac_cold, hot_assign, cold_assign

    def evaluate(self, chromosome):
        dt_splits, qfrac_hot, qfrac_cold, hot_assign, cold_assign = self.decode_chromosome(chromosome)
        deltaT_min = 10
        penalty = 0

        hot_deltas = []
        for i, hs in enumerate(self.hot_streams):
            total_dT = hs.Tin - hs.Tout
            splits = dt_splits[i]
            splits = np.maximum(splits, 1e-6) # Ensure positive values, avoid zero splits
            sum_splits = np.sum(splits)
            if sum_splits < 1e-6: # Check if sum is effectively zero after max(1e-6)
                penalty += 1e7 # High penalty for no temperature change defined for a stream
                hot_deltas.append(np.zeros(self.stage_num))
            else:
                hot_deltas.append(splits / sum_splits * total_dT)
        
        cold_deltas = []
        for j, cs in enumerate(self.cold_streams):
            total_dT = cs.Tout - cs.Tin
            splits = dt_splits[self.n_hot + j]
            splits = np.maximum(splits, 1e-6) # Ensure positive values
            sum_splits = np.sum(splits)
            if sum_splits < 1e-6:
                penalty += 1e7
                cold_deltas.append(np.zeros(self.stage_num))
            else:
                cold_deltas.append(splits / sum_splits * total_dT)

        hot_deltas = np.array(hot_deltas) # shape (n_hot, stage_num)
        cold_deltas = np.array(cold_deltas) # shape (n_cold, stage_num)

        hot_util_idx = np.zeros(self.n_hot, dtype=int)
        if self.n_cold_util > 0:
            # Check if sum is 1.0. If not, means the one-hot structure was broken by crossover/mutation.
            if not np.all(np.isclose(np.sum(hot_assign, axis=1), 1.0, atol=1e-3)):
                penalty += 1e6 # Penalty for non-one-hot utility assignment
            hot_util_idx = np.argmax(hot_assign, axis=1)

        cold_util_idx = np.zeros(self.n_cold, dtype=int)
        if self.n_hot_util > 0:
            if not np.all(np.isclose(np.sum(cold_assign, axis=1), 1.0, atol=1e-3)):
                penalty += 1e6 # Penalty for non-one-hot utility assignment
            cold_util_idx = np.argmax(cold_assign, axis=1)

        for i in range(self.n_hot):
            for k in range(self.stage_num):
                s = np.sum(qfrac_hot[i, :, k])
                if not np.isclose(s, 1.0, atol=1e-3):
                    penalty += 1e5 * abs(s - 1.0)
        for j in range(self.n_cold):
            for k in range(self.stage_num):
                s = np.sum(qfrac_cold[j, :, k])
                if not np.isclose(s, 1.0, atol=1e-3):
                    penalty += 1e5 * abs(s - 1.0)

        # Cost coefficients (Yee 1990)
        process_U, process_C, process_B, process_CF = 1.0, 1000, 0.6, 5000
        hotutil_U, hotutil_C, hotutil_B, hotutil_CF = 1.2, 1200, 0.6, 7000
        coldu_U, coldu_C, coldu_B, coldu_CF = 1.0, 1200, 0.6, 7000
        
        total_area_cost = 0.0
        total_fixed_cost = 0.0 
        total_utility_cost = 0.0

        # Track Q delivered/received per stream across all stages (process-process + final utility)
        Q_hot_delivered = np.zeros(self.n_hot) 
        Q_cold_received = np.zeros(self.n_cold) 

        # Build temperature profiles stage by stage (Process-process only)
        hot_temps = np.zeros((self.n_hot, self.stage_num+1))
        cold_temps = np.zeros((self.n_cold, self.stage_num+1))
        for i, hs in enumerate(self.hot_streams):
            hot_temps[i, 0] = hs.Tin
        for j, cs in enumerate(self.cold_streams):
            cold_temps[j, 0] = cs.Tin

        # Stagewise energy balance and cost calculation (PROCESS-PROCESS ONLY)
        for k in range(self.stage_num):
            T_hot_in_stage = hot_temps[:, k].copy() # Temperatures entering this stage
            T_cold_in_stage = cold_temps[:, k].copy()

            for i, hs in enumerate(self.hot_streams):
                hot_temps[i, k+1] = T_hot_in_stage[i] - hot_deltas[i, k]
            for j, cs in enumerate(self.cold_streams):
                cold_temps[j, k+1] = T_cold_in_stage[j] + cold_deltas[j, k]

            # Total Q available/needed from streams for THIS STAGE based on deltaTs
            Q_hot_stage_total = np.array([hs.CP * hot_deltas[i, k] for i, hs in enumerate(self.hot_streams)])
            Q_cold_stage_total = np.array([cs.CP * cold_deltas[j, k] for j, cs in enumerate(self.cold_streams)])

            # Proposed Q transfer for each potential process-process match (H_i <-> C_j)
            Q_match_proposal = np.zeros((self.n_hot, self.n_cold))
            for i in range(self.n_hot):
                for j in range(self.n_cold):
                    Q_h_prop_from_frac = Q_hot_stage_total[i] * qfrac_hot[i, j, k]
                    Q_c_prop_from_frac = Q_cold_stage_total[j] * qfrac_cold[j, i, k]
                    Q_match_proposal[i, j] = min(Q_h_prop_from_frac, Q_c_prop_from_frac)
                    Q_match_proposal[i, j] = max(0.0, Q_match_proposal[i, j])

            for i in range(self.n_hot):
                for j in range(self.n_cold):
                    Q_ij = Q_match_proposal[i, j]
                    if Q_ij > 1e-8: # Only proceed if there's actual heat transfer
                        # Temperatures for LMTD are based on stage entry/exit temperatures
                        T_hi_in = hot_temps[i, k]
                        T_hi_out = hot_temps[i, k+1] 
                        T_cj_in = cold_temps[j, k]
                        T_cj_out = cold_temps[j, k+1] 

                        dt1 = T_hi_in - T_cj_out
                        dt2 = T_hi_out - T_cj_in

                        if dt1 < deltaT_min or dt2 < deltaT_min:
                            penalty += 1e6 # High penalty for pinch violation
                            continue 

                        try:
                            if abs(dt1 - dt2) < 1e-6: # Handle cases where deltaTs are almost equal
                                LMTD = dt1
                            else:
                                LMTD = (dt1 - dt2) / (np.log(dt1 / dt2))
                            if LMTD <= 0 or not np.isfinite(LMTD): # Check for invalid LMTD values
                                penalty += 1e6 
                                continue
                        except Exception: # Catch other potential errors during log calculation (e.g. log of negative)
                            penalty += 1e6 
                            continue

                        area = Q_ij / (process_U * LMTD)
                        area_cost = process_C * (area ** process_B)
                        total_area_cost += area_cost
                        total_fixed_cost += process_CF
                    
                    Q_hot_delivered[i] += Q_ij
                    Q_cold_received[j] += Q_ij
        
        # --- NEW SECTION: Utility Calculation AFTER all process-process stages ---
        for i, hs in enumerate(self.hot_streams):
            T_current = hot_temps[i, -1] # Temperature after all process-process stages
            Q_needed_from_CU = hs.CP * (T_current - hs.Tout) # Heat to be removed by utility
            
            if Q_needed_from_CU > 1e-6: # If hot stream still needs cooling
                if self.n_cold_util > 0:
                    uidx = hot_util_idx[i]
                    cu = self.cold_utilities[uidx]

                    dt1 = T_current - cu.Tout
                    dt2 = hs.Tout - cu.Tin 

                    can_form_utility_exchanger = True
                    # Check deltaT_min for utility exchanger
                    if dt1 < deltaT_min or dt2 < deltaT_min:
                        can_form_utility_exchanger = False
                        penalty += 1e6 # Penalty for utility pinch violation
                    
                    if can_form_utility_exchanger: # Proceed if deltaT_min is okay
                        try:
                            if abs(dt1 - dt2) < 1e-6: LMTD = dt1
                            else: LMTD = (dt1 - dt2) / np.log(dt1 / dt2)
                            if LMTD <= 0 or not np.isfinite(LMTD):
                                can_form_utility_exchanger = False
                                penalty += 1e6 # Penalty for LMTD issue
                        except Exception:
                            can_form_utility_exchanger = False
                            penalty += 1e6 # Penalty for other LMTD calculation errors

                    if can_form_utility_exchanger:
                        area = Q_needed_from_CU / (coldu_U * LMTD)
                        total_area_cost += coldu_C * (area ** coldu_B)
                        total_fixed_cost += coldu_CF
                        total_utility_cost += Q_needed_from_CU * cu.cost
                        Q_hot_delivered[i] += Q_needed_from_CU # Add utility duty to total delivered
                    else:
                        # CRITICAL CHANGE: Utility assigned but cannot be used due to constraints
                        # Apply a high penalty to force the GA to resolve this
                        penalty += 1e7 * Q_needed_from_CU # Severe penalty for unfulfilled utility duty
                else:
                    # Original case: utility is needed but no utility option exists at all
                    penalty += 1e8 * Q_needed_from_CU 
            # Penalize if hot stream is OVER-COOLED (i.e., went below target temp)
            elif Q_needed_from_CU < -1e-6:
                penalty += 1e7 * abs(Q_needed_from_CU)

        for j, cs in enumerate(self.cold_streams):
            T_current = cold_temps[j, -1] # Temperature after all process-process stages
            Q_needed_from_HU = cs.CP * (cs.Tout - T_current) # Heat to be added by utility

            if Q_needed_from_HU > 1e-6: # If cold stream still needs heating
                if self.n_hot_util > 0:
                    uidx = cold_util_idx[j]
                    hu = self.hot_utilities[uidx]

                    dt1 = hu.Tin - cs.Tout 
                    dt2 = hu.Tout - T_current

                    can_form_utility_exchanger = True
                    if dt1 < deltaT_min or dt2 < deltaT_min:
                        can_form_utility_exchanger = False
                        penalty += 1e6
                    
                    if can_form_utility_exchanger:
                        try:
                            if abs(dt1 - dt2) < 1e-6: LMTD = dt1
                            else: LMTD = (dt1 - dt2) / np.log(dt1 / dt2)
                            if LMTD <= 0 or not np.isfinite(LMTD):
                                can_form_utility_exchanger = False
                                penalty += 1e6
                        except Exception:
                            can_form_utility_exchanger = False
                            penalty += 1e6

                    if can_form_utility_exchanger:
                        area = Q_needed_from_HU / (hotutil_U * LMTD)
                        total_area_cost += hotutil_C * (area ** hotutil_B)
                        total_fixed_cost += hotutil_CF
                        total_utility_cost += Q_needed_from_HU * hu.cost
                        Q_cold_received[j] += Q_needed_from_HU 
                    else:
                        penalty += 1e7 * Q_needed_from_HU 
                else:
                    penalty += 1e8 * Q_needed_from_HU 
            # Penalize if cold stream is OVER-HEATED (i.e., went above target temp)
            elif Q_needed_from_HU < -1e-6:
                penalty += 1e7 * abs(Q_needed_from_HU) 

        # After all stages, check if total Q delivered/received matches required duty for each stream
        for i, hs in enumerate(self.hot_streams):
            Q_required = hs.CP * (hs.Tin - hs.Tout)
            # Use relative tolerance for energy balance check
            if Q_required > 1e-6 and abs(Q_hot_delivered[i] - Q_required) / Q_required > 1e-3: # 0.1% tolerance
                penalty += 1e6 * abs(Q_hot_delivered[i] - Q_required) # Reduced penalty
            elif Q_required <= 1e-6 and abs(Q_hot_delivered[i] - Q_required) > 1e-3: # Absolute for very small duties
                penalty += 1e6 * abs(Q_hot_delivered[i] - Q_required)
        for j, cs in enumerate(self.cold_streams):
            Q_required = cs.CP * (cs.Tout - cs.Tin)
            if Q_required > 1e-6 and abs(Q_cold_received[j] - Q_required) / Q_required > 1e-3: # 0.1% tolerance
                penalty += 1e6 * abs(Q_cold_received[j] - Q_required) # Reduced penalty
            elif Q_required <= 1e-6 and abs(Q_cold_received[j] - Q_required) > 1e-3:
                penalty += 1e6 * abs(Q_cold_received[j] - Q_required)
            
        total_cost = total_area_cost + total_fixed_cost + self.utility_penalty_factor * total_utility_cost + penalty
        return total_cost

    def run(self):
        best_overall_chromosome = None
        best_overall_fitness = float('inf')

        for generation in range(self.gen):
            fitness_scores = [self.evaluate(ch) for ch in self.population]
            current_best_idx = np.argmin(fitness_scores)
            current_best_fitness = fitness_scores[current_best_idx]

            if current_best_fitness < best_overall_fitness:
                best_overall_fitness = current_best_fitness
                best_overall_chromosome = self.population[current_best_idx].copy()

            new_pop = [self.population[current_best_idx].copy()]  # elitism
            while len(new_pop) < self.pop_size:
                # Rank-based selection for parents
                parents_indices = np.random.choice(len(self.population), 2, replace=False, p=self._get_selection_probs(fitness_scores))
                parents = [self.population[idx] for idx in parents_indices]
                child = self.crossover(parents[0], parents[1])
                child = self.mutate(child)
                new_pop.append(child)
            self.population = new_pop
            print(f'Generation {generation+1}, Best Fitness: {current_best_fitness:.2f}, Overall Best: {best_overall_fitness:.2f}')
        
        return best_overall_chromosome, best_overall_fitness

    def _get_selection_probs(self, fitness_scores):
        # Rank-based selection: Lower cost gets higher rank/prob
        sorted_indices = np.argsort(fitness_scores) # Ascending order (lowest cost first)
        # Assign higher rank to lower cost (e.g., if N individuals, rank N for best, 1 for worst)
        ranks = np.arange(len(fitness_scores), 0, -1) 
        # Normalize ranks to sum to 1 to form probabilities
        probs = ranks / np.sum(ranks)
        
        # Reorder probabilities back to original population order
        ordered_probs = np.zeros_like(probs)
        ordered_probs[sorted_indices] = probs
        return ordered_probs

    def crossover(self, p1, p2):
        # Uniform crossover for real-valued and one-hot genes
        mask = np.random.rand(len(p1)) < 0.5
        child = np.where(mask, p1, p2)

        # After crossover, re-normalize real-valued gene blocks and enforce one-hot
        # dt_splits: sum to 1 per stream
        dt_splits_section = child[:self.dt_split_len].reshape((self.n_hot + self.n_cold, self.stage_num))
        for s in range(self.n_hot + self.n_cold):
            s_splits = dt_splits_section[s]
            s_splits = np.maximum(s_splits, 1e-6) # Ensure positive values
            sum_s_splits = np.sum(s_splits)
            if sum_s_splits > 1e-6: # Only normalize if sum is not effectively zero
                s_splits = s_splits / sum_s_splits
            else: # If all are effectively zero, reinitialize with uniform split
                s_splits = np.ones(self.stage_num) / self.stage_num if self.stage_num > 0 else np.array([])
            dt_splits_section[s] = s_splits
        child[:self.dt_split_len] = dt_splits_section.flatten()

        # qfrac_hot: sum to 1 per hot stream per stage
        qfrac_hot_start = self.dt_split_len
        qfrac_hot_end = qfrac_hot_start + self.qfrac_hot_len
        qfrac_hot = child[qfrac_hot_start:qfrac_hot_end].reshape((self.n_hot, self.n_cold, self.stage_num))
        if self.n_cold > 0 and self.stage_num > 0: 
            for i in range(self.n_hot):
                for k in range(self.stage_num):
                    q = qfrac_hot[i, :, k]
                    q = np.maximum(q, 1e-6)
                    sum_q = np.sum(q)
                    if sum_q > 1e-6:
                        q = q / sum_q
                    else: # If all are effectively zero, reinitialize uniformly
                        q = np.ones(self.n_cold) / self.n_cold
                    qfrac_hot[i, :, k] = q
        child[qfrac_hot_start:qfrac_hot_end] = qfrac_hot.flatten()

        # qfrac_cold: sum to 1 per cold stream per stage
        qfrac_cold_start = qfrac_hot_end
        qfrac_cold_end = qfrac_cold_start + self.qfrac_cold_len
        qfrac_cold = child[qfrac_cold_start:qfrac_cold_end].reshape((self.n_cold, self.n_hot, self.stage_num))
        if self.n_hot > 0 and self.stage_num > 0:
            for j in range(self.n_cold):
                for k in range(self.stage_num):
                    q = qfrac_cold[j, :, k]
                    q = np.maximum(q, 1e-6)
                    sum_q = np.sum(q)
                    if sum_q > 1e-6:
                        q = q / sum_q
                    else: # If all are effectively zero, reinitialize uniformly
                        q = np.ones(self.n_hot) / self.n_hot
                    qfrac_cold[j, :, k] = q
        child[qfrac_cold_start:qfrac_cold_end] = qfrac_cold.flatten()

        # Utility assignment: Ensure one-hot property (only one utility selected per stream)
        current_start_idx = qfrac_cold_end
        if self.n_cold_util > 0:
            for i in range(self.n_hot):
                util_segment = child[current_start_idx + i*self.n_cold_util : current_start_idx + (i+1)*self.n_cold_util]
                if np.sum(util_segment) < 0.5: # If not already clearly one-hot, or all zeros
                    idx = np.random.choice(self.n_cold_util) # Randomly pick one
                    util_segment[:] = 0.0
                    util_segment[idx] = 1.0
                else: # Otherwise, normalize to one-hot based on argmax
                    idx = np.argmax(util_segment)
                    util_segment[:] = 0.0
                    util_segment[idx] = 1.0
                child[current_start_idx + i*self.n_cold_util : current_start_idx + (i+1)*self.n_cold_util] = util_segment
        
        current_start_idx += self.n_hot * self.n_cold_util
        if self.n_hot_util > 0:
            for j in range(self.n_cold):
                util_segment = child[current_start_idx + j*self.n_hot_util : current_start_idx + (j+1)*self.n_hot_util]
                if np.sum(util_segment) < 0.5:
                    idx = np.random.choice(self.n_hot_util)
                    util_segment[:] = 0.0
                    util_segment[idx] = 1.0
                else:
                    idx = np.argmax(util_segment)
                    util_segment[:] = 0.0
                    util_segment[idx] = 1.0
                child[current_start_idx + j*self.n_hot_util : current_start_idx + (j+1)*self.n_hot_util] = util_segment
        
        return child

    def mutate(self, chromosome, rate=0.05): # Increased mutation rate slightly
        chrom = chromosome.copy()

        # ΔT splits mutation
        splits = chrom[:self.dt_split_len].reshape((self.n_hot + self.n_cold, self.stage_num))
        for s in range(splits.shape[0]):
            if np.random.rand() < rate:
                noise = np.random.normal(0, 0.08, size=self.stage_num) # Increased stddev for more exploration
                splits[s] = splits[s] + noise
                splits[s] = np.maximum(splits[s], 1e-6) 
                if np.sum(splits[s]) > 1e-6:
                    splits[s] = splits[s] / np.sum(splits[s]) 
                else: # Reinitialize if sum becomes zero after noise
                    splits[s] = np.ones(self.stage_num) / self.stage_num if self.stage_num > 0 else np.array([])
        chrom[:self.dt_split_len] = splits.flatten()

        # qfrac_hot mutation
        qfrac_hot_start = self.dt_split_len
        qfrac_hot_end = qfrac_hot_start + self.qfrac_hot_len
        qfrac_hot = chrom[qfrac_hot_start:qfrac_hot_end].reshape((self.n_hot, self.n_cold, self.stage_num))
        if self.n_cold > 0 and self.stage_num > 0:
            for i in range(self.n_hot):
                for k in range(self.stage_num):
                    if np.random.rand() < rate:
                        noise = np.random.normal(0, 0.08, size=self.n_cold) 
                        q = qfrac_hot[i, :, k] + noise
                        q = np.maximum(q, 1e-6)
                        if np.sum(q) > 1e-6:
                            q = q / np.sum(q)
                        else:
                            q = np.ones(self.n_cold) / self.n_cold
                        qfrac_hot[i, :, k] = q
        chrom[qfrac_hot_start:qfrac_hot_end] = qfrac_hot.flatten()

        # qfrac_cold mutation
        qfrac_cold_start = qfrac_hot_end
        qfrac_cold_end = qfrac_cold_start + self.qfrac_cold_len
        qfrac_cold = chrom[qfrac_cold_start:qfrac_cold_end].reshape((self.n_cold, self.n_hot, self.stage_num))
        if self.n_hot > 0 and self.stage_num > 0:
            for j in range(self.n_cold):
                for k in range(self.stage_num):
                    if np.random.rand() < rate:
                        noise = np.random.normal(0, 0.08, size=self.n_hot) 
                        q = qfrac_cold[j, :, k] + noise
                        q = np.maximum(q, 1e-6)
                        if np.sum(q) > 1e-6:
                            q = q / np.sum(q)
                        else:
                            q = np.ones(self.n_hot) / self.n_hot
                        qfrac_cold[j, :, k] = q
        chrom[qfrac_cold_start:qfrac_cold_end] = qfrac_cold.flatten()

        # Utility assignments mutation (one-hot): random re-selection
        current_start_idx = qfrac_cold_end
        if self.n_cold_util > 0:
            for i in range(self.n_hot):
                if np.random.rand() < rate:
                    chrom[current_start_idx + i*self.n_cold_util : current_start_idx + (i+1)*self.n_cold_util] = 0 
                    idx = np.random.choice(self.n_cold_util) 
                    chrom[current_start_idx + i*self.n_cold_util + idx] = 1 
        
        current_start_idx += self.n_hot * self.n_cold_util
        if self.n_hot_util > 0:
            for j in range(self.n_cold):
                if np.random.rand() < rate:
                    chrom[current_start_idx + j*self.n_hot_util : current_start_idx + (j+1)*self.n_hot_util] = 0 
                    idx = np.random.choice(self.n_hot_util) 
                    chrom[current_start_idx + j*self.n_hot_util + idx] = 1 
        return chrom

    def print_solution(self, chromosome):
        print("\n--- Optimal Heat Exchanger Network Solution (Yee 1990 MINLP-style) ---\n")
        dt_splits, qfrac_hot, qfrac_cold, hot_assign, cold_assign = self.decode_chromosome(chromosome)
        deltaT_min = 10
        
        hot_deltas = []
        for i, hs in enumerate(self.hot_streams):
            total_dT = hs.Tin - hs.Tout
            splits = dt_splits[i]
            splits = np.maximum(splits, 1e-6)
            sum_splits = np.sum(splits)
            if sum_splits < 1e-6: 
                hot_deltas.append(np.zeros(self.stage_num))
            else:
                hot_deltas.append(splits / sum_splits * total_dT)
        cold_deltas = []
        for j, cs in enumerate(self.cold_streams):
            total_dT = cs.Tout - cs.Tin
            splits = dt_splits[self.n_hot + j]
            splits = np.maximum(splits, 1e-6)
            sum_splits = np.sum(splits)
            if sum_splits < 1e-6:
                cold_deltas.append(np.zeros(self.stage_num))
            else:
                cold_deltas.append(splits / sum_splits * total_dT)
        hot_deltas = np.array(hot_deltas)
        cold_deltas = np.array(cold_deltas)

        hot_util_idx = np.zeros(self.n_hot, dtype=int)
        if self.n_cold_util > 0: hot_util_idx = np.argmax(hot_assign, axis=1)
        cold_util_idx = np.zeros(self.n_cold, dtype=int)
        if self.n_hot_util > 0: cold_util_idx = np.argmax(cold_assign, axis=1)

        # Build temperature profiles (Process-process only)
        hot_temps = np.zeros((self.n_hot, self.stage_num+1))
        cold_temps = np.zeros((self.n_cold, self.stage_num+1))
        for i, hs in enumerate(self.hot_streams):
            hot_temps[i, 0] = hs.Tin
        for j, cs in enumerate(self.cold_streams):
            cold_temps[j, 0] = cs.Tin

        print("Stagewise stream temperature evolution (Process-Process Only):")
        for k in range(self.stage_num):
            print(f"  Stage {k+1}:")
            T_hot_in_stage = hot_temps[:, k].copy()
            T_cold_in_stage = cold_temps[:, k].copy()

            for i, hs in enumerate(self.hot_streams):
                hot_temps[i, k+1] = T_hot_in_stage[i] - hot_deltas[i, k]
                print(f"    Hot stream H{i+1}: {T_hot_in_stage[i]:.2f} -> {hot_temps[i, k+1]:.2f} °C (ΔT={hot_deltas[i,k]:.2f})")
            for j, cs in enumerate(self.cold_streams):
                cold_temps[j, k+1] = T_cold_in_stage[j] + cold_deltas[j, k]
                print(f"    Cold stream C{j+1}: {T_cold_in_stage[j]:.2f} -> {cold_temps[j, k+1]:.2f} °C (ΔT={cold_deltas[j,k]:.2f})")

        # Track Q delivered/received per stream for summary
        Q_hot_delivered_total = np.zeros(self.n_hot)
        Q_cold_received_total = np.zeros(self.n_cold)
        Q_hot_util_total = np.zeros(self.n_hot) 
        Q_cold_util_total = np.zeros(self.n_cold) 

        print("\nStagewise process-process heat transfer:")
        for k in range(self.stage_num):
            Q_hot_stage_total = np.array([hs.CP * hot_deltas[i, k] for i, hs in enumerate(self.hot_streams)])
            Q_cold_stage_total = np.array([cs.CP * cold_deltas[j, k] for j, cs in enumerate(self.cold_streams)])

            Q_match_proposal = np.zeros((self.n_hot, self.n_cold))
            for i in range(self.n_hot):
                for j in range(self.n_cold):
                    Q_h_prop_from_frac = Q_hot_stage_total[i] * qfrac_hot[i, j, k]
                    Q_c_prop_from_frac = Q_cold_stage_total[j] * qfrac_cold[j, i, k]
                    Q_match_proposal[i, j] = min(Q_h_prop_from_frac, Q_c_prop_from_frac)
                    Q_match_proposal[i, j] = max(0.0, Q_match_proposal[i, j])

            for i in range(self.n_hot):
                for j in range(self.n_cold):
                    Q_ij = Q_match_proposal[i, j]
                    if Q_ij > 1e-8:
                        Q_hot_delivered_total[i] += Q_ij
                        Q_cold_received_total[j] += Q_ij
                        print(f"  Stage {k+1}: H{i+1} <-> C{j+1}: Q = {Q_ij:.2f} kW (Qfrac_hot={qfrac_hot[i,j,k]:.2f}, Qfrac_cold={qfrac_cold[j,i,k]:.2f})")

        print("\nFinal Utility duties (after all stages):")
        for i, hs in enumerate(self.hot_streams):
            T_current = hot_temps[i, -1]
            Q_needed_from_CU = hs.CP * (T_current - hs.Tout)

            if Q_needed_from_CU > 1e-6: # If hot stream still needs cooling
                if self.n_cold_util > 0:
                    uidx = hot_util_idx[i]
                    cu = self.cold_utilities[uidx]
                    
                    dt1 = T_current - cu.Tout
                    dt2 = hs.Tout - cu.Tin 

                    can_form_utility_exchanger_print = True
                    reason_not_formed = ""
                    if dt1 < deltaT_min or dt2 < deltaT_min:
                        can_form_utility_exchanger_print = False
                        reason_not_formed = "deltaT_min violation"
                    
                    if can_form_utility_exchanger_print:
                        try:
                            if abs(dt1 - dt2) < 1e-6: LMTD = dt1
                            else: LMTD = (dt1 - dt2) / np.log(dt1 / dt2)
                            if LMTD <= 0 or not np.isfinite(LMTD):
                                can_form_utility_exchanger_print = False
                                reason_not_formed = "LMTD invalid"
                        except Exception:
                            can_form_utility_exchanger_print = False
                            reason_not_formed = "LMTD calculation error"

                    if can_form_utility_exchanger_print:
                        Q_hot_util_total[i] += Q_needed_from_CU
                        Q_hot_delivered_total[i] += Q_needed_from_CU
                        print(f"  Hot stream H{i+1} final cooling: {Q_needed_from_CU:.2f} kW from Cold Utility CU{uidx+1} ({cu.Tin}-{cu.Tout}°C)")
                    else:
                        print(f"  Hot stream H{i+1} needs {Q_needed_from_CU:.2f} kW final cooling from Cold Utility CU{uidx+1}, but cannot form exchanger due to {reason_not_formed}.")
                else:
                    print(f"  Hot stream H{i+1} needs {Q_needed_from_CU:.2f} kW final cooling (no cold utility assigned or available).")
            elif Q_needed_from_CU < -1e-6: # Penalize if hot stream is OVER-COOLED
                print(f"  Hot stream H{i+1} OVER-COOLED: {abs(Q_needed_from_CU):.2f} kW past target {hs.Tout}°C. Current temp: {T_current:.2f}°C")
            else:
                print(f"  Hot stream H{i+1} reached target {hs.Tout:.2f}°C after process-process exchange.")

        for j, cs in enumerate(self.cold_streams):
            T_current = cold_temps[j, -1]
            Q_needed_from_HU = cs.CP * (cs.Tout - T_current)

            if Q_needed_from_HU > 1e-6: # If cold stream still needs heating
                if self.n_hot_util > 0:
                    uidx = cold_util_idx[j]
                    hu = self.hot_utilities[uidx]

                    dt1 = hu.Tin - cs.Tout 
                    dt2 = hu.Tout - T_current

                    can_form_utility_exchanger_print = True
                    reason_not_formed = ""
                    if dt1 < deltaT_min or dt2 < deltaT_min:
                        can_form_utility_exchanger_print = False
                        reason_not_formed = "deltaT_min violation"
                    
                    if can_form_utility_exchanger_print:
                        try:
                            if abs(dt1 - dt2) < 1e-6: LMTD = dt1
                            else: LMTD = (dt1 - dt2) / np.log(dt1 / dt2)
                            if LMTD <= 0 or not np.isfinite(LMTD):
                                can_form_utility_exchanger_print = False
                                reason_not_formed = "LMTD invalid"
                        except Exception:
                            can_form_utility_exchanger_print = False
                            reason_not_formed = "LMTD calculation error"

                    if can_form_utility_exchanger_print:
                        Q_cold_util_total[j] += Q_needed_from_HU
                        Q_cold_received_total[j] += Q_needed_from_HU
                        print(f"  Cold stream C{j+1} final heating: {Q_needed_from_HU:.2f} kW from Hot Utility HU{uidx+1} ({hu.Tin}-{hu.Tout}°C)")
                    else:
                        print(f"  Cold stream C{j+1} needs {Q_needed_from_HU:.2f} kW final heating from Hot Utility HU{uidx+1}, but cannot form exchanger due to {reason_not_formed}.")
                else:
                    print(f"  Cold stream C{j+1} needs {Q_needed_from_HU:.2f} kW final heating (no hot utility assigned or available).")
            elif Q_needed_from_HU < -1e-6: # Penalize if cold stream is OVER-HEATED
                print(f"  Cold stream C{j+1} OVER-HEATED: {abs(Q_needed_from_HU):.2f} kW past target {cs.Tout}°C. Current temp: {T_current:.2f}°C")
            else:
                print(f"  Cold stream C{j+1} reached target {cs.Tout:.2f}°C after process-process exchange.")

        print("\nStream energy balances (all stages combined, including final utility if used):")
        for i, hs in enumerate(self.hot_streams):
            Q_required = hs.CP * (hs.Tin - hs.Tout)
            mismatch = abs(Q_hot_delivered_total[i] - Q_required)
            msg = f"  Hot stream H{i+1}: Q delivered = {Q_hot_delivered_total[i]:.2f} kW, Required = {Q_required:.2f} kW"
            if Q_required > 1e-6 and mismatch / Q_required > 1e-3:
                msg += f"  <-- MISMATCH! (ΔQ={mismatch:.2e})"
            elif Q_required <= 1e-6 and mismatch > 1e-3:
                msg += f"  <-- MISMATCH! (ΔQ={mismatch:.2e})"
            print(msg)
        for j, cs in enumerate(self.cold_streams):
            Q_required = cs.CP * (cs.Tout - cs.Tin)
            mismatch = abs(Q_cold_received_total[j] - Q_required)
            msg = f"  Cold stream C{j+1}: Q received = {Q_cold_received_total[j]:.2f} kW, Required = {Q_required:.2f} kW"
            if Q_required > 1e-6 and mismatch / Q_required > 1e-3:
                msg += f"  <-- MISMATCH! (ΔQ={mismatch:.2e})"
            elif Q_required <= 1e-6 and mismatch > 1e-3:
                msg += f"  <-- MISMATCH! (ΔQ={mismatch:.2e})"
            print(msg)
        
        print("\nTotal Utility Usage:")
        total_HU = np.sum(Q_cold_util_total)
        total_CU = np.sum(Q_hot_util_total)
        print(f"  Total Hot Utility: {total_HU:.2f} kW")
        print(f"  Total Cold Utility: {total_CU:.2f} kW")

        # Re-calculate costs for breakdown to ensure consistency (evaluate also calculates penalties)
        cost = self.evaluate(chromosome)
        process_U, process_C, process_B, process_CF = 1.0, 1000, 0.6, 5000
        hotutil_U, hotutil_C, hotutil_B, hotutil_CF = 1.2, 1200, 0.6, 7000
        coldu_U, coldu_C, coldu_B, coldu_CF = 1.0, 1200, 0.6, 7000
        
        total_area_cost_print = 0.0
        total_fixed_cost_print = 0.0
        total_utility_cost_print = 0.0

        for k in range(self.stage_num):
            Q_hot_stage_total_p = np.array([hs.CP * hot_deltas[i, k] for i, hs in enumerate(self.hot_streams)])
            Q_cold_stage_total_p = np.array([cs.CP * cold_deltas[j, k] for j, cs in enumerate(self.cold_streams)])
            Q_match_proposal_p = np.zeros((self.n_hot, self.n_cold))
            for i in range(self.n_hot):
                for j in range(self.n_cold):
                    Q_h_prop_from_frac_p = Q_hot_stage_total_p[i] * qfrac_hot[i, j, k]
                    Q_c_prop_from_frac_p = Q_cold_stage_total_p[j] * qfrac_cold[j, i, k]
                    Q_match_proposal_p[i, j] = min(Q_h_prop_from_frac_p, Q_c_prop_from_frac_p)
                    Q_match_proposal_p[i, j] = max(0.0, Q_match_proposal_p[i, j])

            for i in range(self.n_hot):
                for j in range(self.n_cold):
                    Q_ij = Q_match_proposal_p[i, j]
                    if Q_ij > 1e-8:
                        T_hi_in = hot_temps[i, k]
                        T_hi_out = hot_temps[i, k+1]
                        T_cj_in = cold_temps[j, k]
                        T_cj_out = cold_temps[j, k+1]
                        dt1 = T_hi_in - T_cj_out
                        dt2 = T_hi_out - T_cj_in
                        if dt1 < deltaT_min or dt2 < deltaT_min: continue
                        try:
                            if abs(dt1 - dt2) < 1e-6: LMTD = dt1
                            else: LMTD = (dt1 - dt2) / (np.log(dt1 / dt2))
                            if LMTD <= 0 or not np.isfinite(LMTD): continue
                        except Exception: continue
                        area = Q_ij / (process_U * LMTD)
                        total_area_cost_print += process_C * (area ** process_B)
                        total_fixed_cost_print += process_CF
            
        # Utility costs for print
        for i, hs in enumerate(self.hot_streams):
            T_current = hot_temps[i, -1]
            Q_needed_from_CU = hs.CP * (T_current - hs.Tout)
            if Q_needed_from_CU > 1e-6 and self.n_cold_util > 0:
                uidx = hot_util_idx[i]
                cu = self.cold_utilities[uidx]
                dt1 = T_current - cu.Tout
                dt2 = hs.Tout - cu.Tin
                
                can_form_utility_exchanger_print = True
                if dt1 < deltaT_min or dt2 < deltaT_min: can_form_utility_exchanger_print = False
                if can_form_utility_exchanger_print:
                    try:
                        if abs(dt1 - dt2) < 1e-6: LMTD = dt1
                        else: LMTD = (dt1 - dt2) / np.log(dt1 / dt2)
                        if LMTD <= 0 or not np.isfinite(LMTD): can_form_utility_exchanger_print = False
                    except Exception: can_form_utility_exchanger_print = False

                if can_form_utility_exchanger_print:
                    area = Q_needed_from_CU / (coldu_U * LMTD)
                    total_area_cost_print += coldu_C * (area ** coldu_B)
                    total_fixed_cost_print += coldu_CF
                    total_utility_cost_print += Q_needed_from_CU * cu.cost

        for j, cs in enumerate(self.cold_streams):
            T_current = cold_temps[j, -1]
            Q_needed_from_HU = cs.CP * (cs.Tout - T_current)
            if Q_needed_from_HU > 1e-6 and self.n_hot_util > 0:
                uidx = cold_util_idx[j]
                hu = self.hot_utilities[uidx]
                dt1 = hu.Tin - cs.Tout
                dt2 = hu.Tout - T_current

                can_form_utility_exchanger_print = True
                if dt1 < deltaT_min or dt2 < deltaT_min: can_form_utility_exchanger_print = False
                if can_form_utility_exchanger_print:
                    try:
                        if abs(dt1 - dt2) < 1e-6: LMTD = dt1
                        else: LMTD = (dt1 - dt2) / np.log(dt1 / dt2)
                        if LMTD <= 0 or not np.isfinite(LMTD): can_form_utility_exchanger_print = False
                    except Exception: can_form_utility_exchanger_print = False

                if can_form_utility_exchanger_print:
                    area = Q_needed_from_HU / (hotutil_U * LMTD)
                    total_area_cost_print += hotutil_C * (area ** hotutil_B)
                    total_fixed_cost_print += hotutil_CF
                    total_utility_cost_print += Q_needed_from_HU * hu.cost

        print(f"\nCost Breakdown (excluding penalties):")
        print(f"  Total Area Cost: {total_area_cost_print:.2f}")
        print(f"  Total Fixed Cost (exchangers): {total_fixed_cost_print:.2f}")
        print(f"  Total Utility Cost (annualized, pre-penalty factor): {total_utility_cost_print:.2f}")
        print(f"  Utility Cost (annualized, post-penalty factor): {self.utility_penalty_factor * total_utility_cost_print:.2f}")
        print(f"\nTotal Annual Cost (TAC) (including penalties): {cost:.2f}")


# --- Execution example ---
if __name__ == "__main__":
    if not os.path.exists('streams.csv'):
        print("Creating dummy streams.csv...")
        streams_data = {
            'Type': ['Hot', 'Hot', 'Cold', 'Cold'],
            'TIN_spec': [180, 150, 40, 80],
            'TOUT_spec': [60, 40, 140, 120],
            'Fcp': [10, 20, 15, 12]
        }
        streams_df = pd.DataFrame(streams_data)
        streams_df.to_csv('streams.csv', index=False)

    if not os.path.exists('utilities.csv'):
        print("Creating dummy utilities.csv...")
        utilities_data = {
            'Type': ['Hot_Utility', 'Cold_Utility'],
            'TIN_utility': [200, 30],
            'TOUT_utility': [199, 40],
            'Unit_Cost_Energy': [0.1, 0.01]
        }
        utilities_df = pd.DataFrame(utilities_data)
        utilities_df.to_csv('utilities.csv', index=False)

    hot_streams, cold_streams, hot_utilities, cold_utilities, stage_num = load_streams('streams.csv', 'utilities.csv')
    deltaTmin = 10 
    Q_HU_min, Q_CU_min = pinch_analysis(hot_streams, cold_streams, deltaTmin)
    print(f"Pinch analysis: Minimum Hot Utility = {Q_HU_min:.2f} kW, Minimum Cold Utility = {Q_CU_min:.2f} kW")
    
    ga = YeeHEN_GA(
        hot_streams, cold_streams, hot_utilities, cold_utilities, stage_num,
        pop_size=2000, gen=200, Q_HU_min=Q_HU_min, Q_CU_min=Q_CU_min
    )
    
    best_solution, best_cost = ga.run()
    ga.print_solution(best_solution)