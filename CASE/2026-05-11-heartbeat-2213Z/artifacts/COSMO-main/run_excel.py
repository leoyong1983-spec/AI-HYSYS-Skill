"""
This script performs heat exchange network synthesis (HENS) analysis based on
data provided in an Excel file. It reads process stream information from the
Excel file, calculates minimum utility requirements, generates composite and
grand composite curves, and solves transshipment models to design heat exchanger
networks. The script supports multiple models and can handle cases with and 
without pinch points.
"""
from hens import *
import os
import pandas as pd
import argparse

if __name__ == '__main__':
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Run heat exchange network synthesis from an Excel file.")
    parser.add_argument("excel_file", nargs='?', default="cases.xlsx", help="The path to the Excel file containing the case study data. Defaults to 'cases.xlsx' if not provided.")
    args = parser.parse_args()
    excel_file = args.excel_file  # Get the excel file from argument
    
    # Define the models and cost function to use
    models = ["M1", "M2", "M3", "M5", "M6"]
    cost = "cost"
    alpha_w = 25.0
    
    # Error check: Ensure the Excel file exists
    if not os.path.exists(excel_file):
        print(f"Error: Excel file '{excel_file}' not found.")
        exit()  # Stop execution if the file doesn't exist

    print(f"Reading from Excel file: {excel_file}")
    xls = pd.ExcelFile(excel_file)

    # Print the list of sheet names
    print("Sheet names in the Excel file:")
    for sheet_name in xls.sheet_names:
        print(f"- {sheet_name}")
    
    # Loop through each sheet in the Excel file to find the Maching Networks
    for sheet_name in xls.sheet_names:
        print(f"================================= Sheet:{sheet_name} =================================")
        # Create a MinUtilityProblem instance from the Excel sheet
        min_u_problem: MinUtilityProblem = MinUtilityProblem.generate_from_excel_sheet(xls, sheet_name)
        
        # Print the minimum demanded utility and pinch point temperature
        min_u_problem.print_minimum_demanded_utility()
        
        # Save composite and grand composite plots to output directory
        # Check if the output directory exists, create it if not
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        print("- Saving Composite and Grand Composite Plots -")
        filename = os.path.join(output_dir, f"{sheet_name}_composite.png")
        min_u_problem.plot_composite_diagram(save=True, filename=filename)
        filename = os.path.join(output_dir, f"{sheet_name}_grand_composite.png")
        min_u_problem.plot_grand_composite_curve(save=True, filename=filename)
        
        pinch_temperature = min_u_problem.pinch_temperature
        
        print("- Solving Min Utility Problem -")
        # Solve the Min Utility Problem
        sigma_HU, delta_HU, pinch_interval = solve_min_utility(min_u_problem, debug=False, pinch_temperature=pinch_temperature)

        for model_selected in models:
            print(f"================================= Model:{model_selected} =================================")
            print("------- Matches without Pinch -------")
            no_pinch_network: Network = Network(min_u_problem, sigma_HU, delta_HU)
            hexs = solve_transshipment_model(no_pinch_network, log_file=False, model_selected=model_selected, cost_selected=cost, alpha_w=alpha_w, debug=True)
            print_matches_transshipment(hexs)

            if pinch_interval > 0:
                print("- Solve Transshipment Model with Pinch Point : Above pinch point")
                above_pinch_network: Network = Network(min_u_problem, sigma_HU, delta_HU, pinch_interval, below_pinch=False)
                ab_hexs = solve_transshipment_model(above_pinch_network, log_file=False, model_selected=model_selected, cost_selected=cost, alpha_w=alpha_w)

                print("- Solve Transshipment Model with Pinch Point : Below pinch point")
                below_pinch_network: Network = Network(min_u_problem, sigma_HU, delta_HU, pinch_interval, below_pinch=True)
                bl_hexs = solve_transshipment_model(below_pinch_network, log_file=False, model_selected=model_selected, cost_selected=cost, alpha_w=alpha_w)

                print("------- Match with Pinch -------")
                print("Combine Above and Below Pinch")
                print_matches_transshipment(ab_hexs)
                print(f"--- Pinch Temperature (hot): {pinch_temperature} ---")
                print_matches_transshipment(bl_hexs)
            
            # Temporary break
            exit()

    print("================================= Done =================================")