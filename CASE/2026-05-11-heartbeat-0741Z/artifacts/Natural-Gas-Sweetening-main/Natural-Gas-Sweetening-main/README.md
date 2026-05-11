# Natural Gas Sweetening — DEA Absorption Simulation

Steady-state process simulation of a natural gas sweetening unit using diethanolamine (DEA), built in **Aspen HYSYS Version 14**. The unit removes H₂S and CO₂ from a sour associated gas stream to meet pipeline quality specifications.



## What This Simulates

A complete **absorption-regeneration loop** processing 1,244 kgmole/h of sour natural gas at 32.22°C and 6,893 kPa. Feed contains 1.74 mol% H₂S and 4.18 mol% CO₂ — both above pipeline limits.

The simulation covers:
- **T-100 Absorber** — 20 equilibrium stages, countercurrent DEA-gas contact at high pressure
- **V-101 Flash Vessel** — depressurisation to liberate co-absorbed hydrocarbons
- **T-101 Regenerator** — 18-stage stripping column with condenser and reboiler
- **E-100, E-101, E-102** — sour gas pre-cooler, lean/rich cross-exchanger, lean amine trim cooler
- **P-100, P-101** — rich and lean amine pumps
- **VLV-100, VLV-101** — pressure letdown valves
- **RCY-1** — recycle convergence block closing the lean amine loop

Thermodynamic framework: **Acid Gas — Chemical Solvents** property package (Kent-Eisenberg with NRTL activity coefficient corrections), the industry-standard choice for amine-acid gas systems.



## Key Results

| Parameter | Value |
|---|---|
| H₂S in sweet gas | 5.053 × 10⁻² ppm |
| H₂S removal efficiency | >99.9% |
| CO₂ removal efficiency | >99.7% |
| Lean amine circulation rate | 1,901 kgmole/h |
| Absorber L/G ratio | 1.528 mol/mol |
| Reboiler duty | 14,700,000 kJ/h (4,083 kW) |
| Condenser duty | 4,751,000 kJ/h (1,320 kW) |
| Reboiler temperature | 131.3°C |
| Specific reboiler duty | ~196,000 kJ/kgmole acid gas removed |

Pipeline spec is 4 ppm H₂S. The simulation achieves **0.05 ppm** — roughly 80× below the limit.

The specific reboiler duty falls within the published DEA benchmark range of 150,000–250,000 kJ/kgmole, confirming the simulation is physically realistic rather than artificially optimised.



## Feed and Solvent Specifications

**Sour Gas Feed (S1)**

| Component | mol% |
|---|---|
| Methane | 88.00 |
| Ethane | 3.98 |
| Propane | 0.94 |
| i-Butane | 0.26 |
| n-Butane | 0.29 |
| i-Pentane | 0.14 |
| n-Pentane | 0.12 |
| n-Hexane | 0.18 |
| H₂S | 1.74 |
| CO₂ | 4.18 |
| Nitrogen | 0.16 |

**Lean DEA Solution (DEA1)**

| Parameter | Value |
|---|---|
| DEA concentration | 6.25 mol% (~25–30 wt%) |
| Temperature | 40.56°C |
| Pressure | 6,844 kPa |
| Molar flow | 1,901 kgmole/h |
| Lean H₂S loading | 0.01 mol% |

## Energy Summary

| Stream | Equipment | Duty (kW) |
|---|---|---|
| Qe | T-101 Reboiler | 4,083.3 |
| H2 | E-102 Lean cooler | 2,628.3 |
| QC | T-101 Condenser | 1,319.7 |
| H1 | E-100 Pre-heater | 134.7 |
| P2 | P-101 Lean pump | 103.1 |
| P1 | P-100 Rich pump | 3.3 |

The reboiler accounts for 100% of external heat input. Pumps together contribute less than 3% of reboiler energy — liquid circulation is not the energy driver here, thermal regeneration is.

The trim cooler E-102 rejects 2,628 kW to cooling water after the lean/rich cross-exchange. That gap is the primary target for future heat integration work.



## Column Profiles

**Absorber T-100** — temperature rises from 40.67°C (top) to a peak of 74.93°C at Stage 18, then drops slightly to 64.12°C at the bottom. The mid-column bulge is characteristic of a well-loaded DEA absorber; it marks where acid gas loading and heat of reaction are highest.

**Regenerator T-101** — temperature jumps from 45.05°C at the condenser to ~110°C at Stage 1, then climbs steadily to 131.3°C at the reboiler. The sharp liquid flow increase at Stage 4 (113 → 2,143 kgmole/h) marks the rich amine feed entry.



## Convergence

Both columns converged fully in HYSYS (green status):

- **T-100**: reflux ratio = 1.628
- **T-101**: reflux ratio = 1.343, boilup ratio = 0.1954
- **RCY-1**: lean amine recycle loop closed within default HYSYS tolerance, no manual tear stream required



## Future Work

Three parametric studies are identified as the highest-value next steps:

1. **Circulation rate sweep** (1,500–2,500 kgmole/h) — map the optimum where energy cost of over-circulation exceeds the gain in removal efficiency
2. **Reboiler duty sweep** (3,000–5,000 kW) — find the minimum duty that still meets 4 ppm H₂S specification
3. **Feed composition upsets** — test robustness at 3.00 and 5.00 mol% inlet H₂S

Longer term: integrate the lean amine cooling train with **Aspen Energy Analyzer** for systematic Pinch Analysis, targeting further reboiler duty reduction beyond what the E-101 cross-exchanger alone achieves.



## Software

- **Aspen HYSYS Version 14** — Aspen Technology Inc.
- **Thermodynamic package** — Acid Gas — Chemical Solvents (Kent-Eisenberg + NRTL)
- **Unit set** — SI10



## References

1. Kohl, A.L. and Nielsen, R.B. (1997) *Gas Purification*, 5th edn. Gulf Publishing Company.
2. Kidnay, A.J., Parrish, W.R. and McCartney, D.G. (2011) *Fundamentals of Natural Gas Processing*, 2nd edn. CRC Press.
3. Gas Processors Suppliers Association (2012) *GPSA Engineering Data Book*, 13th edn.
4. Oyenekan, B.A. and Rochelle, G.T. (2006) 'Energy performance of stripper configurations for CO₂ capture by aqueous amines', *Industrial and Engineering Chemistry Research*, 45(8), pp. 2457–2464.



## Author

**Shahriar Hossain Suny**  
Department of Chemical Engineering  
Jashore University of Science and Technology (JUST), Bangladesh  
AIChE Member ID: 009905932744  
[LinkedIn](https://www.linkedin.com/in/shahriarhossainsuny/) · [GitHub](https://github.com/shahria-sunny)
