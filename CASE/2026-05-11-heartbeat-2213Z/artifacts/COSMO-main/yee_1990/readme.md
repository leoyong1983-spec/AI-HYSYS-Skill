# HEN Synthesis using Yee & Grossmann (1990) Stage-wise Superstructure

This Python script implements the Heat Exchanger Network (HEN) synthesis model proposed by T. F. Yee and I. E. Grossmann (1990). The model formulates HEN synthesis as a Mixed Integer Nonlinear Programming (MINLP) problem based on a stage-wise superstructure. It simultaneously optimizes utility costs, exchanger areas, and the selection of matches.

## References

-   Yee, T. F., and Grossmann, I. E. (1990). Simultaneous optimization models for heat integration—II. Heat exchanger network synthesis. _Computers & Chemical Engineering, 14_(10), 1165-1184.
-   Chen, J. J. J. (1987). Letter to the Editors: Comments on improvement on a replacement for the logarithmic mean. _Chemical Engineering Science, 42_(10), 2488-2489. (For LMTD approximation)

## Model Features

-   **Simultaneous Optimization**: Considers trade-offs between energy (utility) cost, fixed exchanger costs, and area-dependent capital costs.
-   **Stage-wise Superstructure**: Allows potential matches between any hot and cold stream in any stage.
-   **Linear Constraints**: Most constraints are linear, with nonlinearities primarily in the area cost terms of the objective function (due to LMTD approximation and power law for cost).
-   **Isothermal Mixing Assumption**: Simplifies heat balances for stream splits within the MINLP. The paper suggests an NLP sub-optimization if splits occur in the solution (not implemented in this script's core MINLP).
-   **Flexibility**:
    -   Handles multiple utilities.
    -   Can incorporate forbidden/required matches.
    -   Can model variable inlet/outlet temperatures (extension).
    -   No-split constraints can be optionally enforced.

## Usage

1.  **Prepare Input CSV Files**:

    -   `streams.csv`: Hot and cold process stream data (Name, Type, TIN_spec, TOUT_spec, Fcp).
    -   `utilities.csv`: Utility stream data (Name, Type, TIN_utility, TOUT_utility, Unit_Cost_Energy, U_overall, cost parameters).
    -   `matches_U_cost.csv`: Parameters for process-process matches (Hot_Stream, Cold_Stream, U_overall, Fixed_Cost_Unit, Area_Cost_Coeff, Area_Cost_Exp).
    -   (Optional) `forbidden_matches.csv`, `required_matches.csv`.

2.  **Configure Parameters**:

    -   Edit the `config` dictionary in the main script execution part. Key parameters:
        -   `NOK`: Number of stages. 'auto' calculates `max(num_hot_streams, num_cold_streams)`.
        -   `Epsilon_dt`: Minimum temperature approach (EMAT).
        -   `Omega_Q_factor`: Factor to estimate Big-M for heat loads.
        -   `Omega_T`: Big-M for temperature approaches in inactive matches.
        -   `Allow_Splits`: Boolean, if False, no-split constraints are added.
        -   `Fixed_Cost_Exchanger_Process`: Global fixed cost if not specified per match.

3.  **Run the Script**:

    ```bash
    python hen_synthesis_yee_grossmann.py
    ```

    Ensure a compatible MINLP solver (e.g., Couenne, Bonmin, SCIP, BARON) is installed and accessible by Pyomo.

4.  **Review Output**:
    -   The script will print the total annual cost, cost breakdown, details of active matches and utility usage (heat loads, areas, temperatures), and stream temperature profiles.

## Python Dependencies

-   `pandas`
-   `pyomo`
-   An MINLP solver compatible with Pyomo (e.g., Couenne, Bonmin, BARON, SCIP). Some solvers might require separate installation and licensing.

## Traceability to Paper Equations

Inline comments in the `build_hen_model` function link parts of the code to the equation numbers in Yee & Grossmann (1990), Part II.

## Extensions

-   **Variable Temperatures**: Modify input and model to allow `TIN_actual` and `TOUT_actual` to be variables within specified bounds.
-   **NLP Sub-optimization for Splits**: If the MINLP solution includes stream splits (multiple `z_match` active for a stream in a stage), implement the NLP sub-optimization step (Fig. 3 of the paper) to refine flow rates and areas.
-   **More Complex Costing**: User-defined Python functions for area or cost calculations.
-   **Multi-period Operation**: Extend the model for varying operating conditions.
-   **Pressure Drop**: Incorporate pressure drop considerations and pumping costs.

## Limitations & Pitfalls

-   **MINLP Solvers**: Requires a robust MINLP solver. Open-source solvers like Couenne or Bonmin can handle moderately sized problems. Commercial solvers like BARON or Gurobi (with non-convex capabilities) may be needed for larger or more complex instances.
-   **Non-convexity**: The objective function is non-convex due to area cost terms (LMTD approximation and power law). The solver may find a local optimum. Good initialization or multi-start strategies can help (not implemented here).
-   **Computational Time**: MINLP problems can be computationally intensive. Problem size (number of streams, stages) significantly impacts solution time.
-   **Big-M Values**: Appropriate selection of `Omega_Q` (for heat loads) and `Omega_T` (for temperature approaches) is crucial for model robustness and correctness. If too small, they can cut off feasible solutions; if too large, they can cause numerical issues.
-   **Isothermal Mixing**: The MINLP relies on this assumption. If significant temperature changes occur upon mixing split branches, the area calculations might be inaccurate, necessitating the NLP sub-optimization step mentioned in the paper.
-   **Chen's LMTD Approximation**: While widely used, it is an approximation. The `(dt1 * dt2 * (dt1+dt2)/2)^(1/3)` term can be problematic if `dt1+dt2` becomes negative or zero, or if `dt1` or `dt2` are zero when `q > 0`. The model uses `Epsilon_dt` to keep `dt` values positive.
