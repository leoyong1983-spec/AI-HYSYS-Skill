# Aspen HYSYS Case Discovery Heartbeat - 2026-05-22 22:19Z

## Run Context

- Automation ID: `ai-hysys-case-2`
- Trigger time: `2026-05-22T22:19:29.562Z`
- Repository: `D:\CODEX\AI-HYSYS-Skill`
- Branch gate: `main`
- Git gate: `git pull --ff-only origin main` completed with `Already up to date.`
- Model run status: `not_run`

## Search Mines

- GitHub repository search for recent Aspen HYSYS and HYSYS/HSC candidates.
- GitHub tree inspection for model-bearing or automation repositories.
- Zenodo API search for Aspen HYSYS/HSC/HSCZ and simulation-file leads.
- CASE dedupe scan using existing `sources.json` and `index.md` records.

## Keywords

- `Aspen HYSYS`
- `HYSYS hsc`
- `extension:hsc`
- `extension:hscz`
- `HYSYS XML Cases`
- `Aspen HYSYS simulation files`
- `Python-COM HYSYS`
- `Excel validation HYSYS`

## Downloaded Case List

No new case was downloaded in this run.

All qualifying public and licensed model-bearing GitHub hits were duplicates of earlier archived assets. New or refreshed candidates either had no explicit license, had no HYSYS main model file, or exposed only paper/data artifacts.

## Candidate Review

| Candidate | Source page | Download URL | Local path | Selection decision | Quality |
|---|---|---|---|---|---|
| shahria-sunny/Natural-Gas-Sweetening | https://github.com/shahria-sunny/Natural-Gas-Sweetening | https://codeload.github.com/shahria-sunny/Natural-Gas-Sweetening/zip/refs/heads/main | Not downloaded | MIT repository with `Gas Sweetening.hsc`, report, README, and V14 metadata, but already archived. | D |
| shahria-sunny/CDU-Simulation-Optimization | https://github.com/shahria-sunny/CDU-Simulation-Optimization | https://codeload.github.com/shahria-sunny/CDU-Simulation-Optimization/zip/refs/heads/main | Not downloaded | MIT repository with `project.hsc`, report, README, and V14 metadata, but already archived. | D |
| Mahdi-Arashian/sour-gas-sweetening-hysys | https://github.com/Mahdi-Arashian/sour-gas-sweetening-hysys | https://raw.githubusercontent.com/Mahdi-Arashian/sour-gas-sweetening-hysys/main/GTU%20Simulation.hsc | Not downloaded | Contains `GTU Simulation.hsc` and a report PDF, but no license; already in manual permission queue. | D |
| Anikesh31/simulator_codingplatform_integration | https://github.com/Anikesh31/simulator_codingplatform_integration | https://raw.githubusercontent.com/Anikesh31/simulator_codingplatform_integration/main/Test_file_hysys_python.hsc | Not downloaded | Contains `Test_file_hysys_python.hsc`, but no license; already recorded as candidate. | D |
| Corey-McInrue/Node-C-ASPEN-HYSYS | https://github.com/Corey-McInrue/Node-C-ASPEN-HYSYS | https://raw.githubusercontent.com/Corey-McInrue/Node-C-ASPEN-HYSYS/main/NODECFINAL.hsc | Not downloaded | Contains `NODECFINAL.hsc`, but no license; already recorded as candidate. | D |
| Avest-AI/MemCal | https://github.com/Avest-AI/MemCal | https://codeload.github.com/Avest-AI/MemCal/zip/refs/heads/main | Not downloaded | HYSYS membrane-extension context but inspected tree exposed README only in this pass; no HYSYS main model and no license. | D |
| Zenodo Hydrogen Co-Firing in Gas Turbines | https://zenodo.org/records/19469917 | https://zenodo.org/api/records/19469917/files | Not downloaded | DOI-backed CC BY 4.0 metadata, but file list exposes only ambiguous `Upload data.rar`; no confirmed `.hsc/.hscz` case. Already recorded as candidate. | D |

## Source Notes

- GitHub search returned no new licensed, non-duplicate `.hsc`, `.hscz`, HYSYS XML, or `.compound` case suitable for archival.
- `shahria-sunny/Natural-Gas-Sweetening` and `shahria-sunny/CDU-Simulation-Optimization` remain valid MIT model-bearing sources, but their payloads and hashes are already present in earlier CASE records.
- No-license model repositories were kept out of `artifacts/` to avoid unclear redistribution.
- Zenodo latest results were mostly false-positive `HSC` astronomy/science records, PDF-only paper deposits, or known ambiguous packages.

## License / Public Access Notes

- No files were downloaded.
- Public GitHub metadata was inspected through unauthenticated/public APIs and `gh`.
- Public Zenodo metadata was inspected through the Zenodo API.
- No login, paywall, institutional access, customer support resource, or commercial training material was accessed.

## Recommended Automation Use

- Use existing archived MIT copies of `Gas Sweetening.hsc` and `project.hsc` for gas sweetening and CDU automation tests.
- Keep no-license `.hsc` repositories in a manual permission queue only.
- Treat Zenodo `19469917` as a literature/candidate lead until the archive contents are safely identified without executing unknown files.

## Dedupe Basis

- Existing `CASE/**/sources.json` and `index.md` records match by `source_page`, `download_url`, filenames, and earlier candidate titles.
- `Gas Sweetening.hsc` SHA256 is recorded in earlier CASE metadata as `fcda75090796e9ba8a69bfb29a769deea36761d11d26c93d51d98318d19d4610`.
- `project.hsc` SHA256 is recorded in earlier CASE metadata as `795c3587c611405f4786115514030036987615e47c33fe74aba1fcb1610fbdd2`.
- No-license candidates overlap prior source pages and filenames: `GTU Simulation.hsc`, `Test_file_hysys_python.hsc`, and `NODECFINAL.hsc`.

## Residual Risks

- GitHub and Zenodo search ranking is noisy; exact tree and file-list inspection remains required on future runs.
- No-license repositories could become usable if maintainers add licenses later.
- Ambiguous archive formats such as `.rar` may hide useful models, but they were not downloaded because contents and safety could not be verified from metadata alone.

## Follow-Up Suggestions

1. Recheck no-license model repositories only when a license appears in repository metadata or author permission is documented.
2. Keep Zenodo `19469917` in the candidate list, but do not archive `Upload data.rar` until its contents are safely described.
3. Prefer DOI-backed deposits with explicit `.hsc`, `.hscz`, or HYSYS XML file listings for future downloads.
