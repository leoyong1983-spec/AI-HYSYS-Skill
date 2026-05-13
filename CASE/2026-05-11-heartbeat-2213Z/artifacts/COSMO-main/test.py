from cosmo import *

sim = hysys_simulation.simulation(filename='Test_1')

if sim:
    component_list = sim.component_list
    for cl in component_list:
        print(cl["fluid package"])
        print(cl["property package"])
        print(cl["components"])
