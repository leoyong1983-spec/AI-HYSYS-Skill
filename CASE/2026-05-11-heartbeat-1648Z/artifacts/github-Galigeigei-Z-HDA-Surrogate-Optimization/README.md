# Sustainability assessment and optimization of a toluene hydrodealkylation process using surrogate models

## Overview

This project presents a data-driven and explainable framework for the sustainability assessment and optimization of a full toluene hydrodealkylation (HDA) flowsheet, integrating global sensitivity analysis (GSA), surrogate modeling, and Bayesian optimization (BO) within a composite Life-Cycle Sustainability Index (LCSI) framework.

The methodology is designed to address the intrinsically coupled and multi-objective nature of process-level sustainability, simultaneously considering economic, environmental, social, and technological performance metrics while maintaining high computational efficiency.

<img width="1193" height="712" alt="Framework overview" src="https://github.com/user-attachments/assets/ae1d8f72-0d16-40ca-917c-ac6057f7beee" />

Within this broader framework, this repository now exposes two focused demos:

- `heat_network_supertargeting/`
  - the original workbook-based heat-network and pinch-analysis workflow
  - includes the Excel input sheet, local helper package, pre-rendered figures,
    and a standalone notebook
- `hysys_interface_demo/`
  - a teaching-oriented Aspen HYSYS COM automation demo
  - shows how to connect Python to an active HYSYS case, map stream and unit-op
    names, apply parameter changes, and inspect results

## Folder Guide

### `heat_network_supertargeting/`

Use this folder when you want the original heat-integration workflow:

- read thermal streams from Excel
- convert the rows into `ThermalStream` objects
- run automatic supertargeting at a selected `Delta Tmin`
- review summary metrics, area intervals, and composite-curve style plots

### `hysys_interface_demo/`

Use this folder when you want the Aspen HYSYS automation workflow:

- connect to an already-open HYSYS case through `win32com`
- inspect material streams and unit operations from Python
- apply flowsheet changes in a structured way
- run the same notebook in mock mode when HYSYS is not available


## Citation

If this repository is useful for your work, please consider citing:

**Ziyun Zhang and Eldin Wee Chuan Lim**  
*Sustainability assessment and optimization of a toluene hydrodealkylation process using surrogate models*  
Chemical Engineering Science (2026)  
https://doi.org/10.1016/j.ces.2026.124158

## Acknowledgement

The authors also gratefully acknowledge A/Prof. Sachin V. Jangam for for his teaching in `CN4205 Pinch Analysis and Process Integration`, from which this work benefited.


## Contact

Questions, feedback, or collaboration ideas are welcome. Feel free to contact me: "Ziyoon_Zhang@outlook.com"
