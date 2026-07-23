# Aspen HYSYS Case Discovery Heartbeat - 2026-05-17 1711Z

- Run time UTC: 2026-05-17T17:11:15Z
- Local HYSYS model run status: not_run; no model was opened, executed, solved, or macro/script-run.
- Repository gate: main branch, clean worktree, git pull --ff-only origin main completed before discovery.
- Model-bearing rule: only `.hsc`, `.hscz`, `.compound`, or XML paths explicitly containing `hysys` count as HYSYS primary models.
- Existing CASE dedupe baseline: 214 source entries, 167 source pages, 122 download URLs, 887 filenames, 769 SHA256 values.

## Searched Mines
- GitHub code search via `gh search code`
- GitHub repository search via GitHub REST API
- GitHub repository tree and license inspection
- Zenodo records API quick scan
- GitLab project API quick scan
- Bitbucket repository API quick scan

## Keywords
- `HYSYS --extension py`
- `OpenCase HYSYS --extension py`
- `SimulationCase HYSYS --extension py`
- `.hsc HYSYS`
- `Aspen HYSYS`
- `HYSYS --extension m`
- `HYSYS --extension bas`
- `Aspen HYSYS hsc`
- `HYSYS case file`
- `Aspen HYSYS simulation files`
- `Aspen HYSYS optimization`
- `HYSYS Python COM`
- `HYSYS MATLAB Aspen`
- `HYSYS Excel automation`
- `Aspen HYSYS .hsc`
- `Aspen HYSYS .hscz`
- `HYSYS XML Cases .xml`

## Downloaded Cases
- No new high-confidence downloadable nonduplicate HYSYS cases were found this run.

## Candidate And Duplicate Records
- Candidate only: Ahmedhassan676/Python4ChemicalEngineers (D)
  - Source page: https://github.com/Ahmedhassan676/Python4ChemicalEngineers
  - Download URL: https://codeload.github.com/Ahmedhassan676/Python4ChemicalEngineers/zip/refs/heads/main
  - Local evidence: CASE/2026-05-17-heartbeat-1711Z/artifacts/github-1711-repo-Ahmedhassan676__Python4ChemicalEngineers.json, CASE/2026-05-17-heartbeat-1711Z/artifacts/github-1711-tree-Ahmedhassan676__Python4ChemicalEngineers.json, CASE/2026-05-17-heartbeat-1711Z/artifacts/github-1711-license-Ahmedhassan676__Python4ChemicalEngineers.json
  - License/public access: Public GitHub repository; license metadata NOASSERTION. Not downloaded because explicit archival/redistribution license was not detected.
  - Recommended automation use: Use existing archived copy if duplicate; otherwise request maintainer license clarification before download.
  - Dedupe basis: source_page `https://github.com/Ahmedhassan676/Python4ChemicalEngineers`, download_url `https://codeload.github.com/Ahmedhassan676/Python4ChemicalEngineers/zip/refs/heads/main`, filenames ['water&gas.hsc']
  - Residual risks: License/redistribution permission requires human review.; No local Aspen HYSYS runtime validation performed.

## Skipped Non-Model Candidates
- Inspected GitHub repositories without true HYSYS primary model: 19. See `artifacts/github-1711-skipped-no-model.json`.

## Search Evidence Artifacts
- `artifacts/dedupe-summary.json`
- `artifacts/github-1711-search-summary.json`
- `artifacts/github-1711-inspection-summary.json`
- `artifacts/github-1711-model-bearing-repositories.json`
- `artifacts/github-1711-dedupe-assessment.json`
- `artifacts/github-1711-skipped-no-model.json`
- `artifacts/external-1711-search-summary.json`
- `artifacts/download-summary.json`
- `artifacts/security-inventory.json`

## Quality Ratings
- A: model + paper/report + validation data + DOI/license/clear provenance.
- B: model + README/report/public repository with clear license but limited validation.
- C: model with basic credible provenance but limited support material.
- D: candidate/duplicate record only; not downloaded or not recommended for new benchmark inclusion this run.

## Residual Risks
- No Aspen HYSYS runtime validation was performed.
- Some code-search hits are useful automation references but lack primary HYSYS model files.
- Public repository license metadata remains repository-level and should be reviewed before redistribution of proprietary-format model binaries.

## Follow-Up Suggestions
- Continue code-search-first discovery but keep the strict true-model classifier.
- Add persistent denylist entries for no-model automation repositories to reduce hourly inspection load.
- For no-license model-bearing repositories, request explicit license before archival.

## Summary
- New downloaded cases: 0
- New nonduplicate candidate-only records: 1
- Duplicate model-bearing records retained: 0
- Inspected GitHub repositories: 20
- True model-bearing GitHub repositories: 1
- Skipped no-model repositories: 19
