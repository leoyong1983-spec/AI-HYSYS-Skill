# Minimization of Matches Solver via Transport Model
from pyomo.environ import ConcreteModel, Var, NonNegativeReals, Objective, Constraint, SolverFactory, Binary
from time import time
from hens import Network


def solve_transport_model(network: Network, greedy: bool = False):
    # declaring model
    model_to_solve: ConcreteModel = ConcreteModel(name="MIN_MATCHES_TRANSPORT")

    # declaring model inputs
    hots = network.H            # hot streams including utilities
    colds = network.C           # cold streams including utilities
    interval = network.T        # temperature intervals
    p_ij = network.P            # stream exchange permission
    sigma = network.sigmas      # heat supply per hot stream per interval
    delta = network.deltas      # heat demand per cold stream per interval
    if not greedy:
        u_ij = network.U        # Big-M parameter
    else:
        u_ij = network.U_greedy
    # declaring model variables
    model_to_solve.y_ij = Var(hots, colds, within=Binary)
    model_to_solve.q_ijkl = Var(hots, interval, colds, interval, within=NonNegativeReals)

    # declaring model objective
    def matches_min_rule(model):
        """
        objective function: minimize the number of matches between hot stream and cold stream, y_ij
        """
        return sum(model.y_ij[h, c] for h in hots for c in colds)
    model_to_solve.obj = Objective(rule=matches_min_rule)

    # heat balance for supplies
    def supply_balance_constraint(model, h, s):
        return sum(model.q_ijkl[h, s, c, t] for c in colds for t in interval) == sigma[h, s]
    model_to_solve.supply_balance_constraint = Constraint(hots, interval, rule=supply_balance_constraint)

    # heat balance for demands
    def demand_balance_constraint(model, c, t):
        return sum(model.q_ijkl[h, s, c, t] for h in hots for s in interval) == delta[c, t]
    model_to_solve.demand_balance_constraint = Constraint(colds, interval, rule=demand_balance_constraint)

    # big-M constraint
    def big_matrix_rule(model, h, c):
        return sum(model.q_ijkl[h, s, c, t] for s in interval for t in interval) <= u_ij[h, c] * model.y_ij[h, c]
    model_to_solve.big_M_constraint = Constraint(hots, colds, rule=big_matrix_rule)

    # zero heat transmission constraint
    def zero_heat_rule(model, h, c, s, t):
        s_index = interval.index(s)
        t_index = interval.index(t)
        if s_index > t_index:
            return model.q_ijkl[h, s, c, t] == 0
        else:
            return Constraint.Skip
        
    model_to_solve.zero_heat_constraint = Constraint(hots, colds, interval, interval, rule=zero_heat_rule)

    # define hot to cold matching permission
    model_to_solve.stream_exchange_permission = Constraint(hots, colds, rule=lambda m, h, c: m.y_ij[h, c] <= p_ij[h, c])

    # solving model
    s_time = time()
    solver = SolverFactory("glpk")
    results = solver.solve(model_to_solve)
    sum_y = sum([model_to_solve.y_ij[h, c].value for h in hots for c in colds])
    print("HS: {}, CS: {}, TI: {}".format(len(hots), len(colds), len(interval)))
    print("Objective: y = {}, in {} seconds".format(sum_y, round(time() - s_time, 6)))

    return results, model_to_solve


def print_matches_transport(network: Network, model: ConcreteModel):
    print('------- Matching Streams ------')
    for h in network.H:
        for c in network.C:
            if model.y_ij[h, c].value != 0:
                print(f'{h.name} with {c.name}', end="")
                total_h = 0.0
                for s in network.T:
                    for t in network.T:
                        if model.q_ijkl[h, s, c, t].value > 0.0:
                            total_h += model.q_ijkl[h, s, c, t].value
                            pass
                print(f' - q = {total_h:.2f}')
