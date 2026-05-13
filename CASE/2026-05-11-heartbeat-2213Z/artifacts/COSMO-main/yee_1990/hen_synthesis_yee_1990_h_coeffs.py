# --- hen_synthesis_yee_grossmann.py ---
import pandas as pd
import pyomo.environ as pyo
from pyomo.opt import SolverFactory
import json
import os

def load_data(base_path="yee_1990/ex1", 
              config_filename='config.json', 
              streams_filename='streams.csv', 
              utilities_filename='utilities.csv', 
              matches_U_cost_filename='matches_U_cost.csv', 
              forbidden_matches_filename='forbidden_matches.csv', 
              required_matches_filename='required_matches.csv'): # Add a base_path argument
    """Loads data from CSV files and config.json."""

    config_filepath = os.path.join(base_path, config_filename)
    streams_filepath = os.path.join(base_path, streams_filename) # Or make this dynamic
    utilities_filepath = os.path.join(base_path, utilities_filename) # Or make this dynamic
    matches_U_cost_filepath = os.path.join(base_path, matches_U_cost_filename) # Or make this dynamic
    forbidden_matches_filepath = os.path.join(base_path, forbidden_matches_filename)
    required_matches_filepath = os.path.join(base_path, required_matches_filename)

    data = {}
    
    # Load configuration from JSON
    try:
        with open(config_filepath, 'r') as f:
            config = json.load(f)
        data['config'] = config
        print(f"Loaded configuration from {config_filepath}")
    except FileNotFoundError:
        print(f"Warning: {config_filepath} not found. Using default fallback configuration.")
        # Fallback config if file not found (same as your previous dict)
        data['config'] = {
            'NOK': 'auto',
            'Epsilon_dt': 10.0, # Defaulting to a more stable Epsilon_dt
            'Omega_Q_factor': 2.0,
            'Omega_T': 200,    # Defaulting to a tighter Omega_T
            'Allow_Splits': True,
            'solver_name': 'couenne',
            'time_limit_seconds': 300
        }
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON from {config_filepath}. Please check its format.")


    df_streams = pd.read_csv(streams_filepath)
    data['streams'] = df_streams.set_index('Name').to_dict('index')
    
    data['HP'] = [s for s, props in data['streams'].items() if props['Type'] == 'Hot']
    data['CP'] = [s for s, props in data['streams'].items() if props['Type'] == 'Cold']

    df_utilities = pd.read_csv(utilities_filepath)
    data['utilities'] = df_utilities.set_index('Name').to_dict('index')
    data['HU'] = [u for u, props in data['utilities'].items() if props['Type'] == 'Hot_Utility']
    data['CU'] = [u for u, props in data['utilities'].items() if props['Type'] == 'Cold_Utility']
    
    df_matches_U = pd.read_csv(matches_U_cost_filepath)
    data['matches_U_cost'] = {}
    for _, row in df_matches_U.iterrows():
        data['matches_U_cost'][(row['Hot_Stream'], row['Cold_Stream'])] = {
            'U': row['U_overall'],
            'CF': row['Fixed_Cost_Unit'],
            'CA': row['Area_Cost_Coeff'],
            'CB': row['Area_Cost_Exp']
        }

    # Determine NOK from config or auto-calculate
    nok_config = data['config'].get('NOK', 'auto')
    if isinstance(nok_config, str) and nok_config.lower() == 'auto':
        data['NOK'] = max(len(data['HP']) if data['HP'] else 0, len(data['CP']) if data['CP'] else 0)
        if data['NOK'] == 0 and (data['HU'] or data['CU']):
             data['NOK'] = 1 
        elif data['NOK'] == 0:
            raise ValueError("No process streams defined and NOK cannot be determined.")
    elif isinstance(nok_config, int):
        data['NOK'] = nok_config
    else:
        raise ValueError(f"Invalid NOK value in config: {nok_config}. Must be 'auto' or an integer.")
        
    data['STAGES'] = list(range(1, data['NOK'] + 1))
    data['TEMP_LOCS'] = list(range(1, data['NOK'] + 2))

    # Estimate Omega_Q
    max_enthalpy_change = 0
    if not (data['HP'] or data['CP']): # No process streams
        if data['HU'] or data['CU']: # Only utilities
             # Base Omega_Q on some arbitrary large number or utility duties if estimable
             max_enthalpy_change = data['config'].get("Default_Omega_Q_For_Utilities_Only", 5000) 
        else: # No streams at all
            max_enthalpy_change = 0 # will lead to Omega_Q = 0 or default small value
    else:
        for s, props in data['streams'].items():
            enthalpy = abs(props['TIN_spec'] - props['TOUT_spec']) * props['Fcp']
            if enthalpy > max_enthalpy_change:
                max_enthalpy_change = enthalpy
    
    data['Omega_Q'] = data['config'].get('Omega_Q_factor', 1.5) * max_enthalpy_change
    if data['Omega_Q'] == 0 and (data['HP'] or data['CP'] or data['HU'] or data['CU']):
        default_omega_q = data['config'].get("Default_Omega_Q_If_Zero_Enthalpy", 1000)
        data['Omega_Q'] = default_omega_q 
        print(f"Warning: Max enthalpy change is 0. Setting Omega_Q to {data['Omega_Q']}. Check stream data if this is not expected.")

    # Load forbidden matches (optional)
    data['forbidden_matches'] = []
    if os.path.exists(forbidden_matches_filepath):
        try:
            df_forbidden = pd.read_csv(forbidden_matches_filepath)
            if not df_forbidden.empty:
                for _, row in df_forbidden.iterrows():
                    # Assuming columns are 'Hot_Stream', 'Cold_Stream_Or_Utility'
                    # You might add a 'Stage' column if forbidding in specific stages
                    data['forbidden_matches'].append((row['Hot_Stream'], row['Cold_Stream_Or_Utility']))
                print(f"Loaded {len(data['forbidden_matches'])} forbidden matches from {forbidden_matches_filepath}")
        except pd.errors.EmptyDataError:
            print(f"{forbidden_matches_filepath} is empty. No forbidden matches loaded.")
        except Exception as e:
            print(f"Warning: Could not load or parse {forbidden_matches_filepath}. Error: {e}")
    else:
        print(f"{forbidden_matches_filepath} not found. No forbidden matches loaded.")

    # Load required matches (optional)
    data['required_matches'] = {} # Dict: {(h,c): {'Min_Q_Total': val}}
    if os.path.exists(required_matches_filepath):
        try:
            df_required = pd.read_csv(required_matches_filepath)
            if not df_required.empty:
                for _, row in df_required.iterrows():
                     # Assuming 'Hot_Stream', 'Cold_Stream', 'Min_Q_Total'
                    data['required_matches'][(row['Hot_Stream'], row['Cold_Stream'])] = {'Min_Q_Total': row['Min_Q_Total']}
                print(f"Loaded {len(data['required_matches'])} required matches from {required_matches_filepath}")
        except pd.errors.EmptyDataError:
            print(f"{required_matches_filepath} is empty. No required matches loaded.")
        except Exception as e:
            print(f"Warning: Could not load or parse {required_matches_filepath}. Error: {e}")
    else:
        print(f"{required_matches_filepath} not found. No required matches loaded.")
        
    return data

def build_hen_model(data):
    """Builds the Pyomo MINLP model."""
    model = pyo.ConcreteModel(name="HEN_Yee_Grossmann")
    
    # --- SETS ---
    model.HP = pyo.Set(initialize=data['HP'])
    model.CP = pyo.Set(initialize=data['CP'])
    model.HU = pyo.Set(initialize=data['HU'])
    model.CU = pyo.Set(initialize=data['CU'])
    model.STAGES = pyo.Set(initialize=data['STAGES'])
    model.TEMP_LOCS = pyo.Set(initialize=data['TEMP_LOCS'])

    # --- PARAMETERS ---
    model.TIN_spec = pyo.Param(model.HP | model.CP, initialize={s: data['streams'][s]['TIN_spec'] for s in model.HP | model.CP})
    model.TOUT_spec = pyo.Param(model.HP | model.CP, initialize={s: data['streams'][s]['TOUT_spec'] for s in model.HP | model.CP})
    model.Fcp = pyo.Param(model.HP | model.CP, initialize={s: data['streams'][s]['Fcp'] for s in model.HP | model.CP})

    model.TIN_utility = pyo.Param(model.HU | model.CU, initialize={u: data['utilities'][u]['TIN_utility'] for u in model.HU | model.CU})
    model.TOUT_utility = pyo.Param(model.HU | model.CU, initialize={u: data['utilities'][u]['TOUT_utility'] for u in model.HU | model.CU}) # Outlet utility temp (e.g. for LMTD calc)
    model.Cost_Unit_Energy_CU = pyo.Param(model.CU, initialize={u: data['utilities'][u]['Unit_Cost_Energy'] for u in model.CU})
    model.Cost_Unit_Energy_HU = pyo.Param(model.HU, initialize={u: data['utilities'][u]['Unit_Cost_Energy'] for u in model.HU})

    # Match/Exchanger specific parameters
    def U_match_init(m, h, c): return data['matches_U_cost'][(h,c)]['U']
    model.U_match = pyo.Param(model.HP, model.CP, initialize=U_match_init)
    def CF_match_init(m, h, c): return data['matches_U_cost'][(h,c)]['CF']
    model.CF_match = pyo.Param(model.HP, model.CP, initialize=CF_match_init)
    def CA_match_init(m, h, c): return data['matches_U_cost'][(h,c)]['CA']
    model.CA_match = pyo.Param(model.HP, model.CP, initialize=CA_match_init)
    def CB_match_init(m, h, c): return data['matches_U_cost'][(h,c)]['CB']
    model.CB_match = pyo.Param(model.HP, model.CP, initialize=CB_match_init)

    model.U_cu = pyo.Param(model.HP, model.CU, initialize={(h,cu): data['utilities'][cu]['U_overall'] for h in model.HP for cu in model.CU})
    model.CF_cu = pyo.Param(model.HP, model.CU, initialize={(h,cu): data['utilities'][cu]['Fixed_Cost_Unit'] for h in model.HP for cu in model.CU})
    model.CA_cu = pyo.Param(model.HP, model.CU, initialize={(h,cu): data['utilities'][cu]['Area_Cost_Coeff'] for h in model.HP for cu in model.CU})
    model.CB_cu = pyo.Param(model.HP, model.CU, initialize={(h,cu): data['utilities'][cu]['Area_Cost_Exp'] for h in model.HP for cu in model.CU})
    
    model.U_hu = pyo.Param(model.CP, model.HU, initialize={(c,hu): data['utilities'][hu]['U_overall'] for c in model.CP for hu in model.HU})
    model.CF_hu = pyo.Param(model.CP, model.HU, initialize={(c,hu): data['utilities'][hu]['Fixed_Cost_Unit'] for c in model.CP for hu in model.HU})
    model.CA_hu = pyo.Param(model.CP, model.HU, initialize={(c,hu): data['utilities'][hu]['Area_Cost_Coeff'] for c in model.CP for hu in model.HU})
    model.CB_hu = pyo.Param(model.CP, model.HU, initialize={(c,hu): data['utilities'][hu]['Area_Cost_Exp'] for c in model.CP for hu in model.HU})

    model.NOK = data['NOK']
    model.Omega_Q = data['Omega_Q']
    model.Omega_T = data['config'].get('Omega_T', 500) # For inactive match dt
    model.Epsilon_dt = data['config'].get('Epsilon_dt', 10.0) # Min approach temp

    # --- VARIABLES ---
    # Temperatures at each location
    # Bounds: Consider min/max possible temperatures in the system
    # For simplicity, using a wide range; tighten if possible.
    min_sys_T = min(min(props['TIN_spec'], props['TOUT_spec']) for s, props in data['streams'].items())
    max_sys_T = max(max(props['TIN_spec'], props['TOUT_spec']) for s, props in data['streams'].items())
    min_util_T = min(props['TIN_utility'] for u, props in data['utilities'].items()) if data['utilities'] else min_sys_T
    max_util_T = max(props['TIN_utility'] for u, props in data['utilities'].items()) if data['utilities'] else max_sys_T
    
    abs_min_T = min(min_sys_T, min_util_T) - 20 # buffer
    abs_max_T = max(max_sys_T, max_util_T) + 20 # buffer

    model.t_hot = pyo.Var(model.HP, model.TEMP_LOCS, domain=pyo.NonNegativeReals, bounds=(abs_min_T, abs_max_T))
    model.t_cold = pyo.Var(model.CP, model.TEMP_LOCS, domain=pyo.NonNegativeReals, bounds=(abs_min_T, abs_max_T))

    # Heat loads
    model.q_match = pyo.Var(model.HP, model.CP, model.STAGES, domain=pyo.NonNegativeReals, bounds=(0, model.Omega_Q))
    model.q_cu = pyo.Var(model.HP, model.CU, domain=pyo.NonNegativeReals, bounds=(0, model.Omega_Q))
    model.q_hu = pyo.Var(model.CP, model.HU, domain=pyo.NonNegativeReals, bounds=(0, model.Omega_Q))

    # Binary variables for existence of matches/utility use
    model.z_match = pyo.Var(model.HP, model.CP, model.STAGES, domain=pyo.Binary)
    model.z_cu = pyo.Var(model.HP, model.CU, domain=pyo.Binary)
    model.z_hu = pyo.Var(model.CP, model.HU, domain=pyo.Binary)

    # Approach temperatures for LMTD calculation
    # For a match (i,j) in stage k (between temp_loc k and k+1)
    model.dt_match_s1 = pyo.Var(model.HP, model.CP, model.STAGES, domain=pyo.NonNegativeReals, bounds=(model.Epsilon_dt, model.Omega_T)) # Approach at t_hot[i,k], t_cold[j,k]
    model.dt_match_s2 = pyo.Var(model.HP, model.CP, model.STAGES, domain=pyo.NonNegativeReals, bounds=(model.Epsilon_dt, model.Omega_T)) # Approach at t_hot[i,k+1], t_cold[j,k+1]
    
    model.dt_cu_s1 = pyo.Var(model.HP, model.CU, domain=pyo.NonNegativeReals, bounds=(model.Epsilon_dt, model.Omega_T)) # t_hot[i,NOK+1] - TOUT_utility[cu]
    # dt_cu_s2 is TOUT_spec[i] - TIN_utility[cu] - this is a parameter/expression if TOUT_spec[i] is fixed
    
    model.dt_hu_s1 = pyo.Var(model.CP, model.HU, domain=pyo.NonNegativeReals, bounds=(model.Epsilon_dt, model.Omega_T)) # TIN_utility[hu] - t_cold[j,1]
    # dt_hu_s2 is TOUT_utility[hu] - TOUT_spec[j] - this is a parameter/expression
    
    # Inside build_hen_model, after loading stream and utility data including h_coeffs

    # For Process-Process Matches
    def U_match_init_calc(m, h, c):
        h_hot = data['streams'][h]['h_coeff']
        h_cold = data['streams'][c]['h_coeff']
        if h_hot == 0 or h_cold == 0: # Avoid division by zero if h_coeff is missing or zero
            return 1e-6 # A very small U, effectively no heat transfer
        return 1.0 / ( (1.0/h_hot) + (1.0/h_cold) )
    model.U_match = pyo.Param(model.HP, model.CP, initialize=U_match_init_calc)

    # For Process-Cold Utility Matches
    def U_cu_init_calc(m, h, cu):
        h_proc = data['streams'][h]['h_coeff']
        h_util = data['utilities'][cu]['h_coeff']
        if h_proc == 0 or h_util == 0:
            return 1e-6
        return 1.0 / ( (1.0/h_proc) + (1.0/h_util) )
    model.U_cu = pyo.Param(model.HP, model.CU, initialize=U_cu_init_calc)

    # For Process-Hot Utility Matches
    def U_hu_init_calc(m, c, hu):
        h_proc = data['streams'][c]['h_coeff']
        h_util = data['utilities'][hu]['h_coeff']
        if h_proc == 0 or h_util == 0:
            return 1e-6
        return 1.0 / ( (1.0/h_proc) + (1.0/h_util) )
    model.U_hu = pyo.Param(model.CP, model.HU, initialize=U_hu_init_calc)

    # Cost parameters CF, CA, CB would still be initialized from the CSVs as before
    # model.CF_match = pyo.Param(model.HP, model.CP, initialize=lambda m,h,c: data['matches_U_cost'][(h,c)]['CF'])
    # etc.

    # Actual outlet temperatures (if variable, otherwise these are fixed by TOUT_spec)
    # Example: model.TOUT_actual_H1 = pyo.Var(bounds=(data['streams']['H1']['TOUT_min'], data['streams']['H1']['TOUT_max']))
    # For now, assume fixed TIN_spec, TOUT_spec for overall balance. Can be extended.

    # --- CONSTRAINTS ---
    # Eq. 1: Overall Heat Balance (Implicitly handled by stagewise and utility balances if TIN/TOUT are fixed)
    # If TIN/TOUT are variables, this equation is needed. For now, assume fixed.
    # (TIN_spec[i] - TOUT_spec[i]) * Fcp[i] == sum(q_match...) + q_cu...

    # Eq. 2: Heat Balance at Each Stage
    def stage_balance_hot_rule(m, i, k): # i in HP, k in STAGES
        return (m.t_hot[i,k] - m.t_hot[i,k+1]) * m.Fcp[i] == sum(m.q_match[i,j,k] for j in m.CP)
    model.stage_balance_hot = pyo.Constraint(model.HP, model.STAGES, rule=stage_balance_hot_rule)

    def stage_balance_cold_rule(m, j, k): # j in CP, k in STAGES
        return (m.t_cold[j,k] - m.t_cold[j,k+1]) * m.Fcp[j] == sum(m.q_match[i,j,k] for i in m.HP)
    model.stage_balance_cold = pyo.Constraint(model.CP, model.STAGES, rule=stage_balance_cold_rule)
    
    # Eq. 3: Assignment of Superstructure Inlet Temperatures
    def superstructure_inlet_hot_rule(m, i): # i in HP
        return m.t_hot[i,1] == m.TIN_spec[i]
    model.superstructure_inlet_hot = pyo.Constraint(model.HP, rule=superstructure_inlet_hot_rule)

    def superstructure_inlet_cold_rule(m, j): # j in CP
        return m.t_cold[j, m.NOK+1] == m.TIN_spec[j]
    model.superstructure_inlet_cold = pyo.Constraint(model.CP, rule=superstructure_inlet_cold_rule)

    # Eq. 4: Feasibility of Temperatures (Monotonicity)
    def temp_mono_hot_rule(m, i, k_loc): # i in HP, k_loc in STAGES (i.e. 1 to NOK)
        return m.t_hot[i, k_loc] >= m.t_hot[i, k_loc+1] + m.Epsilon_dt/1000 # small epsilon to avoid strict equality issues
    model.temp_mono_hot = pyo.Constraint(model.HP, model.STAGES, rule=temp_mono_hot_rule)
    
    def temp_mono_cold_rule(m, j, k_loc): # j in CP, k_loc in STAGES
        # Cold stream: t_cold[j,k] is "hotter" than t_cold[j,k+1]
        return m.t_cold[j, k_loc] >= m.t_cold[j, k_loc+1] + m.Epsilon_dt/1000
    model.temp_mono_cold = pyo.Constraint(model.CP, model.STAGES, rule=temp_mono_cold_rule)

    # Outlet process temperatures before utility
    def hot_outlet_before_cu_rule(m,i): # i in HP
        return m.t_hot[i, m.NOK+1] >= m.TOUT_spec[i]
    model.hot_outlet_before_cu = pyo.Constraint(model.HP, rule=hot_outlet_before_cu_rule)
    
    def cold_outlet_before_hu_rule(m,j): # j in CP
        return m.t_cold[j,1] <= m.TOUT_spec[j]
    model.cold_outlet_before_hu = pyo.Constraint(model.CP, rule=cold_outlet_before_hu_rule)

    # Eq. 5: Hot and Cold Utility Load
    def cu_load_rule(m, i): # i in HP
        return (m.t_hot[i, m.NOK+1] - m.TOUT_spec[i]) * m.Fcp[i] == sum(m.q_cu[i,cu] for cu in m.CU)
    model.cu_load = pyo.Constraint(model.HP, rule=cu_load_rule)

    def hu_load_rule(m, j): # j in CP
        return (m.TOUT_spec[j] - m.t_cold[j,1]) * m.Fcp[j] == sum(m.q_hu[j,hu] for hu in m.HU)
    model.hu_load = pyo.Constraint(model.CP, rule=hu_load_rule)

    # Eq. 6: Logical Constraints for Match Existence
    def q_match_logic_rule(m,i,j,k):
        return m.q_match[i,j,k] <= m.Omega_Q * m.z_match[i,j,k]
    model.q_match_logic = pyo.Constraint(model.HP, model.CP, model.STAGES, rule=q_match_logic_rule)

    def q_cu_logic_rule(m,i,cu):
        return m.q_cu[i,cu] <= m.Omega_Q * m.z_cu[i,cu]
    model.q_cu_logic = pyo.Constraint(model.HP, model.CU, rule=q_cu_logic_rule)

    def q_hu_logic_rule(m,j,hu):
        return m.q_hu[j,hu] <= m.Omega_Q * m.z_hu[j,hu]
    model.q_hu_logic = pyo.Constraint(model.CP, model.HU, rule=q_hu_logic_rule)

    # Eq. 7 & 8: Calculation of Approach Temperatures and EMAT
    # dt_match_s1 is approach at (t_hot[i,k], t_cold[j,k]) for stage k
    def dt_match_s1_rule(m,i,j,k):
        return m.dt_match_s1[i,j,k] <= m.t_hot[i,k] - m.t_cold[j,k] + m.Omega_T * (1 - m.z_match[i,j,k])
    model.dt_match_s1_constr = pyo.Constraint(model.HP, model.CP, model.STAGES, rule=dt_match_s1_rule)
    
    # dt_match_s2 is approach at (t_hot[i,k+1], t_cold[j,k+1]) for stage k
    def dt_match_s2_rule(m,i,j,k):
        return m.dt_match_s2[i,j,k] <= m.t_hot[i,k+1] - m.t_cold[j,k+1] + m.Omega_T * (1 - m.z_match[i,j,k])
    model.dt_match_s2_constr = pyo.Constraint(model.HP, model.CP, model.STAGES, rule=dt_match_s2_rule)

    # For utilities
    # dt_cu_s1 is t_hot[i,NOK+1] - TOUT_utility[cu]
    def dt_cu_s1_rule(m,i,cu):
        return m.dt_cu_s1[i,cu] <= m.t_hot[i,m.NOK+1] - m.TOUT_utility[cu] + m.Omega_T * (1 - m.z_cu[i,cu])
    model.dt_cu_s1_constr = pyo.Constraint(model.HP, model.CU, rule=dt_cu_s1_rule)
    # The other approach for CU is dt_cu_s2 = TOUT_spec[i] - TIN_utility[cu] (parameter or expression)
    
    # dt_hu_s1 is TIN_utility[hu] - t_cold[j,1]
    def dt_hu_s1_rule(m,j,hu):
        return m.dt_hu_s1[j,hu] <= m.TIN_utility[hu] - m.t_cold[j,1] + m.Omega_T * (1 - m.z_hu[j,hu])
    model.dt_hu_s1_constr = pyo.Constraint(model.CP, model.HU, rule=dt_hu_s1_rule)
    # The other approach for HU is dt_hu_s2 = TOUT_utility[hu] - TOUT_spec[j] (parameter or expression)
    
    # ADD THE FEASIBILITY CONSTRAINTS FOR dt2 OF UTILITIES:
    def dt2_cu_feasibility_rule(m, i, cu):
        # If z_cu is 1, then TOUT_spec[i] - TIN_utility[cu] must be >= Epsilon_dt
        dt2_val = m.TOUT_spec[i] - m.TIN_utility[cu]
        # This constraint means: if z_cu[i,cu] = 1, then dt2_val >= m.Epsilon_dt
        # If z_cu[i,cu] = 0, then dt2_val >= m.Epsilon_dt - m.Omega_T (relaxed)
        return dt2_val + m.Omega_T * (1 - m.z_cu[i,cu]) >= m.Epsilon_dt
    model.dt2_cu_feasibility = pyo.Constraint(model.HP, model.CU, rule=dt2_cu_feasibility_rule)

    def dt2_hu_feasibility_rule(m, j, hu):
        # If z_hu is 1, then TOUT_utility[hu] - TOUT_spec[j] must be >= Epsilon_dt
        dt2_val = m.TOUT_utility[hu] - m.TOUT_spec[j]
        return dt2_val + m.Omega_T * (1 - m.z_hu[j,hu]) >= m.Epsilon_dt
    model.dt2_hu_feasibility = pyo.Constraint(model.CP, model.HU, rule=dt2_hu_feasibility_rule)
    
    # Eq. 10: Optional No Stream Splits
    if not data['config'].get('Allow_Splits', True):
        def no_split_hot_rule(m, i, k):
            return sum(m.z_match[i,j,k] for j in m.CP) <= 1
        model.no_split_hot = pyo.Constraint(model.HP, model.STAGES, rule=no_split_hot_rule)
        
        def no_split_cold_rule(m, j, k):
            return sum(m.z_match[i,j,k] for i in m.HP) <= 1
        model.no_split_cold = pyo.Constraint(model.CP, model.STAGES, rule=no_split_cold_rule)

    # Make sure constraints like dt2_feasibility use model.Epsilon_dt_param and model.Omega_T_param
    # Example for temp_mono rules:
    def temp_mono_hot_rule(m, i, k_loc):
        return m.t_hot[i, k_loc] >= m.t_hot[i, k_loc+1] # Removed + m.Epsilon_dt/1000
    model.temp_mono_hot = pyo.Constraint(model.HP, model.STAGES, rule=temp_mono_hot_rule)
    
    def temp_mono_cold_rule(m, j, k_loc):
        return m.t_cold[j, k_loc] >= m.t_cold[j, k_loc+1] # Removed + m.Epsilon_dt/1000
    model.temp_mono_cold = pyo.Constraint(model.CP, model.STAGES, rule=temp_mono_cold_rule)

    # Apply Forbidden Matches
    for h_forbid, c_forbid_util in data.get('forbidden_matches', []):
        # Check if h_forbid and c_forbid_util are valid stream/utility names
        # to prevent KeyError if names in CSV don't match model sets
        if h_forbid in model.HP:
            if c_forbid_util in model.CP: # Process-Process
                for k_forbid in model.STAGES:
                    # Ensure the specific index is valid for z_match before trying to fix
                    if (h_forbid, c_forbid_util, k_forbid) in model.z_match:
                         model.z_match[h_forbid, c_forbid_util, k_forbid].fix(0)
            elif c_forbid_util in model.CU: # Process-ColdUtil
                if (h_forbid, c_forbid_util) in model.z_cu:
                    model.z_cu[h_forbid, c_forbid_util].fix(0)
            # Add elif for CP-HU if that's a possible forbidden type
            # Example: if h_forbid is a Cold Process stream, and c_forbid_util is a Hot Utility
            # This case is less common for "Hot_Stream" column in CSV, so naming might need adjustment
    
    # Apply Required Matches (Total Q Constraint)
    model.required_q_constraints = pyo.ConstraintList() # Define ConstraintList on the model
    for (h_req, c_req), props in data.get('required_matches', {}).items():
        if h_req in model.HP and c_req in model.CP: # Check if streams exist in the model sets
            min_q_total = props.get('Min_Q_Total', 0)
            if min_q_total > 0:
                # Sum of q_match for all stages for the specific pair (h_req, c_req)
                # Ensure that q_match is indexed correctly and exists for these streams
                try:
                    expr = sum(model.q_match[h_req, c_req, k_stage] for k_stage in model.STAGES) >= min_q_total
                    model.required_q_constraints.add(expr)
                    print(f"Added required match constraint: {h_req}-{c_req} >= {min_q_total} kW total")
                except KeyError:
                    print(f"Warning: Could not create required match constraint for {h_req}-{c_req}. Check stream names and model indexing.")
                    
    # --- OBJECTIVE FUNCTION (Eq. 9) ---
    def area_cost_term_expression(m, q, U, dt1, dt2, CA, CB, z_var):
        """
        Returns a Pyomo expression for the area-dependent capital cost for one exchanger.
        This function is called during model construction, so it must return expressions,
        not evaluate numeric values.
        """

        # dt1 and dt2 are variables bounded by m.Epsilon_dt, so they are >= small_positive_value

        # Chen's LMTD approximation term: (dt1 * dt2 * (dt1+dt2)/2)^(1/3)
        # Ensure the base of the power is non-negative. Since dt1, dt2 >= Epsilon_dt,
        # dt1*dt2 will be positive, and dt1+dt2 will be positive.
        # So, (dt1 * dt2 * (dt1 + dt2) / 2) will be positive.
        lmtd_factor_base = (dt1 * dt2 * (dt1 + dt2) / 2.0)
        
        # Add a small epsilon to the base to prevent issues if it's numerically zero,
        # although dt bounds should prevent this.
        # And to ensure the argument to power is always > 0 for fractional exponents.
        lmtd_factor = (lmtd_factor_base + 1e-9)**(1/3.0) 

        # Denominator for area calculation
        # Add small epsilon to prevent division by zero if lmtd_factor or U is zero
        # (though U is a param, and lmtd_factor should be positive)
        denominator_for_area = (lmtd_factor * U) + 1e-9

        # Area expression: q / denominator_for_area
        # q is also a variable. If z_var is 0, q should be 0 due to logical constraints.
        # So, if z_var=0, area should effectively be 0.
        area_expr = q / denominator_for_area
        
        # Cost expression: CA * area_expr**CB
        # To handle area_expr potentially being zero for non-active units (where q=0):
        # If CB < 0, (0)**CB is undefined. If CB is fractional, base must be non-negative.
        # Area_expr should be >= 0 since q >=0 and denominator > 0.
        # Add a small epsilon to area_expr before power to avoid 0**negative_power if CB could be <1 and area is 0.
        # However, if q=0, then area_expr = 0. Cost should be 0.
        # Multiplying by z_var at the end handles this: if z_var=0, entire cost term is 0.
        # If z_var=1, then q might be >0, area_expr >0.
        
        # To be very safe with the power function for area_expr**CB when area_expr might be zero:
        # (area_expr + epsilon_for_power_base)**CB
        # But since we multiply by z_var, if z_var=0, q=0, area_expr=0, and z_var*cost = 0.
        # If z_var=1, q can be >0, so area_expr should be >0.
        epsilon_for_power_base = 1e-6 # Small epsilon to avoid issues with zero base in power

        cost_for_active_unit = CA * ( (area_expr + epsilon_for_power_base)**CB ) # Add small epsilon to base of power

        # The entire cost term is only active if z_var is 1.
        return cost_for_active_unit * z_var

    # Utility cost expression
    utility_cost_expr = sum(model.Cost_Unit_Energy_CU[cu] * model.q_cu[i,cu] for i in model.HP for cu in model.CU) + \
                        sum(model.Cost_Unit_Energy_HU[hu] * model.q_hu[j,hu] for j in model.CP for hu in model.HU)
            
    # Fixed charges expression
    fixed_charges_expr = sum(model.CF_match[i,j] * model.z_match[i,j,k] for i in model.HP for j in model.CP for k in model.STAGES) + \
                         sum(model.CF_cu[i,cu] * model.z_cu[i,cu] for i in model.HP for cu in model.CU) + \
                         sum(model.CF_hu[j,hu] * model.z_hu[j,hu] for j in model.CP for hu in model.HU)

    # Capital cost (area-dependent) expression
    process_capital_cost_area_expr = 0 
    for i in model.HP:
        for j in model.CP:
            for k in model.STAGES:
                process_capital_cost_area_expr += area_cost_term_expression(
                                                model, model.q_match[i,j,k], model.U_match[i,j], 
                                                model.dt_match_s1[i,j,k], model.dt_match_s2[i,j,k],
                                                model.CA_match[i,j], model.CB_match[i,j], model.z_match[i,j,k])
    cold_utilities_capital_cost_area_expr = 0
    for i in model.HP:
        for cu in model.CU:
            # This expression represents the "other end" delta T for the cold utility exchanger
            dt2_cu_expr = model.TOUT_spec[i] - model.TIN_utility[cu] 
            # The feasibility constraint dt2_cu_feasibility ensures dt2_cu_expr >= Epsilon_dt if z_cu[i,cu] = 1

            cold_utilities_capital_cost_area_expr += area_cost_term_expression(
                                                model, model.q_cu[i,cu], model.U_cu[i,cu],
                                                model.dt_cu_s1[i,cu], dt2_cu_expr, # Pass the direct expression
                                                model.CA_cu[i,cu], model.CB_cu[i,cu], model.z_cu[i,cu])
    hot_utilities_capital_cost_area_expr = 0
    for j in model.CP:
        for hu in model.HU:
            # This expression represents the "other end" delta T for the hot utility exchanger
            dt2_hu_expr = model.TOUT_utility[hu] - model.TOUT_spec[j]
            # The feasibility constraint dt2_hu_feasibility ensures dt2_hu_expr >= Epsilon_dt if z_hu[j,hu] = 1

            hot_utilities_capital_cost_area_expr += area_cost_term_expression(
                                                model, model.q_hu[j,hu], model.U_hu[j,hu],
                                                model.dt_hu_s1[j,hu], dt2_hu_expr, # Pass the direct expression
                                                model.CA_hu[j,hu], model.CB_hu[j,hu], model.z_hu[j,hu])

    # Objective function: Minimize total annual cost
    objective_expr = utility_cost_expr + fixed_charges_expr #+ process_capital_cost_area_expr #+ cold_utilities_capital_cost_area_expr + hot_utilities_capital_cost_area_expr

    model.total_annual_cost = pyo.Objective(
        expr = objective_expr,
        sense = pyo.minimize
    )
    return model

def solve_hen_model(model, solver_name='couenne', tee=True, time_limit=None):
    """Solves the Pyomo model."""
    solver = SolverFactory(solver_name)
    if time_limit:
        if solver_name.lower() in ['gurobi', 'cplex']: # Check specific solver options
            solver.options['TimeLimit'] = time_limit
        elif solver_name.lower() in ['couenne', 'bonmin', 'scip']: # Generic option often 'maxtime' or similar
             # Couenne uses 'max_cpu_time' or simply relies on external timer for non-commercial
             # For open source, time limits might be harder to enforce directly via pyomo options consistently.
             # Example for SCIP: solver.options['limits/time'] = time_limit
             solver.options['max_cpu_time'] = time_limit
    else:
             pass # Add specific options if known for the solver
    results = solver.solve(model, tee=tee)
    return results

def report_results(model, data):
    """Prints a summary of the results."""
    # ... (Solver status, Total Annual Cost, Cost Breakdown, Active Matches, Utility Usage - all same as before) ...
    
    print(f"\n--- Solver Status: {model.results.solver.status}, Termination: {model.results.solver.termination_condition} ---")
    if model.results.solver.termination_condition != pyo.TerminationCondition.optimal and \
       model.results.solver.termination_condition != pyo.TerminationCondition.feasible and \
       model.results.solver.termination_condition != pyo.TerminationCondition.locallyOptimal and \
       model.results.solver.termination_condition != pyo.TerminationCondition.globallyOptimal : # common for MINLP
        print("Warning: Optimal/Feasible solution not found or solver terminated prematurely.")
        # You might want to still try and print whatever values are available if the solver found something
        # but for now, let's assume we proceed if it's at least feasible or optimal-like.
        # return # Optionally exit if no good solution

    try:
        print(f"Total Annual Cost: {pyo.value(model.total_annual_cost):.2f}")

        # Calculate and print cost breakdown
        utility_cost_val = 0
        for i in model.HP:
            for cu in model.CU: utility_cost_val += pyo.value(model.Cost_Unit_Energy_CU[cu] * model.q_cu[i,cu])
        for j in model.CP:
            for hu in model.HU: utility_cost_val += pyo.value(model.Cost_Unit_Energy_HU[hu] * model.q_hu[j,hu])
        print(f"  Utility Cost: {utility_cost_val:.2f}")

        fixed_charges_val = 0
        for i in model.HP:
            for j in model.CP:
                for k in model.STAGES: fixed_charges_val += pyo.value(model.CF_match[i,j] * model.z_match[i,j,k])
        for i in model.HP:
            for cu in model.CU: fixed_charges_val += pyo.value(model.CF_cu[i,cu] * model.z_cu[i,cu])
        for j in model.CP:
            for hu in model.HU: fixed_charges_val += pyo.value(model.CF_hu[j,hu] * model.z_hu[j,hu])
        print(f"  Fixed Charges: {fixed_charges_val:.2f}")
        
        # Ensure total_annual_cost has a value before trying to subtract from it
        total_cost_val = pyo.value(model.total_annual_cost)
        capital_cost_area_val = total_cost_val - utility_cost_val - fixed_charges_val
        print(f"  Area-dependent Capital Cost: {capital_cost_area_val:.2f}")


        print("\n--- Active Process Matches (z_match=1) ---")
        # ... (same as before) ...
        for i in model.HP:
            for j in model.CP:
                for k in model.STAGES:
                    if pyo.value(model.z_match[i,j,k]) > 0.5:
                        q_val = pyo.value(model.q_match[i,j,k])
                        dt1_val = pyo.value(model.dt_match_s1[i,j,k])
                        dt2_val = pyo.value(model.dt_match_s2[i,j,k])
                        U_val = pyo.value(model.U_match[i,j])
                        area_val = 0
                        if q_val > 1e-6: # Avoid issues if q is effectively zero
                            lmtd_factor_base_val = (dt1_val * dt2_val * (dt1_val + dt2_val) / 2.0)
                            if lmtd_factor_base_val > 1e-9: # Avoid root of zero/negative
                                lmtd_factor_val = (lmtd_factor_base_val)**(1/3.0)
                                denominator_val = (lmtd_factor_val * U_val)
                                if denominator_val > 1e-9: # Avoid division by zero
                                    area_val = q_val / denominator_val
                        
                        print(f"  H:{i}-C:{j} in Stage {k}: Q={q_val:.2f}, Area={area_val:.2f}, "+
                            f"dt1={dt1_val:.2f} (at T_h={pyo.value(model.t_hot[i,k]):.2f}, T_c={pyo.value(model.t_cold[j,k]):.2f}), "+
                            f"dt2={dt2_val:.2f} (at T_h={pyo.value(model.t_hot[i,k+1]):.2f}, T_c={pyo.value(model.t_cold[j,k+1]):.2f})")

        print("\n--- Active Cold Utility Usage (z_cu=1) ---")
        # ... (same as before, ensure area calculation is robust) ...
        for i in model.HP:
            for cu in model.CU:
                if pyo.value(model.z_cu[i,cu]) > 0.5:
                    q_val = pyo.value(model.q_cu[i,cu])
                    dt1_val = pyo.value(model.dt_cu_s1[i,cu])
                    dt2_val = pyo.value(model.TOUT_spec[i] - model.TIN_utility[cu])
                    U_val = pyo.value(model.U_cu[i,cu])
                    area_val = 0
                    if q_val > 1e-6 and dt1_val > 0 and dt2_val > 0: # Basic check for LMTD validity
                        lmtd_factor_base_val = (dt1_val * dt2_val * (dt1_val + dt2_val) / 2.0)
                        if lmtd_factor_base_val > 1e-9:
                            lmtd_factor_val = (lmtd_factor_base_val)**(1/3.0)
                            denominator_val = (lmtd_factor_val * U_val)
                            if denominator_val > 1e-9:
                                area_val = q_val / denominator_val
                    print(f"  H:{i} with CU:{cu}: Q={q_val:.2f}, Area={area_val:.2f}, "+
                        f"dt1={dt1_val:.2f} (Th_in_cooler={pyo.value(model.t_hot[i,model.NOK+1]):.2f}, Tcu_out={pyo.value(model.TOUT_utility[cu]):.2f}), "+
                        f"dt2={dt2_val:.2f} (Th_out_cooler={pyo.value(model.TOUT_spec[i]):.2f}, Tcu_in={pyo.value(model.TIN_utility[cu]):.2f})")

        print("\n--- Active Hot Utility Usage (z_hu=1) ---")
        # ... (same as before, ensure area calculation is robust) ...
        for j in model.CP:
            for hu in model.HU:
                if pyo.value(model.z_hu[j,hu]) == 1: # Check if the match exists
                    q_val = pyo.value(model.q_hu[j,hu])
                    dt1_val = pyo.value(model.dt_hu_s1[j,hu])
                    dt2_val = pyo.value(model.TOUT_utility[hu] - model.TOUT_spec[j])
                    U_val = pyo.value(model.U_hu[j,hu])
                    area_val = 0
                    if q_val > 1e-6 and dt1_val > 0 and dt2_val > 0:
                        lmtd_factor_base_val = (dt1_val * dt2_val * (dt1_val + dt2_val) / 2.0)
                        if lmtd_factor_base_val > 1e-9:
                            lmtd_factor_val = (lmtd_factor_base_val)**(1/3.0)
                            denominator_val = (lmtd_factor_val * U_val)
                            if denominator_val > 1e-9:
                                area_val = q_val / denominator_val
                    print(f"  C:{j} with HU:{hu}: Q={q_val:.2f}, Area={area_val:.2f}, "+
                        f"dt1={dt1_val:.2f} (Thu_in={pyo.value(model.TIN_utility[hu]):.2f}, Tc_in_heater={pyo.value(model.t_cold[j,1]):.2f}), "+
                        f"dt2={dt2_val:.2f} (Thu_out={pyo.value(model.TOUT_utility[hu]):.2f}, Tc_out_heater={pyo.value(model.TOUT_spec[j]):.2f})")

    except AttributeError:
        print("Solver did not produce results or results object is not structured as expected.")
        print("This might happen if the solver was interrupted or failed before finding a solution.")
        return # Exit report_results if essential results attributes are missing
    except ValueError as e:
        print(f"ValueError during results reporting (possibly uninitialized variable): {e}")
        print("This can happen if the solver terminated without a feasible solution.")
        return


    print("\n--- Temperature Profiles (Location 1 is 'Hot End' of Superstructure Stage) ---")
    # Hot streams: t_hot[i,1] (inlet) -> ... -> t_hot[i,NOK+1] (outlet before CU)
    for i in model.HP:
        # Iterate TEMP_LOCS in ascending order (1, 2, ..., NOK+1)
        profile_values = []
        for tl in model.TEMP_LOCS:
            try:
                temp_val = pyo.value(model.t_hot[i,tl])
                profile_values.append(f"{tl}:{temp_val:.2f}")
            except ValueError:
                profile_values.append(f"{tl}:N/A") # Handle uninitialized vars if solver failed
        
        inlet_temp_actual = "N/A"
        outlet_temp_spec = "N/A"
        try:
            inlet_temp_actual = f"{pyo.value(model.t_hot[i,1]):.2f}" # Should match TIN_spec
            outlet_temp_spec = f"{pyo.value(model.TOUT_spec[i]):.2f}"
        except ValueError:
            pass

        print(f"  H:{i}: (Inlet {inlet_temp_actual} at loc 1) " + " -> ".join(profile_values) + \
              f" (Outlet before CU {pyo.value(model.t_hot[i,model.NOK+1]):.2f}, Target Stream OUT: {outlet_temp_spec})")

    # Cold streams: 
    # Displayed as: t_cold[j,1] (hottest after process exch) -> ... -> t_cold[j,NOK+1] (inlet to superstructure)
    for j in model.CP:
        # Iterate TEMP_LOCS in ascending order (1, 2, ..., NOK+1) for display
        profile_values = []
        for tl in model.TEMP_LOCS: # CHANGED: No longer reversed
            try:
                temp_val = pyo.value(model.t_cold[j,tl])
                profile_values.append(f"{tl}:{temp_val:.2f}")
            except ValueError:
                profile_values.append(f"{tl}:N/A")
        
        inlet_temp_spec_val = "N/A"
        outlet_temp_after_process_val = "N/A"
        outlet_temp_target_val = "N/A"
        try:
            inlet_temp_spec_val = f"{pyo.value(model.TIN_spec[j]):.2f}"
            # t_cold[j,1] is the temperature of cold stream j exiting stage 1 (hottest point before HU)
            outlet_temp_after_process_val = f"{pyo.value(model.t_cold[j,1]):.2f}" 
            outlet_temp_target_val = f"{pyo.value(model.TOUT_spec[j]):.2f}"
        except ValueError:
            pass

        # Clarify what the locations mean for cold streams in the printout
        print(f"  C:{j}: (Outlet before HU {outlet_temp_after_process_val} at loc 1, Target Stream OUT: {outlet_temp_target_val}) " + \
              f" <- ".join(profile_values) + f" (Inlet {inlet_temp_spec_val} at loc {model.NOK+1})")

if __name__ == "__main__":
    # Define the base path to your data files
    data_base_path = "yee_1990/ex4" # Assuming your CSVs and config.json are here

    # Load data (now uses config.json internally)
    read_problem_data = load_data(base_path=data_base_path)
    
    # Get solver settings from the loaded config
    solver_name_from_config = read_problem_data['config'].get('solver_name', 'couenne')
    time_limit_from_config = read_problem_data['config'].get('time_limit_seconds', None)


    # --- Your previous build_hen_model function needs to be defined above this point ---
    # Ensure temp_mono_hot/cold rules and Epsilon_dt are correctly set in build_hen_model
    # from data_ex1['config']

    # Modify build_hen_model to use data['config'] parameters
    # Example (inside build_hen_model):
    # model.Epsilon_dt = data['config'].get('Epsilon_dt', 0.1)
    # model.Omega_T = data['config'].get('Omega_T', 500)
    # if not data['config'].get('Allow_Splits', True):
    # ... add no_split_hot_rule etc.

    # Build the model
    print("Building HEN model...")
    model_ex1 = build_hen_model(read_problem_data) # build_hen_model should now use data['config']
    
    print(f"Solving Example 1 with solver: {solver_name_from_config}. Time limit: {time_limit_from_config}s. This may take some time...")
    results_ex1 = solve_hen_model(model_ex1, 
                                  solver_name=solver_name_from_config, 
                                  tee=True, 
                                  time_limit=time_limit_from_config)

    # Report results
    if results_ex1: # Check if solver actually ran and returned results
        model_ex1.results = results_ex1 # Attach results to model for reporting function
        report_results(model_ex1, read_problem_data)
    else:
        print("Solver did not produce results.")