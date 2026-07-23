# This file tests the implementation of the classes
from hens import *
import os


if __name__ == '__main__':
    problems: list[str] = []
    problems += ["4sp1", "6sp-cf1", "6sp-gg1", "6sp1", "7sp-cm1", "7sp-s1", "7sp-torw1", "7sp1", "7sp2"]
#    problems += ["8sp-fs1", "8sp1", "9sp-al1", "9sp-has1", "10sp-la1", "10sp-ol1", "10sp1", "12sp1", "14sp1"]
#    problems += ["15sp-tkm", "20sp1", "22sp-ph", "22sp1", "23sp1", "28sp-as1", "37sp-yfyv"]
#    problems += ["balanced5"] #  , "balanced8"]
#    problems += ["balance10", "balance12", "balance15"]
#    problems += ["unbalanced5", "unbalanced8", "unbalanced10", "unbalanced15", "unbalanced17", "unbalanced20"]

    problems = ["14sp1"]
    filenames = ["test.csv"]
    models = ["M1", "M2", "M3", "M4", "M5", "M6"]
    cost = "cost"
    alpha_w = 25.0
    read_from_csv = True

    for filename in filenames:
        for model_selected in models:
            if read_from_csv:
                csv_path: str = os.path.join(os.getcwd(), filename)
                min_up_test: MinUtilityProblem = MinUtilityProblem.generate_from_csv(csv_path)
            else:
                min_up_test: MinUtilityProblem = MinUtilityProblem.generate_from_data(problems[0])
            # min_up_test.plot_composite_diagram()
            # min_up_test.plot_grand_composite_curve()
            sigma_HU, delta_HU, pinch_interval = solve_min_utility(min_up_test, debug=False)

            print("---- No Pinch ----")
            no_pinch_network: Network = Network(min_up_test, sigma_HU, delta_HU)
            hexs = solve_transshipment_model(no_pinch_network, log_file=False, model_selected=model_selected, cost_selected=cost, alpha_w=alpha_w)
            print_matches_transshipment(hexs)

            if pinch_interval > 0:
                print("---- Above Pinch ----")
                above_pinch_network: Network = Network(min_up_test, sigma_HU, delta_HU, pinch_interval, below_pinch=False)
                ab_hexs = solve_transshipment_model(above_pinch_network, log_file=False, model_selected=model_selected, cost_selected=cost, alpha_w=alpha_w)

                print("---- Below Pinch ----")
                below_pinch_network: Network = Network(min_up_test, sigma_HU, delta_HU, pinch_interval, below_pinch=True)
                bl_hexs = solve_transshipment_model(below_pinch_network, log_file=False, model_selected=model_selected, cost_selected=cost, alpha_w=alpha_w)

                print("---- Combined ----")
                print_matches_transshipment(ab_hexs + bl_hexs)
