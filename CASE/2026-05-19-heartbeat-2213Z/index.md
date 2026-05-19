# Aspen HYSYS Case Discovery Heartbeat - 2026-05-19 22:13Z

## Run Time

- Trigger UTC time: 2026-05-19T22:13:37.399Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-19-heartbeat-2213Z
- Artifacts directory: CASE/2026-05-19-heartbeat-2213Z/artifacts
- Model run status: not_run

## Repository Gate

- Confirmed Git repository: yes
- Confirmed branch: main
- Pull mode: git pull --ff-only origin main
- Pull result: success; repository already up to date after pushing the prior local CASE commit e67c67a
- Scope written this run: CASE/2026-05-19-heartbeat-2213Z/index.md and sources.json only

## Search Mines

- GitHub repository search
- GitHub repository tree inspection
- Existing CASE index and sources.json dedupe scan

## Keywords And Search Patterns

- Aspen HYSYS
- HYSYS simulation
- AspenHYSYS
- Aspen-HYSYS
- Aspen HYSYS README
- HYSYS .hsc
- HYSYS XML
- HYSYS Excel validation

## Downloaded Case List

No model payload was downloaded in this run.

Reason: the high-license hits were duplicates already archived or already recorded, while the new leads lacked a HYSYS case payload or lacked explicit redistribution permission.

## New Candidate Findings

### Alnawakhtha/Computer-aided-CDU-Revamp

- Source page: https://github.com/Alnawakhtha/Computer-aided-CDU-Revamp
- Download URL considered: https://codeload.github.com/Alnawakhtha/Computer-aided-CDU-Revamp/zip/refs/heads/main
- Local files downloaded: none
- Selection reason: public CDU/VDU revamp repository explicitly describes Aspen HYSYS modeling and heat integration.
- Quality rating: D
- License/public access note: public GitHub repository, but no explicit license detected.
- Recommended automation use: no benchmark use now; possible README-only planning reference if permission and model assets are later published.
- Dedupe basis: source_page was not found in prior CASE records.
- Residual risks: default tree inspection found README only among target artifact types; no .hsc/.hscz/.xml/.compound exposed; no license.

### Ankesh-cloud/Simulation-of-Acid-Gas-Removal-Unit-using-ASPEN-HYSYS

- Source page: https://github.com/Ankesh-cloud/Simulation-of-Acid-Gas-Removal-Unit-using-ASPEN-HYSYS
- Download URL considered: https://codeload.github.com/Ankesh-cloud/Simulation-of-Acid-Gas-Removal-Unit-using-ASPEN-HYSYS/zip/refs/heads/main
- Local files downloaded: none
- Selection reason: public acid gas removal HYSYS project lead with README and poster PDF.
- Quality rating: D
- License/public access note: public GitHub repository, but no explicit license detected.
- Recommended automation use: manual source review only; no automation benchmark use without model file and license.
- Dedupe basis: source_page was not found in prior CASE records.
- Residual risks: no HYSYS case file exposed in inspected tree; no license.

### Mo-Somji/HYSYS-ME-Balance-Formatting

- Source page: https://github.com/Mo-Somji/HYSYS-ME-Balance-Formatting
- Download URL considered: https://codeload.github.com/Mo-Somji/HYSYS-ME-Balance-Formatting/zip/refs/heads/main
- Local files downloaded: none
- Selection reason: public HYSYS mass and energy balance formatting repository with Excel input/output examples.
- Quality rating: D
- License/public access note: public GitHub repository, but no explicit license detected.
- Recommended automation use: possible future HYSYS report post-processing reference after license review; not a case benchmark.
- Dedupe basis: source_page was not found in prior CASE records.
- Residual risks: no HYSYS model payload; no license; data provenance unclear.

## Duplicate/Skip Notes

- edgarsmdn/Aspen_HYSYS_Python, kavinrajachakravarthy/Pressure-Drop-Estimation-in-Pipelines, shahria-sunny/Natural-Gas-Sweetening, shahria-sunny/CDU-Simulation-Optimization, may3rd/COSMO, and andr1976/dwsim-paper are licensed or strong GitHub hits but already present in prior CASE records.
- Jeslin-Jacob/rbf-interpolation-atmospheric-distillation is MIT licensed but already recorded as a data-only candidate with no exposed HYSYS model payload.
- Galigeigei-Z/HDA-Surrogate-Optimization is MIT licensed but already recorded as a no-case interface candidate.

## Residual Risk

- GitHub public visibility does not equal permission to archive or redistribute Aspen HYSYS binary models.
- Several current leads are descriptive repositories without exposed case files.
- No HYSYS model was downloaded, opened, run, or solved.

## Follow-Up

- Continue GitHub-first search, but filter earlier for explicit LICENSE plus actual .hsc/.hscz/.xml/.compound paths.
- Build a manual permission queue for no-license repositories that expose case files but are not eligible for automatic archival.
- Consider adding a lightweight dedupe helper that stores prior source_page and representative filenames in a generated lookup table.
