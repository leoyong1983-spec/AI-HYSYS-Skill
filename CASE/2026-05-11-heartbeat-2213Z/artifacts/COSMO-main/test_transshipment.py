# This file tests the implementation of the classes
from hens import Stream
from hens import Utility
from hens import MinUtilityProblem
from hens import solve_min_utility
from hens import solve_transshipment_model
from hens import solve_transport_model
from hens import Network


if __name__ == '__main__':

    # problems = ["balanced5", "balanced8", "balanced10", "balanced12", "balanced15"]
    # problems += ["unbalanced5", "unbalanced10", "unbalanced15", "unbalanced17", "unbalanced20"]

    problems = ["balanced5", "4sp1", "6sp-cf1", "6sp-gg1", "6sp1", "7sp-cm1", "7sp-s1", "7sp-torw1", "7sp1", "7sp2", "7sp4"]
    problems += ["8sp-fs1", "8sp1", "9sp-al1", "9sp-has1", "10sp-la1", "10sp-ol1", "10sp1", "12sp1", "14sp1", "15sp-tkm"] 
    problems += ["20sp1", "22sp-ph", "22sp1", "23sp1", "28sp-as1", "37sp-yfyv"]

    problems = ["balanced5"]

    for problem in problems:
        print("-----------------------------------{}-----------------------------------".format(problem))
        minup = MinUtilityProblem.generate_from_data(problem)
        sigma_HU, delta_HU, _ = solve_min_utility(minup)
        network = Network(minup, sigma_HU, delta_HU)
        solve_transshipment_model(network)
