# Aspen HYSYS Case Discovery Heartbeat - 2026-05-17 1611Z

- Run time UTC: 2026-05-17T16:11:15Z
- Local HYSYS model run status: not_run; no model was opened, executed, solved, or macro/script-run.
- Repository gate: main branch, clean worktree, git pull --ff-only origin main completed before discovery.
- Existing CASE dedupe baseline: 212 source entries, 165 source pages, 120 download URLs, 876 filenames, 756 SHA256 values.
- Classification correction: generic XML search hits were removed unless the path explicitly indicated HYSYS XML; only `.hsc`, `.hscz`, `.compound`, or path-explicit HYSYS XML is treated as model-bearing.

## Searched Mines
- GitHub code search via `gh search code` for HYSYS Python/MATLAB/.hsc references
- GitHub repository search via GitHub REST API
- GitHub repository tree and license inspection
- Zenodo records API quick scan
- GitLab project API quick scan
- Bitbucket repository API quick scan

## Keywords
- `HYSYS --extension py`
- `Aspen HYSYS`
- `.hsc HYSYS`
- `HYSYS --extension m`
- `win32com.client HYSYS --extension py`
- `HYSYS simulation files`
- `Aspen HYSYS hsc`
- `HYSYS case file`
- `Aspen HYSYS Python COM`
- `HYSYS optimization case`
- `HYSYS simulation Aspen license MIT`
- `Aspen HYSYS .hsc`
- `Aspen HYSYS .hscz`
- `HYSYS XML Cases .xml`

## Downloaded Cases
- CAChemE/stochastic-optimization (B)
  - Source page: https://github.com/CAChemE/stochastic-optimization
  - Download URL: https://codeload.github.com/CAChemE/stochastic-optimization/zip/refs/heads/master
  - Local paths:
    - `CASE/2026-05-17-heartbeat-1611Z/artifacts/GitHub_2026_HYSYS_CAChemE__stochastic-optimization/ConventionalDistillationColumn/PSO_Algorithm.py` (py, sha256 `836bbbeaf29aee33983bdfc7a3a1005e5a7dcfaf5650ff1f40380a99d9db4e9a`)
    - `CASE/2026-05-17-heartbeat-1611Z/artifacts/GitHub_2026_HYSYS_CAChemE__stochastic-optimization/ConventionalDistillationColumn/Test_Column.hsc` (hsc, sha256 `2f818d792fee86d3b499dfce667b72b37b9de4a5544600c1c3489dd89a61b43d`)
    - `CASE/2026-05-17-heartbeat-1611Z/artifacts/GitHub_2026_HYSYS_CAChemE__stochastic-optimization/ConventionalDistillationColumn/Test_Column_ObjFnc.py` (py, sha256 `25cb5d2e7e170ce52c8f61c417e025fb5a831242eaf51f70a70b0b4d3a597588`)
    - `CASE/2026-05-17-heartbeat-1611Z/artifacts/GitHub_2026_HYSYS_CAChemE__stochastic-optimization/ConventionalDistillationColumn/column_algorithm.py` (py, sha256 `10b81e649fb261ce987f4667aa089b68c1f2e182519ddbca6bf07ed139de6c18`)
    - `CASE/2026-05-17-heartbeat-1611Z/artifacts/GitHub_2026_HYSYS_CAChemE__stochastic-optimization/ConventionalDistillationColumn/hyInterface.py` (py, sha256 `175535820b3c1639829c3ac0d2b5a55dde81597c2e13b035dd4e009de323fc0e`)
    - `CASE/2026-05-17-heartbeat-1611Z/artifacts/GitHub_2026_HYSYS_CAChemE__stochastic-optimization/ConventionalDistillationColumn/main_Column.py` (py, sha256 `9238232295d079258b10392ecfb478ba57bb67763b4655bfc6c0142e44187996`)
    - `CASE/2026-05-17-heartbeat-1611Z/artifacts/GitHub_2026_HYSYS_CAChemE__stochastic-optimization/ConventionalDistillationColumn/print_pso.py` (py, sha256 `bcba241730b5e6dbcd6877c7175e5e3d7f3853e280a67374cafcf3455d101988`)
    - `CASE/2026-05-17-heartbeat-1611Z/artifacts/GitHub_2026_HYSYS_CAChemE__stochastic-optimization/ConventionalDistillationColumn/pso_column.py` (py, sha256 `bda00a2b02fd0aa66f45a7d9f0266a8e09c0100978b8b329b18ef10771ea463b`)
    - `CASE/2026-05-17-heartbeat-1611Z/artifacts/GitHub_2026_HYSYS_CAChemE__stochastic-optimization/LICENSE` (license, sha256 `d655bfaaa56b795bd2bc7ae9efb10220305e7856ec6b699655f25199de53b4d1`)
    - `CASE/2026-05-17-heartbeat-1611Z/artifacts/GitHub_2026_HYSYS_CAChemE__stochastic-optimization/README.md` (md, sha256 `ab4f289bc6926eb40d1a31acac2e6917f6b16da6cec63af56576c55d467806bf`)
  - Selection reason: nonduplicate `.hsc` HYSYS case plus public BSD-3-Clause repository license and Python optimization/COM companion scripts.
  - License/public access: Public GitHub repository; repository license metadata reports BSD-3-Clause. Scoped files archived; HYSYS model not opened or run.
  - Recommended automation use: Distillation-column HYSYS/PSO automation benchmark candidate for COM interface smoke tests, optimization-loop regression, and column variable access checks after human review.
  - Dedupe basis: source_page `https://github.com/CAChemE/stochastic-optimization`, download_url `https://codeload.github.com/CAChemE/stochastic-optimization/zip/refs/heads/master`, filenames ['PSO_Algorithm.py', 'Test_Column.hsc', 'Test_Column_ObjFnc.py', 'column_algorithm.py', 'hyInterface.py', 'main_Column.py', 'print_pso.py', 'pso_column.py', 'LICENSE', 'README.md']
  - Residual risks: Repository-level BSD-3-Clause license should be reviewed before redistributing binary HYSYS model files beyond research archival.; No local Aspen HYSYS runtime validation performed.

## Candidate And Duplicate Records
- Duplicate: Gallo05952/Articolo_energies (D)
  - Source page: https://github.com/Gallo05952/Articolo_energies
  - Download URL: https://codeload.github.com/Gallo05952/Articolo_energies/zip/refs/heads/main
  - Local evidence: CASE/2026-05-17-heartbeat-1611Z/artifacts/github-1611-repo-Gallo05952__Articolo_energies.json, CASE/2026-05-17-heartbeat-1611Z/artifacts/github-1611-tree-Gallo05952__Articolo_energies.json, CASE/2026-05-17-heartbeat-1611Z/artifacts/github-1611-license-Gallo05952__Articolo_energies.json
  - Selection reason: model-bearing repository found; not archived as a new download due to duplicate/license gate.
  - License/public access: Public GitHub repository; license metadata NOASSERTION. Not downloaded because it matches existing CASE dedupe keys.
  - Recommended automation use: Use existing archived copy if needed; do not redownload duplicate no-license case.
  - Dedupe basis: source_page `https://github.com/Gallo05952/Articolo_energies`, download_url `https://codeload.github.com/Gallo05952/Articolo_energies/zip/refs/heads/main`, filenames ['50kmol_h_ALIM_N2_H2S_O2_Hashemi.hsc', 'Articolo_energies.hsc']
  - Residual risks: Duplicate source/title/filename already exists in CASE.; No local Aspen HYSYS runtime validation performed.

## Skipped Non-Model Candidates
- GitHub code/repository search produced 18 inspected repositories without a true HYSYS primary model file after XML false-positive correction. These are recorded in `artifacts/github-1611-skipped-no-model.json`.

## Search Evidence Artifacts
- `artifacts/dedupe-summary.json`
- `artifacts/github-1611-search-summary.json`
- `artifacts/github-1611-inspection-summary.json`
- `artifacts/github-1611-model-bearing-repositories.json`
- `artifacts/github-1611-dedupe-assessment.json`
- `artifacts/github-1611-skipped-no-model.json`
- `artifacts/external-1611-search-summary.json`
- `artifacts/download-summary.json`
- `artifacts/classification-corrections.json`
- `artifacts/pruned-large-tree-files.json`
- `artifacts/security-inventory.json`

## Quality Ratings
- A: model + paper/report + validation data + DOI/license/clear provenance.
- B: model + README/report/public repository with clear license but limited validation.
- C: model with basic credible provenance but limited support material.
- D: candidate/duplicate record only; not downloaded or not recommended for new benchmark inclusion this run.

## Residual Risks
- No Aspen HYSYS runtime validation was performed.
- The downloaded `.hsc` binary was not opened or solved.
- Public repository license metadata remains repository-level and should be reviewed before redistribution of proprietary-format model binaries.

## Follow-Up Suggestions
- Keep GitHub code search in the heartbeat loop; this run produced one true nonduplicate `.hsc` case that repository search alone could miss.
- Add a denylist for no-model automation repositories and generic XML repositories to reduce future false positives.
- Continue requesting maintainers of no-license model-bearing repositories to add clear licenses.

## Summary
- New downloaded cases: 1
- New nonduplicate candidate-only records: 0
- Duplicate model-bearing records retained: 1
- Inspected GitHub repositories: 20
- True model-bearing GitHub repositories: 2
- Skipped no-model repositories after correction: 18
