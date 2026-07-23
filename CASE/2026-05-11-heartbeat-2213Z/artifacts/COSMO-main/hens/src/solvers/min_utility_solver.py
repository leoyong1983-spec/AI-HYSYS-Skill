# Minimization of Utility Solver
from pyomo.environ import ConcreteModel, Var, NonNegativeReals, RangeSet, Objective, Constraint, SolverFactory, value
from hens import MinUtilityProblem
import logging  # Import the logging module

# Configure logging (you can adjust level and format as needed)
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def solve_min_utility(problem_instance: MinUtilityProblem, debug: bool = False, pinch_temperature = None) -> tuple:
    """
    Solves the minimum utility problem using linear programming.

    Args:
        problem_instance: An instance of MinUtilityProblem containing the problem data.
        debug: If True, prints additional debug information.
        pinch_temperature: The pinch temperature to use for the pinch point. If 0.0, the pinch point will be determined automatically.

    Returns:
        A tuple containing:
            - sigma_hu: Dictionary of hot utility heat exchange values.
            - delta_cu: Dictionary of cold utility heat exchange values.
            - pinch_interval: The pinch temperature interval.
    
    Raises:
        ValueError: If the solver fails to find an optimal solution or if input data is invalid.
        TypeError: If there are type mismatches in the input data.
        Exception: For any unexpected errors during the process.
    """
    try:
        # --- Input Validation ---
        if not isinstance(problem_instance, MinUtilityProblem):
            raise TypeError("Input 'problem_instance' must be of type MinUtilityProblem.")
        
        # Check if necessary data is available in problem instance
        if not problem_instance.hot_streams or not problem_instance.cold_streams or \
           not problem_instance.hot_utilities or not problem_instance.cold_utilities or \
           not problem_instance.intervals:
            raise ValueError("The MinUtilityProblem instance is incomplete. Ensure it contains hot streams, cold streams, hot utilities, cold utilities, and intervals.")

        # --- Model Setup ---
        model_to_solve: ConcreteModel = ConcreteModel(name="MIN_UTILITY")

        # declaring model inputs
        hot_streams = problem_instance.hot_streams
        cold_streams = problem_instance.cold_streams
        hot_utilities = problem_instance.hot_utilities
        cold_utilities = problem_instance.cold_utilities
        intervals = problem_instance.intervals
        sigmas = problem_instance.sigmas
        deltas = problem_instance.deltas
        accepted_hu_sigmas = problem_instance.accepted_hu_sigmas
        accepted_cu_deltas = problem_instance.accepted_cu_deltas
        k_hu = {}
        for hot_utility in hot_utilities:
            k_hu[hot_utility] = hot_utility.cost
        k_cu = {}
        for cold_utility in cold_utilities:
            k_cu[cold_utility] = cold_utility.cost

        # declaring model variables
        model_to_solve.cost = Var(within=NonNegativeReals)
        model_to_solve.sigma_hu = Var(hot_utilities, cold_streams, intervals, within=NonNegativeReals)
        model_to_solve.delta_cu = Var(hot_streams, cold_utilities, intervals, within=NonNegativeReals)
        model_to_solve.residual_set = RangeSet(0, len(intervals))
        model_to_solve.residual_ik = Var(model_to_solve.residual_set, within=NonNegativeReals)
        last_residual = len(intervals)

        # defining model cost computation
        def utility_cost_rule(model):
            hu_cost = sum(k_hu[hu] * model.sigma_hu[hu, cs, ti] for hu in hot_utilities for cs in cold_streams for ti in intervals)
            cu_cost = sum(k_cu[cu] * model.delta_cu[hs, cu, ti] for hs in hot_streams for cu in cold_utilities for ti in intervals)
            return model.cost == hu_cost + cu_cost
        model_to_solve.utility_cost_constraint = Constraint(rule=utility_cost_rule)

        # defining model objective
        def cost_min_rule(model):
            return model.cost
        model_to_solve.obj = Objective(rule=cost_min_rule)

        # heat balance restriction
        def heat_balance_rule(model, t_interval):
            interval_index = intervals.index(t_interval) + 1
            entering_energy = sum(sigmas[hs, t_interval] for hs in hot_streams) + sum(model.sigma_hu[hu, cs, t_interval] for hu in hot_utilities for cs in cold_streams) + model.residual_ik[interval_index - 1]
            exiting_energy = sum(deltas[cs, t_interval] for cs in cold_streams) + sum(model.delta_cu[hs, cu, t_interval] for hs in hot_streams for cu in cold_utilities) + model.residual_ik[interval_index]
            return entering_energy == exiting_energy
        model_to_solve.heat_balance_constraint = Constraint(intervals, rule=heat_balance_rule)

        # residual heat entering the first temperature interval and the one exiting the last temperature interval
        # must be zero
        def r_zero_rule(model, r):
            if (r == 0) or (r == last_residual):
                return model.residual_ik[r] == 0
            else:
                return Constraint.Skip
        model_to_solve.r_zero_constraint = Constraint(model_to_solve.residual_set, rule=r_zero_rule)

        # forbidden heat exchanges for hot utilities
        def forbidden_hu_intervals(model, hu, cs, ti):
            if accepted_hu_sigmas[hu, ti]:
                return Constraint.Skip
            else:
                return model.sigma_hu[hu, cs, ti] == 0
        model_to_solve.forbidden_hu_intervals_constraint = Constraint(hot_utilities, cold_streams, intervals, rule=forbidden_hu_intervals)

        # forbidden heat exchanges for cold utilities
        def forbidden_cu_intervals(model, hs, cu, ti):
            if accepted_cu_deltas[cu, ti]:
                return Constraint.Skip
            else:
                return model.delta_cu[hs, cu, ti] == 0
        model_to_solve.forbidden_cu_intervals_constraint = Constraint(hot_streams, cold_utilities, intervals, rule=forbidden_cu_intervals)

        # --- Solving model ---
        solver = SolverFactory("glpk")
        results = solver.solve(model_to_solve, tee=False)  # Suppress solver output unless debugging

        # Check solver status and termination condition
        from pyomo.opt import SolverStatus, TerminationCondition
        if results.solver.status != SolverStatus.ok:
            error_message = f"Solver failed with status: {results.solver.status}"
            logging.error(error_message)
            raise ValueError(error_message)

        if results.solver.termination_condition != TerminationCondition.optimal:
            error_message = f"Solver did not converge to an optimal solution. Termination condition: {results.solver.termination_condition}"
            logging.error(error_message)
            raise ValueError(error_message)

        # --- Result Processing ---
        # generating sigmas dictionary for hot utilities
        sigma_hu = {}
        min_hu = 0
        for hot in hot_utilities:
            for k in intervals:
                sigma_hu[hot, k] = sum(value(model_to_solve.sigma_hu[hot, cs, k]) for cs in cold_streams)
                min_hu += sigma_hu[hot, k]

        # print the minimum hot utility
        print(f"Minimum hot utility: {min_hu}")

        # generating deltas dictionary for cold utilities
        delta_cu = {}
        min_cu = 0
        for cold in cold_utilities:
            for k in intervals:
                delta_cu[cold, k] = sum(value(model_to_solve.delta_cu[hs, cold, k]) for hs in hot_streams)
                min_cu += delta_cu[cold, k]
        # print the minimum cold utility
        print(f"Minimum cold utility: {min_cu}")

        # determine the pinch temperature interval
        # residual_ik_value = {i: value(model_to_solve.residual_ik[i]) for i in model_to_solve.residual_ik}
        # zero_indices = [i for i in residual_ik_value.keys() if abs(residual_ik_value[i]) < 1e-6]  # Using abs for comparison
        # pinch_interval = 0
        # if zero_indices:
        #     for i in zero_indices:
        #         if not (i == 0 or i == len(intervals)):
        #             pinch_interval = i
        #             break
        
        if pinch_temperature is None:
            # Assume residual_ik is a dictionary or list from your model, and intervals, hot_streams, cold_streams are defined
            residual_ik_value = {i: model_to_solve.residual_ik[i].value for i in model_to_solve.residual_ik}  # Extract values
            tolerance = 1e-6
            candidate_pinches = [i for i in range(1, len(intervals)) if abs(residual_ik_value[i]) < tolerance]

            pinch_interval = 0  # Default to no pinch
            for i in candidate_pinches:
                # Check if hot and cold streams pass through the interval above the residual (intervals[i-1])
                hot_present = any(intervals[i-1].t_min <= hot.t_in and intervals[i-1].t_max >= hot.t_out 
                                for hot in hot_streams)
                cold_present = any(intervals[i-1].t_min <= cold.t_out and intervals[i-1].t_max >= cold.t_in 
                                for cold in cold_streams)
                if hot_present and cold_present:
                    pinch_interval = i
                    break  # Stop at the highest temperature (smallest i) valid pinch

            if pinch_interval == 0:
                print("No valid pinch point found with active streams.")
            else:
                print(f"Pinch point identified at interval boundary {pinch_interval}, temperature: {intervals[pinch_interval-1].t_max}")
        else:
            # Use the pinch temperature provided by the user
            pinch_interval = 0
            for i in range(1, len(intervals)):
                if intervals[i-1].t_min <= pinch_temperature and intervals[i-1].t_max >= pinch_temperature:
                    pinch_interval = i
                    break
                
        pinch_hots_pass: bool = False
        pinch_colds_pass: bool = False
        for hot in problem_instance.hot_streams:
            pinch_hots_pass = intervals[pinch_interval].passes_through_interval(hot.interval)
            if pinch_hots_pass:
                break
        for cold in problem_instance.cold_streams:
            pinch_colds_pass = intervals[pinch_interval].passes_through_interval(cold.interval)
            if pinch_colds_pass:
                break
        if not (pinch_colds_pass and pinch_hots_pass):
            pinch_interval = 0

        if debug:
            print('--------------------- debug mode : begin ---------------------')
            print('hot utility')
            for hot in hot_utilities:
                for k in intervals:
                    if sigma_hu[hot, k] > 0:
                        print(hot, k, sigma_hu[hot, k])

            print('cold utility')
            for cold in cold_utilities:
                for k in intervals:
                    if delta_cu[cold, k] > 0:
                        print(cold, k, delta_cu[cold, k])

            if pinch_interval > 0:
                print('pinch interval')
                print(intervals[pinch_interval])
            else:
                print("No pinch")
            print('--------------------- debug mode : end ---------------------')

        return sigma_hu, delta_cu, pinch_interval

    except ValueError as ve:
        logging.error(f"Value Error: {ve}")
        raise  # Re-raise the exception to propagate it
    except TypeError as te:
        logging.error(f"Type Error: {te}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise