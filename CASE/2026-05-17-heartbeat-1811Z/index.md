# Aspen HYSYS Case Discovery Heartbeat - 2026-05-17 1811Z

- Run time UTC: 2026-05-17T18:11:44Z
- Local HYSYS model run status: not_run; no model was opened, executed, solved, or macro/script-run.
- Repository gate: main branch, clean worktree, git pull --ff-only origin main completed before discovery.
- Model-bearing rule: only `.hsc`, `.hscz`, `.compound`, or XML paths explicitly containing `hysys` count as HYSYS primary models.
- Existing CASE dedupe baseline: 215 source entries, 168 source pages, 123 download URLs, 891 filenames, 771 SHA256 values.

## Searched Mines
- GitHub code search via `gh search code`
- GitHub repository search via GitHub REST API
- GitHub repository tree and license inspection
- Zenodo records API quick scan
- GitLab project API quick scan
- Bitbucket repository API quick scan

## Keywords
- `HYSYS --extension py`
- `HYSYS COM --extension py`
- `OpenCase HYSYS --extension py`
- `HYSYS Spreadsheet --extension py`
- `.hsc HYSYS`
- `.hscz HYSYS`
- `Aspen HYSYS README`
- `HYSYS --extension m`
- `Aspen HYSYS hsc`
- `Aspen HYSYS hscz`
- `HYSYS case file`
- `Aspen HYSYS simulation files`
- `HYSYS Python COM`
- `HYSYS MATLAB Aspen`
- `HYSYS Excel validation`
- `Aspen HYSYS optimization case`
- `Aspen HYSYS .hsc`
- `Aspen HYSYS .hscz`
- `HYSYS XML Cases .xml`

## Downloaded Cases
- No new high-confidence downloadable nonduplicate HYSYS cases were found this run.

## Candidate And Duplicate Records
- Candidate only: EmPajak21/multiagentllms (D)
  - Source page: https://github.com/EmPajak21/multiagentllms
  - Download URL: https://codeload.github.com/EmPajak21/multiagentllms/zip/refs/heads/main
  - Local evidence: CASE/2026-05-17-heartbeat-1811Z/artifacts/github-1811-repo-EmPajak21__multiagentllms.json, CASE/2026-05-17-heartbeat-1811Z/artifacts/github-1811-tree-EmPajak21__multiagentllms.json, CASE/2026-05-17-heartbeat-1811Z/artifacts/github-1811-license-EmPajak21__multiagentllms.json
  - License/public access: Public GitHub repository; license metadata NOASSERTION. Not downloaded because explicit archival/redistribution license was not detected.
  - Recommended automation use: Use existing archived copy if duplicate; otherwise request maintainer license clarification before download.
  - Dedupe basis: source_page `https://github.com/EmPajak21/multiagentllms`, download_url `https://codeload.github.com/EmPajak21/multiagentllms/zip/refs/heads/main`, filenames ['GOSP A_EP.hsc']
  - Residual risks: License/redistribution permission requires human review.; No local Aspen HYSYS runtime validation performed.

## Skipped Non-Model Candidates
- Inspected GitHub repositories without true HYSYS primary model: 19. See `artifacts/github-1811-skipped-no-model.json`.

## Search Evidence Artifacts
- `artifacts/dedupe-summary.json`
- `artifacts/github-1811-search-summary.json`
- `artifacts/github-1811-inspection-summary.json`
- `artifacts/github-1811-model-bearing-repositories.json`
- `artifacts/github-1811-dedupe-assessment.json`
- `artifacts/github-1811-skipped-no-model.json`
- `artifacts/external-1811-search-summary.json`
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
