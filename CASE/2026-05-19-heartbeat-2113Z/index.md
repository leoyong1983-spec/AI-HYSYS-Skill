# Aspen HYSYS Case Discovery Heartbeat - 2026-05-19 21:13Z

## Run Time

- Trigger UTC time: 2026-05-19T21:13:41.705Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-19-heartbeat-2113Z
- Artifacts directory: CASE/2026-05-19-heartbeat-2113Z/artifacts
- Model run status: not_run for all entries

## Repository Gate

- Confirmed Git repository: yes
- Confirmed branch: main
- Pull mode: git pull --ff-only origin main
- Pull result: success, fast-forwarded to origin/main before discovery
- Scope written this run: CASE/2026-05-19-heartbeat-2113Z/index.md and sources.json only

## Search Mines

- GitHub repository search and repository tree inspection
- Existing CASE index and sources.json dedupe scan

## Keywords And Search Patterns

- HYSYS
- Aspen HYSYS
- Aspen HYSYS .hsc
- Aspen HYSYS README
- HYSYS XML
- extension:hsc
- extension:hscz
- HYSYS automation
- HYSYS Excel validation

## Downloaded Case List

No model payload was downloaded in this run.

Reason: all non-duplicate new targets found in this pass lacked an explicit license or had additional provenance risk. Per the safety rule, they were recorded as candidates only and not downloaded.

## Candidate Findings

### lior-abadi/chemEng-system-design

- Source page: https://github.com/lior-abadi/chemEng-system-design
- Download URL considered: https://codeload.github.com/lior-abadi/chemEng-system-design/zip/refs/heads/main
- Local files downloaded: none
- Selection reason: public repository with formaldehyde process design material, HYSYS/UniSim XML-like files, PDF reports, and Excel workbooks.
- Quality rating: D
- License/public access note: public GitHub repository, but no explicit license detected; do not archive model files until author permission or license is clarified.
- Recommended automation use: candidate for future HYSYS XML import/parser triage and spreadsheet-interface review after permission.
- Dedupe basis: source_page not found in prior CASE records; filenames checked against prior candidate list.
- Residual risks: unclear license; XML files may be UniSim/HYSYS-adjacent rather than confirmed HYSYS XML cases; XLSM files may contain macros and were not downloaded or executed.

### puttak/aspen

- Source page: https://github.com/puttak/aspen
- Download URL considered: https://codeload.github.com/puttak/aspen/zip/refs/heads/master
- Local files downloaded: none
- Selection reason: public repository exposes several .hsc files under udemyHYSYS.
- Quality rating: D
- License/public access note: public GitHub repository, but no explicit license detected.
- Recommended automation use: only manual provenance review; do not use as benchmark until redistribution rights are confirmed.
- Dedupe basis: source_page not found in prior CASE records; representative .hsc filenames checked.
- Residual risks: folder naming suggests possible course-derived material; license absent; no supporting validation package found in this scan.

### zulfanadiputra/DME-plant-HYSYS

- Source page: https://github.com/zulfanadiputra/DME-plant-HYSYS
- Download URL considered: https://codeload.github.com/zulfanadiputra/DME-plant-HYSYS/zip/refs/heads/main
- Local files downloaded: none
- Selection reason: public repository includes DMEPlant in V12.hsc and README, matching DME/methanol process priority.
- Quality rating: D
- License/public access note: public GitHub repository, but no explicit license detected.
- Recommended automation use: possible future HYSYS V12 compatibility smoke candidate after permission.
- Dedupe basis: source_page and filename were not found in prior CASE records.
- Residual risks: no explicit license; limited documentation; HYSYS version inferred only from filename.

### JeePeiQi0101/Design.Distillation.Column.HYSYS

- Source page: https://github.com/JeePeiQi0101/Design.Distillation.Column.HYSYS
- Download URL considered: https://codeload.github.com/JeePeiQi0101/Design.Distillation.Column.HYSYS/zip/refs/heads/main
- Local files downloaded: none
- Selection reason: public repository exposes a HYSYS-named XML file and distillation design report.
- Quality rating: D
- License/public access note: public GitHub repository, but no explicit license detected.
- Recommended automation use: candidate for future distillation XML import review after permission.
- Dedupe basis: source_page not found in prior CASE records; related JeePeiQi0101/Aspen.HYSYS records exist but this is a distinct repository.
- Residual risks: no explicit license; XML may require manual HYSYS/UniSim verification; model was not downloaded or opened.

## Deduplication Summary

Existing CASE records already contain prior entries for IcedCoffeeBoy/PSO_hysys_optimisation, theodoreOnzGit/hysys-tutorials, SinaGhanbarii/HDA-Plant-Simulation, masoud-abdi/The-simulation-of-Acetic-Acid-process, Corey-McInrue/Node-C-ASPEN-HYSYS, and JeePeiQi0101/Aspen.HYSYS, so those were not re-recorded except as context during screening.

## Residual Risk

- GitHub public visibility does not equal permission to archive or redistribute Aspen HYSYS binary cases.
- Several candidate repositories contain XLSM files or possible course-derived assets; no macros, scripts, or binaries were downloaded or executed.
- No model was loaded in Aspen HYSYS; all model_run_status values remain not_run.

## Follow-Up

- Ask authors for explicit permission or license clarification for the four candidate repositories above.
- Continue GitHub-first search, but bias toward repositories with LICENSE files or DOI-backed supplemental archives.
- Add candidate repositories with license gaps to a manual permission queue instead of repeatedly re-discovering them.
