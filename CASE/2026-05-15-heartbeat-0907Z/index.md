# CASE Heartbeat 2026-05-15 0907Z

## 1. Run Time

- Trigger UTC time: 2026-05-15T09:07:50.854Z
- Local workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-15-heartbeat-0907Z
- Artifacts directory: CASE/2026-05-15-heartbeat-0907Z/artifacts
- Model run status: not_run for all entries; no HYSYS model, script, macro, workbook or executable was run.

## 2. Searched Mining Areas

- GitHub repository search, with emphasis on licensed results and README-indexed HYSYS case mentions.
- GitHub tree inspection for selected MIT/GPL/Apache/NOASSERTION and no-license high-signal candidates.
- Existing CASE dedupe pass over 25 previous sources.json files and 126 source entries.

## 3. Keywords Used

- `HYSYS license:mit`, `HYSYS license:gpl-3.0`, `HYSYS license:apache-2.0`
- `Aspen HYSYS in:readme`, `HYSYS hsc in:readme`, `HYSYS hscz in:readme`, `HYSYS case file in:readme`
- `HYSYS Excel validation in:readme`, `HYSYS win32com Python in:readme`

## 4. Downloaded Case List

Final new downloads: 0.

Three MIT repositories were re-discovered and briefly fetched for SHA verification, then identified as already archived. Their current-run payload directories were removed before commit, leaving only metadata and duplicate evidence:

- `shahria-sunny/Natural-Gas-Sweetening`: already archived in `CASE/2026-05-11-heartbeat-0741Z`; matching `Gas Sweetening.hsc` SHA256 `fcda75090796e9ba8a69bfb29a769deea36761d11d26c93d51d98318d19d4610`.
- `shahria-sunny/CDU-Simulation-Optimization`: already archived in `CASE/2026-05-11-heartbeat-0741Z`; matching `project.hsc` SHA256 `795c3587c611405f4786115514030036987615e47c33fe74aba1fcb1610fbdd2`.
- `kavinrajachakravarthy/Pressure-Drop-Estimation-in-Pipelines`: already archived in `CASE/2026-05-11-heartbeat-0741Z`; matching HYSYS model SHA256 `312418da47afc724bd75ef9d61c05c95cb1ad783010d39bc06793a25b579b9ac`.

## 5. Duplicate Licensed Cases Confirmed

### B - Natural Gas Sweetening DEA Absorption Simulation

- Source page: https://github.com/shahria-sunny/Natural-Gas-Sweetening
- Local canonical archive: `CASE/2026-05-11-heartbeat-0741Z`
- Selection reason: MIT repository with `.hsc`, PDF report, README and License.
- Dedupe basis: source URL plus matching model/report/license/README SHA256 values.
- Recommended automation use: natural gas sweetening, DEA absorption and acid-gas removal regression tests.
- Residual risk: no HYSYS runtime validation was performed in this run.

### B - Crude Oil Atmospheric Distillation Simulation and Energy Optimization

- Source page: https://github.com/shahria-sunny/CDU-Simulation-Optimization
- Local canonical archive: `CASE/2026-05-11-heartbeat-0741Z`
- Selection reason: MIT repository with `project.hsc`, CDU report, README and License.
- Dedupe basis: source URL plus matching `project.hsc` SHA256.
- Recommended automation use: crude distillation, refinery CDU and energy optimization regression tests.
- Residual risk: no HYSYS runtime validation was performed in this run.

### B - Pressure Drop Estimation in Pipelines

- Source page: https://github.com/kavinrajachakravarthy/Pressure-Drop-Estimation-in-Pipelines
- Local canonical archive: `CASE/2026-05-11-heartbeat-0741Z`
- Selection reason: MIT repository with `.hsc`, Excel workbook, report PDFs and Python/MATLAB scripts.
- Dedupe basis: source URL plus matching HYSYS model and companion file SHA256 values.
- Recommended automation use: pipeline pressure-drop comparison, HYSYS-vs-script checks and data extraction tests.
- Residual risk: no scripts or HYSYS models were executed in this run.

### B - ap-python Aspen HYSYS automation test case

- Source page: https://github.com/bsha0/ap-python
- Local canonical archive: `CASE/2026-05-11-heartbeat-1057Z`
- Selection reason: MIT repository with `Atmospheric Crude Tower.hsc` and Python automation package.
- Dedupe basis: existing source URL and prior archive record.
- Recommended automation use: package-level Python/HYSYS automation smoke tests.
- Residual risk: no HYSYS runtime validation was performed in this run.

## 6. New Candidate-Only Findings

- `iraola/tennessee-eastman-hysys`: contains `TENNESSEE_EASTMAN_PROCESS_HYSYS.HSC`; GitHub license field is `NOASSERTION`, so manual license review is required.
- `Pouria-MK/_Jan.2024_Simulation-and-Economic-Evaluation-of-Syngas-Generation-Plant-using-DMR-and-SMR-Reactors`: contains two `.hsc` files, XML, Excel and PDF reports; no License detected.
- `Pouria-MK/_Dec.2023_Technical-and-Financial-Analysis-and-Feasibility-of-Styrene-plant`: contains `.hsc` and `.hscz` files, reports and spreadsheets; filenames indicate HYSYS V12, but no License detected.
- `lihaijie1228/hysys_python_GA`: contains `Decarbonization.hsc`, CSV/TXT and Python scripts; no License detected.
- `chickenhgbla/gaussian-process-rto`: contains `testing.hsc`, Excel and MATLAB scripts; no License detected.

These were not downloaded because license or redistribution rights are unresolved.

## 7. Licensed But No-Model References

- `Galigeigei-Z/HDA-Surrogate-Optimization`: MIT, automation/surrogate material, no HYSYS case file found.
- `Jeslin-Jacob/rbf-interpolation-atmospheric-distillation`: MIT, data/code reference, no HYSYS case file found.
- `OptiMaL-PSE-Lab/Sketch2Simulation`: MIT, AI-to-flowsheet reference, no HYSYS case file found.

## 8. Safety Notes

- No final model payload was added this run.
- Current-run duplicate payload copies were removed before commit after SHA/source-page dedupe.
- Final committed artifacts are JSON metadata plus `index.md` and `sources.json` only.
- Security inventory reports no executable or macro-like files in final run artifacts.

## 9. Residual Risks

- Some public repositories may have unclear licensing despite visible files.
- GitHub search can miss binary `.hsc/.hscz` files; repository-tree inspection remains the better method.
- Candidate repository metadata confirms filenames, not model integrity, because payloads were not retained or opened.

## 10. Follow-up Recommendations

1. Add an explicit duplicate allowlist for the four already archived MIT cases above to stop repeated fetch attempts.
2. Ask maintainers/authors for license clarification on Tennessee Eastman, Syngas DMR/SMR, Styrene V12, Decarbonization GA and Gaussian-process RTO candidates.
3. Prefer repository-tree scanning over GitHub code search for `.hsc` discovery.
4. Keep `CASE/2026-05-11-heartbeat-0741Z` as the canonical location for the three confirmed duplicate MIT engineering cases.
