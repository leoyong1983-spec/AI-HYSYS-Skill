import pandas as pd
import pyomo.environ as pe
from pyomo.opt import SolverFactory
import math

# --- Helper Functions ---
def smooth_max_zero(x, epsilon_smooth):
    """
    Smooth approximation of max(0, x).
    This is a common hyperbolic smoothing: (x + sqrt(x^2 + epsilon^2))/2
    """
    # Add a small constant to epsilon_smooth**2 to prevent issues if epsilon_smooth is zero.
    # However, epsilon_smooth should be a small positive number.
    return (x + (x**2 + epsilon_smooth**2 + 1e-12)**0.5) / 2.0


# --- 1. Data Loading ---
def load_data(streams_file, utilities_file, params_file, constraints_file=None):
    """
    Loads data. For this implementation, using hardcoded data based on Example 1/3.
    Modified to potentially support multiple utilities in structure, though example data has one of each.
    """
    data = {}

    data['NOK'] = 2
    data['AreaCostCoeff'] = 200
    data['AreaCostExponent'] = 1.0
    data['EpsilonSmoothMax'] = 1e-4
    data['DeltaLMTD'] = 1e-6
    data['EMAT_min'] = 10.0

    data['hot_streams_data'] = {
        'H1': {'TIN': 395, 'TOUT': 343, 'Fcp': 2.0},
        'H2': {'TIN': 405, 'TOUT': 288, 'Fcp': 4.5},
    }
    data['cold_streams_data'] = {
        'C1': {'TIN': 293, 'TOUT': 493, 'Fcp': 2.0},
        'C2': {'TIN': 353, 'TOUT': 383, 'Fcp': 3.0},
    }

    # Example with one hot and one cold utility
    data['hot_utilities_data'] = {
        'S1': {'TIN': 520, 'TOUT': 520, 'Cost': 80, 'U_val': 2.0}
        # Add more HUs here if needed: 'S2': {'TIN': ..., 'Cost': ..., 'U_val': ...}
    }
    data['cold_utilities_data'] = {
        'W1': {'TIN': 278, 'TOUT': 288, 'Cost': 20, 'U_val': 2.0}
        # Add more CUs here: 'W2': {'TIN': ..., 'Cost': ..., 'U_val': ...}
    }

    data['U_match_data'] = {
        ('H1', 'C1'): 2.0, ('H1', 'C2'): 0.2,
        ('H2', 'C1'): 0.2, ('H2', 'C2'): 0.2,
    }
    
    data['forbidden_matches'] = []
    return data

# --- 2. Model Building ---
def build_model(data):
    m = pe.ConcreteModel(name="HEN_YeeGrossmann_NLP1_MultiUtil_EMAT")

    # --- Sets ---
    m.HP = pe.Set(initialize=data['hot_streams_data'].keys())
    m.CP = pe.Set(initialize=data['cold_streams_data'].keys())
    m.HU = pe.Set(initialize=data['hot_utilities_data'].keys())
    m.CU = pe.Set(initialize=data['cold_utilities_data'].keys())
    m.STAGES = pe.RangeSet(1, data['NOK'])
    m.TEMP_LOCS = pe.RangeSet(1, data['NOK'] + 1)

    # --- Parameters ---
    # (Your parameters remain the same, including m.EMAT_min)
    m.TIN_h = pe.Param(m.HP, initialize={s: d['TIN'] for s, d in data['hot_streams_data'].items()})
    m.TOUT_h = pe.Param(m.HP, initialize={s: d['TOUT'] for s, d in data['hot_streams_data'].items()})
    m.Fcp_h = pe.Param(m.HP, initialize={s: d['Fcp'] for s, d in data['hot_streams_data'].items()})

    m.TIN_c = pe.Param(m.CP, initialize={s: d['TIN'] for s, d in data['cold_streams_data'].items()})
    m.TOUT_c = pe.Param(m.CP, initialize={s: d['TOUT'] for s, d in data['cold_streams_data'].items()})
    m.Fcp_c = pe.Param(m.CP, initialize={s: d['Fcp'] for s, d in data['cold_streams_data'].items()})

    m.TIN_hu_p = pe.Param(m.HU, initialize={s: d['TIN'] for s,d in data['hot_utilities_data'].items()})
    m.TOUT_hu_p = pe.Param(m.HU, initialize={s: d['TOUT'] for s,d in data['hot_utilities_data'].items()})
    m.Cost_hu_p = pe.Param(m.HU, initialize={s: d['Cost'] for s,d in data['hot_utilities_data'].items()})
    m.U_hu_match = pe.Param(m.HU, m.CP, initialize={(hu, cp): data['hot_utilities_data'][hu]['U_val'] for hu in m.HU for cp in m.CP})

    m.TIN_cu_p = pe.Param(m.CU, initialize={s: d['TIN'] for s,d in data['cold_utilities_data'].items()})
    m.TOUT_cu_p = pe.Param(m.CU, initialize={s: d['TOUT'] for s,d in data['cold_utilities_data'].items()})
    m.Cost_cu_p = pe.Param(m.CU, initialize={s: d['Cost'] for s,d in data['cold_utilities_data'].items()})
    m.U_cu_match = pe.Param(m.CU, m.HP, initialize={(cu, hp): data['cold_utilities_data'][cu]['U_val'] for cu in m.CU for hp in m.HP})

    m.U_match = pe.Param(m.HP, m.CP, initialize=data['U_match_data'], default=0.001)

    m.AreaCostCoeff = pe.Param(initialize=data['AreaCostCoeff'])
    m.AreaCostExponent = pe.Param(initialize=data['AreaCostExponent'])
    m.EpsilonSmooth = pe.Param(initialize=data['EpsilonSmoothMax'])
    m.DeltaLMTD = pe.Param(initialize=data['DeltaLMTD'])
    m.NOK_param = pe.Param(initialize=data['NOK'])
    m.EMAT_min = pe.Param(initialize=data['EMAT_min'])

    # --- Variables ---
    # (Variables remain the same)
    m.q_match = pe.Var(m.HP, m.CP, m.STAGES, domain=pe.NonNegativeReals, initialize=0)
    m.q_hu = pe.Var(m.HU, m.CP, domain=pe.NonNegativeReals, initialize=0)
    m.q_cu = pe.Var(m.CU, m.HP, domain=pe.NonNegativeReals, initialize=0)

    def t_hot_bounds(m, h, k_loc):
        return (m.TOUT_h[h] - 20, m.TIN_h[h] + 20)
    m.t_hot = pe.Var(m.HP, m.TEMP_LOCS, domain=pe.Reals, bounds=t_hot_bounds,
                     initialize=lambda m,h,kloc: data['hot_streams_data'][h]['TIN'])

    def t_cold_bounds(m, c, k_loc):
        return (m.TIN_c[c] - 20, m.TOUT_c[c] + 20)
    m.t_cold = pe.Var(m.CP, m.TEMP_LOCS, domain=pe.Reals, bounds=t_cold_bounds,
                      initialize=lambda m,c,kloc: data['cold_streams_data'][c]['TOUT'] if kloc <= data['NOK'] else data['cold_streams_data'][c]['TIN'])

    # --- Constraints ---
    # (Existing constraints 1-5 remain the same)
    def overall_heat_balance_hot_rule(m, h):
        total_q_process = sum(m.q_match[h,c,k] for c in m.CP for k in m.STAGES)
        total_q_util = sum(m.q_cu[cu,h] for cu in m.CU)
        return m.Fcp_h[h] * (m.TIN_h[h] - m.TOUT_h[h]) == total_q_process + total_q_util
    m.OverallHeatBalanceHot = pe.Constraint(m.HP, rule=overall_heat_balance_hot_rule)

    def overall_heat_balance_cold_rule(m, c):
        total_q_process = sum(m.q_match[h,c,k] for h in m.HP for k in m.STAGES)
        total_q_util = sum(m.q_hu[hu,c] for hu in m.HU)
        return m.Fcp_c[c] * (m.TOUT_c[c] - m.TIN_c[c]) == total_q_process + total_q_util
    m.OverallHeatBalanceCold = pe.Constraint(m.CP, rule=overall_heat_balance_cold_rule)

    def stage_heat_balance_hot_rule(m, h, k):
        return m.Fcp_h[h] * (m.t_hot[h,k] - m.t_hot[h,k+1]) == sum(m.q_match[h,c,k] for c in m.CP)
    m.StageHeatBalanceHot = pe.Constraint(m.HP, m.STAGES, rule=stage_heat_balance_hot_rule)

    def stage_heat_balance_cold_rule(m, c, k):
        return m.Fcp_c[c] * (m.t_cold[c,k] - m.t_cold[c,k+1]) == sum(m.q_match[h,c,k] for h in m.HP)
    m.StageHeatBalanceCold = pe.Constraint(m.CP, m.STAGES, rule=stage_heat_balance_cold_rule)

    def inlet_temp_hot_rule(m,h):
        return m.t_hot[h,1] == m.TIN_h[h]
    m.InletTempHot = pe.Constraint(m.HP, rule=inlet_temp_hot_rule)

    def inlet_temp_cold_rule(m,c):
        return m.t_cold[c, m.NOK_param+1] == m.TIN_c[c]
    m.InletTempCold = pe.Constraint(m.CP, rule=inlet_temp_cold_rule)

    def temp_feas_hot_rule(m,h,k):
        return m.t_hot[h,k] >= m.t_hot[h,k+1]
    m.TempFeasHot = pe.Constraint(m.HP, m.STAGES, rule=temp_feas_hot_rule)

    def temp_feas_cold_rule(m,c,k):
        return m.t_cold[c,k] >= m.t_cold[c,k+1]
    m.TempFeasCold = pe.Constraint(m.CP, m.STAGES, rule=temp_feas_cold_rule)

    def temp_bound_hot_outlet_rule(m,h):
        return m.t_hot[h, m.NOK_param+1] >= m.TOUT_h[h]
    m.TempBoundHotOutlet = pe.Constraint(m.HP, rule=temp_bound_hot_outlet_rule)

    def temp_bound_cold_outlet_rule(m,c):
        return m.t_cold[c, 1] <= m.TOUT_c[c]
    m.TempBoundColdOutlet = pe.Constraint(m.CP, rule=temp_bound_cold_outlet_rule)

    def total_cold_utility_load_for_hot_stream_rule(m, h):
        return sum(m.q_cu[cu,h] for cu in m.CU) == m.Fcp_h[h] * (m.t_hot[h, m.NOK_param+1] - m.TOUT_h[h])
    m.TotalColdUtilityLoad = pe.Constraint(m.HP, rule=total_cold_utility_load_for_hot_stream_rule)

    def total_hot_utility_load_for_cold_stream_rule(m, c):
        return sum(m.q_hu[hu,c] for hu in m.HU) == m.Fcp_c[c] * (m.TOUT_c[c] - m.t_cold[c,1])
    m.TotalHotUtilityLoad = pe.Constraint(m.CP, rule=total_hot_utility_load_for_cold_stream_rule)

    # --- ADDED: EMAT Constraints ---
    # For Process-Process Exchangers
    m.EMAT_Process_HotEnd = pe.ConstraintList()
    m.EMAT_Process_ColdEnd = pe.ConstraintList()
    for h_iter in m.HP: # Use m.HP, m.CP which are Pyomo sets from data keys
        for c_iter in m.CP:
            for k_iter in m.STAGES:
                m.EMAT_Process_HotEnd.add(m.t_hot[h_iter,k_iter] - m.t_cold[c_iter,k_iter] >= m.EMAT_min)
                m.EMAT_Process_ColdEnd.add(m.t_hot[h_iter,k_iter+1] - m.t_cold[c_iter,k_iter+1] >= m.EMAT_min)

    # For Cold Utility Exchangers (Coolers)
    m.EMAT_ColdUtility_Var = pe.ConstraintList() # Renamed for clarity
    if len(m.CU) > 0 and len(m.HP) > 0:
        for h_key in m.HP: # Iterate over Pyomo set m.HP
            h_data_check = data['hot_streams_data'][h_key] # For data check
            for cu_key in m.CU: # Iterate over Pyomo set m.CU
                cu_data_check = data['cold_utilities_data'][cu_key] # For data check

                # Constraint involving a variable (m.t_hot) - THIS IS A VALID PYOMO CONSTRAINT
                # Hot stream inlet to cooler (variable temp) vs. Cold utility outlet (param temp)
                m.EMAT_ColdUtility_Var.add(m.t_hot[h_key, m.NOK_param+1] - m.TOUT_cu_p[cu_key] >= m.EMAT_min)

                # Data validation check for fixed temperatures - NOT A PYOMO CONSTRAINT
                # Hot stream outlet from cooler (param: final target) vs. Cold utility inlet (param)
                fixed_approach_cu = h_data_check['TOUT'] - cu_data_check['TIN']
                if fixed_approach_cu < data['EMAT_min']:
                    print(f"❗ WARNING: EMAT Data Inconsistency (Cold Utility Interface).")
                    print(f"  Hot Stream {h_key} (Target TOUT={h_data_check['TOUT']}) vs. Cold Utility {cu_key} (TIN={cu_data_check['TIN']})")
                    print(f"  Fixed Approach = {fixed_approach_cu:.2f} K < EMAT_min ({data['EMAT_min']:.2f} K).")
                    print(f"  This might indicate an issue with input data or chosen EMAT_min if this utility path is used.")
                    # Consider raising an error if strict adherence at fixed points is critical before solving:
                    # raise ValueError(f"EMAT_min violation in input data: HS {h_key} ({h_data_check['TOUT']}K) and CU {cu_key} ({cu_data_check['TIN']}K) gives {fixed_approach_cu}K.")

    # For Hot Utility Exchangers (Heaters)
    m.EMAT_HotUtility_Var = pe.ConstraintList() # Renamed for clarity
    if len(m.HU) > 0 and len(m.CP) > 0:
        for c_key in m.CP: # Iterate over Pyomo set m.CP
            c_data_check = data['cold_streams_data'][c_key] # For data check
            for hu_key in m.HU: # Iterate over Pyomo set m.HU
                hu_data_check = data['hot_utilities_data'][hu_key] # For data check

                # Constraint involving a variable (m.t_cold) - THIS IS A VALID PYOMO CONSTRAINT
                # Hot utility outlet (param temp) vs. Cold stream inlet to heater (variable temp: t_cold at stage 1 outlet)
                m.EMAT_HotUtility_Var.add(m.TOUT_hu_p[hu_key] - m.t_cold[c_key,1] >= m.EMAT_min)

                # Data validation check for fixed temperatures - NOT A PYOMO CONSTRAINT
                # Hot utility inlet (param temp) vs. Cold stream outlet from heater (param: final target)
                fixed_approach_hu = hu_data_check['TIN'] - c_data_check['TOUT']
                if fixed_approach_hu < data['EMAT_min']:
                    print(f"❗ WARNING: EMAT Data Inconsistency (Hot Utility Interface).")
                    print(f"  Hot Utility {hu_key} (TIN={hu_data_check['TIN']}) vs. Cold Stream {c_key} (Target TOUT={c_data_check['TOUT']})")
                    print(f"  Fixed Approach = {fixed_approach_hu:.2f} K < EMAT_min ({data['EMAT_min']:.2f} K).")
                    print(f"  This might indicate an issue with input data or chosen EMAT_min if this utility path is used.")
                    # Consider raising an error:
                    # raise ValueError(f"EMAT_min violation in input data: HU {hu_key} ({hu_data_check['TIN']}K) and CS {c_key} ({c_data_check['TOUT']}K) gives {fixed_approach_hu}K.")
    # --- End of EMAT Constraints ---

    # (LMTD Expressions, Area Expressions, Forbidden Matches, Objective, Initialization remain the same)
    # LMTD and Area calculations (Expressions)
    def lmtd_match_expr_rule(m,h,c,k):
        dt1 = smooth_max_zero(m.t_hot[h,k] - m.t_cold[c,k], m.EpsilonSmooth)
        dt2 = smooth_max_zero(m.t_hot[h,k+1] - m.t_cold[c,k+1], m.EpsilonSmooth)
        return (dt1 * dt2 * (dt1 + dt2) / 2.0)**(1/3.0) + m.DeltaLMTD
    m.LMTD_match = pe.Expression(m.HP, m.CP, m.STAGES, rule=lmtd_match_expr_rule)

    def area_match_expr_rule(m,h,c,k):
        u_val = m.U_match[h,c]
        if u_val < 1e-6 : return m.q_match[h,c,k] * 1e6
        return m.q_match[h,c,k] / (u_val * m.LMTD_match[h,c,k])
    m.Area_match = pe.Expression(m.HP, m.CP, m.STAGES, rule=area_match_expr_rule)

    def lmtd_cu_expr_rule(m,cu,h):
        dt1 = smooth_max_zero(m.t_hot[h,m.NOK_param+1] - m.TOUT_cu_p[cu], m.EpsilonSmooth)
        dt2 = smooth_max_zero(m.TOUT_h[h] - m.TIN_cu_p[cu], m.EpsilonSmooth) # This dt2 uses fixed params
        return (dt1 * dt2 * (dt1 + dt2) / 2.0)**(1/3.0) + m.DeltaLMTD
    m.LMTD_cu = pe.Expression(m.CU, m.HP, rule=lmtd_cu_expr_rule)

    def area_cu_expr_rule(m,cu,h):
        u_val = m.U_cu_match[cu,h]
        if u_val < 1e-6: return m.q_cu[cu,h] * 1e6
        return m.q_cu[cu,h] / (u_val * m.LMTD_cu[cu,h])
    m.Area_cu = pe.Expression(m.CU, m.HP, rule=area_cu_expr_rule)

    def lmtd_hu_expr_rule(m,hu,c):
        dt1 = smooth_max_zero(m.TOUT_hu_p[hu] - m.t_cold[c,1], m.EpsilonSmooth)
        dt2 = smooth_max_zero(m.TIN_hu_p[hu] - m.TOUT_c[c], m.EpsilonSmooth) # This dt2 uses fixed params
        return (dt1 * dt2 * (dt1 + dt2) / 2.0)**(1/3.0) + m.DeltaLMTD
    m.LMTD_hu = pe.Expression(m.HU, m.CP, rule=lmtd_hu_expr_rule)

    def area_hu_expr_rule(m,hu,c):
        u_val = m.U_hu_match[hu,c]
        if u_val < 1e-6: return m.q_hu[hu,c] * 1e6
        return m.q_hu[hu,c] / (u_val * m.LMTD_hu[hu,c])
    m.Area_hu = pe.Expression(m.HU, m.CP, rule=area_hu_expr_rule)

    if 'forbidden_matches' in data and data['forbidden_matches']:
        m.ForbiddenMatches = pe.ConstraintList()
        for h_f, c_f in data['forbidden_matches']:
            if h_f in m.HP and c_f in m.CP:
                for k_stage in m.STAGES:
                    m.ForbiddenMatches.add(m.q_match[h_f, c_f, k_stage] == 0)

    # --- Objective Function (NLP1) ---
    def objective_rule(m):
        cost = 0
        # Utility operating costs
        cost += sum(m.Cost_cu_p[cu] * m.q_cu[cu,h] for cu in m.CU for h in m.HP)
        cost += sum(m.Cost_hu_p[hu] * m.q_hu[hu,c] for hu in m.HU for c in m.CP)

        # Area capital costs for process exchangers
        for h_ in m.HP:
            for c_ in m.CP:
                for k_ in m.STAGES:
                    cost += m.AreaCostCoeff * (m.Area_match[h_,c_,k_]**m.AreaCostExponent)
        
        # Area capital costs for cold utility exchangers
        for cu_ in m.CU:
            for h_ in m.HP:
                cost += m.AreaCostCoeff * (m.Area_cu[cu_,h_]**m.AreaCostExponent)

        # Area capital costs for hot utility exchangers
        for hu_ in m.HU:
            for c_ in m.CP:
                cost += m.AreaCostCoeff * (m.Area_hu[hu_,c_]**m.AreaCostExponent)
        return cost
    m.Objective = pe.Objective(rule=objective_rule, sense=pe.minimize)

    # Initialization
    for h_ in m.HP:
        for c_ in m.CP:
            for k_ in m.STAGES:
                q_h_total = m.Fcp_h[h_] * (m.TIN_h[h_] - m.TOUT_h[h_])
                q_c_total = m.Fcp_c[c_] * (m.TOUT_c[c_] - m.TIN_c[c_])
                init_q_val = min(max(0, q_h_total), max(0, q_c_total)) / data['NOK']
                m.q_match[h_,c_,k_].value = init_q_val if init_q_val > 1e-6 else 0

    num_hu = len(m.HU) if len(m.HU) > 0 else 1
    num_cu = len(m.CU) if len(m.CU) > 0 else 1

    for hu_ in m.HU:
        for c_ in m.CP:
            val = 0.01 * m.Fcp_c[c_] * (m.TOUT_c[c_] - m.TIN_c[c_]) / num_hu
            m.q_hu[hu_,c_].value = max(0, val)
    for cu_ in m.CU:
        for h_ in m.HP:
            val = 0.01 * m.Fcp_h[h_] * (m.TIN_h[h_] - m.TOUT_h[h_]) / num_cu
            m.q_cu[cu_,h_].value = max(0, val)
            
    return m

# --- 3. Solver ---
def solve_model(model, solver_name='ipopt', tee=True):
    solver = SolverFactory(solver_name)
    # Common IPOPT options for difficult NLPs:
    # solver.options['nlp_scaling_method'] = 'gradient-based'
    # solver.options['max_iter'] = 500
    # solver.options['tol'] = 1e-7
    results = solver.solve(model, tee=tee)
    return results

# --- 4. Display Results ---
def display_results(m, results):
    print(f"\nSolver Status: {results.solver.status}, Termination: {results.solver.termination_condition}")
    if results.solver.termination_condition == pe.TerminationCondition.optimal or \
       results.solver.termination_condition == pe.TerminationCondition.locallyOptimal or \
       results.solver.termination_condition == pe.TerminationCondition.feasible: # Added feasible for cases where solver stops early but has a point
        
        obj_val = pe.value(m.Objective) 
        print(f"Optimal Objective Value: {obj_val:.2f} $/yr")

        total_q_cu_val = sum(pe.value(m.q_cu[cu,h]) for cu in m.CU for h in m.HP)
        total_q_hu_val = sum(pe.value(m.q_hu[hu,c]) for hu in m.HU for c in m.CP)
        cost_cu_total_val = sum(pe.value(m.Cost_cu_p[cu] * m.q_cu[cu,h]) for cu in m.CU for h in m.HP)
        cost_hu_total_val = sum(pe.value(m.Cost_hu_p[hu] * m.q_hu[hu,c]) for hu in m.HU for c in m.CP)
        
        print(f"\nTotal Cold Utility Used: {total_q_cu_val:.2f} kW, Cost: {cost_cu_total_val:.2f} $/yr")
        if len(m.CU) > 1 or len(m.CU) == 0: # Print breakdown if multiple CUs or none
            for cu_ in m.CU:
                q_this_cu = sum(pe.value(m.q_cu[cu_,h]) for h in m.HP)
                print(f"  - Utility {cu_}: {q_this_cu:.2f} kW")

        print(f"Total Hot Utility Used: {total_q_hu_val:.2f} kW, Cost: {cost_hu_total_val:.2f} $/yr")
        if len(m.HU) > 1 or len(m.HU) == 0: # Print breakdown if multiple HUs or none
            for hu_ in m.HU:
                q_this_hu = sum(pe.value(m.q_hu[hu_,c]) for c in m.CP)
                print(f"  - Utility {hu_}: {q_this_hu:.2f} kW")


        total_area_cost_val = 0
        print("\n--- Process Stream Matches ---")
        for k in m.STAGES:
            print(f"Stage {k}:")
            for h in m.HP:
                for c in m.CP:
                    q = pe.value(m.q_match[h,c,k])
                    if q > 1e-3: 
                        area = pe.value(m.Area_match[h,c,k])
                        lmtd = pe.value(m.LMTD_match[h,c,k])
                        area_cost = pe.value(m.AreaCostCoeff * (m.Area_match[h,c,k]**m.AreaCostExponent))
                        total_area_cost_val += area_cost
                        print(f"  Match {h}-{c}: Q={q:.2f} kW, Area={area:.2f} m^2, LMTD={lmtd:.2f} K, Cost={area_cost:.2f}")
                        print(f"    Hot Stream Temps: T_in(k)={pe.value(m.t_hot[h,k]):.2f} K, T_out(k)={pe.value(m.t_hot[h,k+1]):.2f} K")
                        print(f"    Cold Stream Temps: T_out(k)={pe.value(m.t_cold[c,k]):.2f} K, T_in(k)={pe.value(m.t_cold[c,k+1]):.2f} K")
        
        print("\n--- Cold Utility Matches ---")
        for cu in m.CU:
            for h in m.HP:
                q = pe.value(m.q_cu[cu,h])
                if q > 1e-3:
                    area = pe.value(m.Area_cu[cu,h])
                    lmtd = pe.value(m.LMTD_cu[cu,h])
                    area_cost = pe.value(m.AreaCostCoeff * (m.Area_cu[cu,h]**m.AreaCostExponent))
                    total_area_cost_val += area_cost
                    print(f"  Cooler {h}-{cu}: Q={q:.2f} kW, Area={area:.2f} m^2, LMTD={lmtd:.2f} K, Cost={area_cost:.2f}")
                    print(f"    Hot Stream Temps: T_in_util={pe.value(m.t_hot[h,m.NOK_param+1]):.2f} K, T_out_util={pe.value(m.TOUT_h[h]):.2f} K")
                    print(f"    Cold Util Temps: T_in_cu={pe.value(m.TIN_cu_p[cu]):.2f} K, T_out_cu={pe.value(m.TOUT_cu_p[cu]):.2f} K")

        print("\n--- Hot Utility Matches ---")
        for hu in m.HU:
            for c in m.CP:
                q = pe.value(m.q_hu[hu,c])
                if q > 1e-3:
                    area = pe.value(m.Area_hu[hu,c])
                    lmtd = pe.value(m.LMTD_hu[hu,c])
                    area_cost = pe.value(m.AreaCostCoeff * (m.Area_hu[hu,c]**m.AreaCostExponent))
                    total_area_cost_val += area_cost
                    print(f"  Heater {hu}-{c}: Q={q:.2f} kW, Area={area:.2f} m^2, LMTD={lmtd:.2f} K, Cost={area_cost:.2f}")
                    print(f"    Cold Stream Temps: T_in_util={pe.value(m.t_cold[c,1]):.2f} K, T_out_util={pe.value(m.TOUT_c[c]):.2f} K")
                    print(f"    Hot Util Temps: T_in_hu={pe.value(m.TIN_hu_p[hu]):.2f} K, T_out_hu={pe.value(m.TOUT_hu_p[hu]):.2f} K")
        
        print(f"\nTotal Area Cost: {total_area_cost_val:.2f} $/yr")
        calculated_total_cost = cost_cu_total_val + cost_hu_total_val + total_area_cost_val
        print(f"Calculated Total Annual Cost: {calculated_total_cost:.2f} $/yr (should match objective)")

        print("\nStream Temperatures at Stage Boundaries (Hot Streams t_hot[h, loc]):")
        for h in m.HP:
            temps = [f"{pe.value(m.t_hot[h,loc]):.2f}" for loc in m.TEMP_LOCS]
            print(f"  {h}: {', '.join(temps)} K (Locs 1 to {m.NOK_param+1})")

        print("\nStream Temperatures at Stage Boundaries (Cold Streams t_cold[c, loc]):")
        for c in m.CP:
            temps = [f"{pe.value(m.t_cold[c,loc]):.2f}" for loc in m.TEMP_LOCS]
            print(f"  {c}: {', '.join(temps)} K (Locs 1 to {m.NOK_param+1})")
            
    else:
        print("Solver did not find an optimal/feasible solution.")
        print(f"Solver message: {results.solver.message if hasattr(results.solver, 'message') else 'No message'}")
        # Optional: print variable values even if not optimal for debugging
        # m.display()


# --- Main execution ---
if __name__ == "__main__":
    input_data = load_data(None, None, None)
    
    # Example of adding a second cold utility to test multiple utility logic
    # input_data['cold_utilities_data']['W2'] = {'TIN': 280, 'TOUT': 290, 'Cost': 25, 'U_val': 1.8}
    # Note: If adding utilities, ensure m.CU set is re-initialized if model is rebuilt,
    # or ensure load_data is called before build_model. The current structure is fine.

    hen_model = build_model(input_data)
    print("Model Built.")
    
    # For debugging, you can write the model to an LP file
    # hen_model.write("hen_model.lp", io_options={'symbolic_solver_labels': True})

    print("Solving model...")
    solver_results = solve_model(hen_model, solver_name='ipopt', tee=True) 

    display_results(hen_model, solver_results)