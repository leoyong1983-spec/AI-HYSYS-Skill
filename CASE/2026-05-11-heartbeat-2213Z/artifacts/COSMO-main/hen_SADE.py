import numpy as np
import random
import math
import csv
import time
import copy
# (Import csv and time if used directly within HENProblem, but likely not needed here)

class Stream:
    def __init__(self, id_val, Tin, Tout_target, CP, h_coeff, stream_type):
        self.id = id_val; self.Tin = Tin; self.Tout_target = Tout_target; self.CP = CP; self.h = h_coeff; self.type = stream_type

class Utility:
    def __init__(self, id_val, Tin, Tout, h_coeff, cost_per_energy_unit, utility_type):
        self.id = id_val; self.Tin = Tin; self.Tout = Tout; self.h = h_coeff; self.cost = cost_per_energy_unit; self.type = utility_type

class CostParameters:
    def __init__(self, exch_fixed, exch_area_coeff, exch_area_exp, heater_fixed, heater_area_coeff, heater_area_exp, cooler_fixed, cooler_area_coeff, cooler_area_exp, EMAT, U_overall=None):
        self.exch_fixed = exch_fixed; self.exch_area_coeff = exch_area_coeff; self.exch_area_exp = exch_area_exp; self.heater_fixed = heater_fixed; self.heater_area_coeff = heater_area_coeff; self.heater_area_exp = heater_area_exp; self.cooler_fixed = cooler_fixed; self.cooler_area_coeff = cooler_area_coeff; self.cooler_area_exp = cooler_area_exp; self.EMAT = EMAT; self.U_overall = U_overall

class HENProblem:
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
        
        # --- Your existing U value calculation logic ---
        if self.cost_params.U_overall is None: 
            for i in range(self.NH):
                for j in range(self.NC):
                    h_hot = self.hot_streams[i].h if self.hot_streams[i].h > 1e-9 else 1e9 
                    h_cold = self.cold_streams[j].h if self.cold_streams[j].h > 1e-9 else 1e9
                    if self.hot_streams[i].h <= 1e-9 or self.cold_streams[j].h <= 1e-9: 
                        self.U_matrix_process[i,j] = 1e-6 
                    else: self.U_matrix_process[i, j] = 1.0 / (1.0/h_hot + 1.0/h_cold)
            if self.hot_utility: 
                for j in range(self.NC):
                    h_hot_util = self.hot_utility.h if self.hot_utility.h > 1e-9 else 1e9
                    h_cold_stream = self.cold_streams[j].h if self.cold_streams[j].h > 1e-9 else 1e9
                    if self.hot_utility.h <=1e-9 or self.cold_streams[j].h <= 1e-9: self.U_heaters[j] = 1e-6
                    else: self.U_heaters[j] = 1.0 / (1.0/h_hot_util + 1.0/h_cold_stream)
            if self.cold_utility:
                for i in range(self.NH):
                    h_hot_stream = self.hot_streams[i].h if self.hot_streams[i].h > 1e-9 else 1e9
                    h_cold_util = self.cold_utility.h if self.cold_utility.h > 1e-9 else 1e9
                    if self.hot_streams[i].h <= 1e-9 or self.cold_utility.h <= 1e-9: self.U_coolers[i] = 1e-6
                    else: self.U_coolers[i] = 1.0 / (1.0/h_hot_stream + 1.0/h_cold_util)
        else: 
            self.U_matrix_process.fill(self.cost_params.U_overall)
            if self.hot_utility:
                for j_idx in range(self.NC):
                    if self.hot_utility.h > 1e-9 and self.cold_streams[j_idx].h > 1e-9: self.U_heaters[j_idx] = 1.0 / (1.0/self.hot_utility.h + 1.0/self.cold_streams[j_idx].h)
                    else: self.U_heaters[j_idx] = self.cost_params.U_overall
            if self.cold_utility:
                for i_idx in range(self.NH):
                    if self.hot_streams[i_idx].h > 1e-9 and self.cold_utility.h > 1e-9: self.U_coolers[i_idx] = 1.0 / (1.0/self.hot_streams[i_idx].h + 1.0/self.cold_utility.h)
                    else: self.U_coolers[i_idx] = self.cost_params.U_overall
        # --- End of U value calculation logic ---

        self.Q_H_min_pinch, self.Q_C_min_pinch, self.T_pinch_hot_actual, self.T_pinch_cold_actual = self._calculate_pinch_targets()

    def _calculate_lmtd(self, Th_in, Th_out, Tc_in, Tc_out): # LMTD is part of HENProblem
        delta_T1 = Th_in - Tc_out; delta_T2 = Th_out - Tc_in
        if delta_T1 <= 1e-6 or delta_T2 <= 1e-6:
             if abs(delta_T1 - delta_T2) < 1e-6 and delta_T1 > 1e-6 : return delta_T1
             return 1e-6 
        if abs(delta_T1 - delta_T2) < 1e-6: lmtd = (delta_T1 + delta_T2) / 2.0
        else: lmtd = (delta_T1 - delta_T2) / math.log(delta_T1 / delta_T2)
        if lmtd <= 1e-6: return 1e-6
        return lmtd

    def _calculate_pinch_targets(self):
        # ... (Your existing _calculate_pinch_targets method) ...
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
            T_h = sorted_temps[i]; T_l = sorted_temps[i+1]; delta_Tint = T_h - T_l
            if delta_Tint < 1e-6: continue
            sum_fcp_h = sum(hs.CP for hs in self.hot_streams if hs.Tin > T_l and hs.Tout_target < T_h)
            sum_fcp_c = sum(cs.CP for cs in self.cold_streams if (cs.Tout_target + EMAT) > T_l and (cs.Tin + EMAT) < T_h)
            delta_H_int = (sum_fcp_h - sum_fcp_c) * delta_Tint
            heat_cascade.append(heat_cascade[-1] + delta_H_int)
        q_h_min = max(0, -min(heat_cascade)) if min(heat_cascade) < -1e-6 else 0
        feasible_cascade = [q + q_h_min for q in heat_cascade]; q_c_min = feasible_cascade[-1]
        try: pinch_idx = feasible_cascade.index(min(feasible_cascade)) 
        except ValueError: pinch_idx = 0
        T_pinch_s = sorted_temps[pinch_idx]; t_ph = T_pinch_s; t_pc = T_pinch_s - EMAT
        return (abs(q_h_min) if abs(q_h_min) > 1e-6 else 0), (abs(q_c_min) if abs(q_c_min) > 1e-6 else 0), t_ph, t_pc

    # vvvvv  THIS IS WHERE THE NEW METHOD GOES vvvvv
    def run_sws_simulation_for_de(self, Z_ijk, Q_ijk_from_de, FH_ijk_from_de, FC_ijk_from_de):
        """
        Performs SWS simulation for a fixed Z_ijk topology, given Q_ijk, FH_ijk, and FC_ijk.
        Calculates temperatures, EMAT violations, areas, utility needs, costs.
        Returns: (TAC_physical_and_penalties, detailed_costs_dictionary, exchanger_details_list)
        """
        NH = self.NH; NC = self.NC; ST = self.num_stages
        EMAT = self.cost_params.EMAT
        
        # Cost parameters for process-process exchangers from self.cost_params
        CF_process = self.cost_params.exch_fixed
        C_area_process = self.cost_params.exch_area_coeff
        B_exp_process = self.cost_params.exch_area_exp
        
        # Utility objects from self
        hot_util_obj = self.hot_utility
        cold_util_obj = self.cold_utility

        capital_cost_process_exchangers = 0.0
        capital_cost_heaters = 0.0
        capital_cost_coolers = 0.0
        annual_hot_utility_op_cost = 0.0
        annual_cold_utility_op_cost = 0.0
        penalty_EMAT = 0.0
        penalty_unmet_targets = 0.0
        
        exchanger_details_list = []

        # SWS Temperature Iteration Loop (using GIVEN Q_ijk_from_de)
        T_mix_H_out_current = np.zeros((NH, ST))
        T_mix_C_out_current = np.zeros((NC, ST))
        # Initialize prev_iter temps. For the first pass of DE's SWS, these are effectively stage inlets
        T_mix_H_out_prev_iter = np.array([[hs.Tin for _ in range(ST)] for hs in self.hot_streams])
        T_mix_C_out_prev_iter = np.array([[cs.Tin for _ in range(ST)] for cs in self.cold_streams])
        
        MAX_SWS_ITER_DE = 20 # Max iterations for DE's SWS simulation
        SWS_CONV_TOL_DE = 0.1 # Convergence tolerance for DE's SWS

        for sws_iter in range(MAX_SWS_ITER_DE):
            T_mix_H_out_before_pass = T_mix_H_out_current.copy()
            T_mix_C_out_before_pass = T_mix_C_out_current.copy()
            
            # Hot Pass: Calculate T_mix_H_out_current based on Q_ijk_from_de
            for k_stage in range(ST):
                TinH_to_stage_k_matches = np.zeros(NH)
                for i_hs in range(NH):
                    TinH_to_stage_k_matches[i_hs] = T_mix_H_out_prev_iter[i_hs, k_stage-1] if k_stage > 0 else self.hot_streams[i_hs].Tin
                
                Q_sum_from_hot_stream_branches_at_k = np.zeros(NH)
                for i_hot in range(NH):
                    for j_cold in range(NC):
                        if Z_ijk[i_hot, j_cold, k_stage] == 1: # Use GA-provided Z_ijk
                            # Q for this match is GIVEN by DE
                            Q_sum_from_hot_stream_branches_at_k[i_hot] += Q_ijk_from_de[i_hot, j_cold, k_stage] 
                
                for i_hot_mixer in range(NH):
                    hs_m = self.hot_streams[i_hot_mixer]
                    if hs_m.CP > 1e-9:
                        T_mix_H_out_current[i_hot_mixer, k_stage] = TinH_to_stage_k_matches[i_hot_mixer] - Q_sum_from_hot_stream_branches_at_k[i_hot_mixer] / hs_m.CP
                    else:
                        T_mix_H_out_current[i_hot_mixer, k_stage] = TinH_to_stage_k_matches[i_hot_mixer]

            # Cold Pass: Calculate T_mix_C_out_current based on Q_ijk_from_de
            for k_stage in range(ST - 1, -1, -1):
                TinC_to_stage_k_matches = np.zeros(NC)
                for j_cs in range(NC):
                    TinC_to_stage_k_matches[j_cs] = T_mix_C_out_prev_iter[j_cs, k_stage+1] if k_stage < ST-1 else self.cold_streams[j_cs].Tin
                
                Q_sum_to_cold_stream_branches_at_k = np.zeros(NC)
                for j_cold in range(NC):
                    for i_hot in range(NH):
                        if Z_ijk[i_hot, j_cold, k_stage] == 1: # Use GA-provided Z_ijk
                            Q_sum_to_cold_stream_branches_at_k[j_cold] += Q_ijk_from_de[i_hot,j_cold,k_stage]
                                            
                for j_cold_mixer in range(NC):
                    cs_m = self.cold_streams[j_cold_mixer]
                    if cs_m.CP > 1e-9:
                        T_mix_C_out_current[j_cold_mixer, k_stage] = TinC_to_stage_k_matches[j_cold_mixer] + Q_sum_to_cold_stream_branches_at_k[j_cold_mixer] / cs_m.CP
                    else:
                        T_mix_C_out_current[j_cold_mixer, k_stage] = TinC_to_stage_k_matches[j_cold_mixer]

            # Convergence Check
            delta_H_conv = np.max(np.abs(T_mix_H_out_before_pass - T_mix_H_out_current)) if NH > 0 and ST > 0 else 0
            delta_C_conv = np.max(np.abs(T_mix_C_out_before_pass - T_mix_C_out_current)) if NC > 0 and ST > 0 else 0

            T_mix_H_out_prev_iter = T_mix_H_out_current.copy() # For next SWS iteration
            T_mix_C_out_prev_iter = T_mix_C_out_current.copy() # For next SWS iteration
            
            if delta_H_conv < SWS_CONV_TOL_DE and delta_C_conv < SWS_CONV_TOL_DE and sws_iter > 0 : 
                break
        
        # Calculate Areas and EMAT penalties using converged T_mix_..._current and Q_ijk_from_de
        for k_stage in range(ST):
            for i_hot in range(NH):
                hs = self.hot_streams[i_hot]
                for j_cold in range(NC):
                    cs = self.cold_streams[j_cold]
                    if Z_ijk[i_hot, j_cold, k_stage] == 1 and Q_ijk_from_de[i_hot, j_cold, k_stage] > 1e-6:
                        Q_ex = Q_ijk_from_de[i_hot, j_cold, k_stage]
                        Th_in_ex = T_mix_H_out_current[i_hot, k_stage-1] if k_stage > 0 else hs.Tin
                        Tc_in_ex = T_mix_C_out_current[j_cold, k_stage+1] if k_stage < ST-1 else cs.Tin
                        
                        CPH_b_ex = hs.CP * FH_ijk_from_de[i_hot, j_cold, k_stage] # Use splits from DE
                        CPC_b_ex = cs.CP * FC_ijk_from_de[i_hot, j_cold, k_stage] # Use splits from DE
                        
                        if CPH_b_ex < 1e-9 or CPC_b_ex < 1e-9: 
                            if Q_ex > 1e-3: penalty_EMAT += 1e8 # Q assigned but no flow
                            continue 

                        Th_out_ex = Th_in_ex - Q_ex / CPH_b_ex
                        Tc_out_ex = Tc_in_ex + Q_ex / CPC_b_ex

                        dTa_ex = Th_in_ex - Tc_out_ex; dTb_ex = Th_out_ex - Tc_in_ex
                        # Ensure penalty is positive
                        if dTa_ex < EMAT - 1e-3: penalty_EMAT += 1e7 * max(0, EMAT - dTa_ex)
                        if dTb_ex < EMAT - 1e-3: penalty_EMAT += 1e7 * max(0, EMAT - dTb_ex)
                        
                        lmtd_ex = self._calculate_lmtd(Th_in_ex, Th_out_ex, Tc_in_ex, Tc_out_ex) # Use self._calculate_lmtd
                        U_ex = self.U_matrix_process[i_hot, j_cold] # From HENProblem init
                        area_ex = 1e9
                        if U_ex > 1e-9 and lmtd_ex > 1e-9 : area_ex = Q_ex / (U_ex * lmtd_ex)
                        if area_ex < 0: area_ex = 1e9 ; penalty_EMAT += 1e7 # Negative area
                        
                        cost_ex = CF_process + C_area_process * (area_ex ** B_exp_process)
                        capital_cost_process_exchangers += cost_ex
                        exchanger_details_list.append({'H': i_hot, 'C': j_cold, 'k': k_stage, 'Q': Q_ex, 'Area': area_ex, 
                                                       'Th_in': Th_in_ex, 'Th_out': Th_out_ex, 
                                                       'Tc_in': Tc_in_ex, 'Tc_out': Tc_out_ex})
        
        # Utility Calculation & Final Target Check
        final_Th_after_all_stages = T_mix_H_out_current[:, ST-1] if ST > 0 else np.array([hs.Tin for hs in self.hot_streams])
        final_Tc_after_all_stages = T_mix_C_out_current[:, 0] if ST > 0 else np.array([cs.Tin for cs in self.cold_streams])
        final_outlet_Th_de = final_Th_after_all_stages.copy(); final_outlet_Tc_de = final_Tc_after_all_stages.copy()
        Q_hot_consumed_kW_de = 0.0; Q_cold_consumed_kW_de = 0.0

        if cold_util_obj:
            for i_hot_util in range(NH):
                hs_util = self.hot_streams[i_hot_util]; temp_before_cu = final_Th_after_all_stages[i_hot_util]
                if temp_before_cu > hs_util.Tout_target + 1e-3:
                    Q_cu_val = hs_util.CP * (temp_before_cu - hs_util.Tout_target)
                    if Q_cu_val > 1e-6 and hs_util.CP > 1e-9:
                        Q_cold_consumed_kW_de += Q_cu_val
                        Th_in_cu = temp_before_cu; Th_out_cu = hs_util.Tout_target
                        Tc_in_cu_u = cold_util_obj.Tin; Tc_out_cu_u = cold_util_obj.Tout if cold_util_obj.Tout is not None and cold_util_obj.Tout > Tc_in_cu_u else Tc_in_cu_u + 5 
                        if Th_in_cu < Tc_out_cu_u + EMAT - 1e-3: penalty_EMAT += 1e6 * max(0, Tc_out_cu_u + EMAT - Th_in_cu)
                        if Th_out_cu < Tc_in_cu_u + EMAT - 1e-3: penalty_EMAT += 1e6 * max(0, Tc_in_cu_u + EMAT - Th_out_cu)
                        lmtd_cu_u = self._calculate_lmtd(Th_in_cu, Th_out_cu, Tc_in_cu_u, Tc_out_cu_u); U_cu_u = self.U_coolers[i_hot_util]; area_cu_u = 1e9
                        if U_cu_u > 1e-9 and lmtd_cu_u > 1e-9: area_cu_u = Q_cu_val / (U_cu_u * lmtd_cu_u)
                        if area_cu_u < 0: area_cu_u = 1e9
                        cost_cu_u = self.cost_params.cooler_fixed + self.cost_params.cooler_area_coeff * (area_cu_u ** self.cost_params.cooler_area_exp)
                        capital_cost_coolers += cost_cu_u; annual_cold_utility_op_cost += cold_util_obj.cost * Q_cu_val 
                        exchanger_details_list.append({'type': 'cooler', 'H_idx': i_hot_util, 'Q': Q_cu_val, 'Area': area_cu_u, 'Th_in': Th_in_cu, 'Th_out': Th_out_cu, 'util_Tin': Tc_in_cu_u, 'util_Tout':Tc_out_cu_u})
                        final_outlet_Th_de[i_hot_util] = hs_util.Tout_target
        
        if hot_util_obj:
            for j_cold_util in range(NC):
                cs_util = self.cold_streams[j_cold_util]; temp_before_hu = final_Tc_after_all_stages[j_cold_util]
                if temp_before_hu < cs_util.Tout_target - 1e-3:
                    Q_hu_val = cs_util.CP * (cs_util.Tout_target - temp_before_hu)
                    if Q_hu_val > 1e-6 and cs_util.CP > 1e-9:
                        Q_hot_consumed_kW_de += Q_hu_val
                        Th_in_hu_u = hot_util_obj.Tin; Th_out_hu_u = hot_util_obj.Tout if hot_util_obj.Tout is not None and hot_util_obj.Tout < Th_in_hu_u else Th_in_hu_u -1
                        Tc_in_hu_u = temp_before_hu; Tc_out_hu_u = cs_util.Tout_target
                        if Th_in_hu_u < Tc_out_hu_u + EMAT - 1e-3: penalty_EMAT += 1e6 * max(0, Tc_out_hu_u + EMAT - Th_in_hu_u)
                        if Th_out_hu_u < Tc_in_hu_u + EMAT - 1e-3: penalty_EMAT += 1e6 * max(0, Tc_in_hu_u + EMAT - Th_out_hu_u)
                        lmtd_hu_u = self._calculate_lmtd(Th_in_hu_u, Th_out_hu_u, Tc_in_hu_u, Tc_out_hu_u); U_hu_u = self.U_heaters[j_cold_util]; area_hu_u = 1e9
                        if U_hu_u > 1e-9 and lmtd_hu_u > 1e-9: area_hu_u = Q_hu_val / (U_hu_u * lmtd_hu_u)
                        if area_hu_u < 0: area_hu_u = 1e9
                        cost_hu_u = self.cost_params.heater_fixed + self.cost_params.heater_area_coeff * (area_hu_u ** self.cost_params.heater_area_exp)
                        capital_cost_heaters += cost_hu_u; annual_hot_utility_op_cost += hot_util_obj.cost * Q_hu_val
                        exchanger_details_list.append({'type': 'heater', 'C_idx': j_cold_util, 'Q': Q_hu_val, 'Area': area_hu_u, 'Tc_in': Tc_in_hu_u, 'Tc_out': Tc_out_hu_u, 'util_Tin':Th_in_hu_u, 'util_Tout':Th_out_hu_u})
                        final_outlet_Tc_de[j_cold_util] = cs_util.Tout_target
        
        target_temp_penalty_factor_de = 1e7; temp_tolerance_de = 0.5
        for i in range(NH):
            if abs(final_outlet_Th_de[i] - self.hot_streams[i].Tout_target) > temp_tolerance_de:
                penalty_unmet_targets += target_temp_penalty_factor_de * abs(final_outlet_Th_de[i] - self.hot_streams[i].Tout_target)
        for j in range(NC):
            if abs(final_outlet_Tc_de[j] - self.cold_streams[j].Tout_target) > temp_tolerance_de:
                penalty_unmet_targets += target_temp_penalty_factor_de * abs(final_outlet_Tc_de[j] - self.cold_streams[j].Tout_target)

        total_capital_de = capital_cost_process_exchangers + capital_cost_heaters + capital_cost_coolers
        total_op_de = annual_hot_utility_op_cost + annual_cold_utility_op_cost
        total_physical_penalty_de = penalty_EMAT + penalty_unmet_targets

        tac_for_de_evaluation = total_capital_de + total_op_de + total_physical_penalty_de
        
        detailed_costs_for_de_evaluation = {
            "TAC_true_report": tac_for_de_evaluation, # This is the key TAC DE minimizes
            "capital_process_exchangers": capital_cost_process_exchangers,
            "capital_heaters": capital_cost_heaters,
            "capital_coolers": capital_cost_coolers,
            "op_cost_hot_utility": annual_hot_utility_op_cost,
            "op_cost_cold_utility": annual_cold_utility_op_cost,
            "Q_hot_consumed_kW_actual": Q_hot_consumed_kW_de,
            "Q_cold_consumed_kW_actual": Q_cold_consumed_kW_de,
            "total_capital_cost": total_capital_de,
            "total_operating_cost": total_op_de,
            "penalty_EMAT_etc": penalty_EMAT,
            "penalty_unmet_targets": penalty_unmet_targets
        }
        return tac_for_de_evaluation, detailed_costs_for_de_evaluation, exchanger_details_list
    # ^^^^^ END OF run_sws_simulation_for_de METHOD ^^^^^


# --- load_data_from_csv function (as previously defined) ---
# ... (ensure this is present in your script) ...
def load_data_from_csv(streams_filepath, utilities_filepath):
    loaded_hot_streams = []
    loaded_cold_streams = []
    loaded_hot_utilities = []
    loaded_cold_utilities = []

    # Load Streams
    try:
        with open(streams_filepath, mode='r', newline='') as sf: # File 'sf' is opened here
            reader = csv.DictReader(sf)
            if not reader.fieldnames:
                print(f"Error: Streams CSV file '{streams_filepath}' is empty or has no header.")
                return None, None, None, None
            
            expected_stream_cols = {'Name', 'Type', 'TIN_spec', 'TOUT_spec', 'Fcp'}
            missing_s_cols = expected_stream_cols - set(reader.fieldnames)
            if missing_s_cols:
                print(f"Error: Streams CSV '{streams_filepath}' missing one or more required columns: {missing_s_cols}")
                return None, None, None, None

            # vvvvv THIS LOOP MUST BE INSIDE THE 'with' BLOCK vvvvv
            for r_idx, row in enumerate(reader):
                try: 
                    stream_data = {
                        'Name': row['Name'],
                        'Type': row['Type'].strip().lower(),
                        'TIN_spec': float(row['TIN_spec']),
                        'TOUT_spec': float(row['TOUT_spec']),
                        'Fcp': float(row['Fcp'])
                    }
                    if stream_data['Type'] == 'hot':
                        loaded_hot_streams.append(stream_data)
                    elif stream_data['Type'] == 'cold':
                        loaded_cold_streams.append(stream_data)
                    else:
                        print(f"Warning: Unknown stream type '{row['Type']}' for stream '{row['Name']}' at row {r_idx+2}. Skipping.")
                except KeyError as e_key:
                    print(f"Error: Missing column {e_key} in streams.csv processing row {r_idx+2}. Row data: {row}")
                    # Continue to next row or decide to abort all loading
                except ValueError as e_val:
                    print(f"Error: Could not convert value to float in streams.csv at row {r_idx+2}. Details: {e_val}. Row data: {row}")
                    # Skip this row and continue
            # ^^^^^ END OF THE LOOP THAT MUST BE INSIDE THE 'with' BLOCK ^^^^^
    except FileNotFoundError:
        print(f"Error: Streams file not found at {streams_filepath}")
        return None, None, None, None
    except Exception as e_file: 
        print(f"Error reading streams CSV file '{streams_filepath}': {e_file}")
        return None, None, None, None

    # Load Utilities (apply the same fix here)
    try:
        with open(utilities_filepath, mode='r', newline='') as uf: # File 'uf' is opened
            reader = csv.DictReader(uf)
            if not reader.fieldnames:
                print(f"Error: Utilities CSV file '{utilities_filepath}' is empty or has no header.")
                # Return what might have been loaded from streams if successful
                return loaded_hot_streams, loaded_cold_streams, None, None
            
            expected_util_cols = {'Name', 'Type', 'TIN_utility', 'TOUT_utility', 'Unit_Cost_Energy', 
                                  'U_overall', 'Fixed_Cost_Unit', 'Area_Cost_Coeff', 'Area_Cost_Exp'}
            missing_u_cols = expected_util_cols - set(reader.fieldnames)
            if missing_u_cols:
                print(f"Error: Utilities CSV '{utilities_filepath}' missing one or more required columns: {missing_u_cols}")
                return loaded_hot_streams, loaded_cold_streams, None, None

            # vvvvv THIS LOOP MUST BE INSIDE THE 'with' BLOCK vvvvv
            for r_idx, row in enumerate(reader):
                try:
                    util_data = {
                        'Name': row['Name'],
                        'Type': row['Type'].strip().lower(),
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
                        print(f"Warning: Unknown utility type '{row['Type']}' for utility '{row['Name']}' at row {r_idx+2}. Skipping.")
                except KeyError as e_key:
                    print(f"Error: Missing column {e_key} in utilities.csv processing row {r_idx+2}. Row data: {row}")
                except ValueError as e_val:
                    print(f"Error: Could not convert value to float in utilities.csv at row {r_idx+2}. Details: {e_val}. Row data: {row}")
            # ^^^^^ END OF THE LOOP THAT MUST BE INSIDE THE 'with' BLOCK ^^^^^
    except FileNotFoundError:
        print(f"Error: Utilities file not found at {utilities_filepath}")
        return loaded_hot_streams, loaded_cold_streams, None, None
    except Exception as e_file:
        print(f"Error reading utilities CSV file '{utilities_filepath}': {e_file}")
        return loaded_hot_streams, loaded_cold_streams, None, None
        
    # Warnings for missing utilities (these are fine where they are)
    if not loaded_hot_utilities and any(s['Type'] == 'cold' for s in loaded_cold_streams if s): # Check if s is not None
        print("Warning: No hot utilities loaded from CSV, but cold streams exist. Heaters will use defaults or fail if no defaults.")
    if not loaded_cold_utilities and any(s['Type'] == 'hot' for s in loaded_hot_streams if s): # Check if s is not None
        print("Warning: No cold utilities loaded from CSV, but hot streams exist. Coolers will use defaults or fail if no defaults.")

    return loaded_hot_streams, loaded_cold_streams, loaded_hot_utilities, loaded_cold_utilities

# --- LowerLevelDEOptimizer Class (as provided in the previous response) ---
# ... (This class needs to be defined here. Ensure its _fitness_de calls self.problem.run_sws_simulation_for_de)
class LowerLevelDEOptimizer:
    def __init__(self, problem, fixed_topology_Z_ijk, pop_size_de, gens_de, F_mutation, CR_crossover, random_seed_de=None):
        self.problem = problem; self.fixed_Z_ijk = fixed_topology_Z_ijk; self.pop_size_de = pop_size_de; self.generations_de = gens_de; self.F = F_mutation; self.CR = CR_crossover

        if random_seed_de is not None:
            py_seed = int(random_seed_de)
            random.seed(py_seed)
            
            np_seed = py_seed % (2**32) # Ensure numpy seed is a valid 32-bit integer
            if np_seed < 0: np_seed += 2**32 # Ensure non-negative seed
            np.random.seed(np_seed)
        self.active_q_indices = []
        for r_ in range(self.problem.NH):
            for c_ in range(self.problem.NC):
                for s_idx_ in range(self.problem.num_stages):
                    if self.fixed_Z_ijk[r_,c_,s_idx_] == 1: self.active_q_indices.append((r_,c_,s_idx_))
        self.num_q_vars = len(self.active_q_indices)
        self.split_config = []; current_de_gene_idx = self.num_q_vars
        for k_stage_ in range(self.problem.num_stages):
            for i_hot_ in range(self.problem.NH):
                branches_ = [j_cold_ for j_cold_ in range(self.problem.NC) if self.fixed_Z_ijk[i_hot_, j_cold_, k_stage_] == 1]
                if len(branches_) > 1: self.split_config.append({'type': 'hot', 'stream_idx': i_hot_, 'stage_idx': k_stage_, 'branch_target_indices': branches_, 'num_r_genes': len(branches_), 'de_gene_start_idx': current_de_gene_idx}); current_de_gene_idx += len(branches_)
            for j_cold_ in range(self.problem.NC):
                branches_ = [i_hot_ for i_hot_ in range(self.problem.NH) if self.fixed_Z_ijk[i_hot_, j_cold_, k_stage_] == 1]
                if len(branches_) > 1: self.split_config.append({'type': 'cold', 'stream_idx': j_cold_, 'stage_idx': k_stage_, 'branch_target_indices': branches_, 'num_r_genes': len(branches_), 'de_gene_start_idx': current_de_gene_idx}); current_de_gene_idx += len(branches_)
        self.num_r_split_vars = current_de_gene_idx - self.num_q_vars; self.de_chromosome_length = self.num_q_vars + self.num_r_split_vars
        self.de_population = []; self.de_fitness = []
    def _initialize_de_population(self):
        self.de_population = []
        for _ in range(self.pop_size_de):
            de_chromo = np.zeros(self.de_chromosome_length)
            q_idx_chromo = 0
            for i_hot, j_cold, k_stage in self.active_q_indices:
                hs = self.problem.hot_streams[i_hot]; cs = self.problem.cold_streams[j_cold]
                max_q_h = hs.CP * abs(hs.Tin - hs.Tout_target); max_q_c = cs.CP * abs(cs.Tout_target - cs.Tin)
                q_upper_bound = min(max_q_h, max_q_c, 1e6) # Added a large practical upper bound
                de_chromo[q_idx_chromo] = random.uniform(0, q_upper_bound * 0.5) if q_upper_bound > 0 else 0
                q_idx_chromo +=1
            for split_info in self.split_config:
                for r_offset in range(split_info['num_r_genes']): de_chromo[split_info['de_gene_start_idx'] + r_offset] = random.uniform(0.01, 1.0)
            self.de_population.append(de_chromo)
    def _decode_de_chromosome(self, de_chromosome):
        Q_ijk_matrix = np.zeros((self.problem.NH, self.problem.NC, self.problem.num_stages)); FH_ijk = np.zeros((self.problem.NH, self.problem.NC, self.problem.num_stages)); FC_ijk = np.zeros((self.problem.NH, self.problem.NC, self.problem.num_stages))
        de_gene_idx = 0
        for i_hot, j_cold, k_stage in self.active_q_indices: Q_ijk_matrix[i_hot, j_cold, k_stage] = max(0, de_chromosome[de_gene_idx]); de_gene_idx += 1
        for split_detail in self.split_config:
            raw_r_values = de_chromosome[split_detail['de_gene_start_idx'] : split_detail['de_gene_start_idx'] + split_detail['num_r_genes']]; raw_r_values = np.maximum(1e-6, raw_r_values)
            sum_r = np.sum(raw_r_values); normalized_fractions = raw_r_values / sum_r if sum_r > 1e-6 else np.ones(split_detail['num_r_genes']) / split_detail['num_r_genes']
            s_idx = split_detail['stream_idx']; k_s = split_detail['stage_idx']
            if split_detail['type'] == 'hot':
                for branch_num, target_j in enumerate(split_detail['branch_target_indices']): FH_ijk[s_idx, target_j, k_s] = normalized_fractions[branch_num]
            elif split_detail['type'] == 'cold':
                for branch_num, target_i in enumerate(split_detail['branch_target_indices']): FC_ijk[target_i, s_idx, k_s] = normalized_fractions[branch_num]
        for k_s in range(self.problem.num_stages):
            for i_hot in range(self.problem.NH):
                if not any(sc['type']=='hot' and sc['stream_idx']==i_hot and sc['stage_idx']==k_s for sc in self.split_config):
                    active_matches = [j for j in range(self.problem.NC) if self.fixed_Z_ijk[i_hot,j,k_s]==1]
                    if len(active_matches) == 1: FH_ijk[i_hot, active_matches[0], k_s] = 1.0
            for j_cold in range(self.problem.NC):
                if not any(sc['type']=='cold' and sc['stream_idx']==j_cold and sc['stage_idx']==k_s for sc in self.split_config):
                    active_matches = [i for i in range(self.problem.NH) if self.fixed_Z_ijk[i,j_cold,k_s]==1]
                    if len(active_matches) == 1: FC_ijk[active_matches[0], j_cold, k_s] = 1.0
        return Q_ijk_matrix, FH_ijk, FC_ijk
    def _fitness_de(self, de_chromosome):
        Q_ijk_de, FH_ijk_de, FC_ijk_de = self._decode_de_chromosome(de_chromosome)
        tac_val, _, _ = self.problem.run_sws_simulation_for_de(self.fixed_Z_ijk, Q_ijk_de, FH_ijk_de, FC_ijk_de)
        return tac_val
    def run(self):
        if self.de_chromosome_length == 0: # No Q or Splits to optimize for this Z_ijk (e.g. no matches)
            empty_Q = np.zeros((self.problem.NH, self.problem.NC, self.problem.num_stages))
            empty_FH = np.zeros((self.problem.NH, self.problem.NC, self.problem.num_stages))
            empty_FC = np.zeros((self.problem.NH, self.problem.NC, self.problem.num_stages))
            return self.problem.run_sws_simulation_for_de(self.fixed_Z_ijk, empty_Q, empty_FH, empty_FC)

        self._initialize_de_population()
        self.de_fitness = [self._fitness_de(ind) for ind in self.de_population]
        best_overall_de_tac = min(self.de_fitness) if self.de_fitness else float('inf')
        if best_overall_de_tac != float('inf'): best_overall_de_chromo = self.de_population[self.de_fitness.index(best_overall_de_tac)].copy()
        else: best_overall_de_chromo = self.de_population[0].copy() if self.de_population else np.zeros(self.de_chromosome_length)
        for _ in range(self.generations_de):
            new_pop_de = []
            for i in range(self.pop_size_de):
                target_vec = self.de_population[i]
                idxs = [idx for idx in range(self.pop_size_de) if idx != i]
                if len(idxs) < 3: trial_vec = target_vec.copy()
                else:
                    a,b,c = np.random.choice(idxs, 3, replace=False)
                    mutant_vec = self.de_population[a] + self.F * (self.de_population[b] - self.de_population[c])
                    mutant_vec[:self.num_q_vars] = np.maximum(0, mutant_vec[:self.num_q_vars])
                    mutant_vec[self.num_q_vars:] = np.maximum(1e-6, mutant_vec[self.num_q_vars:])
                    trial_vec = np.zeros_like(target_vec); j_rand = random.randrange(self.de_chromosome_length) if self.de_chromosome_length > 0 else 0
                    if self.de_chromosome_length > 0 : # Ensure not empty
                        for k_de_gene in range(self.de_chromosome_length):
                            if random.random() < self.CR or k_de_gene == j_rand: trial_vec[k_de_gene] = mutant_vec[k_de_gene]
                            else: trial_vec[k_de_gene] = target_vec[k_de_gene]
                    else: # no variables to optimize for DE
                        trial_vec = target_vec.copy()

                trial_fitness = self._fitness_de(trial_vec)
                if trial_fitness <= self.de_fitness[i]:
                    new_pop_de.append(trial_vec); self.de_fitness[i] = trial_fitness
                    if trial_fitness < best_overall_de_tac: best_overall_de_tac = trial_fitness; best_overall_de_chromo = trial_vec.copy()
                else: new_pop_de.append(target_vec)
            self.de_population = new_pop_de
        if best_overall_de_chromo is not None:
            Q_final_de, FH_final_de, FC_final_de = self._decode_de_chromosome(best_overall_de_chromo)
            return self.problem.run_sws_simulation_for_de(self.fixed_Z_ijk, Q_final_de, FH_final_de, FC_final_de)
        else: # Fallback if DE somehow didn't produce a best chromosome
            dummy_costs = {"TAC_true_report": float('inf'),"op_cost_hot_utility":0, "op_cost_cold_utility":0, "total_operating_cost":0, "total_capital_cost":0, "penalty_EMAT_etc":0, "penalty_unmet_targets":0 }
            return float('inf'), dummy_costs, []

# --- Upper-Level Genetic Algorithm (GeneticAlgorithmHEN_TwoLevel) ---
# ... (This class remains as defined in the previous response, ensuring it calls the DE optimizer) ...
class GeneticAlgorithmHEN_TwoLevel: 
    def __init__(self, problem, population_size_ga, generations_ga, crossover_prob_ga, mutation_prob_Z_ga, elitism_count_ga=1, random_seed_ga=None, utility_cost_factor_ga=1.0, pinch_deviation_penalty_factor_ga=0.0, de_params=None):
        self.problem = problem; self.population_size = population_size_ga; self.generations = generations_ga; self.crossover_prob = crossover_prob_ga; self.mutation_prob_Z = mutation_prob_Z_ga; self.elitism_count = elitism_count_ga; self.random_seed = random_seed_ga; self.utility_cost_factor = utility_cost_factor_ga; self.pinch_deviation_penalty_factor = pinch_deviation_penalty_factor_ga
        if de_params is None: self.de_params = {"pop_size_de": 20, "gens_de": 30, "F_de": 0.7, "CR_de": 0.9}
        else: self.de_params = de_params
        if random_seed_ga is not None: random.seed(random_seed_ga); np.random.seed(random_seed_ga)
        self.len_Z = self.problem.NH * self.problem.NC * self.problem.num_stages; self.population = []
    def _initialize_population(self):
        self.population = []; 
        for _ in range(self.population_size): self.population.append(np.random.randint(0, 2, size=self.len_Z))
    def _decode_ga_chromosome(self, ga_chromosome_flat_z): return ga_chromosome_flat_z.reshape((self.problem.NH, self.problem.NC, self.problem.num_stages)).astype(int)
    def _calculate_fitness_ga(self, ga_chromosome_flat_z):
        Z_ijk_topology = self._decode_ga_chromosome(ga_chromosome_flat_z)
        
        
        de_run_seed = None
        if self.random_seed is not None:
            # Create a derived integer seed for DE for this specific Z_ijk evaluation
            # Hash the Z_ijk array's byte representation to get a somewhat unique value, add to GA seed
            # Ensure the result is an int and handle potential large hash values for np.random.seed
            try:
                # Convert Z_ijk to a hashable form (bytes)
                z_bytes = Z_ijk_topology.tobytes()
                z_hash = hash(z_bytes)
                # Combine with the GA's random seed.
                # Ensure the resulting seed is within a reasonable integer range, especially for np.random.seed
                combined_seed = (self.random_seed + z_hash)
                de_run_seed = int(combined_seed % (2**32 -1 )) # Keep it within typical int range
                if de_run_seed < 0: # Ensure non-negative for np.random.seed
                    de_run_seed += (2**32)
            except Exception: # Fallback if hashing fails or other issues
                de_run_seed = int(self.random_seed + np.sum(ga_chromosome_flat_z)) % (2**32-1)
                if de_run_seed < 0: de_run_seed += (2**32)
        
        de_optimizer = LowerLevelDEOptimizer(problem=self.problem,fixed_topology_Z_ijk=Z_ijk_topology,pop_size_de=self.de_params["pop_size_de"],gens_de=self.de_params["gens_de"],F_mutation=self.de_params["F_de"],CR_crossover=self.de_params["CR_de"],random_seed_de=de_run_seed)
        min_tac_de, detailed_costs_de, exchanger_details_de = de_optimizer.run()
        tac_for_ga_optimization = min_tac_de; utility_deviation_penalty_ga = 0
        if detailed_costs_de and self.pinch_deviation_penalty_factor > 0:
            q_hot_actual_de = detailed_costs_de.get("Q_hot_consumed_kW_actual",0); q_cold_actual_de = detailed_costs_de.get("Q_cold_consumed_kW_actual",0)
            if hasattr(self.problem, 'Q_H_min_pinch') and self.problem.Q_H_min_pinch is not None:
                if q_hot_actual_de > self.problem.Q_H_min_pinch + 1e-3: utility_deviation_penalty_ga += self.pinch_deviation_penalty_factor * (q_hot_actual_de - self.problem.Q_H_min_pinch)
            if hasattr(self.problem, 'Q_C_min_pinch') and self.problem.Q_C_min_pinch is not None:
                if q_cold_actual_de > self.problem.Q_C_min_pinch + 1e-3: utility_deviation_penalty_ga += self.pinch_deviation_penalty_factor * (q_cold_actual_de - self.problem.Q_C_min_pinch)
        op_cost_from_de = detailed_costs_de.get("total_operating_cost", 0) if detailed_costs_de else 0
        cap_cost_from_de = detailed_costs_de.get("total_capital_cost", 0) if detailed_costs_de else 0
        physical_penalties_from_de = detailed_costs_de.get("penalty_EMAT_etc",0) + detailed_costs_de.get("penalty_unmet_targets",0) if detailed_costs_de else float('inf')
        if min_tac_de == float('inf'): tac_for_ga_optimization = float('inf'); true_tac_report = float('inf')
        else:
            tac_for_ga_optimization = cap_cost_from_de + (op_cost_from_de * self.utility_cost_factor) + physical_penalties_from_de + utility_deviation_penalty_ga
            true_tac_report = cap_cost_from_de + op_cost_from_de + physical_penalties_from_de
        ga_level_costs_dict = copy.deepcopy(detailed_costs_de) if detailed_costs_de else {}
        ga_level_costs_dict["TAC_GA_optimizing"] = tac_for_ga_optimization; ga_level_costs_dict["TAC_true_report"] = true_tac_report
        ga_level_costs_dict["penalty_pinch_deviation_GA_Level"] = utility_deviation_penalty_ga
        return ga_level_costs_dict, exchanger_details_de if exchanger_details_de else []
    def _crossover_ga(self, parent1_Z_flat, parent2_Z_flat):
        off1_z = parent1_Z_flat.copy(); off2_z = parent2_Z_flat.copy()
        if random.random() < self.crossover_prob and self.len_Z > 1:
            cx_pt = random.randint(1, self.len_Z -1)
            off1_z = np.concatenate((parent1_Z_flat[:cx_pt], parent2_Z_flat[cx_pt:])); off2_z = np.concatenate((parent2_Z_flat[:cx_pt], parent1_Z_flat[cx_pt:]))
        return off1_z, off2_z
    def _mutation_ga(self, chromosome_Z_flat):
        mut_z = chromosome_Z_flat.copy()
        for i in range(self.len_Z):
            if random.random() < self.mutation_prob_Z: mut_z[i] = 1 - mut_z[i]
        return mut_z
    def run(self, run_id_for_print=""):
        if self.random_seed is not None: random.seed(self.random_seed); np.random.seed(self.random_seed)
        self._initialize_population()
        best_chromosome_Z_overall = None; best_costs_overall_ga = {"TAC_GA_optimizing": float('inf'), "TAC_true_report": float('inf')}; best_details_overall_from_de = None
        print_prefix = f"Run {run_id_for_print} - " if run_id_for_print else ""
        log_best_true_tac_per_gen = []; log_avg_true_tac_per_gen = []; log_best_ga_tac_per_gen = []; log_avg_ga_tac_per_gen = []
        for gen in range(self.generations):
            current_ga_population_evaluations = []; gen_true_tacs_ga = []; gen_ga_tacs_ga = []
            print(f"{print_prefix}Gen {gen+1:03d}/{self.generations} - Evaluating individuals (DE runs)...")
            for idx, ga_chromo_z_flat in enumerate(self.population):
                costs_dict_from_de, details_from_de = self._calculate_fitness_ga(ga_chromo_z_flat)
                current_ga_population_evaluations.append({'chromosome_Z_flat': ga_chromo_z_flat, 'costs': costs_dict_from_de, 'details': details_from_de})
                if costs_dict_from_de.get("TAC_true_report", float('inf')) != float('inf'): gen_true_tacs_ga.append(costs_dict_from_de["TAC_true_report"])
                if costs_dict_from_de.get("TAC_GA_optimizing", float('inf')) != float('inf'): gen_ga_tacs_ga.append(costs_dict_from_de["TAC_GA_optimizing"])
            current_ga_population_evaluations.sort(key=lambda x: x['costs']['TAC_GA_optimizing'])
            best_ga_tac_this_gen_val = current_ga_population_evaluations[0]['costs']['TAC_GA_optimizing'] if current_ga_population_evaluations else float('inf')
            best_true_tac_this_gen_val = current_ga_population_evaluations[0]['costs']['TAC_true_report'] if current_ga_population_evaluations else float('inf')
            if best_ga_tac_this_gen_val < best_costs_overall_ga['TAC_GA_optimizing']:
                best_costs_overall_ga = copy.deepcopy(current_ga_population_evaluations[0]['costs']); best_chromosome_Z_overall = current_ga_population_evaluations[0]['chromosome_Z_flat'].copy(); best_details_overall_from_de = current_ga_population_evaluations[0]['details']
            avg_true_tac_this_gen_ga = np.mean(gen_true_tacs_ga) if gen_true_tacs_ga else float('inf'); avg_ga_tac_this_gen_ga = np.mean(gen_ga_tacs_ga) if gen_ga_tacs_ga else float('inf')
            log_best_true_tac_per_gen.append(best_costs_overall_ga['TAC_true_report']); log_avg_true_tac_per_gen.append(avg_true_tac_this_gen_ga)
            log_best_ga_tac_per_gen.append(best_costs_overall_ga['TAC_GA_optimizing']); log_avg_ga_tac_per_gen.append(avg_ga_tac_this_gen_ga)
            true_overall_str = f"{best_costs_overall_ga['TAC_true_report']:.2f}" if best_costs_overall_ga['TAC_true_report']!=float('inf') else "Inf"; ga_overall_str = f"{best_costs_overall_ga['TAC_GA_optimizing']:.2f}" if best_costs_overall_ga['TAC_GA_optimizing']!=float('inf') else "Inf"
            true_gen_str = f"{best_true_tac_this_gen_val:.2f}" if best_true_tac_this_gen_val!=float('inf') else "Inf"; avg_true_gen_str = f"{avg_true_tac_this_gen_ga:.2f}" if avg_true_tac_this_gen_ga!=float('inf') else "Inf"
            ga_gen_str = f"{best_ga_tac_this_gen_val:.2f}" if best_ga_tac_this_gen_val!=float('inf') else "Inf"; avg_ga_gen_str = f"{avg_ga_tac_this_gen_ga:.2f}" if avg_ga_tac_this_gen_ga!=float('inf') else "Inf"
            print(f"{print_prefix}Gen {gen+1:03d}/{self.generations} - Best True TAC (Overall): {true_overall_str}, Best GA Opt TAC (Overall): {ga_overall_str} | Gen Best True: {true_gen_str}, Gen Avg True: {avg_true_gen_str}, Gen Best GA: {ga_gen_str}, Gen Avg GA: {avg_ga_gen_str}")
            new_ga_population = []
            if current_ga_population_evaluations:
                 for i in range(min(self.elitism_count, len(current_ga_population_evaluations))): new_ga_population.append(current_ga_population_evaluations[i]['chromosome_Z_flat'].copy())
            if not current_ga_population_evaluations: self._initialize_population(); continue
            selected_parent_indices_ga = self._selection_ga(current_ga_population_evaluations)
            num_offspring_ga = self.population_size - len(new_ga_population); children_generated_ga = 0; idx_select_ga = 0
            if not selected_parent_indices_ga:
                while children_generated_ga < num_offspring_ga: new_ga_population.append(np.random.randint(0,2,size=self.len_Z)); children_generated_ga+=1
            else:
                while children_generated_ga < num_offspring_ga:
                    p1_idx = selected_parent_indices_ga[idx_select_ga % len(selected_parent_indices_ga)]; idx_select_ga+=1
                    p2_idx = selected_parent_indices_ga[idx_select_ga % len(selected_parent_indices_ga)]; idx_select_ga+=1
                    parent1_Z = current_ga_population_evaluations[p1_idx]['chromosome_Z_flat']; parent2_Z = current_ga_population_evaluations[p2_idx]['chromosome_Z_flat']
                    off1_Z, off2_Z = self._crossover_ga(parent1_Z, parent2_Z)
                    mut_off1_Z = self._mutation_ga(off1_Z); mut_off2_Z = self._mutation_ga(off2_Z)
                    if children_generated_ga < num_offspring_ga: new_ga_population.append(mut_off1_Z); children_generated_ga+=1
                    if children_generated_ga < num_offspring_ga: new_ga_population.append(mut_off2_Z); children_generated_ga+=1
            self.population = new_ga_population
            if len(self.population) != self.population_size:
                while len(self.population) < self.population_size: self.population.append(np.random.randint(0,2,size=self.len_Z))
                self.population = self.population[:self.population_size]
        return best_chromosome_Z_overall, best_costs_overall_ga, best_details_overall_from_de
    def _selection_ga(self, current_ga_population_evaluations):
        raw_fitness = [1.0 / (item['costs']['TAC_GA_optimizing'] + 1e-9) for item in current_ga_population_evaluations]
        total_fitness = sum(raw_fitness)
        if total_fitness < 1e-9 or total_fitness == float('inf') or np.isnan(total_fitness): return [random.choice(range(len(current_ga_population_evaluations))) for _ in range(len(current_ga_population_evaluations))]
        probabilities = [f / total_fitness for f in raw_fitness]
        if np.isnan(probabilities).any() or np.isinf(probabilities).any() or abs(sum(probabilities) - 1.0) > 1e-5 : probabilities = np.ones(len(current_ga_population_evaluations)) / len(current_ga_population_evaluations)
        num_to_select = len(current_ga_population_evaluations)
        try: selected_indices = np.random.choice(len(current_ga_population_evaluations), size=num_to_select, p=probabilities, replace=True)
        except ValueError as e: probabilities = np.ones(len(current_ga_population_evaluations)) / len(current_ga_population_evaluations); selected_indices = np.random.choice(len(current_ga_population_evaluations), size=num_to_select, p=probabilities, replace=True)
        return selected_indices.tolist()

# --- Main Execution Block ---
if __name__ == "__main__":
    # ... (load_data_from_csv, adapt data to Stream, Utility, CostParameters as before)
    # ... (Instantiate HENProblem as before)
    # ... (Set GA and DE parameters)
    # ... (Run the GeneticAlgorithmHEN_TwoLevel)
    # ... (Print summary using the returned costs dictionary)
    print("HEN Synthesis using Two-Level GA/DE (Conceptual Structure)")
    streams_file = 'streams.csv'
    utilities_file = 'utilities.csv' # Make sure these files exist
    loaded_hot_streams_data, loaded_cold_streams_data, loaded_hot_utilities_data, loaded_cold_utilities_data = load_data_from_csv(streams_file, utilities_file)
    
    if loaded_hot_streams_data is None:
        exit()
    
    hot_streams_obj_list = [Stream(s['Name'],s['TIN_spec'],s['TOUT_spec'],s['Fcp'],0,'hot') for s in loaded_hot_streams_data]
    cold_streams_obj_list = [Stream(s['Name'],s['TIN_spec'],s['TOUT_spec'],s['Fcp'],0,'cold') for s in loaded_cold_streams_data]
    primary_hot_utility_obj = Utility(loaded_hot_utilities_data[0]['Name'],loaded_hot_utilities_data[0]['TIN_utility'],loaded_hot_utilities_data[0]['TOUT_utility'],0,loaded_hot_utilities_data[0]['Unit_Cost_Energy'],'hot_utility') if loaded_hot_utilities_data else Utility("DefHU",500,499,0,100,"hot_utility")
    primary_cold_utility_obj = Utility(loaded_cold_utilities_data[0]['Name'],loaded_cold_utilities_data[0]['TIN_utility'],loaded_cold_utilities_data[0]['TOUT_utility'],0,loaded_cold_utilities_data[0]['Unit_Cost_Energy'],'cold_utility') if loaded_cold_utilities_data else Utility("DefCU",290,300,0,10,"cold_utility")

    EMAT_setting = 3.0
    U_proc_def = 0.8
    CF_proc = 0
    C_area_proc = 1000
    B_exp_proc = 0.6

    h_f = loaded_hot_utilities_data[0]['Fixed_Cost_Unit'] if loaded_hot_utilities_data else 0
    h_c = loaded_hot_utilities_data[0]['Area_Cost_Coeff'] if loaded_hot_utilities_data else 0
    h_e = loaded_hot_utilities_data[0]['Area_Cost_Exp'] if loaded_hot_utilities_data else 0.6
    c_f = loaded_cold_utilities_data[0]['Fixed_Cost_Unit'] if loaded_cold_utilities_data else 0
    c_c = loaded_cold_utilities_data[0]['Area_Cost_Coeff'] if loaded_cold_utilities_data else 0
    c_e = loaded_cold_utilities_data[0]['Area_Cost_Exp'] if loaded_cold_utilities_data else 0.6
    
    cost_params_instance = CostParameters(CF_proc,C_area_proc,B_exp_proc,h_f,h_c,h_e,c_f,c_c,c_e,EMAT_setting,U_proc_def)
    num_stages = max(1,len(hot_streams_obj_list),len(cold_streams_obj_list)) if hot_streams_obj_list or cold_streams_obj_list else 1
    
    if not hot_streams_obj_list and not cold_streams_obj_list:
        exit()
    
    hen_problem_instance = HENProblem(hot_streams_obj_list,cold_streams_obj_list,primary_hot_utility_obj,primary_cold_utility_obj,cost_params_instance,num_stages)
    if loaded_hot_utilities_data:
        hen_problem_instance.U_heaters.fill(loaded_hot_utilities_data[0]['U_overall'])
    if loaded_cold_utilities_data:
        hen_problem_instance.U_coolers.fill(loaded_cold_utilities_data[0]['U_overall'])
        
    print(f"\nPinch: QHmin={hen_problem_instance.Q_H_min_pinch:.2f}, QCmin={hen_problem_instance.Q_C_min_pinch:.2f}")
    
    if hen_problem_instance.T_pinch_hot_actual is not None:
        print(f"  T_Pinch_Hot: {hen_problem_instance.T_pinch_hot_actual:.2f} K, T_Pinch_Cold: {hen_problem_instance.T_pinch_cold_actual:.2f} K")

    ga_pop_size = 20 # Small for quick test
    ga_gens = 50     # Small for quick test
    ga_cx_prob = 0.9
    ga_mut_prob_Z = 0.1
    ga_elitism = 1
    ga_util_cost_factor = 1.0
    ga_pinch_penalty_factor = 100.0
    de_params_cfg = {
        "pop_size_de": 200,
        "gens_de": 50,
        "F_de": 0.7,
        "CR_de": 0.9
    }
    number_of_ga_runs = 1
    all_run_results_ga = []
    base_seed = int(time.time())
    for i_ga_run in range(number_of_ga_runs):
        current_ga_seed = base_seed + i_ga_run
        print(f"\n--- Running GA: Trial {i_ga_run+1}/{number_of_ga_runs} (Seed: {current_ga_seed}) ---")
        
        upper_ga_optimizer = GeneticAlgorithmHEN_TwoLevel(
            problem=hen_problem_instance,
            population_size_ga=ga_pop_size,
            generations_ga=ga_gens,
            crossover_prob_ga=ga_cx_prob,
            mutation_prob_Z_ga=ga_mut_prob_Z, # Ensure this is ga_mut_prob_Z_setting
            elitism_count_ga=ga_elitism,
            random_seed_ga=current_ga_seed,
            utility_cost_factor_ga=ga_util_cost_factor,
            pinch_deviation_penalty_factor_ga=ga_pinch_penalty_factor, # Ensure this is ga_pinch_dev_penalty_factor
            de_params=de_params_cfg # Ensure this is de_params_config
        )
        
        # run() returns: best_Z_chromosome, best_overall_costs_dict (from DE), best_exchanger_details (from DE)
        best_Z_topo_flat, final_best_costs, final_best_details = upper_ga_optimizer.run(run_id_for_print=f"{i_ga_run+1}")
        all_run_results_ga.append({'seed': current_ga_seed, 'costs': final_best_costs, 'Z_flat': best_Z_topo_flat, 'details': final_best_details})
        
        # --- MODIFIED PRINT STATEMENT FOR END OF TRIAL ---
        true_tac_val = final_best_costs.get('TAC_true_report', float('inf'))
        true_tac_str_end_trial = f"{true_tac_val:.2f}" if true_tac_val != float('inf') else "Inf"
        
        print(f"--- Finished GA Run {i_ga_run+1} - Best True TAC: {true_tac_str_end_trial} ---")
        # --- END OF MODIFICATION ---
    print("\n\n--- Summary of Multiple GA Runs ---") # ... (Summary print as before, using results from all_run_results_ga) ...
    if not all_run_results_ga:
        print("No results to summarize.")
    else:
        best_overall_ga_opt_tac = float('inf'); best_run_final_package = None; true_tac_values_for_stats = []
        for res_item in all_run_results_ga:
            ga_opt_tac = res_item['costs']['TAC_GA_optimizing']; true_tac_disp = res_item['costs']['TAC_true_report']
            ga_str = f"{ga_opt_tac:.2f}" if ga_opt_tac != float('inf') else "Inf"; true_str = f"{true_tac_disp:.2f}" if true_tac_disp != float('inf') else "Inf"
            print(f"Run Seed {res_item['seed']}: TrueTAC={true_str} (GA_Opt_TAC={ga_str})")
            if true_tac_disp != float('inf'): true_tac_values_for_stats.append(true_tac_disp)
            if ga_opt_tac < best_overall_ga_opt_tac: best_overall_ga_opt_tac = ga_opt_tac; best_run_final_package = res_item
        if best_run_final_package and best_run_final_package['costs']['TAC_GA_optimizing'] != float('inf'):
            costs_to_show = best_run_final_package['costs']
            true_overall_str = f"{costs_to_show['TAC_true_report']:.2f}" if costs_to_show['TAC_true_report']!=float('inf') else "Inf"
            ga_overall_str = f"{costs_to_show['TAC_GA_optimizing']:.2f}" if costs_to_show['TAC_GA_optimizing']!=float('inf') else "Inf"
            print(f"\nBest True TAC (from best GA opt run): {true_overall_str}, (GA Opt TAC: {ga_overall_str}), Seed: {best_run_final_package['seed']}")
            print("Cost Breakdown:"); print(f"  TrueTAC: {costs_to_show['TAC_true_report']:.2f}, GA Opt TAC: {costs_to_show['TAC_GA_optimizing']:.2f}")
            print(f"  CapEx(Proc): {costs_to_show.get('capital_process_exchangers',0):.2f}, CapEx(H): {costs_to_show.get('capital_heaters',0):.2f}, CapEx(C): {costs_to_show.get('capital_coolers',0):.2f}")
            print(f"  OpEx(HotU): {costs_to_show.get('op_cost_hot_utility',0):.2f}, OpEx(ColdU): {costs_to_show.get('op_cost_cold_utility',0):.2f}")
            print(f"  Penalty(EMAT): {costs_to_show.get('penalty_EMAT_etc',0):.2f}, Penalty(UnmetT): {costs_to_show.get('penalty_unmet_targets',0):.2f}, Penalty(PinchGA): {costs_to_show.get('penalty_pinch_deviation_GA_Level',0):.2f}")
            if best_run_final_package['Z_flat'] is not None:
                Z_best_decoded = upper_ga_optimizer._decode_ga_chromosome(best_run_final_package['Z_flat'])
                details_best = best_run_final_package['details']
                print("Structure:") # ... (Print structure using Z_best_decoded)
                active_matches = np.argwhere(Z_best_decoded == 1)
                if active_matches.size > 0:
                    for match in active_matches:
                        q_val = 0
                        if details_best:
                            for detail in details_best:
                                if detail.get('H')==match[0] and detail.get('C')==match[1] and detail.get('k')==match[2]: q_val=detail.get('Q',0); break
                        if q_val > 1e-6: print(f"  H{match[0]+1}({hen_problem_instance.hot_streams[match[0]].id})-C{match[1]+1}({hen_problem_instance.cold_streams[match[1]].id}) S{match[2]+1} Q={q_val:.2f}")
                else: print("  No active process matches.")
                # ... (Print exchanger details and utility details from details_best)
                if details_best: # ... (full printout logic as before)
                    print("Exchanger Details:")
                    for item in details_best:
                        if 'H' in item and 'C' in item : print(f"    H{item['H']+1}-C{item['C']+1} S{item['k']+1} Q={item['Q']:.2f} A={item['Area']:.2f} TinH={item['Th_in']:.1f} ToutH={item['Th_out']:.1f} TinC={item['Tc_in']:.1f} ToutC={item['Tc_out']:.1f}")
                    print("Utility Details:")
                    for item in details_best:
                        if item.get('type') == 'heater': print(f"    Heater C{item['C_idx']+1} Q={item['Q']:.2f} A={item['Area']:.2f}")
                        elif item.get('type') == 'cooler': print(f"    Cooler H{item['H_idx']+1} Q={item['Q']:.2f} A={item['Area']:.2f}")
        else: print("\nNo valid best solution found.")
        if true_tac_values_for_stats: print(f"\nAvgTrueTAC:{np.mean(true_tac_values_for_stats):.2f} StdTrueTAC:{np.std(true_tac_values_for_stats):.2f}")
        else: print("\nNo finite TrueTACs for stats.")