import numpy as np
import copy
import time
from typing import Any, Tuple
import random
import concurrent.futures

from gth import Stream, Utility, CostParameters, HENProblem, \
                GeneticAlgorithmHEN, TeachingLearningBasedOptimizationHEN, \
                load_data_from_csv

def run_one_trial(
    trial_index: int,
    problem: HENProblem,
    model: str,
    random_seed: int,
    population_size: int,
    generations: int,
    ga_crossover_prob: float,
    ga_mutation_prob_Z_setting: float,
    ga_mutation_prob_R_setting: float,
    ga_r_mutation_std_dev_factor_setting: float,
    ga_elitism_frac: float,
    utility_cost_factor: float,
    pinch_dev_penalty_factor: float,
    sws_max_iter: int,
    sws_conv_tol: float,
) -> Tuple[int, Any, Any, Any]:
    """
    Run exactly one GA or TLBO trial, using trial_index as the RNG seed.
    Returns a tuple (trial_index, best_solution, best_cost).
    """

    # 1) Seed the RNG so each trial is reproducible but different:
    random.seed(trial_index)
    np.random.seed(trial_index)

    # 3) Solve with GA or TLBO depending on “model”:
    if model.upper() == "GA":
        elitism_count = int(population_size * ga_elitism_frac)
        if elitism_count < 1:
            elitism_count = 1
        solver = GeneticAlgorithmHEN(
            problem=problem,
            population_size=population_size,
            generations=generations,
            crossover_prob=ga_crossover_prob,
            mutation_prob_Z=ga_mutation_prob_Z_setting,
            mutation_prob_R=ga_mutation_prob_R_setting,
            elitism_count=elitism_count,
            random_seed=random_seed,
            utility_cost_factor=utility_cost_factor,
            pinch_deviation_penalty_factor=pinch_dev_penalty_factor,
            sws_max_iter=sws_max_iter,
            sws_conv_tol=sws_conv_tol
        )
    else:  # TLBO
        solver = TeachingLearningBasedOptimizationHEN(
            problem=problem,
            population_size=population_size,
            generations=generations,
            random_seed=trial_index,
            utility_cost_factor=utility_cost_factor,
            pinch_deviation_penalty_factor=pinch_dev_penalty_factor,
            sws_max_iter=sws_max_iter,
            sws_conv_tol=sws_conv_tol
        )

    best_chromosome, best_solution, best_cost = solver.run(run_id_for_print=f"{trial_index+1}")
    return (trial_index, best_chromosome,best_solution, best_cost)

def main_parallel(
    problem: HENProblem,
    model: str,
    population_size: int,
    generations: int,
    ga_crossover_prob: float,
    ga_mutation_prob_Z_setting: float,
    ga_mutation_prob_R_setting: float,
    ga_r_mutation_std_dev_factor_setting: float,
    ga_elitism_frac: float,
    utility_cost_factor: float,
    pinch_dev_penalty_factor: float,
    sws_max_iter: int,
    sws_conv_tol: float,
    number_of_runs: int=8,
    num_workers=None,
):
    """
    Run exactly parallel GA or TLBO trial, using trial_index as the RNG seed.
    Returns a tuple (trial_index, best_solution, best_cost).
    """

    args_list = []
    base_seed = int(time.time() / 265)

    for run_index in range(number_of_runs):
        random_seed = base_seed + run_index
        args_list.append(
            (
                run_index,
                problem,
                model,
                random_seed,
                population_size,
                generations,
                ga_crossover_prob,
                ga_mutation_prob_Z_setting,
                ga_mutation_prob_R_setting,
                ga_r_mutation_std_dev_factor_setting,
                ga_elitism_frac,
                utility_cost_factor,
                pinch_dev_penalty_factor,
                sws_max_iter,
                sws_conv_tol,
            )
        )
    
    # 2) Spawn a process pool. By default, max_workers=os.cpu_count().
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
        # Submit each trial as a separate future to avoid lambda in map
        futures = [executor.submit(run_one_trial, *args) for args in args_list]
        all_results = [f.result() for f in concurrent.futures.as_completed(futures)]
    
    return all_results
    
def main(streams_file="streams.csv", utilities_file="utilities.csv", matches_U_file=None, forbidden_matches_file=None, required_matches_file=None,
         EMAT_setting=3.0, model='GA', population_size=200, generations=200, ga_crossover_prob=0.85, ga_mutation_prob_Z_setting=0.1, ga_mutation_prob_R_setting=0.1,
         ga_r_mutation_std_dev_factor_setting=0.1, ga_elitism_frac=0.1, utility_cost_factor=1.0, pinch_dev_penalty_factor=150.0, 
         sws_max_iter=200, sws_conv_tol=0.0001, 
         number_of_runs=8, number_of_workers=1):
    # ... (load_data_from_csv, adapt data to Stream, Utility, CostParameters, HENProblem - as before) ...
    print(f"HEN Synthesis using {model} with CSV Data Loading & Evolving Splits")
    loaded_hot_streams_data, loaded_cold_streams_data, loaded_hot_utilities_data, loaded_cold_utilities_data, loaded_matches_U, loaded_forbidden_matches, loaded_required_matches= load_data_from_csv(streams_file, utilities_file, matches_U_file, forbidden_matches_file, required_matches_file)
    
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
        print(f"At least data should have one hot and one cold stream. Exiting...")
        exit()
    
    hen_problem_instance = HENProblem(hot_streams=hot_streams_obj_list,
                                      cold_streams=cold_streams_obj_list,
                                      hot_utility=primary_hot_utility_obj_list,
                                      cold_utility=primary_cold_utility_obj_list,
                                      cost_params=cost_params_instance,
                                      num_stages=num_stages_for_problem,
                                      matches_U_cost=loaded_matches_U,
                                      forbidden_matches=loaded_forbidden_matches,
                                      required_matches=loaded_required_matches)

    if loaded_hot_utilities_data:
        hen_problem_instance.U_heaters.fill(loaded_hot_utilities_data[0]['U_overall'])
    if loaded_cold_utilities_data:
        hen_problem_instance.U_coolers.fill(loaded_cold_utilities_data[0]['U_overall'])
    
    print(f"\nPinch Analysis Results (EMAT={hen_problem_instance.cost_params.EMAT}K): Q_H_min: {hen_problem_instance.Q_H_min_pinch:.2f} kW, Q_C_min: {hen_problem_instance.Q_C_min_pinch:.2f} kW")
    
    if hen_problem_instance.T_pinch_hot_actual is not None:
        print(f"  T_Pinch_Hot: {hen_problem_instance.T_pinch_hot_actual:.2f} K, T_Pinch_Cold: {hen_problem_instance.T_pinch_cold_actual:.2f} K")

    # If ga_elitism_frac is povide
    if ga_elitism_frac is not None:
        ga_elitism_count = int(ga_elitism_frac * population_size)
    elif ga_elitism_count is None and ga_elitism_frac is None:
        ga_elitism_count = 1
    else:
        ga_elitism_count = ga_elitism_count
        
    all_run_results = []
    base_seed = int(time.time() / 265)
    print(f"\n--- Starting {number_of_runs} {model} Runs with EMAT = {EMAT_setting}K, Evolving Splits ---")
    parallel_results = main_parallel(problem=hen_problem_instance,
                        model=model, population_size=population_size, generations=generations,
                        ga_crossover_prob=ga_crossover_prob, ga_mutation_prob_Z_setting=ga_mutation_prob_Z_setting,
                        ga_mutation_prob_R_setting=ga_mutation_prob_R_setting,
                        ga_r_mutation_std_dev_factor_setting=ga_r_mutation_std_dev_factor_setting,
                        ga_elitism_frac=ga_elitism_frac, utility_cost_factor=utility_cost_factor,
                        pinch_dev_penalty_factor=pinch_dev_penalty_factor, sws_max_iter=sws_max_iter,
                        sws_conv_tol=sws_conv_tol, number_of_runs=number_of_runs, num_workers=number_of_workers)
    for res in parallel_results:
        (current_seed, best_Z_chromo_part, best_costs_dict_run, best_details_run) = res
        # Note: best_Z_chromo_part is now the full chromosome (Z and R parts)
        all_run_results.append({'seed': current_seed, 'costs': best_costs_dict_run, 'chromosome': best_Z_chromo_part, 'details': best_details_run})
    
    # --- Summarize and Analyze Results ---
    # (The summary print section needs to be adapted to use 'chromosome' instead of 'Z' if you stored the full one,
    #  and then decode it again if printing the Z_ijk structure of the overall best.)
    print(f"\n\n--- Summary of Multiple {model} Runs ---")
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
            if 'hen_problem_instance' in locals() and hen_problem_instance is not None:
                Z_overall_best, _, _ = hen_problem_instance._decode_chromosome(full_chromosome_best)
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
                            if detail['Q'] < 1e-6: continue
                            if abs(detail['Th_in'] - detail['Th_out']) < 1e-6: continue
                            if abs(detail['Tc_in'] - detail['Tc_out']) < 1e-6: continue
                            if hot_Split_ratio < 1e-6: continue
                            if cold_Split_ratio < 1e-6: continue
                            print_str = f"    {hot_name}-{cold_name} (S{detail['k']+1}): Q={detail['Q']:.2f}, A={detail['Area']:.2f}"
                            print_str += f", Hot stream: CFp = {hot_CFp:.2f} (SP = {hot_Split_ratio:.2f}), Th_in={detail['Th_in']:.1f}, Th_out={detail['Th_out']:.1f}"
                            print_str += f", Cold stream: CFp = {cold_CFp:.2f} (SP = {cold_Split_ratio:.2f}), Tc_in={detail['Tc_in']:.1f}, Tc_out={detail['Tc_out']:.1f}"
                            print(print_str)
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
            print(f"\nNo valid (finite {model} TAC) best solution found across all runs.")

# --- Main Execution Block ---
if __name__ == "__main__":
    main(streams_file="streams.csv",
         utilities_file="utilities.csv",
         matches_U_file="matches_U_cost.csv",
         forbidden_matches_file="forbidden_matches.csv",
         required_matches_file="required_matches.csv",
         EMAT_setting=3.0,
         model='TLBO',
         population_size=200,
         generations=100,
         ga_crossover_prob=0.85,
         ga_mutation_prob_Z_setting=0.1,
         ga_mutation_prob_R_setting=0.1,
         ga_r_mutation_std_dev_factor_setting=0.1,
         ga_elitism_frac=0.1,
         utility_cost_factor=1.0,
         pinch_dev_penalty_factor=150.0,
         sws_max_iter=300,
         sws_conv_tol=0.00001,
         number_of_runs=8,
         number_of_workers=8)
    