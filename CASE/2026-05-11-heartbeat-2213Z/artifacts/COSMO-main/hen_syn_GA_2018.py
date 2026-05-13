import numpy as np
import random
import math
import copy
import csv # For reading CSV files
import time # For seeding

# --- YOUR ORIGINAL HELPER CLASSES ---
class Stream:
    def __init__(self, id_val, Tin, Tout_target, CP, h_coeff, stream_type): # Keep h_coeff
        self.id = id_val
        self.Tin = Tin
        self.Tout_target = Tout_target
        self.CP = CP
        self.h = h_coeff # Individual heat transfer coefficient
        self.type = stream_type

class Utility: # Your original Utility class
    def __init__(self, id_val, Tin, Tout, h_coeff, cost_per_energy_unit, utility_type):
        self.id = id_val
        self.Tin = Tin
        self.Tout = Tout
        self.h = h_coeff # Individual h_coeff for utility side
        self.cost = cost_per_energy_unit
        self.type = utility_type

class CostParameters: # Your original CostParameters class
    def __init__(self, exch_fixed, exch_area_coeff, exch_area_exp,
                 heater_fixed, heater_area_coeff, heater_area_exp,
                 cooler_fixed, cooler_area_coeff, cooler_area_exp,
                 EMAT, U_overall=None): # U_overall for process-process if h_coeffs not used
        self.exch_fixed = exch_fixed
        self.exch_area_coeff = exch_area_coeff
        self.exch_area_exp = exch_area_exp
        self.heater_fixed = heater_fixed
        self.heater_area_coeff = heater_area_coeff
        self.heater_area_exp = heater_area_exp
        self.cooler_fixed = cooler_fixed
        self.cooler_area_coeff = cooler_area_coeff
        self.cooler_area_exp = cooler_area_exp
        self.EMAT = EMAT
        self.U_overall = U_overall # Global U for process-process if stream h_coeffs are 0

class HENProblem: # Your original HENProblem class
    def __init__(self, hot_streams, cold_streams, hot_utility, cold_utility,
                 cost_params, num_stages, annual_op_hours=8000):
        self.hot_streams = hot_streams
        self.cold_streams = cold_streams
        self.hot_utility = hot_utility
        self.cold_utility = cold_utility
        self.cost_params = cost_params
        self.num_stages = num_stages
        self.NH = len(hot_streams)
        self.NC = len(cold_streams)
        self.annual_op_hours = annual_op_hours

        self.U_matrix_process = np.zeros((self.NH, self.NC))
        self.U_heaters = np.zeros(self.NC)
        self.U_coolers = np.zeros(self.NH)

        # Logic for U values based on your original HENProblem
        if self.cost_params.U_overall is None: # Calculate U from individual h_coeffs
            for i in range(self.NH):
                for j in range(self.NC):
                    # Ensure h_coeffs are positive before division
                    h_hot = self.hot_streams[i].h if self.hot_streams[i].h > 1e-9 else 1e9 # Use large h if 0 to avoid 1/0
                    h_cold = self.cold_streams[j].h if self.cold_streams[j].h > 1e-9 else 1e9
                    if self.hot_streams[i].h <= 1e-9 or self.cold_streams[j].h <= 1e-9: # If either original h is ~0
                        self.U_matrix_process[i,j] = 1e-6 # Effectively no heat transfer if h not defined
                    else:
                        self.U_matrix_process[i, j] = 1.0 / (1.0/h_hot + 1.0/h_cold)


            if self.hot_utility: # Check if hot_utility object exists
                for j in range(self.NC):
                    h_hot_util = self.hot_utility.h if self.hot_utility.h > 1e-9 else 1e9
                    h_cold_stream = self.cold_streams[j].h if self.cold_streams[j].h > 1e-9 else 1e9
                    if self.hot_utility.h <=1e-9 or self.cold_streams[j].h <= 1e-9:
                         self.U_heaters[j] = 1e-6 # Effectively no heat transfer
                    else:
                        self.U_heaters[j] = 1.0 / (1.0/h_hot_util + 1.0/h_cold_stream)
            
            if self.cold_utility: # Check if cold_utility object exists
                for i in range(self.NH):
                    h_hot_stream = self.hot_streams[i].h if self.hot_streams[i].h > 1e-9 else 1e9
                    h_cold_util = self.cold_utility.h if self.cold_utility.h > 1e-9 else 1e9
                    if self.hot_streams[i].h <= 1e-9 or self.cold_utility.h <= 1e-9:
                        self.U_coolers[i] = 1e-6 # Effectively no heat transfer
                    else:
                        self.U_coolers[i] = 1.0 / (1.0/h_hot_stream + 1.0/h_cold_util)
        else: # Use the global U_overall from cost_params
            self.U_matrix_process.fill(self.cost_params.U_overall)
            # For utilities, if global U_overall is given, it often applies to them too,
            # or they might have specific U values. The CSV structure introduced different U for utilities.
            # Your original logic when U_overall is present:
            if self.hot_utility:
                for j_idx in range(self.NC):
                    # If utility h is defined, prefer calculating U, else use global
                    if self.hot_utility.h > 1e-9 and self.cold_streams[j_idx].h > 1e-9:
                        self.U_heaters[j_idx] = 1.0 / (1.0/self.hot_utility.h + 1.0/self.cold_streams[j_idx].h)
                    else: # Fallback to global U_overall if h_coeffs are not sufficient
                        self.U_heaters[j_idx] = self.cost_params.U_overall
            if self.cold_utility:
                for i_idx in range(self.NH):
                    if self.hot_streams[i_idx].h > 1e-9 and self.cold_utility.h > 1e-9:
                        self.U_coolers[i_idx] = 1.0 / (1.0/self.hot_streams[i_idx].h + 1.0/self.cold_utility.h)
                    else: # Fallback to global U_overall
                        self.U_coolers[i_idx] = self.cost_params.U_overall

        # Calculate and store Pinch targets during initialization
        self.Q_H_min_pinch, self.Q_C_min_pinch, self.T_pinch_hot_actual, self.T_pinch_cold_actual = self._calculate_pinch_targets()

    def _calculate_pinch_targets(self):
        """
        Calculates minimum utility requirements (Q_H_min, Q_C_min) and Pinch temperatures
        using the Problem Table Algorithm (PTA) for the given EMAT.
        """
        EMAT = self.cost_params.EMAT
        
        if not self.hot_streams and not self.cold_streams:
            return 0, 0, None, None # No streams, no utility needed

        # 1. Identify all unique temperatures for interval creation
        #    Hot stream temperatures (original)
        #    Cold stream temperatures shifted by EMAT (T_cold_shifted = T_cold + EMAT)
        #    Using the convention where cold streams are shifted to create a "zero EMAT" problem
        #    Alternatively, shift hot streams down by EMAT/2 and cold streams up by EMAT/2.
        #    The method I used previously (shifting cold up by EMAT) is common for PTA.

        temp_points = set()
        for hs in self.hot_streams:
            temp_points.add(hs.Tin)
            temp_points.add(hs.Tout_target)
        for cs in self.cold_streams:
            temp_points.add(cs.Tin + EMAT)       # Shifted cold supply
            temp_points.add(cs.Tout_target + EMAT) # Shifted cold target

        # Sort unique temperatures in descending order to define intervals
        sorted_temps = sorted(list(temp_points), reverse=True)
        
        if len(sorted_temps) < 2: # Not enough points to form intervals
            # This might happen if all streams are at the same temperature or only one stream
            # Handle overall balance directly
            total_hot_duty_available = sum([s.CP * (s.Tin - s.Tout_target) for s in self.hot_streams])
            total_cold_duty_required = sum([s.CP * (s.Tout_target - s.Tin) for s in self.cold_streams])
            heat_deficit = total_cold_duty_required - total_hot_duty_available
            q_h_min = max(0, heat_deficit)
            q_c_min = max(0, -heat_deficit)
            return q_h_min, q_c_min, None, None # Pinch temps not well-defined here


        # 2. Create intervals and calculate enthalpy change in each
        heat_cascade = [0.0] # R_0 = 0

        for i in range(len(sorted_temps) - 1):
            T_high = sorted_temps[i]
            T_low = sorted_temps[i+1]
            delta_T_interval = T_high - T_low

            if delta_T_interval < 1e-6: # Skip zero-width intervals
                continue

            sum_fcp_h_active = 0
            for hs in self.hot_streams:
                # A hot stream is active if its range [Tout_target, Tin] overlaps with [T_low, T_high]
                if hs.Tin > T_low and hs.Tout_target < T_high:
                    sum_fcp_h_active += hs.CP
            
            sum_fcp_c_active = 0
            for cs in self.cold_streams:
                # A cold stream is active if its SHIFTED range [Tin+EMAT, Tout_target+EMAT]
                # overlaps with [T_low, T_high]
                cs_tin_shifted = cs.Tin + EMAT
                cs_tout_shifted = cs.Tout_target + EMAT
                if cs_tout_shifted > T_low and cs_tin_shifted < T_high:
                    sum_fcp_c_active += cs.CP
            
            delta_H_interval = (sum_fcp_h_active - sum_fcp_c_active) * delta_T_interval
            heat_cascade.append(heat_cascade[-1] + delta_H_interval)

        # 3. Determine Q_H_min, Q_C_min, and Pinch Temperatures
        min_cascade_value = min(heat_cascade)
        q_h_min = 0
        if min_cascade_value < -1e-6: # If there's a deficit (negative value)
            q_h_min = -min_cascade_value

        # Shifted cascade (Feasible Cascade)
        feasible_cascade = [q + q_h_min for q in heat_cascade]
        q_c_min = feasible_cascade[-1] # Last value of feasible cascade is Q_C_min

        # Pinch Temperature Identification
        # The Pinch occurs where the feasible cascade is zero (its minimum).
        # Find the index of the first occurrence of 0 in the feasible cascade.
        try:
            pinch_interval_index = feasible_cascade.index(min(feasible_cascade)) # Index of the min value (should be 0)
        except ValueError: # Should not happen if cascade is correctly built
            pinch_interval_index = 0
            
        # T_pinch_hot_actual is the T_high of the interval FOLLOWING the zero point in the feasible cascade
        # (or T_low of the interval where the zero point occurs, if using interval start temps)
        # The temperatures in sorted_temps are shifted for cold streams.
        # The Pinch occurs at a temperature T_pinch_shifted in the sorted_temps list.
        # If pinch_interval_index is 'k', the pinch is at sorted_temps[k]
        
        T_pinch_shifted = sorted_temps[pinch_interval_index]
        
        # This T_pinch_shifted is on the "hot composite curve" scale.
        # So, T_pinch_hot_actual = T_pinch_shifted
        # And T_pinch_cold_actual = T_pinch_shifted - EMAT
        
        t_pinch_hot = T_pinch_shifted
        t_pinch_cold = T_pinch_shifted - EMAT
        
        # Small correction: If Q_H_min is very small (e.g. due to float precision), treat as 0.
        if abs(q_h_min) < 1e-6 : q_h_min = 0
        if abs(q_c_min) < 1e-6 : q_c_min = 0
        
        return q_h_min, q_c_min, t_pinch_hot, t_pinch_cold


# --- NEW load_data FUNCTION ---
def load_data_from_csv(streams_filepath, utilities_filepath):
    """
    Loads stream and utility data from specified CSV files.
    Returns data as lists of dictionaries, to be adapted later.
    """
    loaded_hot_streams = []
    loaded_cold_streams = []
    loaded_hot_utilities = []
    loaded_cold_utilities = []

    # Load Streams
    try:
        with open(streams_filepath, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row_idx, row in enumerate(reader):
                try:
                    stream_data = {
                        'Name': row['Name'],
                        'Type': row['Type'].lower(),
                        'TIN_spec': float(row['TIN_spec']),
                        'TOUT_spec': float(row['TOUT_spec']),
                        'Fcp': float(row['Fcp'])
                    }
                    if stream_data['Type'] == 'hot':
                        loaded_hot_streams.append(stream_data)
                    elif stream_data['Type'] == 'cold':
                        loaded_cold_streams.append(stream_data)
                    else:
                        print(f"Warning: Unknown stream type '{row['Type']}' for stream '{row['Name']}'. Skipping.")
                except KeyError as e:
                    print(f"Error: Missing column {e} in streams.csv at row {row_idx+1}.")
                    return None, None, None, None
                except ValueError as e:
                    print(f"Error: Could not convert value to float in streams.csv at row {row_idx+1} for column related to {e}.")
                    return None, None, None, None
    except FileNotFoundError:
        print(f"Error: Streams file not found at {streams_filepath}")
        return None, None, None, None
    except Exception as e:
        print(f"Error reading streams CSV: {e}")
        return None, None, None, None

    # Load Utilities
    try:
        with open(utilities_filepath, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row_idx, row in enumerate(reader):
                try:
                    util_data = {
                        'Name': row['Name'],
                        'Type': row['Type'].lower(),
                        'TIN_utility': float(row['TIN_utility']),
                        'TOUT_utility': float(row['TOUT_utility']),
                        'Unit_Cost_Energy': float(row['Unit_Cost_Energy']),
                        'U_overall': float(row['U_overall']),
                        'Fixed_Cost_Unit': float(row['Fixed_Cost_Unit']),
                        'Area_Cost_Coeff': float(row['Area_Cost_Coeff']),
                        'Area_Cost_Exp': float(row['Area_Cost_Exp'])
                    }
                    if util_data['Type'] == 'hot_utility':
                        loaded_hot_utilities.append(util_data)
                    elif util_data['Type'] == 'cold_utility':
                        loaded_cold_utilities.append(util_data)
                    else:
                        print(f"Warning: Unknown utility type '{row['Type']}' for utility '{row['Name']}'. Skipping.")
                except KeyError as e:
                    print(f"Error: Missing column {e} in utilities.csv at row {row_idx+1}.")
                    return None, None, None, None
                except ValueError as e:
                    print(f"Error: Could not convert value to float in utilities.csv at row {row_idx+1} for column related to {e}.")
                    return None, None, None, None
    except FileNotFoundError:
        print(f"Error: Utilities file not found at {utilities_filepath}")
        return None, None, None, None
    except Exception as e:
        print(f"Error reading utilities CSV: {e}")
        return None, None, None, None
        
    if not loaded_hot_utilities and any(s['Type'] == 'cold' for s in loaded_cold_streams):
        print("Warning: No hot utilities loaded, but cold streams exist. Heaters will not be available or use defaults.")
    if not loaded_cold_utilities and any(s['Type'] == 'hot' for s in loaded_hot_streams):
        print("Warning: No cold utilities loaded, but hot streams exist. Coolers will not be available or use defaults.")

    return loaded_hot_streams, loaded_cold_streams, loaded_hot_utilities, loaded_cold_utilities

# --- GeneticAlgorithmHEN Class (Your existing corrected version) ---
class GeneticAlgorithmHEN:
    def __init__(self, problem, population_size, generations,
                 crossover_prob, mutation_prob, num_crossover_points=1, elitism_count=1, 
                 random_seed=None, utility_cost_factor=1000.0,
                 pinch_deviation_penalty_factor=150.0):
        self.problem = problem
        self.population_size = population_size
        self.generations = generations
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.num_crossover_points = num_crossover_points 
        self.elitism_count = elitism_count
        self.population = [] 
        self.fitness_values = []
        self.utility_cost_factor = utility_cost_factor # Factor for utility cost per energy unit
        
        self.random_seed = random_seed
        
        if random_seed is not None:
            random.seed(random_seed)
            np.random.seed(random_seed)
        
        # Hardcoded values for minimum utility requirements
        # These can be adjusted based on problem requirements
        self.Q_H_min = 200.0
        self.Q_C_min = 600.0
        self.pinch_deviation_penalty_factor = pinch_deviation_penalty_factor

    def _initialize_population(self):
        self.population = []
        for _ in range(self.population_size):
            chromosome = np.random.randint(0, 2,
                                           size=(self.problem.NH, self.problem.NC, self.problem.num_stages))
            self.population.append(chromosome)

    def _calculate_lmtd(self, Th_in, Th_out, Tc_in, Tc_out):
        delta_T1 = Th_in - Tc_out
        delta_T2 = Th_out - Tc_in
        if delta_T1 <= 1e-6 or delta_T2 <= 1e-6:
             if abs(delta_T1 - delta_T2) < 1e-6 and delta_T1 > 1e-6 :
                 return delta_T1
             return 1e-6 
        if abs(delta_T1 - delta_T2) < 1e-6:
            lmtd = (delta_T1 + delta_T2) / 2.0
        else:
            lmtd = (delta_T1 - delta_T2) / math.log(delta_T1 / delta_T2)
        if lmtd <= 1e-6: 
            return 1e-6
        return lmtd

    def _calculate_fitness(self, chromosome_Z):
        # THIS IS YOUR LATEST WORKING _CALCULATE_FITNESS METHOD
        # It uses self.problem.cost_params for EMAT, U_overall (for process-process if set),
        # and specific exchanger/heater/cooler fixed/area/exp costs.
        # It also uses self.problem.U_heaters and self.problem.U_coolers for utility units.
        NH = self.problem.NH; NC = self.problem.NC; ST = self.problem.num_stages
        EMAT = self.problem.cost_params.EMAT
        U_process_default = self.problem.cost_params.U_overall # This is for process-process if stream h are not used

        CF_process = self.problem.cost_params.exch_fixed
        C_area_process = self.problem.cost_params.exch_area_coeff
        B_exp_process = self.problem.cost_params.exch_area_exp

        # Utility objects
        hot_util_obj = self.problem.hot_utility
        cold_util_obj = self.problem.cold_utility
        Q_hot_consumed = 0.0
        Q_cold_consumed = 0.0

        total_capital_cost_exchangers = 0.0
        total_capital_cost_heaters = 0.0
        total_capital_cost_coolers = 0.0
        total_hot_utility_op_cost = 0.0
        total_cold_utility_op_cost = 0.0
        penalty = 0.0

        FH_ijk_est = np.zeros((NH, NC, ST))
        FC_ijk_est = np.zeros((NH, NC, ST))
        for k_idx in range(ST):
            for i_idx in range(NH):
                active_matches_hot_i_k = np.sum(chromosome_Z[i_idx, :, k_idx])
                if active_matches_hot_i_k > 0:
                    split_frac = 1.0 / active_matches_hot_i_k
                    for j_idx in range(NC):
                        if chromosome_Z[i_idx, j_idx, k_idx] == 1: FH_ijk_est[i_idx, j_idx, k_idx] = split_frac
            for j_idx in range(NC):
                active_matches_cold_j_k = np.sum(chromosome_Z[:, j_idx, k_idx])
                if active_matches_cold_j_k > 0:
                    split_frac = 1.0 / active_matches_cold_j_k
                    for i_idx in range(NH):
                        if chromosome_Z[i_idx, j_idx, k_idx] == 1: FC_ijk_est[i_idx, j_idx, k_idx] = split_frac
        
        Q_ijk_values = np.zeros((NH, NC, ST)); _TmixH_iter = np.zeros((NH, ST)); _TmixC_iter = np.zeros((NC, ST))
        MAX_TEMP_ITERATIONS = 30; CONVERGENCE_TOLERANCE = 0.05
        _TmixH_iter_old_for_convergence_check = _TmixH_iter.copy() 
        _TmixC_iter_old_for_convergence_check = _TmixC_iter.copy() 

        for temp_iter in range(MAX_TEMP_ITERATIONS):
            _TmixH_iter_old_for_stage_input = _TmixH_iter.copy() 
            _TmixC_iter_old_for_stage_input = _TmixC_iter.copy()
            Q_ijk_current_pass = np.zeros((NH,NC,ST))
            TinH_overall_stream_at_stage_k = np.zeros(NH)
            for k_idx in range(ST):
                for i_idx_hs_loop in range(NH): TinH_overall_stream_at_stage_k[i_idx_hs_loop] = _TmixH_iter_old_for_stage_input[i_idx_hs_loop, k_idx-1] if k_idx > 0 else self.problem.hot_streams[i_idx_hs_loop].Tin
                total_Q_from_hot_stream_i_at_stage_k_ALL_BRANCHES = np.zeros(NH)
                for i_idx in range(NH):
                    hs = self.problem.hot_streams[i_idx]; TinH_for_matches_of_stream_i_at_stage_k = TinH_overall_stream_at_stage_k[i_idx]
                    for j_idx in range(NC):
                        cs = self.problem.cold_streams[j_idx]
                        if chromosome_Z[i_idx, j_idx, k_idx] == 1:
                            Tcin_for_match_ijk = _TmixC_iter_old_for_stage_input[j_idx, k_idx+1] if k_idx < ST-1 else cs.Tin
                            CPH_branch = hs.CP * FH_ijk_est[i_idx, j_idx, k_idx]; CPC_branch = cs.CP * FC_ijk_est[i_idx, j_idx, k_idx]; Q_match = 0 
                            if CPH_branch > 1e-9 and CPC_branch > 1e-9:
                                Q_max_H = CPH_branch * (TinH_for_matches_of_stream_i_at_stage_k - max(hs.Tout_target, Tcin_for_match_ijk + EMAT))
                                Q_max_C = CPC_branch * (min(cs.Tout_target, TinH_for_matches_of_stream_i_at_stage_k - EMAT) - Tcin_for_match_ijk)
                                Q_match = max(0, min(Q_max_H, Q_max_C))
                            Q_ijk_current_pass[i_idx,j_idx,k_idx] = Q_match
                            total_Q_from_hot_stream_i_at_stage_k_ALL_BRANCHES[i_idx] += Q_match
                for i_idx in range(NH):
                    hs = self.problem.hot_streams[i_idx]
                    if hs.CP > 1e-9: _TmixH_iter[i_idx, k_idx] = TinH_overall_stream_at_stage_k[i_idx] - total_Q_from_hot_stream_i_at_stage_k_ALL_BRANCHES[i_idx] / hs.CP
                    else: _TmixH_iter[i_idx, k_idx] = TinH_overall_stream_at_stage_k[i_idx]
            TinC_overall_stream_at_stage_k = np.zeros(NC)
            for k_idx in range(ST - 1, -1, -1):
                for j_idx_cs_loop in range(NC): TinC_overall_stream_at_stage_k[j_idx_cs_loop] = _TmixC_iter_old_for_stage_input[j_idx_cs_loop, k_idx+1] if k_idx < ST-1 else self.problem.cold_streams[j_idx_cs_loop].Tin
                total_Q_to_cold_stream_j_at_stage_k_ALL_BRANCHES = np.zeros(NC)
                for j_idx in range(NC):
                    for i_idx in range(NH):
                        if chromosome_Z[i_idx, j_idx, k_idx] == 1:
                            Q_match = Q_ijk_current_pass[i_idx,j_idx,k_idx]
                            total_Q_to_cold_stream_j_at_stage_k_ALL_BRANCHES[j_idx] += Q_match
                for j_idx in range(NC):
                    cs = self.problem.cold_streams[j_idx]
                    if cs.CP > 1e-9: _TmixC_iter[j_idx, k_idx] = TinC_overall_stream_at_stage_k[j_idx] + total_Q_to_cold_stream_j_at_stage_k_ALL_BRANCHES[j_idx] / cs.CP
                    else: _TmixC_iter[j_idx, k_idx] = TinC_overall_stream_at_stage_k[j_idx]
            max_delta_T_H = np.max(np.abs(_TmixH_iter_old_for_convergence_check - _TmixH_iter)) if ST > 0 and NH > 0 else 0
            max_delta_T_C = np.max(np.abs(_TmixC_iter_old_for_convergence_check - _TmixC_iter)) if ST > 0 and NC > 0 else 0
            _TmixH_iter_old_for_convergence_check = _TmixH_iter.copy(); _TmixC_iter_old_for_convergence_check = _TmixC_iter.copy()
            Q_ijk_values = Q_ijk_current_pass.copy()
            if max_delta_T_H < CONVERGENCE_TOLERANCE and max_delta_T_C < CONVERGENCE_TOLERANCE and temp_iter > 0: break

        exchanger_details_list = []
        for k_idx in range(ST):
            for i_idx in range(NH):
                hs = self.problem.hot_streams[i_idx]
                for j_idx in range(NC):
                    cs = self.problem.cold_streams[j_idx]
                    if chromosome_Z[i_idx, j_idx, k_idx] == 1 and Q_ijk_values[i_idx, j_idx, k_idx] > 1e-6:
                        Q_val = Q_ijk_values[i_idx, j_idx, k_idx]
                        Thin_actual_exch = _TmixH_iter[i_idx, k_idx-1] if k_idx > 0 else hs.Tin
                        Tcin_actual_exch = _TmixC_iter[j_idx, k_idx+1] if k_idx < ST-1 else cs.Tin
                        CPH_b = hs.CP * FH_ijk_est[i_idx, j_idx, k_idx]; CPC_b = cs.CP * FC_ijk_est[i_idx, j_idx, k_idx]
                        if CPH_b < 1e-9 or CPC_b < 1e-9: continue 
                        Thout_actual_exch = Thin_actual_exch - Q_val / CPH_b; Tcout_actual_exch = Tcin_actual_exch + Q_val / CPC_b
                        delta_T1_calc = Thin_actual_exch - Tcout_actual_exch; delta_T2_calc = Thout_actual_exch - Tcin_actual_exch
                        if delta_T1_calc < EMAT - 1e-3: penalty += 1e7 * (EMAT - delta_T1_calc)
                        if delta_T2_calc < EMAT - 1e-3: penalty += 1e7 * (EMAT - delta_T2_calc)
                        lmtd = self._calculate_lmtd(Thin_actual_exch, Thout_actual_exch, Tcin_actual_exch, Tcout_actual_exch)
                        
                        U_val = self.problem.U_matrix_process[i_idx,j_idx] # Uses pre-calculated U from HENProblem
                        area = 1e9 
                        if U_val > 1e-9 and lmtd > 1e-9 : area = Q_val / (U_val * lmtd)
                        if area < 0: area = 1e9

                        cost_exch = CF_process + C_area_process * (area ** B_exp_process)
                        total_capital_cost_exchangers += cost_exch
                        exchanger_details_list.append({'H': i_idx, 'C': j_idx, 'k': k_idx, 'Q': Q_val, 'Area': area, 'Th_in': Thin_actual_exch, 'Th_out': Thout_actual_exch, 'Tc_in': Tcin_actual_exch, 'Tc_out': Tcout_actual_exch})

        final_Th_after_recovery = np.zeros(NH)
        if ST > 0 : final_Th_after_recovery = _TmixH_iter[:, ST-1] 
        else: 
            for i_idx_hs_loop in range(NH): final_Th_after_recovery[i_idx_hs_loop] = self.problem.hot_streams[i_idx_hs_loop].Tin
        
        if cold_util_obj:
            for i_idx in range(NH):
                hs = self.problem.hot_streams[i_idx]; temp_before_cooler = final_Th_after_recovery[i_idx]
                if temp_before_cooler > hs.Tout_target + 1e-3:
                    Q_cooler = hs.CP * (temp_before_cooler - hs.Tout_target)
                    if Q_cooler > 1e-6 and hs.CP > 1e-9 :
                        Th_in_cu = temp_before_cooler; Th_out_cu = hs.Tout_target
                        Tcold_util_in = cold_util_obj.Tin
                        Tcold_util_out = cold_util_obj.Tout if cold_util_obj.Tout > Tcold_util_in else Tcold_util_in + 5 
                        if Th_in_cu < Tcold_util_out + EMAT - 1e-3: penalty += 1e6 * (Tcold_util_out + EMAT - Th_in_cu)
                        if Th_out_cu < Tcold_util_in + EMAT - 1e-3: penalty += 1e6 * (Tcold_util_in + EMAT - Th_out_cu)
                        lmtd_cooler = self._calculate_lmtd(Th_in_cu, Th_out_cu, Tcold_util_in, Tcold_util_out)
                        U_cu_val = self.problem.U_coolers[i_idx] # Uses pre-calculated U from HENProblem
                        area_cooler = 1e9
                        if U_cu_val > 1e-9 and lmtd_cooler > 1e-9: area_cooler = Q_cooler / (U_cu_val * lmtd_cooler)
                        if area_cooler < 0: area_cooler = 1e9
                        cost_c = self.problem.cost_params.cooler_fixed + self.problem.cost_params.cooler_area_coeff * (area_cooler ** self.problem.cost_params.cooler_area_exp)
                        total_capital_cost_coolers += cost_c
                        total_cold_utility_op_cost += cold_util_obj.cost * Q_cooler 
                        exchanger_details_list.append({'type': 'cooler', 'H_idx': i_idx, 'Q': Q_cooler, 'Area': area_cooler, 'Th_in': Th_in_cu, 'Th_out': Th_out_cu, 'util_Tin': Tcold_util_in, 'util_Tout':Tcold_util_out})
                        
                        # add Q_cooler to total cold utility consumed
                        Q_cold_consumed += Q_cooler
                elif temp_before_cooler < hs.Tout_target - 1e-3 : penalty += 1e6 * (hs.Tout_target - temp_before_cooler)

        final_Tc_after_recovery = np.zeros(NC)
        if ST > 0: final_Tc_after_recovery = _TmixC_iter[:, 0]
        else:
            for i_idx_cs_loop in range(NC): final_Tc_after_recovery[i_idx_cs_loop] = self.problem.cold_streams[i_idx_cs_loop].Tin
        
        if hot_util_obj:
            for j_idx in range(NC):
                cs = self.problem.cold_streams[j_idx]; temp_before_heater = final_Tc_after_recovery[j_idx]
                if temp_before_heater < cs.Tout_target - 1e-3:
                    Q_heater = cs.CP * (cs.Tout_target - temp_before_heater)
                    if Q_heater > 1e-6 and cs.CP > 1e-9:
                        Thot_util_in = hot_util_obj.Tin
                        Thot_util_out = hot_util_obj.Tout if hot_util_obj.Tout < Thot_util_in else Thot_util_in - 1 
                        Tc_in_hu = temp_before_heater; Tc_out_hu = cs.Tout_target
                        if Thot_util_in < Tc_out_hu + EMAT - 1e-3: penalty += 1e6 * (Tc_out_hu + EMAT - Thot_util_in)
                        if Thot_util_out < Tc_in_hu + EMAT - 1e-3: penalty += 1e6 * (Tc_in_hu + EMAT - Thot_util_out)
                        lmtd_heater = self._calculate_lmtd(Thot_util_in, Thot_util_out, Tc_in_hu, Tc_out_hu)
                        U_hu_val = self.problem.U_heaters[j_idx] # Uses pre-calculated U from HENProblem
                        area_heater = 1e9
                        if U_hu_val > 1e-9 and lmtd_heater > 1e-9: area_heater = Q_heater / (U_hu_val * lmtd_heater)
                        if area_heater < 0: area_heater = 1e9
                        cost_h = self.problem.cost_params.heater_fixed + self.problem.cost_params.heater_area_coeff * (area_heater ** self.problem.cost_params.heater_area_exp)
                        total_capital_cost_heaters += cost_h
                        total_hot_utility_op_cost += hot_util_obj.cost * Q_heater
                        exchanger_details_list.append({'type': 'heater', 'C_idx': j_idx, 'Q': Q_heater, 'Area': area_heater, 'Tc_in': Tc_in_hu, 'Tc_out': Tc_out_hu, 'util_Tin':Thot_util_in, 'util_Tout':Thot_util_out})
                        
                        # add Q_heater to total hot utility consumed
                        Q_hot_consumed += Q_heater
                elif temp_before_heater > cs.Tout_target + 1e-3: penalty += 1e6 * (temp_before_heater - cs.Tout_target)
        
        # --- Penalty for utility deviation from Pinch targets ---
        utility_deviation_penalty = 0
        # Ensure Pinch targets are available in self.problem
        if hasattr(self.problem, 'Q_H_min_pinch') and hasattr(self.problem, 'Q_C_min_pinch'):
            pinch_deviation_penalty_factor = 150 # Tunable

            Q_hot_consumed_kW = 0
            if hot_util_obj and hot_util_obj.cost > 1e-9: # Avoid division by zero if cost is somehow 0
                Q_hot_consumed_kW = total_hot_utility_op_cost / hot_util_obj.cost
            
            Q_cold_consumed_kW = 0
            if cold_util_obj and cold_util_obj.cost > 1e-9:
                Q_cold_consumed_kW = total_cold_utility_op_cost / cold_util_obj.cost

            if Q_hot_consumed_kW > self.problem.Q_H_min_pinch + 1e-3 :
                utility_deviation_penalty += pinch_deviation_penalty_factor * \
                                             (Q_hot_consumed_kW - self.problem.Q_H_min_pinch)
            if Q_cold_consumed_kW > self.problem.Q_C_min_pinch + 1e-3:
                utility_deviation_penalty += pinch_deviation_penalty_factor * \
                                             (Q_cold_consumed_kW - self.problem.Q_C_min_pinch)
        else:
            print("Warning: Pinch targets not found in problem object. Skipping utility deviation penalty.")
        
        penalty += utility_deviation_penalty
        
        total_capital_cost = total_capital_cost_exchangers + total_capital_cost_heaters + total_capital_cost_coolers
        total_utility_cost = total_hot_utility_op_cost + total_cold_utility_op_cost

        TAC_GA_optimizing = total_capital_cost + total_utility_cost*self.utility_cost_factor + penalty
        TAC_true_report = total_capital_cost + total_utility_cost
        
        detailed_cost = {
            'total_capital_cost_exchangers': total_capital_cost_exchangers,
            'total_capital_cost_heaters': total_capital_cost_heaters,
            'total_capital_cost_coolers': total_capital_cost_coolers,
            'total_hot_utility_op_cost': total_hot_utility_op_cost,
            'total_cold_utility_op_cost': total_cold_utility_op_cost,
            'total_capital_cost': total_capital_cost,
            'total_utility_cost': total_utility_cost,
            'penalty': penalty,
            'TAC_GA_optimizing': TAC_GA_optimizing,
            'TAC_true_report': TAC_true_report,
        }

        return detailed_cost, exchanger_details_list

    def _crossover(self, parent1_Z, parent2_Z):
        offspring1_Z = parent1_Z.copy(); offspring2_Z = parent2_Z.copy()
        if random.random() < self.crossover_prob:
            p1_flat = parent1_Z.ravel(); p2_flat = parent2_Z.ravel(); size = len(p1_flat)
            if size <= 1: return offspring1_Z, offspring2_Z
            # cx_point = random.randint(1, size - 1) if size > 1 else 0
            # if cx_point == 0 and size > 1 : cx_point = 1
            # offspring1_flat = np.concatenate((p1_flat[:cx_point], p2_flat[cx_point:])); offspring2_flat = np.concatenate((p2_flat[:cx_point], p1_flat[cx_point:]))
            # Inside _crossover, if crossover_prob is met for p1_flat, p2_flat of length 'size':
            if size >= 3: # Ensure enough length for two distinct points
                pt1, pt2 = sorted(random.sample(range(1, size), 2)) # Get two unique points, ensure pt1 < pt2
                
                off1_s1 = p1_flat[:pt1]
                off1_s2 = p2_flat[pt1:pt2] # Middle segment from parent 2
                off1_s3 = p1_flat[pt2:]
                offspring1_flat = np.concatenate((off1_s1, off1_s2, off1_s3))

                off2_s1 = p2_flat[:pt1]
                off2_s2 = p1_flat[pt1:pt2] # Middle segment from parent 1
                off2_s3 = p2_flat[pt2:]
                offspring2_flat = np.concatenate((off2_s1, off2_s2, off2_s3))
            else: # Fallback to single-point for very short chromosomes
                # (current single-point logic)
                cx_point = random.randint(1, size - 1) if size > 1 else 0
                if size <=1 : cx_point = 0 # Avoid error with randint if size is 1
                offspring1_flat = np.concatenate((p1_flat[:cx_point], p2_flat[cx_point:])) if size > 0 else p1_flat.copy()
                offspring2_flat = np.concatenate((p2_flat[:cx_point], p1_flat[cx_point:])) if size > 0 else p2_flat.copy()
    
            offspring1_Z = offspring1_flat.reshape(parent1_Z.shape); offspring2_Z = offspring2_flat.reshape(parent2_Z.shape)
        return offspring1_Z, offspring2_Z

    def _mutation(self, chromosome_Z):
        mutated_Z = chromosome_Z.copy(); flat_Z = mutated_Z.ravel()
        for i in range(len(flat_Z)):
            if random.random() < self.mutation_prob: flat_Z[i] = 1 - flat_Z[i]
        mutated_Z = flat_Z.reshape(chromosome_Z.shape)
        return mutated_Z
# Inside GeneticAlgorithmHEN class:
    def run(self, run_id_for_print=""):
        if self.random_seed is not None:
            random.seed(self.random_seed)
            np.random.seed(self.random_seed)

        self._initialize_population()
        
        best_chromosome_overall = None
        # This will store the dictionary of costs for the best solution found based on TAC_GA_optimizing
        best_costs_overall_dict = {"TAC_GA_optimizing": float('inf'), "TAC_true_report": float('inf')}
        best_details_overall = None

        print_prefix = f"Run {run_id_for_print} - " if run_id_for_print else ""
        
        # For tracking generation-wise progress
        log_best_true_tac_per_gen = []
        log_avg_true_tac_per_gen = []
        log_best_ga_tac_per_gen = []
        log_avg_ga_tac_per_gen = []


        for gen in range(self.generations):
            current_population_evaluations = [] # List of dicts: {'chromosome':c, 'costs':costs_d, 'details':d}
            
            gen_true_tacs = [] # Store true TACs for this generation's population
            gen_ga_tacs = []   # Store GA-optimized TACs for this generation's population

            for chromo in self.population:
                try:
                    costs_dict, details = self._calculate_fitness(chromo)
                    current_population_evaluations.append({'chromosome': chromo, 'costs': costs_dict, 'details': details})
                    if costs_dict.get("TAC_true_report", float('inf')) != float('inf'):
                        gen_true_tacs.append(costs_dict["TAC_true_report"])
                    if costs_dict.get("TAC_GA_optimizing", float('inf')) != float('inf'):
                        gen_ga_tacs.append(costs_dict["TAC_GA_optimizing"])
                except Exception as e:
                    # print(f"Error in fitness gen {gen+1} for a chromosome: {e}")
                    error_costs = {"TAC_GA_optimizing": float('inf'), "TAC_true_report": float('inf'),
                                   "total_capital_cost": float('inf'), "total_operating_cost": float('inf'),
                                   "penalty_EMAT_etc": float('inf'), "penalty_pinch_deviation": float('inf')}
                    current_population_evaluations.append({'chromosome': chromo, 'costs': error_costs, 'details': []})
            
            # Sort by the TAC the GA is optimizing against
            current_population_evaluations.sort(key=lambda x: x['costs']['TAC_GA_optimizing'])

            # Best of current generation (based on GA optimization TAC)
            best_ga_tac_this_gen = float('inf')
            best_true_tac_this_gen = float('inf')
            if current_population_evaluations:
                best_ga_tac_this_gen = current_population_evaluations[0]['costs']['TAC_GA_optimizing']
                best_true_tac_this_gen = current_population_evaluations[0]['costs']['TAC_true_report']

            # Update overall best solution found so far
            if best_ga_tac_this_gen < best_costs_overall_dict['TAC_GA_optimizing']:
                best_costs_overall_dict = copy.deepcopy(current_population_evaluations[0]['costs'])
                best_chromosome_overall = current_population_evaluations[0]['chromosome'].copy()
                best_details_overall = current_population_evaluations[0]['details']

            # Calculate average TACs for the current generation (only finite values)
            avg_true_tac_this_gen = np.mean(gen_true_tacs) if gen_true_tacs else float('inf')
            avg_ga_tac_this_gen = np.mean(gen_ga_tacs) if gen_ga_tacs else float('inf')

            # Log for plotting later if desired
            log_best_true_tac_per_gen.append(best_costs_overall_dict['TAC_true_report'])
            log_avg_true_tac_per_gen.append(avg_true_tac_this_gen)
            log_best_ga_tac_per_gen.append(best_costs_overall_dict['TAC_GA_optimizing'])
            log_avg_ga_tac_per_gen.append(avg_ga_tac_this_gen)


            # --- ENHANCED PRINT STATEMENT ---
            print(f"{print_prefix}Gen {gen+1:03d}/{self.generations} - "
                  f"Best True TAC (Overall): {best_costs_overall_dict['TAC_true_report']:.2f}, "
                  f"Best GA TAC (Overall): {best_costs_overall_dict['TAC_GA_optimizing']:.2f} | "
                  f"Gen Best True: {best_true_tac_this_gen:.2f}, "
                  f"Gen Avg True: {avg_true_tac_this_gen:.2f}, "
                  f"Gen Best GA: {best_ga_tac_this_gen:.2f}, "
                  f"Gen Avg GA: {avg_ga_tac_this_gen:.2f}")
            # --- END OF ENHANCED PRINT ---


            # Elitism, Selection, Crossover, Mutation
            new_population = []
            if current_population_evaluations:
                 for i in range(min(self.elitism_count, len(current_population_evaluations))):
                    new_population.append(current_population_evaluations[i]['chromosome'].copy())
            
            if not current_population_evaluations: 
                self._initialize_population() 
                continue
            
            # _selection expects list of dicts with 'costs':{'TAC_GA_optimizing': val}
            selected_parent_indices = self._selection(current_population_evaluations) 
            
            num_offspring_to_generate = self.population_size - len(new_population)
            children_generated = 0; idx_for_selection = 0
            
            if not selected_parent_indices or not current_population_evaluations :
                while children_generated < num_offspring_to_generate:
                    new_population.append(np.random.randint(0, 2, size=(self.problem.NH, self.problem.NC, self.problem.num_stages)))
                    children_generated += 1
            else:
                while children_generated < num_offspring_to_generate:
                    # Ensure indices are valid for current_population_evaluations
                    parent1_idx = selected_parent_indices[idx_for_selection % len(selected_parent_indices)]; idx_for_selection += 1
                    parent2_idx = selected_parent_indices[idx_for_selection % len(selected_parent_indices)]; idx_for_selection += 1
                    
                    parent1 = current_population_evaluations[parent1_idx]['chromosome']
                    parent2 = current_population_evaluations[parent2_idx]['chromosome']

                    offspring1, offspring2 = self._crossover(parent1, parent2)
                    mutated_offspring1 = self._mutation(offspring1); mutated_offspring2 = self._mutation(offspring2)
                    if children_generated < num_offspring_to_generate: new_population.append(mutated_offspring1); children_generated +=1
                    if children_generated < num_offspring_to_generate: new_population.append(mutated_offspring2); children_generated +=1
            
            self.population = new_population
            if len(self.population) != self.population_size:
                while len(self.population) < self.population_size: self.population.append(np.random.randint(0, 2, size=(self.problem.NH, self.problem.NC, self.problem.num_stages)))
                self.population = self.population[:self.population_size]
        
        # At the end, you can plot log_..._per_gen if you have matplotlib
        # For example:
        # import matplotlib.pyplot as plt
        # generations_axis = range(1, self.generations + 1)
        # plt.figure(figsize=(12, 8))
        # plt.subplot(2, 1, 1)
        # plt.plot(generations_axis, log_best_true_tac_per_gen, label='Best True TAC (Overall Accum.)')
        # plt.plot(generations_axis, log_avg_true_tac_per_gen, label='Avg True TAC (Current Gen)')
        # plt.xlabel('Generation'); plt.ylabel('True TAC'); plt.legend(); plt.title(f'{print_prefix}True TAC Evolution')
        #
        # plt.subplot(2, 1, 2)
        # plt.plot(generations_axis, log_best_ga_tac_per_gen, label='Best GA TAC (Overall Accum.)')
        # plt.plot(generations_axis, log_avg_ga_tac_per_gen, label='Avg GA TAC (Current Gen)')
        # plt.xlabel('Generation'); plt.ylabel('GA-Optimized TAC'); plt.legend(); plt.title(f'{print_prefix}GA-Optimized TAC Evolution')
        # plt.tight_layout(); plt.show()

        return best_chromosome_overall, best_costs_overall_dict, best_details_overall

    # The _selection method needs to correctly use the 'costs' dictionary
    def _selection(self, current_population_evaluations): # Expects list of dicts like [{'chromosome':c, 'costs':costs_d, 'details':d}, ...]
        # Use TAC_GA_optimizing for fitness calculation
        raw_fitness = []
        for item in current_population_evaluations:
            ga_tac = item['costs'].get('TAC_GA_optimizing', float('inf'))
            raw_fitness.append(1.0 / (ga_tac + 1e-9))
            
        total_fitness = sum(raw_fitness)
        if total_fitness < 1e-9 or total_fitness == float('inf') or np.isnan(total_fitness): # Handle bad total_fitness
            # Fallback: select randomly or return indices for uniform selection
            return [random.choice(range(len(current_population_evaluations))) for _ in range(len(current_population_evaluations))]

        probabilities = [f / total_fitness for f in raw_fitness]
        
        # Further checks for probabilities
        if np.isnan(probabilities).any() or np.isinf(probabilities).any() or abs(sum(probabilities) - 1.0) > 1e-5 : # Increased tolerance for sum
             probabilities = np.ones(len(current_population_evaluations)) / len(current_population_evaluations) # Equal prob fallback
        
        num_to_select = len(current_population_evaluations)
        try:
            selected_indices = np.random.choice(len(current_population_evaluations), size=num_to_select, p=probabilities, replace=True)
        except ValueError as e: # Catches if sum(pvals) != 1 due to precision or other issues
            # print(f"ValueError in selection np.random.choice: {e}. Sum p={sum(probabilities)}. Using fallback.")
            probabilities = np.ones(len(current_population_evaluations)) / len(current_population_evaluations)
            selected_indices = np.random.choice(len(current_population_evaluations), size=num_to_select, p=probabilities, replace=True)
        return selected_indices.tolist()

# --- Main Execution Block ---
if __name__ == "__main__":
    print("HEN Synthesis using Genetic Algorithm with CSV Data Loading")

    streams_file = 'streams.csv'
    utilities_file = 'utilities.csv'

    # Load data into generic list of dicts first
    loaded_hot_streams_data, loaded_cold_streams_data, \
    loaded_hot_utilities_data, loaded_cold_utilities_data = load_data_from_csv(streams_file, utilities_file)

    if loaded_hot_streams_data is None:
        print("Exiting due to data loading error.")
        exit()

    # --- Adapt loaded data to your specific class structures ---
    hot_streams_obj_list = []
    # Assign a default h_coeff if not in CSV, or decide how to handle it.
    # Your Stream class expects h_coeff. The CSV does not have it.
    # Let's use a default value (e.g., 0 indicating U_overall should be used, or a typical high value if calculating U)
    default_stream_h_coeff = 0 # Set to 0 to trigger U_overall usage in HENProblem if cost_params.U_overall is set
                               # Or set to a high value like 10 kW/m2K if you want to calculate U based on individual h

    for s_data in loaded_hot_streams_data:
        hot_streams_obj_list.append(
            Stream(id_val=s_data['Name'], Tin=s_data['TIN_spec'], Tout_target=s_data['TOUT_spec'],
                   CP=s_data['Fcp'], h_coeff=default_stream_h_coeff, stream_type='hot')
        )
    cold_streams_obj_list = []
    for s_data in loaded_cold_streams_data:
        cold_streams_obj_list.append(
            Stream(id_val=s_data['Name'], Tin=s_data['TIN_spec'], Tout_target=s_data['TOUT_spec'],
                   CP=s_data['Fcp'], h_coeff=default_stream_h_coeff, stream_type='cold')
        )

    # Adapt Utilities
    # Your Utility class expects h_coeff. The CSV provides U_overall for the utility unit itself.
    # This means the HENProblem's U_heaters/U_coolers calculation might be simplified if we
    # directly use the U_overall from the CSV utility data.
    # For now, let's assume h_coeff for utility objects can also be a default.
    # The more important part is that cost_params for heater/cooler units will come from the CSV.
    
    primary_hot_utility_obj = None
    if loaded_hot_utilities_data:
        hu_data = loaded_hot_utilities_data[0] # Take the first one
        primary_hot_utility_obj = Utility(
            id_val=hu_data['Name'], Tin=hu_data['TIN_utility'], Tout=hu_data['TOUT_utility'],
            h_coeff=0, # Default h_coeff, U_overall from CSV will be more relevant for its own exchanger
            cost_per_energy_unit=hu_data['Unit_Cost_Energy'], utility_type='hot_utility'
        )
    else:
        # Create a dummy/default hot utility if none is loaded but needed.
        print("Warning: No hot utility defined in CSV. Using a placeholder default or calculations might fail.")
        # This placeholder needs to be carefully considered or an error raised if essential.
        primary_hot_utility_obj = Utility("DefaultHU", 500, 499, 1.0, 999, "hot_utility")


    primary_cold_utility_obj = None
    if loaded_cold_utilities_data:
        cu_data = loaded_cold_utilities_data[0] # Take the first one
        primary_cold_utility_obj = Utility(
            id_val=cu_data['Name'], Tin=cu_data['TIN_utility'], Tout=cu_data['TOUT_utility'],
            h_coeff=0, # Default h_coeff
            cost_per_energy_unit=cu_data['Unit_Cost_Energy'], utility_type='cold_utility'
        )
    else:
        print("Warning: No cold utility defined in CSV. Using a placeholder default or calculations might fail.")
        primary_cold_utility_obj = Utility("DefaultCU", 290, 300, 1.0, 999, "cold_utility")


    # --- Define Global Cost Parameters (EMAT and Process-Process Exchanger U/Costs) ---
    EMAT_setting = 3.0
    U_process_default_setting = 0.8 # kW/m^2K for general process-process exchangers
    # These are costs for PROCESS-PROCESS exchangers.
    # Heater/Cooler costs will now come from the utility CSV data.
    CF_process_setting = 0       # Fixed cost for a process-process exchanger
    C_area_process_setting = 1000    # Area coefficient for process-process exchanger
    B_exp_process_setting = 0.6    # Area exponent for process-process exchanger

    # Use cost parameters from utilities.csv for heaters and coolers
    # If utilities were loaded, their specific costs are used.
    # The CostParameters class now needs to reflect this division.
    # Let's assume the CostParameters class holds the EMAT and U_overall for proc-proc,
    # and the individual fixed/area/exp costs for proc-proc, heaters, and coolers.
    # The heater/cooler costs will be sourced from the *first* loaded utility of each type.

    heater_fixed_cost = loaded_hot_utilities_data[0]['Fixed_Cost_Unit'] if loaded_hot_utilities_data else 0
    heater_area_coeff = loaded_hot_utilities_data[0]['Area_Cost_Coeff'] if loaded_hot_utilities_data else 0
    heater_area_exp = loaded_hot_utilities_data[0]['Area_Cost_Exp'] if loaded_hot_utilities_data else 0.6

    cooler_fixed_cost = loaded_cold_utilities_data[0]['Fixed_Cost_Unit'] if loaded_cold_utilities_data else 0
    cooler_area_coeff = loaded_cold_utilities_data[0]['Area_Cost_Coeff'] if loaded_cold_utilities_data else 0
    cooler_area_exp = loaded_cold_utilities_data[0]['Area_Cost_Exp'] if loaded_cold_utilities_data else 0.6

    cost_params_instance = CostParameters(
        exch_fixed=CF_process_setting,
        exch_area_coeff=C_area_process_setting,
        exch_area_exp=B_exp_process_setting,
        heater_fixed=heater_fixed_cost,
        heater_area_coeff=heater_area_coeff,
        heater_area_exp=heater_area_exp,
        cooler_fixed=cooler_fixed_cost,
        cooler_area_coeff=cooler_area_coeff,
        cooler_area_exp=cooler_area_exp,
        EMAT=EMAT_setting,
        U_overall=U_process_default_setting # This U_overall is for process-process if stream h_coeffs are 0
    )

    num_stages_for_problem = max(1, len(hot_streams_obj_list), len(cold_streams_obj_list)) # Ensure at least 1 stage
    if num_stages_for_problem == 0 and (hot_streams_obj_list or cold_streams_obj_list): num_stages_for_problem = 1 # Handles case where one list is empty
    if not hot_streams_obj_list and not cold_streams_obj_list:
        print("No streams loaded. Exiting.")
        exit()
    
    hen_problem_instance = HENProblem(
        hot_streams_obj_list, cold_streams_obj_list,
        primary_hot_utility_obj, primary_cold_utility_obj,
        cost_params_instance,
        num_stages_for_problem
    )
    
    # Update U_heaters and U_coolers in HENProblem if utility CSV provided U_overall
    # This step bridges the U_overall from utilities.csv to your HENProblem's U calculation for utility units.
    # Your HENProblem.__init__ already has logic for this if cost_params.U_overall is None
    # and recalculates based on h_coeffs. If cost_params.U_overall is set, it might use that.
    # The utilities.csv provides specific U_overall for utility units.
    # We need to ensure these are used.
    
    # One way: directly set U_heaters/U_coolers if the specific U is available from CSV data.
    # This might override the h_coeff based calculation in HENProblem.__init__ for utilities.
    if loaded_hot_utilities_data:
        # HENProblem U_heaters is an array. Assuming single hot utility for all heaters.
        hen_problem_instance.U_heaters.fill(loaded_hot_utilities_data[0]['U_overall'])
    if loaded_cold_utilities_data:
        hen_problem_instance.U_coolers.fill(loaded_cold_utilities_data[0]['U_overall'])


    # --- GA Parameters ---
    ga_population_size = 50
    ga_generations = 10
    ga_crossover_prob = 0.85
    ga_mutation_prob = 0.2
    ga_elitism_count = 2

    # --- Multiple Runs ---
    number_of_runs = 1
    all_run_results = []
    base_seed = int(time.time())

    print(f"\n--- Starting {number_of_runs} GA Runs with EMAT = {EMAT_setting}K ---")
    for i in range(number_of_runs):
        current_seed = base_seed + i
        print(f"\n--- Running GA: Trial {i+1}/{number_of_runs} (Seed: {current_seed}) ---")
        
        ga_optimizer = GeneticAlgorithmHEN(
            hen_problem_instance,
            population_size=ga_population_size,
            generations=ga_generations,
            crossover_prob=ga_crossover_prob,
            mutation_prob=ga_mutation_prob,
            elitism_count=ga_elitism_count,
            random_seed=current_seed,
            utility_cost_factor=1.5, # Assuming no additional utility cost factor for simplicity
            pinch_deviation_penalty_factor=0.0 # Penalty factor for pinch deviation
        )
        
        # REFINED: run() now returns best_costs_dict
        best_Z_run, best_costs_dict_run, best_details_run = ga_optimizer.run(run_id_for_print=f"{i+1} (Seed {current_seed})")
        all_run_results.append({'seed': current_seed, 'costs': best_costs_dict_run, 'Z': best_Z_run, 'details': best_details_run})
        
        # Print TAC from the returned dictionary
        current_run_tac = best_costs_dict_run.get('TAC_GA_optimizing', float('inf'))
        if current_run_tac == float('inf'):
            print(f"--- Finished Trial {i+1}/{number_of_runs} - Best TAC: Inf ---")
        else:
            print(f"--- Finished Trial {i+1}/{number_of_runs} - Best TAC: {current_run_tac:.2f} ---")


    # --- Summarize and Analyze Results from Multiple Runs ---
    print("\n\n--- Summary of Multiple GA Runs ---")
    if not all_run_results:
        print("No results to summarize.")
    else:
        best_overall_costs = {"TAC_GA_optimizing": float('inf')} # Store the best costs dictionary
        best_run_details_for_overall_best = None # To store Z and exchanger details of overall best
        tac_values_from_runs = []

        for run_result in all_run_results:
            run_tac = run_result['costs']['TAC_GA_optimizing']
            if run_tac == float('inf'):
                print(f"Run with Seed {run_result['seed']}: TAC = Inf")
            else:
                print(f"Run with Seed {run_result['seed']}: TAC = {run_tac:.2f}")
            
            if run_tac != float('inf'):
                tac_values_from_runs.append(run_tac)
                if run_tac < best_overall_costs['TAC_GA_optimizing']:
                    best_overall_costs = copy.deepcopy(run_result['costs'])
                    best_run_details_for_overall_best = run_result # Store Z, details for this best run

        # Print overall best TAC
        if best_overall_costs['TAC_GA_optimizing'] == float('inf'):
            print(f"\nBest TAC found across all runs: Inf")
        else:
            print(f"\nBest TAC found across all runs: {best_overall_costs['TAC_GA_optimizing']:.2f}")

        if best_run_details_for_overall_best and best_overall_costs['TAC_GA_optimizing'] != float('inf'):
            print(f"Achieved with Seed: {best_run_details_for_overall_best['seed']}")
            
            # REFINED: Print detailed cost breakdown for the best run
            print("\nCost Breakdown for the Best Overall Solution:")
            print(f"  Total Annual Cost (TAC): {best_overall_costs['TAC_true_report']:.2f}")
            print(f"  Total Annual Capital Cost: {best_overall_costs['total_capital_cost']:.2f}")
            print(f"  Total Annual Operating Cost: {best_overall_costs['total_utility_cost']:.2f}")
            if best_overall_costs.get('penalty',0) > 1e-6 :
                 print(f"  Penalty Applied: {best_overall_costs['penalty']:.2f}")

            print("\nStructure of the absolute best run (Z_ijk - Active Matches [HotIdx, ColdIdx, StageIdx]):")
            best_Z_overall = best_run_details_for_overall_best['Z']
            details_overall = best_run_details_for_overall_best['details']
            if best_Z_overall is not None:
                # ... (rest of the structure and details printout as before, using best_Z_overall and details_overall) ...
                active_matches = np.argwhere(best_Z_overall == 1)
                if active_matches.size > 0:
                    for match in active_matches:
                        q_val_for_match = 0
                        if details_overall:
                            for detail_item in details_overall:
                                if detail_item.get('H') == match[0] and detail_item.get('C') == match[1] and detail_item.get('k') == match[2]:
                                    q_val_for_match = detail_item.get('Q',0); break
                        if q_val_for_match > 1e-6 : print(f"  Match: H{match[0]+1} ({hen_problem_instance.hot_streams[match[0]].id}) - C{match[1]+1} ({hen_problem_instance.cold_streams[match[1]].id}) at Stage {match[2]+1} (Q={q_val_for_match:.2f} kW)")
                else: print("  No active process-process matches with Q > 0.")
            
            print("\nDetails of the Best Network Configuration:")
            if details_overall:
                # ... (Detailed printout of exchangers and utilities as before, using details_overall)
                total_Q_recovered = 0; total_area_process_exch = 0; Q_hot_util_op_val = 0; Q_cold_util_op_val = 0
                print("  Process Heat Exchangers:"); 
                for detail in details_overall:
                    if 'H' in detail and 'C' in detail:
                        print(f"    H{detail['H']+1}({hen_problem_instance.hot_streams[detail['H']].id})-C{detail['C']+1}({hen_problem_instance.cold_streams[detail['C']].id}) (S{detail['k']+1}): Q={detail['Q']:.2f}, A={detail['Area']:.2f}, Th_in={detail['Th_in']:.1f}, Th_out={detail['Th_out']:.1f}, Tc_in={detail['Tc_in']:.1f}, Tc_out={detail['Tc_out']:.1f}")
                        total_Q_recovered += detail['Q']; total_area_process_exch += detail['Area']
                print(f"  Total Q_recovered: {total_Q_recovered:.2f} kW, Total Process Area: {total_area_process_exch:.2f} m^2")
                print("\n  Utility Units:")
                for detail in details_overall:
                    if detail.get('type') == 'heater':
                        print(f"    Heater for C{detail['C_idx']+1}({hen_problem_instance.cold_streams[detail['C_idx']].id}): Q={detail['Q']:.2f}, A={detail['Area']:.2f}, Tc_in={detail['Tc_in']:.1f}, Tc_out={detail['Tc_out']:.1f}")
                        Q_hot_util_op_val += detail['Q']
                    elif detail.get('type') == 'cooler':
                        print(f"    Cooler for H{detail['H_idx']+1}({hen_problem_instance.hot_streams[detail['H_idx']].id}): Q={detail['Q']:.2f}, A={detail['Area']:.2f}, Th_in={detail['Th_in']:.1f}, Th_out={detail['Th_out']:.1f}")
                        Q_cold_util_op_val += detail['Q']
                print(f"  Total Hot Utility (Op): {Q_hot_util_op_val:.2f} kW"); print(f"  Total Cold Utility (Op): {Q_cold_util_op_val:.2f} kW")    
        
        # Display the minimum hot and cold utility requirements
        print(f"  Minimum Hot Utility Required: {hen_problem_instance.Q_H_min_pinch:.2f} kW")
        print(f"  Minimum Cold Utility Required: {hen_problem_instance.Q_C_min_pinch:.2f} kW")
        
        if tac_values_from_runs: # Use the list that only contains finite TACs
            print(f"\nAverage TAC (of finite results): {np.mean(tac_values_from_runs):.2f}")
            print(f"Standard Deviation of TAC (of finite results): {np.std(tac_values_from_runs):.2f}")
            print(f"Min/Max TAC (of finite results): {np.min(tac_values_from_runs):.2f} / {np.max(tac_values_from_runs):.2f}")
        else:
            if any(r['costs']['TAC_GA_optimizing'] == float('inf') for r in all_run_results):
                 print("\nAll runs resulted in 'Inf' TAC or no successful finite results.")
            else:
                 print("\nNo finite TAC values recorded for statistics.")