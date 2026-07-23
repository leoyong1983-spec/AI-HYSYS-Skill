from hens import *

filename = r'test.csv'
minup: MinUtilityProblem = MinUtilityProblem.generate_from_csv(filename)

print(minup)

# minup.print_temperature_interval()
# minup.plot_composite_diagram()
# minup.plot_grand_composite_curve()

sigma_HU, delta_HU, pinch_interval = solve_min_utility(minup, debug=False)

print("======= No Pinch =======")
no_pinch_network: Network = Network(minup, sigma_HU, delta_HU)
hexs = solve_transshipment_model(no_pinch_network, log_file=False, model_selected="M1", cost_selected="cost", alpha_w=25.0)
print_matches_transshipment(hexs)

#print("======= Above Pinch =======")
above_pinch_network: Network = Network(minup, sigma_HU, delta_HU, pinch_interval, below_pinch=False)
ab_hexs = solve_transshipment_model(above_pinch_network, log_file=False, model_selected="M1", cost_selected="cost", alpha_w=25.0)
#print_matches_transshipment(ab_hexs)

#print("======= Below Pinch =======")
below_pinch_network: Network = Network(minup, sigma_HU, delta_HU, pinch_interval, below_pinch=True)
bl_hexs = solve_transshipment_model(below_pinch_network, log_file=False, model_selected="M1", cost_selected="cost", alpha_w=25.0)
#print_matches_transshipment(bl_hexs)

print("======= Pinch Matches =======")
print_matches_transshipment(ab_hexs + bl_hexs)