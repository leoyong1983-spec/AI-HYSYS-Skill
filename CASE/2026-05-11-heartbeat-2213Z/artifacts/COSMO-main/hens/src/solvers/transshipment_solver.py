""" Minimization of Matches Solver via Transshipment Model
Change by Maetee L : may3rd@gmail.com
By applying the model list in Chen, Grossmann, and Miller (2015).
Include model M-1 to M-5, selected by parameter model_selected
9 Apr 2024
- change the cost function by parameter cost_selected ["matching", "cost"]
    matching is the default, for minimizing the number of matches
    cost for minimizing the cost of utility
"""
from pyomo.environ import ConcreteModel, Var, NonNegativeReals, RangeSet, Objective, Constraint, SolverFactory, Binary, value
from time import time
from math import log
from hens import Network, Stream, Utility, TemperatureInterval, MatchingHEX
from typing import Union


def solve_transshipment_model(network: Network,
                              model_selected: str = "M1",
                              cost_selected: str = "matching",
                              alpha_w: float = 25,
                              log_file: bool = False,
                              debug: bool = False) -> list[MatchingHEX]:
    """
    Solve the heat exchanger network synthesis using transshipment model listed in Yang (2015)

    :param network: the problem network
    :param model_selected: the model to be used to solve the network problem - ["M1" to "M5"]
    :param cost_selected: the cost function to be used to solve the network problem - ["matching" or "cost"]
    :param alpha_w: weight factor for model-6
    :param log_file: weather show logging and save to solver.log file

    :return:
    list of MatchingHEX
    """
    # ensure that only one model is selected
    if model_selected is None or model_selected not in ["M0", "M1", "M2", "M3", "M4", "M5", "M6"]:
        model_selected = "M1"

    # ensure that only one cost function is selected
    if cost_selected is None or cost_selected not in ["matching", "cost"]:
        cost_selected = "matching"

    # set up the model
    network.model = model_selected
    print(f"The model to be used is {network.model}")
    # declaring model
    model_to_solve: ConcreteModel = ConcreteModel(name="MIN_MATCHES_TRANSSHIPMENT")
    # declaring model inputs
    intervals = network.T  # temperature intervals
    diff_t_min = network.diff_t_min
    hots = sorted(list(set([i for i in network.H for k in intervals if i.interval.passes_through_interval(k)])),
                  key=lambda x: x.name)
    colds = sorted(list(set(j for j in network.C for k in intervals
                            if j.interval.shifted(diff_t_min).passes_through_interval(k))), key=lambda x: x.name)
    sigma: dict[tuple[Stream, TemperatureInterval], float] = network.sigmas  # heat supply per hot stream per interval
    delta: dict[tuple[Stream, TemperatureInterval], float] = network.deltas  # heat demand per cold stream per interval
    p_ij: dict[tuple[Union[Stream, Utility], Union[Stream, Utility]], int] = network.P  # stream exchange permission
    # p_ijk = network.Pk  # stream exchange in interval permission
    # determine the upper bound heat supply and heat demand
    u_ij: dict[tuple[Union[Stream, Utility], Union[Stream, Utility]], float] = {}
    for i in hots:
        for j in colds:
            if i.__class__ == Stream and j.__class__ == Stream:
                u_ij[i, j] = min(float(sum(sigma[i, k] for k in intervals)), float(sum(delta[j, k] for k in intervals)),
                                 max(min(i.FCp, j.FCp)*(i.interval.t_max - j.interval.t_min), 0.0))
            elif i.__class__ == Stream and j.__class__ == Utility:
                u_ij[i, j] = float(sum(sigma[i, k] for k in intervals))
            elif i.__class__ == Utility and j.__class__ == Stream:
                u_ij[i, j] = float(sum(delta[j, k] for k in intervals))
            elif i.__class__ == Utility and j.__class__ == Utility:
                u_ij[i, j] = 0 # no heat exchange between utilities
            else:
                u_ij[i, j] = 0
    # update a tighter upper bound (Gundersen et al. (1997)
    # U_i,j,k for Model-3 and Model-5
    u_ijk = dict([((i, j, k), min(float(sum(sigma[i, l] for l in intervals if intervals.index(l) <= intervals.index(k))),
                                  delta[j, k])) for i in hots for j in colds for k in intervals])
    # U_i,k,j,l for Model-4
    u_ijkl = dict([((i, k, j, l), min(sigma[i, k], delta[j, l])) for i in hots for j in colds
                   for k in intervals for l in intervals])
    if model_selected == "M2":
        # determining weight for M-2
        w_ij: dict[tuple[Union[Stream, Utility], Union[Stream, Utility]], float] = {}
        t_k_max: float = intervals[0].t_max
        t_k_min: float = intervals[-1].t_min
        for i in hots:
            for j in colds:
                if u_ij[i, j] > 0:
                    t_i_in = min(i.interval.t_max, t_k_max)
                    t_i_out = min(i.interval.t_min, t_k_min)
                    t_j_in = min(j.interval.t_min, t_k_min)
                    t_j_out = min(j.interval.t_max, t_k_max)
                    diff_t_in = t_i_in - min(t_j_out, t_j_in - diff_t_min)
                    diff_t_out = max(t_i_out, t_i_in + diff_t_min) - t_j_in
                    if diff_t_in == diff_t_out:
                        diff_t_ij = diff_t_in
                    else:
                        diff_t_ij = (diff_t_out - diff_t_in) / log(diff_t_out / diff_t_in)
                    w_ij[i, j] = u_ij[i, j] / diff_t_ij
                else:
                    w_ij[i, j] = 0
    if model_selected == ["M5", "M6"]:
        # max demand and max supply for M-5
        heats = dict([((i, k), sigma[i, k]) for i in hots for k in intervals])
        demands = dict([((j, k), delta[j, k]) for j in colds for k in intervals])
        max_supply: float = max(sum(heats[i, k] for k in intervals) for i in hots)
        max_demand: float = max(sum(demands[j, k] for k in intervals) for j in colds)
    # declaring model variables
    model_to_solve.q_ijk = Var(hots, colds, intervals, within=NonNegativeReals)
    model_to_solve.q_ijkl = Var(hots, intervals, colds, intervals, within=NonNegativeReals)
    model_to_solve.y_ij = Var(hots, colds, within=Binary)
    model_to_solve.residual_set = RangeSet(0, len(intervals))
    model_to_solve.residual_ik = Var(hots, model_to_solve.residual_set, within=NonNegativeReals)
    last_residual = len(intervals)

    # model objective
    def matches_min_rule(model):
        """
        objective function: minimize the number of matches between hot stream and cold stream, y_ij
        """
        if model_selected == "M2":
            return sum(model.y_ij[i, j] * w_ij[i, j] for i in hots for j in colds)
        elif model_selected == "M6":
            return (sum(model.y_ij[i, j] for i in hots for j in colds) * alpha_w +
                    sum(model.q_ijk[m, j, k] * m.cost for m in hots for j in colds for k in intervals if m.__class__ == Utility) +
                    sum(model.q_ijk[i, n, k] * n.cost for i in hots for n in colds for k in intervals if n.__class__ == Utility))
        else:
            return sum(model.y_ij[i, j] for i in hots for j in colds)

    def utility_cost_min_rule(model):
        total_cost = 0
        if model_selected == "M4":
            total_cost += sum(model.q_ijkl[i, k, j, l] * i.cost for i in hots for k in intervals for j in colds for l in intervals if i.__class__ == Utility)
            total_cost += sum(model.q_ijkl[i, k, j, l] * j.cost for i in hots for k in intervals for j in colds for l in intervals if j.__class__ == Utility)
        else:
            total_cost += sum(model.q_ijk[i, j, k] * i.cost for i in hots for j in colds for k in intervals if i.__class__ == Utility)
            total_cost += sum(model.q_ijk[i, j, k] * j.cost for i in hots for j in colds for k in intervals if j.__class__ == Utility)
        return total_cost

    # set up the objective function
    if cost_selected == "matching":
        model_to_solve.obj = Objective(rule=matches_min_rule)
    elif cost_selected == "cost":
        model_to_solve.obj = Objective(rule=utility_cost_min_rule)

    # zero residual constraint
    def zero_residual_rule(model, i, r):
        """
        constraint function: zero residual at top and bottom temperature interval
        """
        if (r == 0) or (r == last_residual):
            return model.residual_ik[i, r] == 0
        else:
            return Constraint.Skip
    model_to_solve.zero_residual_constraint = Constraint(hots, model_to_solve.residual_set, rule=zero_residual_rule)

    # heat conservation
    def heat_conservation_rule(model, i, k):
        """
        constraint function: heat conservation of each temperature interval
        the total heat entering must equal to heat exiting temperature interval
        , is s.t. in paper.
        """
        if model_selected == "M4":
            return Constraint.Skip
        else:
            interval_index = intervals.index(k) + 1  # the index of residual_k
            exiting_heat = sum(model.q_ijk[i, c, k] for c in colds) + model.residual_ik[i, interval_index]
            entering_heat = sigma[i, k] + model.residual_ik[i, interval_index - 1]
            return exiting_heat == entering_heat
    model_to_solve.heat_conservation_constraint = Constraint(hots, intervals, rule=heat_conservation_rule)

    # heat demand satisfaction
    def heat_demand_rule(model, j, k):
        """
        constraint function: heat demand of the cold stream
        """
        if model_selected == "M4":
            return delta[j, k] == sum(model.q_ijkl[i, l, j, k] for i in hots for l in intervals if intervals.index(l) <= intervals.index(k))
        else:
            return sum(model.q_ijk[h, j, k] for h in hots) == delta[j, k]
    model_to_solve.demand_satisfaction_constraint = Constraint(colds, intervals, rule=heat_demand_rule)

    def heat_supply_model4(model, i, k):
        if model_selected == "M4":
            return sigma[i, k] == sum(model.q_ijkl[i, k, j, l] for j in colds for l in intervals if intervals.index(l) >= intervals.index(k))
        else:
            return Constraint.Skip
    model_to_solve.big_m_constraint2 = Constraint(hots, intervals, rule=heat_supply_model4)

    # big-M restriction
    def big_matrix_rule(model, i, j):
        if model_selected in ["M3", "M4", "M5", "M6"]:
            return Constraint.Skip
        else:
            return sum(model.q_ijk[i, j, k] for k in intervals) <= u_ij[i, j] * model.y_ij[i, j]
    model_to_solve.big_m_constraint = Constraint(hots, colds, rule=big_matrix_rule)

    def big_matrix_rules1(model, i, j, k):
        if model_selected in ["M3", "M5", "M6"]:
            return model.q_ijk[i, j, k] <= u_ijk[i, j, k] * model.y_ij[i, j]
        else:
            return Constraint.Skip
    model_to_solve.big_m_constraint1 = Constraint(hots, colds, intervals, rule=big_matrix_rules1)

    def big_matrix_rules2(model, i, j, k, l):
        if model_selected == "M4":
            return model.q_ijkl[i, k, j, l] <= u_ijkl[i, k, j, l] * model.y_ij[i, j]
        else:
            return Constraint.Skip
    model_to_solve.big_m_constraint3 = Constraint(hots, colds, intervals, intervals, rule=big_matrix_rules2)

    def integer_cuts_h(model, i):
        if model_selected == ["M5", "M6"]:
            return sum(model.y_ij[i, j] for j in colds) >= sum(sigma[i, k] for k in intervals) / max_demand
        else:
            return Constraint.Skip
    model_to_solve.integer_cuts_h = Constraint(hots, rule=integer_cuts_h)

    def integer_cuts_c(model, j):
        if model_selected == ["M5", "M6"]:
            return sum(model.y_ij[i, j] for i in hots) >= sum(delta[j, k] for k in intervals) / max_supply
        else:
            return Constraint.Skip
    model_to_solve.integer_cuts_c = Constraint(colds, rule=integer_cuts_c)

    # def integer_cuts_y(model):
    #     if model_selected == "M5":
    #         return sum(model.y_ij[i, j] for i in hots for j in colds) <= len(hots) + len(colds) - 1
    #     else:
    #         return Constraint.Skip
    # model_to_solve.integer_cuts_y = Constraint(rule=integer_cuts_y)

    # define hot to cold matching permission
    model_to_solve.stream_exchange_permission = Constraint(hots, colds, rule=lambda m, h, c: m.y_ij[h, c] <= p_ij[h, c])

    # solving model
    s_time = time()
    solver = SolverFactory("glpk")
    if log_file:
        results = solver.solve(model_to_solve, logfile="solver.log", tee=True)
    else:
        results = solver.solve(model_to_solve)

    # check if the model is feasible
    from pyomo.opt import SolverStatus, TerminationCondition
    if results.solver.status == SolverStatus.ok and results.solver.termination_condition == TerminationCondition.optimal:
        print("Model is feasible")
    
    # calculate objective value
    sum_y = 0
    if cost_selected == "matching":
        sum_y = sum([value(model_to_solve.y_ij[h, c]) for h in hots for c in colds])
    elif cost_selected == "cost":
        if model_selected == "M4":
            sum_y += sum([value(model_to_solve.q_ijkl[i, k, j, l]) * i.cost for i in hots for k in intervals for j in colds for l in intervals if i.__class__ == Utility])
            sum_y += sum([value(model_to_solve.q_ijkl[i, k, j, l]) * j.cost for i in hots for k in intervals for j in colds for l in intervals if j.__class__ == Utility])
        else:
            sum_y += sum([value(model_to_solve.q_ijk[i, j, k]) * i.cost for i in hots for j in colds for k in intervals if i.__class__ == Utility])
            sum_y += sum([value(model_to_solve.q_ijk[i, j, k]) * j.cost for i in hots for j in colds for k in intervals if j.__class__ == Utility])

    print("Hot stream number: {}\nCold stream number: {}\nTemperature interval number: {}".format(len(hots), len(colds), len(intervals)))
    print("Objective: y = {}\nSolved in {} seconds".format(sum_y, round(time() - s_time, 6)))
    
    # calculate the total hot and cold utility
    total_hot_utility: float = 0
    total_cold_utility: float = 0
    
    total_hot_utility = sum([value(model_to_solve.q_ijk[i, j, k]) for i in hots for j in colds for k in intervals if i.__class__ == Utility])
    total_cold_utility = sum([value(model_to_solve.q_ijk[i, j, k]) for i in hots for j in colds for k in intervals if j.__class__ == Utility])
    
    print("Total hot utility: {}\nTotal cold utility: {}".format(total_hot_utility, total_cold_utility))
    print("Total utility: {}".format(total_hot_utility + total_cold_utility))
    
    # create list of heat exchanger matching from the results
    hexs: list[MatchingHEX] = []
    hx_id: int = 1
    for i in network.H:
        for j in network.C:
            try:
                if value(model_to_solve.y_ij[i, j]) > 0:
                    # for minimizing function is utility cost, need to check the q_ijk value first
                    if cost_selected == "cost":
                        if network.model == "M4":
                            q = sum(value(model_to_solve.q_ijkl[i, k, j, l]) for k in network.T for l in network.T)
                        else:
                            q = sum(value(model_to_solve.q_ijk[i, j, k]) for k in network.T)
                        if q <= 0:
                            continue
                    
                    hx_name: str = f"EX-{hx_id}"
                    hx_id += 1
                    if network.model == "M4":
                        diff_t = network.diff_t_min
                        #q = sum(value(model_to_solve.q_ijkl[i, k, j, l]) for k in network.T for l in network.T)
                        t_h_max: float = max(
                            [k.t_max for k in network.T for l in network.T if value(model_to_solve.q_ijkl[i, k, j, l]) > 0])
                        t_h_min: float = min(
                            [k.t_min for k in network.T for l in network.T if value(model_to_solve.q_ijkl[i, k, j, l]) > 0])
                        t_c_max: float = max([l.t_max - diff_t for k in network.T for l in network.T if
                                              value(model_to_solve.q_ijkl[i, k, j, l]) > 0])
                        t_c_min: float = min([l.t_min - diff_t for k in network.T for l in network.T if
                                              value(model_to_solve.q_ijkl[i, k, j, l]) > 0])
                        hexs.append(MatchingHEX(hot=i, cold=j, hot_interval=TemperatureInterval(t_h_max, t_h_min),
                                                cold_interval=TemperatureInterval(t_c_max, t_c_min), duty=q,
                                                name=hx_name))
                    else:
                        #q = sum(value(model_to_solve.q_ijk[i, j, k]) for k in network.T)
                        t_max: float = max([k.t_max for k in network.T if value(model_to_solve.q_ijk[i, j, k]) > 0])
                        t_min: float = min([k.t_min for k in network.T if value(model_to_solve.q_ijk[i, j, k]) > 0])
                        hexs.append(MatchingHEX(hot=i, cold=j, hot_interval=TemperatureInterval(t_max, t_min),
                                                cold_interval=j.interval, duty=q, name=hx_name))
                    
                    # create matching hex object
                    if debug:
                        print(f"Match: {i} -> {j}")
                        print(f"total duty = {q}")
                        for k in network.T:
                            print(f"q_ijk:{k}:{value(model_to_solve.q_ijk[i, j, k])}")
                        print(f"hot interval: {hexs[-1].hot_interval}")
                        print(f"cold interval: {hexs[-1].cold_interval}")
                        print()
            except KeyError:
                pass
    return hexs


def print_matches_transshipment(hexs: list[MatchingHEX]):
    print("------- Matching Streams ------")
    print(f"Number of Matches: {len(hexs)}")
    i = 1
    for hx in hexs:
        print(f"{i}: {repr(hx)}")
        i += 1
    print("------- End of Matching ------")
    