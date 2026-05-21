# Aspen HYSYS Case Discovery Heartbeat - 2026-05-21 1315Z

## Run Time

- Trigger time UTC: 2026-05-21T13:15:59.803Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-21-heartbeat-1315Z
- Artifacts directory: not created; no files were downloaded this run.
- Model run status: not_run. No Aspen HYSYS model was opened, solved, executed, or validated.

## Repository Gate

- Current branch: main.
- `git pull --ff-only origin main`: completed successfully; repository was already up to date.
- Working tree before CASE write: clean and synced with origin/main.
- Git LFS rule observed: no ZIP or large binary files were added this run.

## Search Mines

- GitHub repository search for Aspen HYSYS public repositories with permissive-license filters.
- GitHub code search for README mentions, simulation-file phrases, `.hsc`, `.hscz`, and HYSYS XML terms.
- GitHub API tree inspection for model-bearing repositories surfaced by README and repository search.
- Web search checks for GitHub, Zenodo, and Figshare HYSYS case leads.
- Existing `CASE/**/sources.json`, `CASE/**/index.md`, and source index records searched for source-page/title/file/SHA dedupe.

## Keywords Used

- `Aspen HYSYS license:mit`
- `HYSYS case license:mit`
- `Aspen HYSYS filename:README.md`
- `"Aspen HYSYS" "simulation files"`
- `HYSYS "*.hsc"`
- `Aspen HYSYS methanol`
- `Aspen HYSYS gas sweetening`
- `site:github.com Aspen HYSYS "*.hsc" "LICENSE"`
- `site:github.com "Aspen HYSYS" "simulation" ".hsc"`
- `site:zenodo.org "Aspen HYSYS" "hsc"`
- `site:figshare.com "Aspen HYSYS" "hsc"`

## Downloaded Case List

No new HYSYS cases were downloaded. The model-bearing repositories inspected in detail were either already recorded in prior CASE heartbeat records or lacked an explicit license suitable for research archival and redistribution. Automation-only and README-only repositories were excluded because they do not satisfy the HYSYS model-file requirement.

## Candidate And Duplicate Review

| Title | Source page | Download URL | Local path | Selection reason | Quality | License / public access note | Recommended automation use | Dedupe basis | Residual risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub search sweep for licensed HYSYS repositories and code | https://github.com/search?q=Aspen+HYSYS+license%3Amit&type=repositories | Not used | Not downloaded | MIT-filtered repository search returned mostly automation-only repositories or already-known candidates; no new licensed, nonduplicate `.hsc/.hscz/HYSYS XML` payload was identified. | D | Public GitHub search only; no qualifying payload downloaded. | Use as negative evidence for permissive-license coverage; continue tree inspection and DOI-backed repository checks. | No new source_page/file/SHA256 suitable for archive. | GitHub search can miss binary files and repositories where HYSYS is mentioned only in metadata or notebooks. |
| Gallo05952/Articolo_energies | https://github.com/Gallo05952/Articolo_energies | Not used | Not downloaded | Public repository contains HYSYS `.hsc` models, workbook/CSV data, notebooks, and scripts for biogas cryogenic distillation analysis, but no explicit license is declared and it has already been reviewed as a no-license candidate. | D | Public GitHub repository, but no explicit license; archival/download rights are unclear. | Manual permission queue only. Potentially useful for biogas cryogenic distillation metadata and surrogate-model workflow design after permission is clarified. | Existing records include CASE/2026-05-16-heartbeat-2108Z, CASE/2026-05-17-heartbeat-0309Z, CASE/2026-05-17-heartbeat-0609Z, and CASE/2026-05-17-heartbeat-1611Z. Key blobs: `50kmol_h_ALIM_N2_H2S_O2_Hashemi.hsc` SHA `75e2c222dceb2a80448b5f9f46842b254c30a9c5`; `Articolo_energies.hsc` SHA `085bbf51c76b2e6b9b280012a6513fb397704ebd`. | Technically relevant model payload exists, but redistribution and reuse rights remain unresolved. No files or scripts were run. |
| Pouria-MK/_Jan.2024_Simulation-and-Economic-Evaluation-of-Syngas-Generation-Plant-using-DMR-and-SMR-Reactors | https://github.com/Pouria-MK/_Jan.2024_Simulation-and-Economic-Evaluation-of-Syngas-Generation-Plant-using-DMR-and-SMR-Reactors | Not used | Not downloaded | Public repository contains syngas SMR/DMR `.hsc`, HYSYS XML, report slides, and sensitivity workbook, but no explicit license is declared and it is already represented in prior CASE records. | D | Public GitHub repository, but no explicit license; archival/download rights are unclear. | Manual permission queue only. Useful as a future hydrogen/syngas process automation benchmark only after license or author permission is clarified. | Existing records include CASE/2026-05-17-heartbeat-0309Z and CASE/2026-05-17-heartbeat-0609Z. Key blobs include `SynGas-SMR-DMR(integration).hsc` SHA `a5639ca1d5f1a4b7a15c5bf7a68531a1bc1476b3`; `SynGas-SMR-DMR(integration).xml` SHA `76cbc4efb6c5c778c194f66f110f3c4ce07222d9`. | Strong engineering relevance, but no-license status blocks archive download. HYSYS version remains unknown because no model was opened. |
| bpalotai/Flowsheet-toolbox | https://github.com/bpalotai/Flowsheet-toolbox | Not used | Not downloaded | Public toolbox repository contains a sample HYSYS `.hsc` model and spreadsheet/CSV/script materials for heat-exchanger model workflows, but no explicit license is declared and it is already recorded. | D | Public GitHub repository, but no explicit license; archival/download rights are unclear. | Manual permission queue only. If licensed later, it could support HYSYS-to-data pipeline and external-model automation tests. | Existing records include CASE/2026-05-11-heartbeat-1411Z and CASE/2026-05-17-heartbeat-0309Z. Key blob: `Cases/HX-model-V1/HysysModel/SampleModel_V2.hsc` SHA `53854097296b54b0a378e6d0f7421c880cbf9c08`. | Repository may be useful for automation research, but redistribution rights are unresolved and included scripts were not run. |

## Source Pages Checked

- https://github.com/search?q=Aspen+HYSYS+license%3Amit&type=repositories
- https://github.com/search?q=HYSYS+case+license%3Amit&type=repositories
- https://github.com/search?q=Aspen+HYSYS+filename%3AREADME.md&type=code
- https://github.com/search?q=%22Aspen+HYSYS%22+%22simulation+files%22&type=code
- https://github.com/search?q=HYSYS+%22*.hsc%22&type=code
- https://github.com/Gallo05952/Articolo_energies
- https://github.com/Pouria-MK/_Jan.2024_Simulation-and-Economic-Evaluation-of-Syngas-Generation-Plant-using-DMR-and-SMR-Reactors
- https://github.com/Pouria-MK/_Nov.2023_Conceptual-Design-and-Economic-Feasibility-of-Valuable-Substances-Recovery-Unit
- https://github.com/bpalotai/Flowsheet-toolbox
- https://zenodo.org/search?q=%22Aspen%20HYSYS%22%20hsc
- https://figshare.com/search?q=%22Aspen%20HYSYS%22%20hsc

## License And Public Access Notes

- No login, paid access, institutional credential, customer-support portal, or private source was used.
- Public repositories without explicit licenses were not downloaded.
- Candidate repositories with model files were treated as D-quality candidate records when license clarity was missing or the source was already recorded.
- Automation-only, README-only, and PDF-only repositories were excluded from the HYSYS model corpus.
- No executable, macro, script, HYSYS model, notebook, workbook, PDF, or unknown binary was run.

## Recommended Automation Uses

- Keep no-license but model-bearing GitHub repositories in a manual-permission queue.
- Continue prioritizing DOI-backed sources or repositories with explicit OSI/CC licenses and validation data.
- Use the negative search evidence to focus future sweeps on repository tree inspection, release assets, and article supplementary files rather than code search alone.
- Preserve existing archive records as the dedupe authority for repeated no-license candidates.

## Residual Risks

- GitHub code search can miss binary HYSYS files.
- No-license repositories can disappear, change structure, or change terms without notice.
- HYSYS versions remain unknown because no model files were opened or inspected with Aspen HYSYS.
- Candidate scripts and notebooks were not executed, so their safety and reproducibility were not evaluated.

## Next Suggestions

- Revisit the no-license watchlist only when a license file appears or author permission is obtained.
- Prefer Zenodo/Figshare/Mendeley records with DOI and license metadata for the next fetch attempt.
- Add targeted searches for `.hscz` release assets and article supplementary ZIP manifests while continuing to avoid unclear redistribution rights.
