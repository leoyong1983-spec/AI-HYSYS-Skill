import numpy as np
import random
import math
import copy
import csv
import time

# --- YOUR ORIGINAL HELPER CLASSES (Stream, Utility, CostParameters, HENProblem) ---
# Assume these are correctly defined as in your script.
class Stream:
    def __init__(self, id_val=None, Tin=None, Tout_target=None, CP=None,
                 h_coeff=None, U=None, stream_type=None):
        self.id = id_val
        self.Tin = Tin
        self.Tout_target = Tout_target
        self.CP = CP
        self.h = h_coeff
        self.U = U
        self.type = stream_type
        
class Utility:
    def __init__(self, id_val=None, Tin=None, Tout=None, h_coeff=None, U=None,
                 cost_per_energy_unit=None, fix_cost=None, area_cost_coeff=None,
                 area_cost_exp=None, utility_type=None):
        self.id = id_val
        self.Tin = Tin
        self.Tout = Tout
        self.h = h_coeff
        self.U = U
        self.cost = cost_per_energy_unit
        self.fix_cost = fix_cost
        self.area_cost_coeff = area_cost_coeff
        self.area_cost_exp = area_cost_exp
        self.type = utility_type
        
class CostParameters:
    def __init__(self, exch_fixed=0.0, exch_area_coeff=1000.0, exch_area_exp=0.6,
                 heater_fixed=0.0, heater_area_coeff=1200.0, heater_area_exp=0.6,
                 cooler_fixed=0.0, cooler_area_coeff=1000.0, cooler_area_exp=0.6,
                 EMAT=10.0, U_overall=None):
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
        self.U_overall = U_overall

class HENProblem:
    def __init__(self, hot_streams=None, cold_streams=None, hot_utility=None, cold_utility=None, 
                 cost_params=None, num_stages=1, matches_U_cost=None, annual_op_hours=8000):
        self.hot_streams = hot_streams
        self.cold_streams = cold_streams
        self.hot_utility = hot_utility
        self.cold_utility = cold_utility
        self.cost_params = cost_params
        self.num_stages = num_stages
        self.NH = len(hot_streams)
        self.NC = len(cold_streams)
        self.NHU = len(hot_utility)
        self.NCU = len(cold_utility)
        self.matches_U_cost = matches_U_cost
        self.annual_op_hours = annual_op_hours
        
        self.U_matrix_process = np.zeros((self.NH, self.NC))
        self.fixed_cost_process_exchangers = np.zeros((self.NH, self.NC))
        self.area_cost_process_coeff = np.zeros((self.NH, self.NC))
        self.area_cost_process_exp = np.zeros((self.NH, self.NC))
        
        self.U_heaters = np.zeros((self.NHU, self.NC))
        self.U_coolers = np.zeros((self.NH, self.NCU))
        
        # Initialize with defaults from global cost_params first
        self.U_matrix_process.fill(self.cost_params.U_overall if self.cost_params.U_overall is not None else 0) # Or handle U_overall is None case
        self.fixed_cost_process_exchangers.fill(self.cost_params.exch_fixed)
        self.area_cost_process_coeff.fill(self.cost_params.exch_area_coeff)
        self.area_cost_process_exp.fill(self.cost_params.exch_area_exp)
        self.U_heaters.fill(self.cost_params.U_overall if self.cost_params.U_overall is not None else 0)
        self.U_coolers.fill(self.cost_params.U_overall if self.cost_params.U_overall is not None else 0)
        
        if matches_U_cost:
            hot_stream_ids = {hs.id: idx for idx, hs in enumerate(self.hot_streams)}
            cold_stream_ids = {cs.id: idx for idx, cs in enumerate(self.cold_streams)}
            for match_spec in matches_U_cost:
                hot_id = match_spec.get('hot')
                cold_id = match_spec.get('cold')
                if hot_id in hot_stream_ids and cold_id in cold_stream_ids:
                    i = hot_stream_ids[hot_id]
                    j = cold_stream_ids[cold_id]
                    self.U_matrix_process[i,j] = match_spec.get('U', self.U_matrix_process[i,j]) # Use U from match, or keep default
                    self.fixed_cost_process_exchangers[i,j] = match_spec.get('fix_cost', self.fixed_cost_process_exchangers[i,j])
                    self.area_cost_process_coeff[i,j] = match_spec.get('area_cost_coeff', self.area_cost_process_coeff[i,j])
                    self.area_cost_process_exp[i,j] = match_spec.get('area_cost_exp', self.area_cost_process_exp[i,j])

        if self.cost_params.U_overall is None:
            for i in range(self.NH):
                for j in range(self.NC):
                    if self.U_matrix_process[i,j] == 0:
                        h_hot = self.hot_streams[i].h if self.hot_streams[i].h > 1e-9 else 1e9
                        h_cold = self.cold_streams[j].h if self.cold_streams[j].h > 1e-9 else 1e9
                        if self.hot_streams[i].h <= 1e-9 or self.cold_streams[j].h <= 1e-9: self.U_matrix_process[i,j] = 1e-6 
                        else: self.U_matrix_process[i, j] = 1.0 / (1.0/h_hot + 1.0/h_cold)
                        
            if self.hot_utility:
                for iu in range(self.NHU):
                    for j in range(self.NC):
                        if self.U_heaters[iu,j].U == 0:
                            h_hot_util = self.hot_utility[iu].h if self.hot_utility[iu].h > 1e-9 else 1e9
                            if self.hot_utility[iu].U is not None:
                                self.U_heaters[iu,j] = self.hot_utility[iu].U
                            else:
                                h_cold_stream = self.cold_streams[j].h if self.cold_streams[j].h > 1e-9 else 1e9
                                
                                if h_hot_util <=1e-9 or h_cold_stream <= 1e-9:
                                    self.U_heaters[iu,j] = 1e-6
                                else:
                                    self.U_heaters[iu,j] = 1.0 / (1.0/h_hot_util + 1.0/h_cold_stream)
                                
            if self.cold_utility:
                for ic in range(self.NCU):
                    for i in range(self.NH):
                        if self.U_coolers[i,ic].U == 0:
                            h_cold_util = self.cold_utility[ic].h if self.cold_utility[ic].h > 1e-9 else 1e9
                            if self.cold_utility[ic].U is not None:
                                self.U_coolers[i,ic] = self.cold_utility[ic].U
                            else:
                                h_hot_stream = self.hot_streams[i].h if self.hot_streams[i].h > 1e-9 else 1e9

                                if h_cold_util <=1e-9 or h_hot_stream <= 1e-9:
                                    self.U_coolers[i,ic] = 1e-6
                                else:
                                    self.U_coolers[i,ic] = 1.0 / (1.0/h_cold_util + 1.0/h_hot_stream)
        
        self.Q_H_min_pinch, self.Q_C_min_pinch, self.T_pinch_hot_actual, self.T_pinch_cold_actual = self._calculate_pinch_targets()
        
    def _calculate_pinch_targets(self):
        EMAT = self.cost_params.EMAT
        if not self.hot_streams and not self.cold_streams: return 0,0,None,None
        temp_points = set()
        for hs in self.hot_streams: temp_points.add(hs.Tin); temp_points.add(hs.Tout_target)
        for cs in self.cold_streams: temp_points.add(cs.Tin + EMAT); temp_points.add(cs.Tout_target + EMAT)
        sorted_temps = sorted(list(temp_points), reverse=True)
        if len(sorted_temps) < 2:
            total_hot_duty_available = sum([s.CP*(s.Tin-s.Tout_target) for s in self.hot_streams]); total_cold_duty_required = sum([s.CP*(s.Tout_target-s.Tin) for s in self.cold_streams])
            heat_deficit = total_cold_duty_required - total_hot_duty_available; q_h_min = max(0,heat_deficit); q_c_min = max(0,-heat_deficit); return q_h_min,q_c_min,None,None
        heat_cascade = [0.0]
        for i in range(len(sorted_temps)-1):
            T_high = sorted_temps[i]; T_low = sorted_temps[i+1]; delta_T_interval = T_high - T_low
            if delta_T_interval < 1e-6: continue
            sum_fcp_h_active = 0
            for hs in self.hot_streams:
                if hs.Tin > T_low and hs.Tout_target < T_high: sum_fcp_h_active += hs.CP
            sum_fcp_c_active = 0
            for cs in self.cold_streams:
                cs_tin_shifted = cs.Tin + EMAT; cs_tout_shifted = cs.Tout_target + EMAT
                if cs_tout_shifted > T_low and cs_tin_shifted < T_high: sum_fcp_c_active += cs.CP
            delta_H_interval = (sum_fcp_h_active - sum_fcp_c_active) * delta_T_interval
            heat_cascade.append(heat_cascade[-1] + delta_H_interval)
        min_cascade_value = min(heat_cascade); q_h_min = 0
        if min_cascade_value < -1e-6: q_h_min = -min_cascade_value
        feasible_cascade = [q + q_h_min for q in heat_cascade]; q_c_min = feasible_cascade[-1]
        try: pinch_interval_index = feasible_cascade.index(min(feasible_cascade))
        except ValueError: pinch_interval_index = 0
        T_pinch_shifted = sorted_temps[pinch_interval_index]; t_pinch_hot = T_pinch_shifted; t_pinch_cold = T_pinch_shifted - EMAT
        if abs(q_h_min) < 1e-6 : q_h_min = 0;
        if abs(q_c_min) < 1e-6 : q_c_min = 0;
        return q_h_min, q_c_min, t_pinch_hot, t_pinch_cold

# --- load_data_from_csv function (as previously defined) ---
def load_data_from_csv(streams_filepath, utilities_filepath, matches_U_filepath=None):
    # ... (exact same implementation as before)
    loaded_hot_streams = []
    loaded_cold_streams = []
    loaded_hot_utilities = []
    loaded_cold_utilities = []
    loaded_matches_U = []
    
    try:
        with open(streams_filepath, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row_idx, row in enumerate(reader):
                try:
                    stream_data = {'Name': row['Name'],'Type': row['Type'].lower(),'TIN_spec': float(row['TIN_spec']),'TOUT_spec': float(row['TOUT_spec']),'Fcp': float(row['Fcp'])}
                    if stream_data['Type'] == 'hot': loaded_hot_streams.append(stream_data)
                    elif stream_data['Type'] == 'cold': loaded_cold_streams.append(stream_data)
                    else: print(f"Warning: Unknown stream type '{row['Type']}' for stream '{row['Name']}'. Skipping.")
                except KeyError as e:
                    print(f"Error: Missing column {e} in streams.csv at row {row_idx+1}.")
                    return None,None,None,None,None
                except ValueError as e:
                    print(f"Error: Could not convert value to float in streams.csv at row {row_idx+1} for column {e}.")
                    return None,None,None,None,None
    except FileNotFoundError:
        print(f"Error: Streams file not found at {streams_filepath}")
        return None,None,None,None,None
    except Exception as e:
        print(f"Error reading streams CSV: {e}")
        return None,None,None,None,None
    
    # load matches_U_cost
    if matches_U_filepath:
        try:
            with open(matches_U_filepath, mode='r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row_idx, row in enumerate(reader):
                    try:
                        match_U_cost = {'hot': row['Hot_Stream'], 'cold': row['Cold_Stream'], 'U': float(row['U_overall']), 'fix_cost': float(row['Fixed_Cost_Unit']), 'area_cost_coeff': float(row['Area_Cost_Coeff']), 'area_cost_exp': float(row['Area_Cost_Exp'])}
                        loaded_matches_U.append(match_U_cost)
                    except KeyError as e:
                        print(f"Error: Missing column {e} in matches_U_cost.csv at row {row_idx+1}.")
                        return None,None,None,None,None
                    except ValueError as e:
                        print(f"Error: Could not convert value to float in matches_U_cost.csv at row {row_idx+1} for column {e}.")
                        return None,None,None,None,None
        except FileNotFoundError:
            print(f"Error: matches_U_cost file not found at {matches_U_filepath}")
            return None,None,None,None,None
        except Exception as e:
            print(f"Error reading matches_U_cost CSV: {e}")
            return None,None,None,None,None
    else:
        loaded_matches_U = None
        
    try:
        with open(utilities_filepath, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row_idx, row in enumerate(reader):
                try:
                    util_data = {'Name': row['Name'],'Type': row['Type'].lower(),'TIN_utility': float(row['TIN_utility']),'TOUT_utility': float(row['TOUT_utility']),'Unit_Cost_Energy': float(row['Unit_Cost_Energy']),'U_overall': float(row['U_overall']),'Fixed_Cost_Unit': float(row['Fixed_Cost_Unit']),'Area_Cost_Coeff': float(row['Area_Cost_Coeff']),'Area_Cost_Exp': float(row['Area_Cost_Exp'])}
                    if util_data['Type'] == 'hot_utility': loaded_hot_utilities.append(util_data)
                    elif util_data['Type'] == 'cold_utility': loaded_cold_utilities.append(util_data)
                    else: print(f"Warning: Unknown utility type '{row['Type']}' for utility '{row['Name']}'. Skipping.")
                except KeyError as e:
                    print(f"Error: Missing column {e} in utilities.csv at row {row_idx+1}.")
                    return None,None,None,None,None
                except ValueError as e:
                    print(f"Error: Could not convert value to float in utilities.csv at row {row_idx+1} for column {e}.")
                    return None,None,None,None,None
    except FileNotFoundError:
        print(f"Error: Utilities file not found at {utilities_filepath}")
        return None,None,None,None,None
    except Exception as e:
        print(f"Error reading utilities CSV: {e}")
        return None,None,None,None,None
    if not loaded_hot_utilities and any(s['Type'] == 'cold' for s in loaded_cold_streams):
        print("Warning: No hot utilities loaded...")
    if not loaded_cold_utilities and any(s['Type'] == 'hot' for s in loaded_hot_streams):
        print("Warning: No cold utilities loaded...")
    return loaded_hot_streams, loaded_cold_streams, loaded_hot_utilities, loaded_cold_utilities, loaded_matches_U

class GeneticAlgorithmHEN:
    def __init__(self, problem,
                 population_size,
                 generations,
                 crossover_prob,
                 mutation_prob_Z,
                 mutation_prob_R,
                 elitism_count=10,
                 random_seed=None,
                 utility_cost_factor=1.0, # For weighting utility costs in GA objective
                 pinch_deviation_penalty_factor=0.0, # For penalizing deviation from Q_pinch
                 r_mutation_std_dev_factor=0.1,
                 sws_max_iter=50,
                 sws_conv_tol=0.001): # For Gaussian mutation of R values

        self.problem = problem
        self.population_size = population_size
        self.generations = generations
        self.crossover_prob = crossover_prob
        self.mutation_prob_Z = mutation_prob_Z
        self.mutation_prob_R = mutation_prob_R
        self.elitism_count = elitism_count
        self.random_seed = random_seed
        self.utility_cost_factor = utility_cost_factor
        self.pinch_deviation_penalty_factor = pinch_deviation_penalty_factor
        self.sws_max_iter = sws_max_iter
        self.sws_conv_tol = sws_conv_tol
        self.r_mutation_std_dev_factor = r_mutation_std_dev_factor

        if random_seed is not None:
            random.seed(random_seed)
            np.random.seed(random_seed)

        # Define chromosome segment lengths
        self.len_Z = self.problem.NH * self.problem.NC * self.problem.num_stages
        self.len_R_hot_splits = self.problem.NH * self.problem.num_stages * self.problem.NC
        self.len_R_cold_splits = self.problem.NC * self.problem.num_stages * self.problem.NH
        self.chromosome_length = self.len_Z + self.len_R_hot_splits + self.len_R_cold_splits
        
        self.population = []

    def _initialize_population(self):
        self.population = []
        for _ in range(self.population_size):
            self.population.append(self._create_random_full_chromosome())

    def _decode_chromosome(self, chromosome):
        z_part_flat = chromosome[:self.len_Z]
        r_hot_part_flat = chromosome[self.len_Z : self.len_Z + self.len_R_hot_splits]
        r_cold_part_flat = chromosome[self.len_Z + self.len_R_hot_splits:]

        Z_ijk = z_part_flat.reshape((self.problem.NH, self.problem.NC, self.problem.num_stages)).astype(int)
        R_hot_splits_decoded = r_hot_part_flat.reshape((self.problem.NH, self.problem.num_stages, self.problem.NC))
        R_cold_splits_decoded = r_cold_part_flat.reshape((self.problem.NC, self.problem.num_stages, self.problem.NH))
        
        return Z_ijk, R_hot_splits_decoded, R_cold_splits_decoded

    def _calculate_lmtd(self, Th_in, Th_out, Tc_in, Tc_out):
        delta_T1 = Th_in - Tc_out
        delta_T2 = Th_out - Tc_in
        if delta_T1 <= 1e-6 or delta_T2 <= 1e-6:
            if abs(delta_T1 - delta_T2) < 1e-6 and delta_T1 > 1e-6:
                return delta_T1
            return 1e-6
        if abs(delta_T1 - delta_T2) < 1e-6:
            lmtd = (delta_T1 + delta_T2) / 2.0
        else:
            lmtd = (delta_T1 - delta_T2) / math.log(delta_T1 / delta_T2)
        if lmtd <= 1e-6:
            return 1e-6
        return lmtd

    # Inside GeneticAlgorithmHEN class:
    def _calculate_fitness(self, chromosome):
        Z_ijk, R_hot_splits, R_cold_splits = self._decode_chromosome(chromosome)

        NH = self.problem.NH
        NC = self.problem.NC
        NHU = self.problem.NHU
        NCU = self.problem.NCU
        ST = self.problem.num_stages
        EMAT = self.problem.cost_params.EMAT
        
        CF_process = self.problem.cost_params.exch_fixed
        C_area_process = self.problem.cost_params.exch_area_coeff
        B_exp_process = self.problem.cost_params.exch_area_exp
        hot_util_obj = self.problem.hot_utility
        cold_util_obj = self.problem.cold_utility

        capital_cost_process_exchangers = 0.0
        capital_cost_heaters = 0.0
        capital_cost_coolers = 0.0
        annual_hot_utility_op_cost = 0.0
        annual_cold_utility_op_cost = 0.0
        penalty_EMAT = 0.0 # For EMAT violations in both process and utility units
        penalty_unmet_targets = 0.0
        penalty_pinch_deviation = 0.0
        
        exchanger_details_list = []

        # --- 1. Determine Actual Split Fractions (FH_ijk, FC_ijk) ---
        FH_ijk = np.zeros((NH, NC, ST)) 
        FC_ijk = np.zeros((NH, NC, ST)) 

        for k_stage_split_loop in range(ST): # Use distinct loop var name
            for i_hot_split_loop in range(NH):
                active_cold_targets_indices = [j_cold_target for j_cold_target in range(NC) if Z_ijk[i_hot_split_loop, j_cold_target, k_stage_split_loop] == 1]
                num_active_hot_branches = len(active_cold_targets_indices)
                if num_active_hot_branches == 1: 
                    FH_ijk[i_hot_split_loop, active_cold_targets_indices[0], k_stage_split_loop] = 1.0
                elif num_active_hot_branches > 1:
                    # R_hot_splits is (NH, ST, NC)
                    raw_r_values = R_hot_splits[i_hot_split_loop, k_stage_split_loop, active_cold_targets_indices]
                    sum_r = np.sum(raw_r_values)
                    if sum_r > 1e-6:
                        normalized_r = raw_r_values / sum_r
                        for idx, j_cold_actual_target_idx in enumerate(active_cold_targets_indices): 
                            FH_ijk[i_hot_split_loop, j_cold_actual_target_idx, k_stage_split_loop] = normalized_r[idx]
                    elif active_cold_targets_indices: # Fallback if all R are zero for active
                        for j_cold_actual_target_idx in active_cold_targets_indices: 
                            FH_ijk[i_hot_split_loop, j_cold_actual_target_idx, k_stage_split_loop] = 1.0 / num_active_hot_branches
            
            for j_cold_split_loop in range(NC):
                active_hot_sources_indices = [i_hot_source for i_hot_source in range(NH) if Z_ijk[i_hot_source, j_cold_split_loop, k_stage_split_loop] == 1]
                num_active_cold_branches = len(active_hot_sources_indices)
                if num_active_cold_branches == 1: 
                    FC_ijk[active_hot_sources_indices[0], j_cold_split_loop, k_stage_split_loop] = 1.0
                elif num_active_cold_branches > 1:
                    # R_cold_splits is (NC, ST, NH)
                    raw_r_values = R_cold_splits[j_cold_split_loop, k_stage_split_loop, active_hot_sources_indices]
                    sum_r = np.sum(raw_r_values)
                    if sum_r > 1e-6:
                        normalized_r = raw_r_values / sum_r
                        for idx, i_hot_actual_source_idx in enumerate(active_hot_sources_indices): 
                            FC_ijk[i_hot_actual_source_idx, j_cold_split_loop, k_stage_split_loop] = normalized_r[idx]
                    elif active_hot_sources_indices: # Fallback
                        for i_hot_actual_source_idx in active_hot_sources_indices: 
                            FC_ijk[i_hot_actual_source_idx, j_cold_split_loop, k_stage_split_loop] = 1.0 / num_active_cold_branches

        # --- 2. SWS Temperature Iteration Loop ---
        Q_ijk_converged = np.zeros((NH, NC, ST))
        T_mix_H_outlet_current_sws = np.array([[hs.Tin for _ in range(ST)] for hs in self.problem.hot_streams]) # Stores T_mix_H_i,k
        T_mix_C_outlet_current_sws = np.array([[cs.Tin for _ in range(ST)] for cs in self.problem.cold_streams]) # Stores T_mix_C_j,k

        # These will hold the values from the *previous complete SWS iteration* to feed the current one
        T_mix_H_outlet_prev_sws_iter = T_mix_H_outlet_current_sws.copy()
        T_mix_C_outlet_prev_sws_iter = T_mix_C_outlet_current_sws.copy()

        MAX_SWS_ITER = self.sws_max_iter
        SWS_CONV_TOL = self.sws_conv_tol

        for sws_iter_count in range(MAX_SWS_ITER): # Renamed sws_iter for clarity
            # Store current mixer temps at start of this pass for convergence check
            T_mix_H_for_convergence_check = T_mix_H_outlet_current_sws.copy()
            T_mix_C_for_convergence_check = T_mix_C_outlet_current_sws.copy()
            
            Q_ijk_this_sws_iter_pass = np.zeros((NH, NC, ST)) # Q values calculated in this current pass

            # --- Hot Pass (stages k = 0 to ST-1) ---
            for k_stage_loop in range(ST):
                # Overall inlet temp of hot stream i_hot to matches in stage k_stage_loop
                # This comes from the *previous SWS iteration's* mixer outlet of the *previous stage*
                TinH_overall_to_stage_k_matches = np.zeros(NH)
                for i_hot_idx in range(NH):
                    TinH_overall_to_stage_k_matches[i_hot_idx] = T_mix_H_outlet_prev_sws_iter[i_hot_idx, k_stage_loop-1] if k_stage_loop > 0 else self.problem.hot_streams[i_hot_idx].Tin
                
                Q_total_from_hot_stream_at_stage_k = np.zeros(NH) # Sum of Q from all branches of a hot stream in this stage
                
                for i_hot_idx in range(NH):
                    hs = self.problem.hot_streams[i_hot_idx]
                    # This is the temperature of hs BEFORE splitting within this stage k_stage_loop
                    TinH_for_hs_branches_in_stage_k = TinH_overall_to_stage_k_matches[i_hot_idx]
                    
                    for j_cold_idx in range(NC):
                        cs = self.problem.cold_streams[j_cold_idx]
                        if Z_ijk[i_hot_idx, j_cold_idx, k_stage_loop] == 1:
                            # Inlet temp of cold stream cs to this specific match
                            # This comes from *previous SWS iteration's* mixer outlet of the *next stage* (for cs)
                            Tcin_for_cs_branch_in_stage_k = T_mix_C_outlet_prev_sws_iter[j_cold_idx, k_stage_loop+1] if k_stage_loop < ST-1 else cs.Tin
                            
                            CPH_b = hs.CP * FH_ijk[i_hot_idx, j_cold_idx, k_stage_loop]
                            CPC_b = cs.CP * FC_ijk[i_hot_idx, j_cold_idx, k_stage_loop] # FC_ijk[i,j,k] is fraction of Cj for match (i,j,k)
                            
                            Q_m = 0 
                            if CPH_b > 1e-9 and CPC_b > 1e-9:
                                Q_H_target_limit = CPH_b * (TinH_for_hs_branches_in_stage_k - hs.Tout_target)
                                Q_H_EMAT_limit   = CPH_b * (TinH_for_hs_branches_in_stage_k - (Tcin_for_cs_branch_in_stage_k + EMAT))
                                Q_C_target_limit = CPC_b * (cs.Tout_target - Tcin_for_cs_branch_in_stage_k)
                                Q_C_EMAT_limit   = CPC_b * ((TinH_for_hs_branches_in_stage_k - EMAT) - Tcin_for_cs_branch_in_stage_k)
                                Q_m = max(0, min(Q_H_target_limit, Q_H_EMAT_limit, Q_C_target_limit, Q_C_EMAT_limit))
                            
                            Q_ijk_this_sws_iter_pass[i_hot_idx, j_cold_idx, k_stage_loop] = Q_m
                            Q_total_from_hot_stream_at_stage_k[i_hot_idx] += Q_m # Accumulate Q for this hot stream
                
                # Update Hot Mixer Outlets for *current* SWS iteration *after this stage*
                for i_hot_mixer_idx in range(NH):
                    hs_m = self.problem.hot_streams[i_hot_mixer_idx]
                    # Mixer outlet temp is based on its inlet temp to the stage, and total Q removed by its branches in this stage
                    if hs_m.CP > 1e-9:
                        T_mix_H_outlet_current_sws[i_hot_mixer_idx, k_stage_loop] = TinH_overall_to_stage_k_matches[i_hot_mixer_idx] - Q_total_from_hot_stream_at_stage_k[i_hot_mixer_idx] / hs_m.CP
                    else:
                        T_mix_H_outlet_current_sws[i_hot_mixer_idx, k_stage_loop] = TinH_overall_to_stage_k_matches[i_hot_mixer_idx]

            # --- Cold Pass (stages k = ST-1 down to 0) ---
            # The Q values (Q_ijk_this_sws_iter_pass) are now fixed from the hot pass of THIS sws_iter_count
            for k_stage_loop in range(ST - 1, -1, -1):
                TinC_overall_to_stage_k_matches = np.zeros(NC)
                for j_cs_idx in range(NC):
                    TinC_overall_to_stage_k_matches[j_cs_idx] = T_mix_C_outlet_prev_sws_iter[j_cs_idx, k_stage_loop+1] if k_stage_loop < ST-1 else self.problem.cold_streams[j_cs_idx].Tin
                
                Q_total_to_cold_stream_at_stage_k = np.zeros(NC)
                for j_cold_idx in range(NC):
                    for i_hot_idx in range(NH):
                        if Z_ijk[i_hot_idx, j_cold_idx, k_stage_loop] == 1:
                            Q_total_to_cold_stream_at_stage_k[j_cold_idx] += Q_ijk_this_sws_iter_pass[i_hot_idx,j_cold_idx,k_stage_loop]
                                            
                for j_cold_mixer_idx in range(NC):
                    cs_m = self.problem.cold_streams[j_cold_mixer_idx]
                    if cs_m.CP > 1e-9:
                        T_mix_C_outlet_current_sws[j_cold_mixer_idx, k_stage_loop] = TinC_overall_to_stage_k_matches[j_cold_mixer_idx] + Q_total_to_cold_stream_at_stage_k[j_cold_mixer_idx] / cs_m.CP
                    else:
                        T_mix_C_outlet_current_sws[j_cold_mixer_idx, k_stage_loop] = TinC_overall_to_stage_k_matches[j_cold_mixer_idx]

            # Convergence Check
            delta_H_conv = np.max(np.abs(T_mix_H_for_convergence_check - T_mix_H_outlet_current_sws)) if NH > 0 and ST > 0 else 0
            delta_C_conv = np.max(np.abs(T_mix_C_for_convergence_check - T_mix_C_outlet_current_sws)) if NC > 0 and ST > 0 else 0

            # Update "previous iteration" values for the *next SWS iteration*
            T_mix_H_outlet_prev_sws_iter = T_mix_H_outlet_current_sws.copy()
            T_mix_C_outlet_prev_sws_iter = T_mix_C_outlet_current_sws.copy()
            Q_ijk_converged = Q_ijk_this_sws_iter_pass.copy() 

            if delta_H_conv < SWS_CONV_TOL and delta_C_conv < SWS_CONV_TOL and sws_iter_count > 0: # sws_iter_count > 0 ensures at least one full update
                break
            
            if sws_iter_count >= MAX_SWS_ITER - 1:
                # print(f"MAX SWS ITERATIONS REACHED.")
                penalty_unmet_targets = 1e9
        
        # --- Stage 3 & 4: Exchanger Area/Cost and Utility Calculations ---
        # Use final converged values: T_mix_H_outlet_current_sws, T_mix_C_outlet_current_sws, Q_ijk_converged
        for k_idx_final_cost_loop in range(ST): # Use distinct var name
            for i_idx_final_cost_loop in range(NH):
                hs_final = self.problem.hot_streams[i_idx_final_cost_loop]
                for j_idx_final_cost_loop in range(NC):
                    cs_final = self.problem.cold_streams[j_idx_final_cost_loop]
                    if Z_ijk[i_idx_final_cost_loop, j_idx_final_cost_loop, k_idx_final_cost_loop] == 1 and \
                       Q_ijk_converged[i_idx_final_cost_loop, j_idx_final_cost_loop, k_idx_final_cost_loop] > 1e-6:
                        
                        Q_final_ex = Q_ijk_converged[i_idx_final_cost_loop, j_idx_final_cost_loop, k_idx_final_cost_loop]
                        
                        # Inlet temp to this exchanger is the MIXER OUTLET of the PREVIOUS stage for that stream
                        Th_in_final_ex = T_mix_H_outlet_current_sws[i_idx_final_cost_loop, k_idx_final_cost_loop-1] if k_idx_final_cost_loop > 0 else hs_final.Tin
                        Tc_in_final_ex = T_mix_C_outlet_current_sws[j_idx_final_cost_loop, k_idx_final_cost_loop+1] if k_idx_final_cost_loop < ST-1 else cs_final.Tin
                        
                        CPH_b_final_ex = hs_final.CP * FH_ijk[i_idx_final_cost_loop, j_idx_final_cost_loop, k_idx_final_cost_loop]
                        CPC_b_final_ex = cs_final.CP * FC_ijk[i_idx_final_cost_loop, j_idx_final_cost_loop, k_idx_final_cost_loop]

                        if CPH_b_final_ex < 1e-9 or CPC_b_final_ex < 1e-9: continue # Should have Q=0 if no flow
                        
                        Th_out_final_ex = Th_in_final_ex - Q_final_ex / CPH_b_final_ex
                        Tc_out_final_ex = Tc_in_final_ex + Q_final_ex / CPC_b_final_ex

                        dTa_final = Th_in_final_ex - Tc_out_final_ex
                        dTb_final = Th_out_final_ex - Tc_in_final_ex
                        # Ensure penalty is positive or zero
                        if dTa_final < EMAT - 1e-3: penalty_EMAT += 1e7 * max(0, EMAT - dTa_final)
                        if dTb_final < EMAT - 1e-3: penalty_EMAT += 1e7 * max(0, EMAT - dTb_final)
                        
                        lmtd_final_ex = self._calculate_lmtd(Th_in_final_ex, Th_out_final_ex, Tc_in_final_ex, Tc_out_final_ex)
                        U_final_ex = self.problem.U_matrix_process[i_idx_final_cost_loop, j_idx_final_cost_loop]
                        area_final_ex = 1e9
                        if U_final_ex > 1e-9 and lmtd_final_ex > 1e-9 :
                            area_final_ex = Q_final_ex / (U_final_ex * lmtd_final_ex)
                        if area_final_ex < 0:
                            area_final_ex = 1e9 # Should not happen if LMTD is positive
                            
                        CF_process = self.problem.fixed_cost_process_exchangers[i_idx_final_cost_loop,j_idx_final_cost_loop]
                        C_area_process = self.problem.area_cost_process_coeff[i_idx_final_cost_loop,j_idx_final_cost_loop]
                        B_exp_process = self.problem.area_cost_process_exp[i_idx_final_cost_loop,j_idx_final_cost_loop]
                        cost_ex_final = CF_process + C_area_process * (area_final_ex ** B_exp_process)
                        capital_cost_process_exchangers += cost_ex_final
                        exchanger_details_list.append({'H': i_idx_final_cost_loop, 'C': j_idx_final_cost_loop, 'k': k_idx_final_cost_loop, 
                                                       'Q': Q_final_ex, 'Area': area_final_ex, 
                                                       'Th_in': Th_in_final_ex, 'Th_out': Th_out_final_ex, 
                                                       'Tc_in': Tc_in_final_ex, 'Tc_out': Tc_out_final_ex})
        
        # --- Utility Calculation & Final Target Check ---
        # Temperatures of streams LEAVING the SWS recovery section
        final_Th_after_sws_recovery = np.zeros(NH)
        if ST > 0 :
            final_Th_after_sws_recovery = T_mix_H_outlet_current_sws[:, ST-1] # Outlet of mixer after last stage ST-1
        else:
            final_Th_after_sws_recovery = np.array([hs.Tin for hs in self.problem.hot_streams])

        final_Tc_after_sws_recovery = np.zeros(NC)
        if ST > 0:
            final_Tc_after_sws_recovery = T_mix_C_outlet_current_sws[:, 0] # Outlet of mixer after first stage 0 (from cold stream perspective)
        else:
            final_Tc_after_sws_recovery = np.array([cs.Tin for cs in self.problem.cold_streams])
        
        target_temp_penalty_factor = 1e9
        temp_tolerance = 0.001
        
        Q_hot_consumed_kW_actual = 0.0
        Q_cold_consumed_kW_actual = 0.0
        
        final_outlet_Th_after_utility = final_Th_after_sws_recovery.copy()
        final_outlet_Tc_after_utility = final_Tc_after_sws_recovery.copy()
        
        # Determine the required hot and cold utilities
        Q_cold_HS_required = np.zeros(NH) # Total Q required from each hot stream
        Q_hot_CS_required = np.zeros(NC) # Total Q required to each cold stream
        
        for i_hot_idx in range(NH):
            hs = self.problem.hot_streams[i_hot_idx]
            Q_total = 0
            for j_cold_idx in range(NC):
                for k_stage_idx in range(ST):
                    Q_total += Q_ijk_converged[i_hot_idx, j_cold_idx, k_stage_idx]
            Q_cold_HS_required[i_hot_idx] = hs.CP * (hs.Tin - hs.Tout_target) - float(Q_total) # Total Q required from this hot stream after SWS recovery
            if Q_cold_HS_required[i_hot_idx] < 1e-6: Q_cold_HS_required[i_hot_idx] = 0 # No negative requirements
            Q_required = float(Q_cold_HS_required[i_hot_idx])

        for j_cold_idx in range(NC):
            cs = self.problem.cold_streams[j_cold_idx]
            Q_total = 0
            for i_hot_idx in range(NH):
                for k_stage_idx in range(ST):
                    Q_total += Q_ijk_converged[i_hot_idx, j_cold_idx, k_stage_idx]
            Q_hot_CS_required[j_cold_idx] = cs.CP * (cs.Tout_target - cs.Tin) - Q_total
            if Q_hot_CS_required[j_cold_idx] < 1e-6: Q_hot_CS_required[j_cold_idx] = 0.0
            Q_required = float(Q_hot_CS_required[j_cold_idx])

        # Assign the utlity by selecting the cheaper
        if cold_util_obj: # Coolers for HOT streams
            for i_hot_util_loop in range(NH):
                # Q_required = Q_cold_HS_required[i_hot_util_loop]
                # if Q_required < 1e-6: continue # No utility needed for this hot stream
                
                # hs_util:Stream = self.problem.hot_streams[i_hot_util_loop]
                # cu:Utility = cold_util_obj[0]
                # Th_in_cu = final_Th_after_sws_recovery[i_hot_util_loop]
                # Th_out_cu = hs_util.Tout_target
                # Tc_in_cu_u = cu.Tin
                # Tc_out_cu_u = cu.Tout
                
                # lmtd_cu_u = self._calculate_lmtd(Th_in_cu, Th_out_cu, Tc_in_cu_u, Tc_out_cu_u)
                # U_cu_u = self.problem.U_coolers[i_hot_util_loop, 0]
                # if U_cu_u <= 1e-9 or lmtd_cu_u <= 1e-9:
                #     area_cu_u = 1e9 # Avoid division by zero
                # else:
                #     area_cu_u = Q_required / (U_cu_u * lmtd_cu_u)

                # cost_cu_u = cu.fix_cost + cu.area_cost_coeff * (area_cu_u ** cu.area_cost_exp)
                # capital_cost_coolers += cost_cu_u
                # annual_cold_utility_op_cost += cu.cost * Q_required
                # exchanger_details_list.append({'type': 'cooler', 'H_idx': i_hot_util_loop, 'Q': Q_required, 'Area': area_cu_u, 'Th_in': Th_in_cu, 'Th_out': Th_out_cu, 'util_Tin': Tc_in_cu_u, 'util_Tout':Tc_out_cu_u})
                # final_outlet_Th_after_utility[i_hot_util_loop] = hs_util.Tout_target
                hs_util = self.problem.hot_streams[i_hot_util_loop]
                temp_before_cu = final_Th_after_sws_recovery[i_hot_util_loop]
                Q_cooler_needed = hs_util.CP * (temp_before_cu - hs_util.Tout_target)

                if Q_cooler_needed > 1e-6 and hs_util.CP > 1e-9:
                    best_cu_obj_for_this_need = None
                    min_incremental_cost_for_this_cooler = float('inf')
                    best_cooler_capital_cost = 0; best_cooler_op_cost_for_this_Q = 0; best_cooler_details = {}

                    for cu_candidate in self.problem.cold_utility: # Iterate through available cold utilities
                        Th_in_cu = temp_before_cu; Th_out_cu = hs_util.Tout_target
                        Tc_in_cu_u = cu_candidate.Tin
                        Tc_out_cu_u = cu_candidate.Tout if cu_candidate.Tout is not None and cu_candidate.Tout > Tc_in_cu_u else Tc_in_cu_u + 5 
                        
                        emat_ok_cu = True
                        if Th_in_cu < Tc_out_cu_u + EMAT - 1e-3: emat_ok_cu = False
                        if Th_out_cu < Tc_in_cu_u + EMAT - 1e-3: emat_ok_cu = False

                        if emat_ok_cu:
                            lmtd_cu_u = self._calculate_lmtd(Th_in_cu, Th_out_cu, Tc_in_cu_u, Tc_out_cu_u)
                            U_cu_u = cu_candidate.U # U from this specific cold utility object
                            area_cu_u = 1e9
                            if U_cu_u > 1e-9 and lmtd_cu_u > 1e-9: area_cu_u = Q_cooler_needed / (U_cu_u * lmtd_cu_u)
                            if area_cu_u < 0: area_cu_u = 1e9
                            
                            current_cooler_capital = cu_candidate.fix_cost + cu_candidate.area_cost_coeff * (area_cu_u ** cu_candidate.area_cost_exp)
                            current_cooler_op = cu_candidate.cost * Q_cooler_needed
                            current_total_impact_cu = current_cooler_capital + current_cooler_op

                            if current_total_impact_cu < min_incremental_cost_for_this_cooler:
                                min_incremental_cost_for_this_cooler = current_total_impact_cu
                                best_cu_obj_for_this_need = cu_candidate
                                best_cooler_capital_cost = current_cooler_capital
                                best_cooler_op_cost_for_this_Q = current_cooler_op
                                best_cooler_details = {'type': 'cooler', 'H_idx': i_hot_util_loop, 'Q': Q_cooler_needed, 
                                                       'Area': area_cu_u, 'Th_in': Th_in_cu, 'Th_out': Th_out_cu, 
                                                       'util_Tin': Tc_in_cu_u, 'util_Tout':Tc_out_cu_u, 'Util_ID': cu_candidate.id}
                    
                    if best_cu_obj_for_this_need:
                        Q_cold_consumed_kW_actual += Q_cooler_needed
                        capital_cost_coolers += best_cooler_capital_cost
                        annual_cold_utility_op_cost += best_cooler_op_cost_for_this_Q
                        exchanger_details_list.append(best_cooler_details)
                        final_outlet_Th_after_utility[i_hot_util_loop] = hs_util.Tout_target
                    else: # No feasible cold utility found
                        penalty_unmet_targets += target_temp_penalty_factor * Q_cooler_needed

        if hot_util_obj: # Heaters for COLD streams
            for j_cold_util_loop in range(NC):
                # Q_required = Q_hot_CS_required[j_cold_util_loop]
                # if Q_required < 1e-6: continue # No utility needed for this cold stream
                
                # cs_util:Stream = self.problem.cold_streams[j_cold_util_loop]
                # hu:Utility = hot_util_obj[0]
                # Tc_in_hu_u = final_Tc_after_sws_recovery[j_cold_util_loop]
                # Tc_out_hu_u = cs_util.Tout_target
                # Th_in_hu_u = hu.Tin
                # Th_out_hu_u = hu.Tout
                # lmtd_hu_u = self._calculate_lmtd(Th_in_hu_u, Th_out_hu_u, Tc_in_hu_u, Tc_out_hu_u)
                # U_hu_u = self.problem.U_heaters[0, j_cold_util_loop]
                # if U_hu_u <= 1e-9 or lmtd_hu_u <= 1e-9:
                #     area_hu_u = 1e9 # Avoid division by zero
                # else:
                #     area_hu_u = Q_required / (U_hu_u * lmtd_hu_u)
                    
                # cost_hu_u = hu.fix_cost + hu.area_cost_coeff * (area_hu_u ** hu.area_cost_exp)
                # capital_cost_heaters += cost_hu_u
                # annual_hot_utility_op_cost += hu.cost * Q_required
                # exchanger_details_list.append({'type': 'heater', 'C_idx': j_cold_util_loop, 'Q': Q_required, 'Area': area_hu_u, 'Tc_in': Tc_in_hu_u, 'Tc_out': Tc_out_hu_u, 'util_Tin':Th_in_hu_u, 'util_Tout':Th_out_hu_u})
                # final_outlet_Tc_after_utility[j_cold_util_loop] = cs_util.Tout_target
                
                # --- Strategy 2 (Heuristic Choice)
                cs_util:Stream = self.problem.cold_streams[j_cold_util_loop]
                Q_heater_val = Q_hot_CS_required[j_cold_util_loop]
                if Q_heater_val > 1e-9 and cs_util.CP > 1e-9:
                    best_hu_obj_for_this_need = None
                    min_incremental_cost_for_this_heater = float('inf')
                    best_heater_capital_cost = 0
                    best_heater_op_cost_for_this_Q = 0
                    best_heater_details = {}
                    
                    for hu_candidate in self.problem.hot_utility:
                        # Check EMAT feasibility for hu_candidate with cs_util
                        Th_in_hu_u = hu_candidate.Tin
                        # If hu_candidate.Tout is fixed, use it. Else, assume it can provide Q_heater_val
                        # A more robust check involves ensuring hu_candidate can actually supply Q_heater_val
                        # without its own temperature crossing or violating EMAT.
                        # For simplicity, assume utility Tout is fixed or can adjust.
                        Th_out_hu_u = hu_candidate.Tout if hu_candidate.Tout is not None and hu_candidate.Tout < Th_in_hu_u else Th_in_hu_u - 1 # Avoid same T if not condensing
                        
                        Tc_in_hu_u = final_Tc_after_sws_recovery[j_cold_util_loop] # Temp of cs_util before this heater
                        Tc_out_hu_u = cs_util.Tout_target

                        # EMAT checks for this specific pairing
                        emat_ok = True
                        if Th_in_hu_u < Tc_out_hu_u + EMAT - 1e-3: emat_ok = False
                        if Th_out_hu_u < Tc_in_hu_u + EMAT - 1e-3: emat_ok = False # Requires knowing Th_out_hu_u if not fixed

                        if emat_ok:
                            lmtd_hu_u = self._calculate_lmtd(Th_in_hu_u, Th_out_hu_u, Tc_in_hu_u, Tc_out_hu_u)
                            U_hu_u = hu_candidate.U # U specific to this utility type
                            area_hu_u = 1e9
                            if U_hu_u > 1e-9 and lmtd_hu_u > 1e-9:
                                area_hu_u = Q_heater_val / (U_hu_u * lmtd_hu_u)
                            if area_hu_u < 0: area_hu_u = 1e9
                            
                            current_heater_capital = hu_candidate.fix_cost + hu_candidate.area_cost_coeff * (area_hu_u ** hu_candidate.area_cost_exp)
                            current_heater_op = hu_candidate.cost * Q_heater_val
                            current_total_impact = current_heater_capital + current_heater_op

                            if current_total_impact < min_incremental_cost_for_this_heater:
                                min_incremental_cost_for_this_heater = current_total_impact
                                best_hu_obj_for_this_need = hu_candidate
                                best_heater_capital_cost = current_heater_capital
                                best_heater_op_cost_for_this_Q = current_heater_op
                                best_heater_details = {'type': 'heater', 'C_idx': j_cold_util_loop, 'Q': Q_heater_val, 
                                                    'Area': area_hu_u, 'Tc_in': Tc_in_hu_u, 'Tc_out': Tc_out_hu_u,
                                                    'util_Tin':Th_in_hu_u, 'util_Tout':Th_out_hu_u, 'Util_ID': hu_candidate.id}
                        else: # EMAT not ok
                            print(f" infeasible to assign hot utility to {cs_util.id} with heater {hu_candidate.id}")
                    
                    if best_hu_obj_for_this_need:
                        # print(f"  {hu_candidate.id} is assigned to {cs_util.id} with Q={Q_heater_val}")
                        Q_hot_consumed_kW_actual += Q_heater_val
                        capital_cost_heaters += best_heater_capital_cost
                        annual_hot_utility_op_cost += best_heater_op_cost_for_this_Q # This is already best_hu_obj.cost * Q_heater_val
                        exchanger_details_list.append(best_heater_details)
                        final_outlet_Tc_after_utility[j_cold_util_loop] = Tc_in_hu_u + Q_heater_val / cs_util.CP
                    else: # No feasible hot utility found for this duty
                        penalty_unmet_targets += target_temp_penalty_factor * Q_heater_val # Penalize by Q needed
                        
        for i_target_check in range(NH):
            hs_target = self.problem.hot_streams[i_target_check]
            # Use final_outlet_Th_after_utility which reflects temps after any utility cooling
            if abs(final_outlet_Th_after_utility[i_target_check] - hs_target.Tout_target) > temp_tolerance:
                penalty_unmet_targets += target_temp_penalty_factor * abs(final_outlet_Th_after_utility[i_target_check] - hs_target.Tout_target)
        for j_target_check in range(NC):
            cs_target = self.problem.cold_streams[j_target_check]
            if abs(final_outlet_Tc_after_utility[j_target_check] - cs_target.Tout_target) > temp_tolerance:
                penalty_unmet_targets += target_temp_penalty_factor * abs(final_outlet_Tc_after_utility[j_target_check] - cs_target.Tout_target)

        # Pinch Deviation Penalty
        if hasattr(self.problem, 'Q_H_min_pinch') and self.problem.Q_H_min_pinch is not None:
            if Q_hot_consumed_kW_actual > self.problem.Q_H_min_pinch + 1e-3 : penalty_pinch_deviation += self.pinch_deviation_penalty_factor * (Q_hot_consumed_kW_actual - self.problem.Q_H_min_pinch)
        if hasattr(self.problem, 'Q_C_min_pinch') and self.problem.Q_C_min_pinch is not None:
            if Q_cold_consumed_kW_actual > self.problem.Q_C_min_pinch + 1e-3: penalty_pinch_deviation += self.pinch_deviation_penalty_factor * (Q_cold_consumed_kW_actual - self.problem.Q_C_min_pinch)
        
        total_annual_capital_cost = capital_cost_process_exchangers + capital_cost_heaters + capital_cost_coolers
        total_annual_operating_cost = annual_hot_utility_op_cost + annual_cold_utility_op_cost
        total_penalty_applied_to_ga = penalty_EMAT + penalty_unmet_targets + penalty_pinch_deviation
        TAC_for_GA = total_annual_capital_cost + (total_annual_operating_cost * self.utility_cost_factor) + total_penalty_applied_to_ga
        true_TAC_report = total_annual_capital_cost + total_annual_operating_cost + (penalty_EMAT + penalty_unmet_targets)
        detailed_costs = {
            "TAC_GA_optimizing": TAC_for_GA, "TAC_true_report": true_TAC_report,
            "capital_process_exchangers": capital_cost_process_exchangers, "capital_heaters": capital_cost_heaters,
            "capital_coolers": capital_cost_coolers, "op_cost_hot_utility": annual_hot_utility_op_cost,
            "op_cost_cold_utility": annual_cold_utility_op_cost, "total_capital_cost": total_annual_capital_cost,
            "total_operating_cost": total_annual_operating_cost, "penalty_EMAT_etc": penalty_EMAT, 
            "penalty_unmet_targets": penalty_unmet_targets, "penalty_pinch_deviation": penalty_pinch_deviation,
            "penalty_total_in_GA_TAC": total_penalty_applied_to_ga,
            "Q_hot_consumed_kW_actual": Q_hot_consumed_kW_actual, # For GA-level pinch penalty
            "Q_cold_consumed_kW_actual": Q_cold_consumed_kW_actual # For GA-level pinch penalty
        }
        return detailed_costs, exchanger_details_list

    # Crossover and Mutation need to handle the new concatenated chromosome parts
    def _crossover(self, parent1_chromo, parent2_chromo):
        offspring1 = parent1_chromo.copy()
        offspring2 = parent2_chromo.copy()

        if random.random() < self.crossover_prob:
            # Simple single-point crossover on the whole chromosome for now
            # More sophisticated: separate crossover for Z, R_hot, R_cold parts
            size = len(parent1_chromo)
            if size > 1:
                cx_pt = random.randint(1, size - 1)
                offspring1 = np.concatenate((parent1_chromo[:cx_pt], parent2_chromo[cx_pt:]))
                offspring2 = np.concatenate((parent2_chromo[:cx_pt], parent1_chromo[cx_pt:]))
        return offspring1, offspring2

    def _mutation(self, chromosome):
        mutated_chromosome = chromosome.copy()
        
        # Mutate Z part (bit-flip)
        for i in range(self.len_Z):
            if random.random() < self.mutation_prob_Z:
                mutated_chromosome[i] = 1 - mutated_chromosome[i]
        
        # Mutate R_hot_splits part (Gaussian noise, ensure positive)
        for i in range(self.len_Z, self.len_Z + self.len_R_hot_splits):
            if random.random() < self.mutation_prob_R:
                # Add scaled Gaussian noise, ensuring result is positive
                current_val = mutated_chromosome[i]
                std_dev = max(1e-3, abs(current_val * self.r_mutation_std_dev_factor)) # Avoid 0 std dev
                noise = random.gauss(0, std_dev)
                mutated_chromosome[i] = max(1e-6, current_val + noise) # Ensure positive

        # Mutate R_cold_splits part
        for i in range(self.len_Z + self.len_R_hot_splits, self.chromosome_length):
            if random.random() < self.mutation_prob_R:
                current_val = mutated_chromosome[i]
                std_dev = max(1e-3, abs(current_val * self.r_mutation_std_dev_factor))
                noise = random.gauss(0, std_dev)
                mutated_chromosome[i] = max(1e-6, current_val + noise)
                
        return mutated_chromosome
    
    # ... (run method and _selection method from previous version, ensuring they use the 'costs' dict properly) ...
    # (Ensure these are complete from your fully working version)
    def run(self, run_id_for_print=""):
        # ... (run method as previously provided, ensuring it correctly handles the 'costs' dictionary for TAC_GA_optimizing and TAC_true_report)
        if self.random_seed is not None:
            random.seed(self.random_seed)
            np.random.seed(self.random_seed)
            
        self._initialize_population()
        best_chromosome_overall = None
        best_costs_overall_dict = {"TAC_GA_optimizing": float('inf'), "TAC_true_report": float('inf')}
        best_details_overall = None
        print_prefix = f"Run {run_id_for_print} - " if run_id_for_print else ""
        log_best_true_tac_per_gen = []
        log_avg_true_tac_per_gen = []
        log_best_ga_tac_per_gen = []
        log_avg_ga_tac_per_gen = []
        for gen in range(self.generations):
            current_population_evaluations = []
            gen_true_tacs = []
            gen_ga_tacs = []
            for chromo in self.population:
                try:
                    costs_dict, details = self._calculate_fitness(chromo)
                    current_population_evaluations.append({'chromosome': chromo, 'costs': costs_dict, 'details': details})
                    if costs_dict.get("TAC_true_report", float('inf')) != float('inf'):
                        gen_true_tacs.append(costs_dict["TAC_true_report"])
                    if costs_dict.get("TAC_GA_optimizing", float('inf')) != float('inf'):
                        gen_ga_tacs.append(costs_dict["TAC_GA_optimizing"])
                except Exception as e:
                    error_costs = {"TAC_GA_optimizing": float('inf'), "TAC_true_report": float('inf'),"total_capital_cost": float('inf'), "total_operating_cost": float('inf'),"penalty_EMAT_etc": float('inf'), "penalty_pinch_deviation": float('inf'), "penalty_unmet_targets": float('inf')}
                    current_population_evaluations.append({'chromosome': chromo, 'costs': error_costs, 'details': []})
            
            # Sort current population evaluations by GA optimizing TAC
            current_population_evaluations.sort(key=lambda x: x['costs']['TAC_GA_optimizing'])
            best_ga_tac_this_gen = float('inf')
            best_true_tac_this_gen = float('inf')
            # If there are evaluations, get the best TACs
            if current_population_evaluations:
                best_ga_tac_this_gen = current_population_evaluations[0]['costs']['TAC_GA_optimizing']
                best_true_tac_this_gen = current_population_evaluations[0]['costs']['TAC_true_report']
            
            # Check if this generation's best is better than overall best
            if best_ga_tac_this_gen < best_costs_overall_dict['TAC_GA_optimizing']:
                # Update overall best
                best_costs_overall_dict = copy.deepcopy(current_population_evaluations[0]['costs'])
                best_chromosome_overall = current_population_evaluations[0]['chromosome'].copy()
                best_details_overall = current_population_evaluations[0]['details']
            # Log best and average TACs for this generation
            avg_true_tac_this_gen = np.mean(gen_true_tacs) if gen_true_tacs else float('inf')
            avg_ga_tac_this_gen = np.mean(gen_ga_tacs) if gen_ga_tacs else float('inf')
            log_best_true_tac_per_gen.append(best_costs_overall_dict['TAC_true_report'])
            log_avg_true_tac_per_gen.append(avg_true_tac_this_gen)
            log_best_ga_tac_per_gen.append(best_costs_overall_dict['TAC_GA_optimizing'])
            log_avg_ga_tac_per_gen.append(avg_ga_tac_this_gen)
            # Enhanced Print
            overall_best_true_str = f"{best_costs_overall_dict['TAC_true_report']:.2f}" if best_costs_overall_dict['TAC_true_report']!=float('inf') else "Inf"
            overall_best_ga_str = f"{best_costs_overall_dict['TAC_GA_optimizing']:.2f}" if best_costs_overall_dict['TAC_GA_optimizing']!=float('inf') else "Inf"
            gen_best_true_str = f"{best_true_tac_this_gen:.2f}" if best_true_tac_this_gen!=float('inf') else "Inf"
            gen_avg_true_str = f"{avg_true_tac_this_gen:.2f}" if avg_true_tac_this_gen!=float('inf') else "Inf"
            gen_best_ga_str = f"{best_ga_tac_this_gen:.2f}" if best_ga_tac_this_gen!=float('inf') else "Inf"
            gen_avg_ga_str = f"{avg_ga_tac_this_gen:.2f}" if avg_ga_tac_this_gen!=float('inf') else "Inf"
            # Print the generation summary
            # print(f"{print_prefix}Gen {gen+1:03d}/{self.generations} - Best True TAC (Overall): {overall_best_true_str}, Best GA TAC (Overall): {overall_best_ga_str} | Gen Best True: {gen_best_true_str}, Gen Avg True: {gen_avg_true_str}, Gen Best GA: {gen_best_ga_str}, Gen Avg GA: {gen_avg_ga_str}")
            print(f"{print_prefix}Gen {gen+1:03d}/{self.generations} - Best True TAC (Overall): {overall_best_true_str}, Best GA TAC (Overall): {overall_best_ga_str}")
            
            # Prepare for next generation
            new_population = []
            
            # Elitism: Keep the best chromosomes from the current population
            # Ensure we don't exceed population size
            if current_population_evaluations:
                for i in range(min(self.elitism_count, len(current_population_evaluations))):
                    new_population.append(current_population_evaluations[i]['chromosome'].copy())
            
            # If no evaluations, reinitialize population
            if not current_population_evaluations:
                self._initialize_population()
                continue
            
            # Selection and Crossover
            # Use the selection method to get indices of parents
            # Ensure we have enough parents selected for crossover
            selected_parent_indices = self._selection(current_population_evaluations)
            
            # Generate Offspring
            num_offspring_to_generate = self.population_size - len(new_population)
            # print(f"{print_prefix}Generating {num_offspring_to_generate} offspring from selected parents...")
            children_generated = 0
            idx_for_selection = 0
            if not selected_parent_indices or not current_population_evaluations:
                while children_generated < num_offspring_to_generate:
                    new_population.append(self._create_random_full_chromosome())
                    children_generated += 1
            else:
                while children_generated < num_offspring_to_generate:
                    # Select two parents from the selected indices
                    parent1_idx = selected_parent_indices[idx_for_selection % len(selected_parent_indices)]
                    idx_for_selection += 1
                    parent2_idx = selected_parent_indices[idx_for_selection % len(selected_parent_indices)]
                    idx_for_selection += 1
                    parent1 = current_population_evaluations[parent1_idx]['chromosome']
                    parent2 = current_population_evaluations[parent2_idx]['chromosome']
                    # Crossover to create offspring
                    offspring1, offspring2 = self._crossover(parent1, parent2)
                    # Mutation of offspring
                    mutated_offspring1 = self._mutation(offspring1)
                    mutated_offspring2 = self._mutation(offspring2)
                    if children_generated < num_offspring_to_generate:
                        new_population.append(mutated_offspring1)
                        children_generated += 1
                    if children_generated < num_offspring_to_generate:
                        new_population.append(mutated_offspring2)
                        children_generated += 1
            self.population = new_population
            
            # Ensure population size is maintained
            if len(self.population) != self.population_size:
                while len(self.population) < self.population_size:
                    self.population.append(self._create_random_full_chromosome())
                self.population = self.population[:self.population_size]
        return best_chromosome_overall, best_costs_overall_dict, best_details_overall

    def _create_random_full_chromosome(self): # Helper for padding population
        z_part = np.random.randint(0, 2, size=self.len_Z)
        r_hot_part = np.random.uniform(0.01, 1.0, size=self.len_R_hot_splits)
        r_cold_part = np.random.uniform(0.01, 1.0, size=self.len_R_cold_splits)
        return np.concatenate((z_part, r_hot_part, r_cold_part))

    def _selection(self, current_population_evaluations): # Expects list of dicts
        raw_fitness = []
        for item in current_population_evaluations:
            ga_tac = item['costs'].get('TAC_GA_optimizing', float('inf'))
            raw_fitness.append(1.0 / (ga_tac + 1e-9))
        total_fitness = sum(raw_fitness)
        if total_fitness < 1e-9 or total_fitness == float('inf') or np.isnan(total_fitness):
            return [random.choice(range(len(current_population_evaluations))) for _ in range(len(current_population_evaluations))]
        probabilities = [f / total_fitness for f in raw_fitness]
        if np.isnan(probabilities).any() or np.isinf(probabilities).any() or abs(sum(probabilities) - 1.0) > 1e-5 :
             probabilities = np.ones(len(current_population_evaluations)) / len(current_population_evaluations)
        num_to_select = len(current_population_evaluations)
        try:
            selected_indices = np.random.choice(len(current_population_evaluations), size=num_to_select, p=probabilities, replace=True)
        except ValueError as e:
            probabilities = np.ones(len(current_population_evaluations)) / len(current_population_evaluations)
            selected_indices = np.random.choice(len(current_population_evaluations), size=num_to_select, p=probabilities, replace=True)
        return selected_indices.tolist()
    
def main(streams_file="streams.csv", utilities_file="utilities.csv", matches_U_file=None, EMAT_setting=3.0, ga_population_size=200, ga_generations=200, ga_crossover_prob=0.85, ga_mutation_prob_Z_setting=0.1, ga_mutation_prob_R_setting=0.1,
         ga_r_mutation_std_dev_factor_setting=0.1, ga_elitism_count=None, ga_elitism_frac=None, ga_utility_cost_factor=1.0, ga_pinch_dev_penalty_factor=150.0, sws_max_iter=200, sws_conv_tol=0.0001, number_of_runs=8):
    # ... (load_data_from_csv, adapt data to Stream, Utility, CostParameters, HENProblem - as before) ...
    print("HEN Synthesis using Genetic Algorithm with CSV Data Loading & Evolving Splits")
    loaded_hot_streams_data, loaded_cold_streams_data, loaded_hot_utilities_data, loaded_cold_utilities_data, loaded_matches_U = load_data_from_csv(streams_file, utilities_file, matches_U_file)
    
    # If no streams loaded
    if loaded_hot_streams_data is None:
        exit()
    
    hot_streams_obj_list = []
    default_stream_h_coeff = 0
    for s_data in loaded_hot_streams_data:
        hot_streams_obj_list.append(Stream(id_val=s_data['Name'], Tin=s_data['TIN_spec'], Tout_target=s_data['TOUT_spec'],CP=s_data['Fcp'], h_coeff=default_stream_h_coeff, stream_type='hot'))
    
    cold_streams_obj_list = []
    for s_data in loaded_cold_streams_data:
        cold_streams_obj_list.append(Stream(id_val=s_data['Name'], Tin=s_data['TIN_spec'], Tout_target=s_data['TOUT_spec'],CP=s_data['Fcp'], h_coeff=default_stream_h_coeff, stream_type='cold'))
    
    primary_hot_utility_obj_list = []
    if loaded_hot_utilities_data:
        for hu_data in loaded_hot_utilities_data:
            primary_hot_utility_obj_list.append(Utility(id_val=hu_data['Name'], Tin=hu_data['TIN_utility'], Tout=hu_data['TOUT_utility'],h_coeff=0, U=hu_data['U_overall'], cost_per_energy_unit=hu_data['Unit_Cost_Energy'], fix_cost=hu_data['Fixed_Cost_Unit'], area_cost_coeff=hu_data['Area_Cost_Coeff'], area_cost_exp=hu_data['Area_Cost_Exp'], utility_type='hot_utility'))
    else:
        primary_hot_utility_obj_list.append(Utility("DefaultHU", 500, 499, 1.0, 1.0, 999, 0, 1200, 0.6, "hot_utility"))
    
    primary_cold_utility_obj_list = []
    if loaded_cold_utilities_data:
        for cu_data in loaded_cold_utilities_data:
            primary_cold_utility_obj_list.append(Utility(id_val=cu_data['Name'], Tin=cu_data['TIN_utility'], Tout=cu_data['TOUT_utility'],h_coeff=0, U=cu_data['U_overall'], cost_per_energy_unit=cu_data['Unit_Cost_Energy'], fix_cost=cu_data['Fixed_Cost_Unit'],area_cost_coeff=cu_data['Area_Cost_Coeff'], area_cost_exp=cu_data['Area_Cost_Exp'], utility_type='cold_utility'))
    else:
        primary_cold_utility_obj_list = Utility("DefaultCU", 290, 300, 1.0, 1.0, 999, 0, 1000, 0.6, "cold_utility")
    
    U_process_default_setting = 0.8
    CF_process_setting = 0
    C_area_process_setting = 1000
    B_exp_process_setting = 0.6
    heater_fixed_cost = loaded_hot_utilities_data[0]['Fixed_Cost_Unit'] if loaded_hot_utilities_data else 0
    heater_area_coeff = loaded_hot_utilities_data[0]['Area_Cost_Coeff'] if loaded_hot_utilities_data else 0
    heater_area_exp = loaded_hot_utilities_data[0]['Area_Cost_Exp'] if loaded_hot_utilities_data else 0.6
    cooler_fixed_cost = loaded_cold_utilities_data[0]['Fixed_Cost_Unit'] if loaded_cold_utilities_data else 0
    cooler_area_coeff = loaded_cold_utilities_data[0]['Area_Cost_Coeff'] if loaded_cold_utilities_data else 0
    cooler_area_exp = loaded_cold_utilities_data[0]['Area_Cost_Exp'] if loaded_cold_utilities_data else 0.6
    
    cost_params_instance = CostParameters(exch_fixed=CF_process_setting,
                                          exch_area_coeff=C_area_process_setting,
                                          exch_area_exp=B_exp_process_setting,
                                          heater_fixed=heater_fixed_cost,
                                          heater_area_coeff=heater_area_coeff,
                                          heater_area_exp=heater_area_exp,
                                          cooler_fixed=cooler_fixed_cost,
                                          cooler_area_coeff=cooler_area_coeff,
                                          cooler_area_exp=cooler_area_exp,
                                          EMAT=EMAT_setting,
                                          U_overall=U_process_default_setting)
    
    num_stages_for_problem = max(1, len(hot_streams_obj_list), len(cold_streams_obj_list)) 
    
    if num_stages_for_problem == 0 and (hot_streams_obj_list or cold_streams_obj_list):
        num_stages_for_problem = 1
    if not hot_streams_obj_list and not cold_streams_obj_list:
        exit()
    
    hen_problem_instance = HENProblem(hot_streams_obj_list,
                                      cold_streams_obj_list,
                                      primary_hot_utility_obj_list,
                                      primary_cold_utility_obj_list,
                                      cost_params_instance,
                                      num_stages_for_problem,
                                      matches_U_cost=loaded_matches_U)

    if loaded_hot_utilities_data:
        hen_problem_instance.U_heaters.fill(loaded_hot_utilities_data[0]['U_overall'])
    if loaded_cold_utilities_data:
        hen_problem_instance.U_coolers.fill(loaded_cold_utilities_data[0]['U_overall'])
    
    print(f"\nPinch Analysis Results (EMAT={hen_problem_instance.cost_params.EMAT}K): Q_H_min: {hen_problem_instance.Q_H_min_pinch:.2f} kW, Q_C_min: {hen_problem_instance.Q_C_min_pinch:.2f} kW")
    
    if hen_problem_instance.T_pinch_hot_actual is not None:
        print(f"  T_Pinch_Hot: {hen_problem_instance.T_pinch_hot_actual:.2f} K, T_Pinch_Cold: {hen_problem_instance.T_pinch_cold_actual:.2f} K")

    # If ga_elitism_frac is povide
    if ga_elitism_frac is not None:
        ga_elitism_count = int(ga_elitism_frac * ga_population_size)
    elif ga_elitism_count is None and ga_elitism_frac is None:
        ga_elitism_count = 1
    else:
        ga_elitism_count = ga_elitism_count
        
    all_run_results = []
    base_seed = int(time.time())
    print(f"\n--- Starting {number_of_runs} GA Runs with EMAT = {EMAT_setting}K, Evolving Splits ---")
    for i in range(number_of_runs):
        current_seed = base_seed + i
        print(f"\n--- Running GA: Trial {i+1}/{number_of_runs} (Seed: {current_seed}) ---")
        ga_optimizer = GeneticAlgorithmHEN(problem=hen_problem_instance,
                                           population_size=ga_population_size,
                                           generations=ga_generations,
                                           crossover_prob=ga_crossover_prob,
                                           mutation_prob_Z=ga_mutation_prob_Z_setting,
                                           mutation_prob_R=ga_mutation_prob_R_setting,
                                           elitism_count=ga_elitism_count,
                                           random_seed=current_seed,
                                           utility_cost_factor=ga_utility_cost_factor,
                                           pinch_deviation_penalty_factor=ga_pinch_dev_penalty_factor,
                                           r_mutation_std_dev_factor=ga_r_mutation_std_dev_factor_setting,
                                           sws_max_iter=sws_max_iter,
                                           sws_conv_tol=sws_conv_tol
        )
        
        best_Z_chromo_part, best_costs_dict_run, best_details_run = ga_optimizer.run(run_id_for_print=f"{i+1} (Seed {current_seed})")
        # Note: best_Z_chromo_part is now the full chromosome (Z and R parts)
        all_run_results.append({'seed': current_seed, 'costs': best_costs_dict_run, 'chromosome': best_Z_chromo_part, 'details': best_details_run})
        
        current_run_true_tac = best_costs_dict_run.get('TAC_true_report', float('inf'))
        if current_run_true_tac == float('inf'):
            print(f"--- Finished Trial {i+1}/{number_of_runs} - Best True TAC: Inf ---")
        else:
            print(f"--- Finished Trial {i+1}/{number_of_runs} - Best True TAC: {current_run_true_tac:.2f} ---")

    # --- Summarize and Analyze Results ---
    # (The summary print section needs to be adapted to use 'chromosome' instead of 'Z' if you stored the full one,
    #  and then decode it again if printing the Z_ijk structure of the overall best.)
    print("\n\n--- Summary of Multiple GA Runs ---")
    if not all_run_results:
        print("No results to summarize.")
    else:
        best_overall_ga_tac = float('inf') 
        best_run_final_info = None   
        true_tac_values_from_runs = []

        for run_result in all_run_results:
            ga_tac = run_result['costs']['TAC_GA_optimizing']
            true_tac_for_display = run_result['costs']['TAC_true_report']

            # --- MODIFIED PRINT LOGIC ---
            ga_tac_str = f"{ga_tac:.2f}" if ga_tac != float('inf') else "Inf"
            true_tac_str = f"{true_tac_for_display:.2f}" if true_tac_for_display != float('inf') else "Inf"
            
            print(f"Run with Seed {run_result['seed']}: True TAC = {true_tac_str} (GA TAC = {ga_tac_str})")
            # --- END OF MODIFICATION ---
            
            if true_tac_for_display != float('inf'):
                true_tac_values_from_runs.append(true_tac_for_display)
            
            # Still compare based on ga_tac for finding the "best" run according to GA's objective
            if ga_tac < best_overall_ga_tac : 
                best_overall_ga_tac = ga_tac
                best_run_final_info = copy.deepcopy(run_result)

        # Overall best printout
        if best_run_final_info and best_run_final_info['costs']['TAC_GA_optimizing'] != float('inf'):
            overall_best_true_tac_val = best_run_final_info['costs']['TAC_true_report']
            overall_best_ga_tac_val = best_run_final_info['costs']['TAC_GA_optimizing']

            true_tac_overall_str = f"{overall_best_true_tac_val:.2f}" if overall_best_true_tac_val != float('inf') else "Inf"
            ga_tac_overall_str = f"{overall_best_ga_tac_val:.2f}" if overall_best_ga_tac_val != float('inf') else "Inf"

            print(f"\nBest True TAC found across all runs (corresponding to best GA TAC): {true_tac_overall_str}")
            print(f"  (This solution had a GA-Optimized TAC of: {ga_tac_overall_str})")
            print(f"Achieved with Seed: {best_run_final_info['seed']}")
            
            costs_to_print = best_run_final_info['costs']
            # ... (rest of your detailed cost breakdown and structure printout) ...
            print("\nCost Breakdown for the Best Overall Solution (based on True TAC of best GA solution):")
            print(f"  True TAC: {costs_to_print['TAC_true_report']:.2f}, GA Opt TAC: {costs_to_print['TAC_GA_optimizing']:.2f}")
            # ... (continue with other cost components)
            print(f"  CapEx (Proc): {costs_to_print.get('capital_process_exchangers',0):.2f}, CapEx (H): {costs_to_print.get('capital_heaters',0):.2f}, CapEx (C): {costs_to_print.get('capital_coolers',0):.2f}")
            print(f"  OpEx (HotU): {costs_to_print.get('op_cost_hot_utility',0):.2f}, OpEx (ColdU): {costs_to_print.get('op_cost_cold_utility',0):.2f}")
            print(f"  Penalty (EMAT): {costs_to_print.get('penalty_EMAT_etc',0):.2f}, Penalty (Pinch): {costs_to_print.get('penalty_pinch_deviation',0):.2f}")

            # ... (Structure and unit details printout)
            print("\nStructure of the absolute best run:")
            full_chromosome_best = best_run_final_info['chromosome']
            # You'll need an instance of GA to decode if _decode_chromosome is not static
            # Or pass the lengths needed for decoding. For simplicity, assuming you might re-instance or have access.
            # If ga_optimizer is the last one from the loop:
            if 'ga_optimizer' in locals() and ga_optimizer is not None:
                 Z_overall_best, _, _ = ga_optimizer._decode_chromosome(full_chromosome_best)
                 details_overall = best_run_final_info['details']
                 if Z_overall_best is not None:
                    active_matches = np.argwhere(Z_overall_best == 1)
                    # ... (the rest of your existing structure print)
                    if active_matches.size > 0:
                        for match in active_matches:
                            continue
                            q_val_for_match = 0
                            if details_overall:
                                for detail_item in details_overall:
                                    if detail_item.get('H') == match[0] and detail_item.get('C') == match[1] and detail_item.get('k') == match[2]:
                                        q_val_for_match = detail_item.get('Q',0); break
                            if q_val_for_match > 1e-6 :
                                print(f"  Match: H{match[0]+1} ({hen_problem_instance.hot_streams[match[0]].id}) - C{match[1]+1} ({hen_problem_instance.cold_streams[match[1]].id}) at Stage {match[2]+1} (Q={q_val_for_match:.2f} kW)")
                    else: print("  No active process-process matches with Q > 0.")
                 # ... (Detailed printout of exchangers and utilities as before, using details_overall)
                 if details_overall:
                    total_Q_recovered = 0
                    total_area_process_exch = 0
                    Q_hot_util_op_val = 0
                    Q_cold_util_op_val = 0
                    print("\n  Process Heat Exchangers:"); 
                    for detail in details_overall:
                        if 'H' in detail and 'C' in detail:
                            hot_name = hen_problem_instance.hot_streams[detail['H']].id
                            cold_name = hen_problem_instance.cold_streams[detail['C']].id
                            hot_CFp = detail['Q'] / abs(detail['Th_in'] - detail['Th_out'])
                            hot_Split_ratio = hot_CFp / hen_problem_instance.hot_streams[detail['H']].CP
                            cold_CFp = detail['Q'] / abs(detail['Tc_in'] - detail['Tc_out'])
                            cold_Split_ratio = cold_CFp / hen_problem_instance.cold_streams[detail['C']].CP
                            print(f"    H{detail['H']+1}({hot_name})-C{detail['C']+1}({cold_name}) (S{detail['k']+1}): Q={detail['Q']:.2f}, A={detail['Area']:.2f}")
                            print(f"    - Hot stream: CFp = {hot_CFp:.2f} (SP = {hot_Split_ratio:.2f}), Th_in={detail['Th_in']:.1f}, Th_out={detail['Th_out']:.1f}")
                            print(f"    - Cold stream: CFp = {cold_CFp:.2f} (SP = {cold_Split_ratio:.2f}), Tc_in={detail['Tc_in']:.1f}, Tc_out={detail['Tc_out']:.1f}")
                            total_Q_recovered += detail['Q']
                            total_area_process_exch += detail['Area']
                    print(f"  Total Q_recovered: {total_Q_recovered:.2f} kW, Total Process Area: {total_area_process_exch:.2f} m^2")
                    
                    print("\n  Utility Units:")
                    for detail in details_overall:
                        if detail.get('type') == 'heater':
                            print(f"    Heater for C{detail['C_idx']+1}({hen_problem_instance.cold_streams[detail['C_idx']].id}): Q={detail['Q']:.2f}, A={detail['Area']:.2f}, Tc_in={detail['Tc_in']:.1f}, Tc_out={detail['Tc_out']:.1f}")
                            Q_hot_util_op_val += detail['Q']
                        elif detail.get('type') == 'cooler':
                            print(f"    Cooler for H{detail['H_idx']+1}({hen_problem_instance.hot_streams[detail['H_idx']].id}): Q={detail['Q']:.2f}, A={detail['Area']:.2f}, Th_in={detail['Th_in']:.1f}, Th_out={detail['Th_out']:.1f}")
                            Q_cold_util_op_val += detail['Q']
                    
                    if Q_hot_util_op_val > 1e-6 or Q_cold_util_op_val > 1e-6:
                        print(f"\nUtility Summary:")
                        if Q_cold_util_op_val > 1e-6:
                            print(f"  Total Cold Utility (Op): {Q_cold_util_op_val:.2f} kW")
                        else:
                            print(f"  Not require Cold Utility.")    
                        if Q_hot_util_op_val > 1e-6:
                            print(f"  Total Hot Utility (Op): {Q_hot_util_op_val:.2f} kW")
                        else:
                            print(f"  Not require Hot Utility.")
                    else:
                        print(f"\nNo Utility Required.")

        else:
            print("\nNo valid (finite GA TAC) best solution found across all runs.")

# --- Main Execution Block ---
# (Needs to be updated to pass new GA parameters like mutation_prob_R, r_mutation_std_dev_factor)
if __name__ == "__main__":
    main(streams_file="streams.csv",
         utilities_file="utilities.csv",
         matches_U_file="matches_U_cost.csv",
         EMAT_setting=3.0,
         ga_population_size=200,
         ga_generations=200,
         ga_crossover_prob=0.85,
         ga_mutation_prob_Z_setting=0.1,
         ga_mutation_prob_R_setting=0.1,
         ga_r_mutation_std_dev_factor_setting=0.1,
         ga_elitism_frac=0.1,
         ga_utility_cost_factor=1.0,
         ga_pinch_dev_penalty_factor=150.0,
         sws_max_iter=300,
         sws_conv_tol=0.00001,
         number_of_runs=5)
    