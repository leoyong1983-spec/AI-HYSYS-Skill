import pyomo.environ as pyo
import pandas as pd
import numpy as np
import os

# --- Utility Functions ---
def smooth_max(x, epsilon=1e-4):
    """Smooth approximation of max(0, x) for NLP differentiability.
    
    Args:
        x: Input value (Pyomo expression or float).
        epsilon: Smoothing parameter (default 1e-4).
    
    Returns:
        Smoothed max(0, x).
    """
    return (x + pyo.sqrt(x**2 + epsilon**2)) / 2

def LMTD_ijk(model, i, j, k):
    """Calculate LMTD for process stream match (i,j) in stage k using Chen approximation.
    
    Args:
        model: Pyomo model with t (temperatures) and other parameters.
        i: Hot stream index.
        j: Cold stream index.
        k: Stage index.
    
    Returns:
        LMTD value (K).
    """
    dt1 = smooth_max(model.t[i, k].value - model.t[j, k].value)
    dt2 = smooth_max(model.t[i, k + 1].value - model.t[j, k + 1].value)
    return (dt1 * dt2 * ((dt1 + dt2) / 2)) ** (1/3) + 1e-6  # Avoid division by zero

def LMTD_cu_i(model, i, cu):
    """Calculate LMTD for cold utility with hot stream i.
    
    Args:
        model: Pyomo model with t, TOUT_CU, TIN_CU, TOUT.
        i: Hot stream index.
        cu: Cold utility index.
    
    Returns:
        LMTD value (K).
    """
    dt1 = smooth_max(model.t[i, model.NOK + 1].value - model.TOUT_U[cu])
    dt2 = smooth_max(model.TOUT[i] - model.TIN_U[cu])
    return (dt1 * dt2 * ((dt1 + dt2) / 2)) ** (1/3) + 1e-6

def LMTD_hu_j(model, j, hu):
    """Calculate LMTD for hot utility with cold stream j.
    
    Args:
        model: Pyomo model with t, TIN_HU, TOUT_HU, TOUT.
        j: Cold stream index.

    Returns:
        LMTD value (K).
    """
    dt1 = smooth_max(model.TIN_U[hu] - model.t[j, 1].value)
    dt2 = smooth_max(model.TOUT_U[hu] - model.TOUT[j])
    return (dt1 * dt2 * ((dt1 + dt2) / 2)) ** (1/3) + 1e-6

# --- Data Import ---
def read_data(streams_file, utilities_file, constraints_file=None):
    """Read input data from CSV files.
    
    Args:
        streams_file (str): Path to streams CSV.
        utilities_file (str): Path to utilities CSV.
        constraints_file (str, optional): Path to constraints CSV.
    
    Returns:
        tuple: Streams DataFrame, Utilities DataFrame, Constraints DataFrame or None.
    """
    streams = pd.read_csv(streams_file)
    utilities = pd.read_csv(utilities_file)
    constraints = pd.read_csv(constraints_file) if constraints_file else None
    return streams, utilities, constraints

# --- Model Construction ---
def build_model(streams, utilities, constraints=None, CF=0, C=1, B=1, epsilon=1e-4):
    """Build the Pyomo NLP model based on Yee & Grossmann (1990) Part I.
    
    Args:
        streams (pd.DataFrame): Streams data.
        utilities (pd.DataFrame): Utilities data.
        constraints (pd.DataFrame, optional): Constraints data.
        CF (float): Fixed charge ($/unit), default 0 for Part I.
        C (float): Area cost coefficient ($/m² yr).
        B (float): Area cost exponent.
        epsilon (float): Small value for smoothing max operator.
    
    Returns:
        pyo.ConcreteModel: The NLP model.
    """
    model = pyo.ConcreteModel()

    # Sets
    model.Streams = pyo.Set(initialize=streams['Name'].tolist(), doc="All Process Streams")
    model.Utilities = pyo.Set(initialize=utilities['Name'].tolist(), doc="All Utilities")
    model.HP = pyo.Set(initialize=streams[streams['Type'] == 'Hot']['Name'].tolist(), doc="Hot Process Streams")
    model.CP = pyo.Set(initialize=streams[streams['Type'] == 'Cold']['Name'].tolist(), doc="Cold Process Streams")
    model.NOK = max(len(model.HP), len(model.CP))
    model.ST = pyo.Set(initialize=range(1, model.NOK + 1), doc="Stages")
    model.temp_locations = pyo.Set(initialize=range(1, model.NOK + 2), doc="Temperature Locations")

    # Parameters
    TIN = {row['Name']: row['TIN_spec'] for _, row in streams.iterrows()}
    TOUT = {row['Name']: row['TOUT_spec'] for _, row in streams.iterrows()}
    F = {row['Name']: row['Fcp'] for _, row in streams.iterrows()}
    U = {row['Name']: row['U'] for _, row in streams.iterrows()}
    
    model.TIN = pyo.Param(model.Streams, initialize=TIN, doc="Inlet temperatures (K)")
    model.TOUT = pyo.Param(model.Streams, initialize=TOUT, doc="Outlet temperatures (K)")
    model.F = pyo.Param(model.Streams, initialize=F, doc="Heat capacity flow rates (kW/K)")
    model.U = pyo.Param(model.Streams, initialize=U, doc="Overall heat transfer coefficients (kW/m² K)")

    TIN_U = {row['Name']: row['TIN_utility'] for _, row in utilities.iterrows()}
    TOUT_U = {row['Name']: row['TOUT_utility'] for _, row in utilities.iterrows()}
    CCU = {row['Name']: row['Unit_Cost_Energy'] for _, row in utilities.iterrows() if row['Type'] == 'Cold_Utility'}
    CHU = {row['Name']: row['Unit_Cost_Energy'] for _, row in utilities.iterrows() if row['Type'] == 'Hot_Utility'}

    model.HU = pyo.Set(initialize=utilities[utilities['Type'] == 'Hot_Utility']['Name'].tolist(), doc="Hot Utility")
    model.CU = pyo.Set(initialize=utilities[utilities['Type'] == 'Cold_Utility']['Name'].tolist(), doc="Cold Utility")
    model.TIN_U = pyo.Param(model.Utilities, initialize=TIN_U, doc="Utility inlet temperatures (K)")
    model.TOUT_U = pyo.Param(model.Utilities, initialize=TOUT_U, doc="Utility outlet temperatures (K)")
    model.CCU = pyo.Param(model.CU, initialize=CCU, doc="Cold utility cost per unit ($/kW)")
    model.CHU = pyo.Param(model.HU, initialize=CHU, doc="Hot utility cost per unit ($/kW)")

    # Variables
    model.q = pyo.Var(model.HP, model.CP, model.ST, domain=pyo.NonNegativeReals, doc="Heat exchanged (kW)")
    model.qu = pyo.Var(model.Streams, model.Utilities, domain=pyo.NonNegativeReals, doc="Cold utility heat (kW)")
    model.t = pyo.Var(model.Streams, model.temp_locations, domain=pyo.NonNegativeReals, doc="Temperature (K)")

    # Constants
    C = 1000
    B = 0.6
    CF = 0  # Fixed charge for Part I
    epsilon = 1e-4  # Smoothing parameter for max function
    
    model.C = pyo.Param(initialize=C, doc="Area cost coefficient ($/m² yr)")
    model.B = pyo.Param(initialize=B, doc="Area cost exponent")
    model.CF = pyo.Param(initialize=CF, doc="Fixed charge ($/unit)")
    model.epsilon = pyo.Param(initialize=epsilon, doc="Smoothing parameter for max function")
    
    # Constraints
    # Overall Heat Balances (Eq. 1)
    def overall_balance_hot(model, i):
        return (model.TIN[i] - model.TOUT[i]) * model.F[i] == sum(model.q[i,j,k] for j in model.CP for k in model.ST) + sum(model.qu[i, u] for u in model.CU)
    model.overall_balance_hot = pyo.Constraint(model.HP, rule=overall_balance_hot)

    def overall_balance_cold(model, j):
        return (model.TOUT[j] - model.TIN[j]) * model.F[j] == sum(model.q[i,j,k] for i in model.HP for k in model.ST) + sum(model.qu[j, u] for u in model.HU)
    model.overall_balance_cold = pyo.Constraint(model.CP, rule=overall_balance_cold)

    # Stagewise Heat Balances (Eq. 2)
    def stage_balance_hot(model, i, k):
        return (model.t[i,k] - model.t[i,k+1]) * model.F[i] == sum(model.q[i,j,k] for j in model.CP)
    model.stage_balance_hot = pyo.Constraint(model.HP, model.ST, rule=stage_balance_hot)

    def stage_balance_cold(model, j, k):
        return (model.t[j,k] - model.t[j,k+1]) * model.F[j] == sum(model.q[i,j,k] for i in model.HP)
    model.stage_balance_cold = pyo.Constraint(model.CP, model.ST, rule=stage_balance_cold)

    # Inlet Temperature Assignments (Eq. 3)
    model.temp_assign_hot = pyo.Constraint(model.HP, rule=lambda model, i: model.t[i,1] == model.TIN[i])
    model.temp_assign_cold = pyo.Constraint(model.CP, rule=lambda model, j: model.t[j,model.NOK+1] == model.TIN[j])

    # Temperature Feasibility (Eq. 4)
    def temp_feas_hot(model, i, k):
        return model.t[i,k] >= model.t[i,k+1]
    model.temp_feas_hot = pyo.Constraint(model.HP, model.ST, rule=temp_feas_hot)

    def temp_feas_cold(model, j, k):
        return model.t[j,k] >= model.t[j,k+1]
    model.temp_feas_cold = pyo.Constraint(model.CP, model.ST, rule=temp_feas_cold)

    model.temp_out_hot = pyo.Constraint(model.HP, rule=lambda model, i: model.t[i,model.NOK+1] >= model.TOUT[i])
    model.temp_out_cold = pyo.Constraint(model.CP, rule=lambda model, j: model.t[j,1] <= model.TOUT[j])

    # Utility Loads (Eq. 5)
    model.util_cold = pyo.Constraint(model.HP, rule=lambda model, i: (model.t[i,model.NOK+1] - model.TOUT[i]) * model.F[i] == sum(model.qu[i, u] for u in model.CU))
    model.util_hot = pyo.Constraint(model.CP, rule=lambda model, j: (model.TOUT[j] - model.t[j,1]) * model.F[j] == sum(model.qu[j, u] for u in model.HU))

    # Objective Function with Smooth LMTD (Eq. 13a)
    def smooth_max(x):
        return (x + pyo.sqrt(x**2 + model.epsilon**2)) / 2

    def LMTD_ijk(model, i, j, k):
        dt1 = smooth_max(model.t[i,k] - model.t[j,k])
        dt2 = smooth_max(model.t[i,k+1] - model.t[j,k+1])
        return (dt1 * dt2 * ((dt1 + dt2) / 2))**(1/3) + 1e-6

    def area_ijk(model, i, j, k):
        U_ij = min(model.U[i], model.U[j])  # Simplified U_ij assumption
        return model.q[i,j,k] / (U_ij * LMTD_ijk(model, i,j,k))

    def LMTD_cu_i(model, i, u):
        dt1 = smooth_max(model.t[i,model.NOK+1] - model.TOUT_U[u])
        dt2 = smooth_max(model.TOUT[i] - model.TIN_U[u])
        return (dt1 * dt2 * ((dt1 + dt2) / 2))**(1/3) + 1e-6

    def area_cu_i(model, i, u):
        return model.qu[i, u] / (model.U[i] * LMTD_cu_i(model, i, u))

    def LMTD_hu_j(model, j, u):
        dt1 = smooth_max(model.TIN_U[u] - model.t[j,1])
        dt2 = smooth_max(model.TOUT_U[u] - model.TOUT[j])
        return (dt1 * dt2 * ((dt1 + dt2) / 2))**(1/3) + 1e-6

    def area_hu_j(model, j, u):
        return model.qu[j, u] / (model.U[j] * LMTD_hu_j(model, j, u))

    def total_cost(model):
        utility_cost = 0
        
        for u in model.CU:
            utility_cost += model.CCU[u] * sum(model.qu[i, u] for i in model.HP)
        for u in model.HU:
            utility_cost += model.CHU[u] * sum(model.qu[j, u] for j in model.CP)
        
        # Area cost calculation
        # Sum over all process streams and utilities
        area_cost = 0

        for i in model.HP:
            for j in model.CP:
                for k in model.ST:
                    area_cost += model.C * area_ijk(model, i,j,k)*model.B
        for i in model.HP:
            for u in model.CU:
                area_cost += model.C * area_cu_i(model, i, u)*model.B
        for j in model.CP:
            for u in model.HU:
                area_cost += model.C * area_hu_j(model, j, u)*model.B
        return utility_cost + area_cost
    
    model.obj = pyo.Objective(rule=total_cost, sense=pyo.minimize)

    return model

# --- Solver Interface ---
def solve_model(model):
    """Solve the NLP model using IPOPT.
    
    Args:
        model (pyo.ConcreteModel): The Pyomo model.
    
    Returns:
        dict: Solver results.
    """
    solver = pyo.SolverFactory('ipopt')
    results = solver.solve(model, tee=True)
    return results

# --- Results Export ---
def export_reports(model, output_path):
    """Export optimization results to CSV.
    
    Args:
        model (pyo.ConcreteModel): Solved Pyomo model.
        output_path (str): Path to output CSV.
    """
        
    data = []
    for i in model.HP:
        for j in model.CP:
            for k in model.ST:
                q_val = model.q[i, j, k].value or 0  # Handle None values
                if q_val > 1e-6:
                    U_ij = min(model.U[i], model.U[j])
                    lmtd = LMTD_ijk(model, i, j, k)
                    area = q_val / (U_ij * lmtd)
                    data.append([i, j, k, q_val, area, model.t[i, k].value or 0, model.t[i, k+1].value or 0, model.t[j, k+1].value or 0, model.t[j, k].value or 0])
    
    # Hot and Cold Utilities
    for i in model.HP:
        for u in model.CU:
            qcu_val = model.qu[i, u].value or 0
            if qcu_val > 1e-6:
                lmtd_cu = LMTD_cu_i(model, i, u)
                area_cu = qcu_val / (model.U[i] * lmtd_cu)
                data.append([i, 'CU', '-', qcu_val, area_cu, model.t[i, model.NOK + 1].value or 0, model.TOUT_U[u], model.TIN_U[u], model.TOUT[i]])
                
    for j in model.CP:
        for u in model.HU:
            qhu_val = model.qu[j, u].value or 0
            if qhu_val > 1e-6:
                lmtd_hu = LMTD_hu_j(model, j, u)
                area_hu = qhu_val / (model.U[j] * lmtd_hu)
                data.append(['HU', j, '-', qhu_val, area_hu, model.TIN_U[u], model.TOUT_U[u], model.t[j, 1].value or 0, model.TOUT[j]])

    df = pd.DataFrame(data, columns=['HotStream', 'ColdStream', 'Stage', 'HeatLoad', 'Area', 'TempHot_IN', 'TempHot_OUT', 'TempCold_IN', 'TempCold_OUT'])
    df.to_csv(output_path, index=False)

# --- Main Script ---
if __name__ == "__main__":
    #
    data_base_path = 'yee_1990/NLP/'  # Base path for data files
    
    # Read data from CSV files
    streams_file = data_base_path + 'streams.csv'
    utilities_file = data_base_path + 'utilities.csv'
    constraints_file = data_base_path + 'constraints.csv' if 'constraints.csv' in os.listdir(data_base_path) else None
    results_file = data_base_path + 'results.csv'
    
    streams, utilities, constraints = read_data(streams_file, utilities_file, constraints_file)
    model = build_model(streams, utilities, constraints, CF=0, C=200, B=0.6)  # Example costs
    results = solve_model(model)
    export_reports(model, results_file)
    print(f"Optimization complete. Results saved to '{results_file}'.")
