# Aspen HYSYS Case Discovery Heartbeat - 2026-05-20 0313Z

## Run Time

- Trigger time UTC: 2026-05-20T03:13:45.811Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-20-heartbeat-0313Z
- Artifacts directory: not created; no files were downloaded this run.
- Model run status: not_run. No Aspen HYSYS model was opened, solved, executed, or validated.

## Repository Gate

- Current branch: main
- `git status --short --branch`: clean at start.
- `git pull --ff-only origin main`: already up to date.
- Git LFS rule observed: no ZIP or large binary files were added this run.

## Search Mines

- GitHub repository search through `gh search repos`.
- GitHub repository tree and metadata inspection through `gh repo view` and GitHub API.
- Web search focused on GitHub, Zenodo, Mendeley Data, Figshare, UPCommons, and HYSYS `.hsc` terms.
- UPCommons publication pages were inspected as higher-education public repository leads.

## Keywords Used

- `extension:hsc HYSYS`
- `extension:hsc Aspen`
- `extension:hsc "Aspen HYSYS"`
- `Aspen HYSYS .hsc`
- `HYSYS .hscz`
- `Aspen HYSYS case`
- `Aspen HYSYS Python`
- `HYSYS simulation`
- `HYSYS Excel`
- `site:upcommons.upc.edu hsc Aspen HYSYS`
- `Zenodo Aspen HYSYS hsc`
- `Mendeley Data Aspen HYSYS hsc`
- `Figshare Aspen HYSYS hsc`

## Downloaded Case List

No new case files were downloaded. GitHub-first searching mostly resurfaced known duplicate or no-license HYSYS repositories already recorded in prior CASE runs. UPCommons exposed two interesting `.hsc` attachments with accompanying reports, but the pages indicate all-rights-reserved/no reusable license status, so they were recorded as D-grade candidates only.

## Candidate And Duplicate Review

| Title | Source page | Download URL | Local path | Selection reason | Quality | License / public access note | Recommended automation use | Dedupe basis | Residual risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub duplicate sweep: known HYSYS `.hsc` and automation repositories | https://github.com/search?q=Aspen+HYSYS+case&type=repositories | Not used | Not downloaded | GitHub search returned repositories already recorded: `GaboTalero/HYSYS-Python-Case-Builder`, `marcellobozzini/Python-Driving-License`, `Corey-McInrue/Node-C-ASPEN-HYSYS`, `royhanikbarr/Aspen-Hysys-Simulation`, `Jeslin-Jacob/rbf-interpolation-atmospheric-distillation`, `ArturTask/HysysExcel`, `cityfamer/HyPy`, and `robfox92/matlab-fitness-hysys`. | D | Mixed: MIT for some automation/data-only repos, no license for several `.hsc` repos. | Duplicate avoidance and search-filter tuning. | Existing CASE source_page matches across 2026-05-11 to 2026-05-17 runs. | No new licensed HYSYS model payload found. |
| UPCommons: Simulation and design study of an ethyl benzene chemical process | https://upcommons.upc.edu/entities/publication/35e0b9f9-59ec-472f-8b4d-4d9dd5ae143d | Not used | Not downloaded | Public university repository record exposes a report PDF and `Muhammad Arieff Bin Idros - Simulation of EthylBenzene Process 2019.hsc`. | D | Public page, but rights panel indicates all rights reserved / no reusable license; not archived. | Manual permission-review candidate for ethylbenzene process design only. | New source_page; no prior CASE match found for UPCommons, Bin Idros, or EthylBenzene HYSYS file. | Licensing does not permit automatic research archive or redistribution. |
| UPCommons: Estudi de la viabilitat economica, energetica i mediambiental d'una planta d'absorcio de CO2 | https://upcommons.upc.edu/entities/publication/a5a9b824-75d8-4611-8f08-f8a82f294e06 | Not used | Not downloaded | Public university repository record exposes a TFM PDF and `Simulacio proces d'absorcio de CO2.hsc`. | D | Public page, but rights panel indicates all rights reserved / no reusable license; not archived. | Manual permission-review candidate for CO2 absorption process economics and environmental assessment only. | New source_page; no prior CASE match found for UPCommons, Castano Cid, or CO2 absorption HYSYS file. | Licensing does not permit automatic research archive or redistribution. |

## Source Pages Checked

- https://github.com/search?q=Aspen+HYSYS+case&type=repositories
- https://github.com/GaboTalero/HYSYS-Python-Case-Builder
- https://github.com/marcellobozzini/Python-Driving-License
- https://github.com/Corey-McInrue/Node-C-ASPEN-HYSYS
- https://github.com/royhanikbarr/Aspen-Hysys-Simulation
- https://github.com/Jeslin-Jacob/rbf-interpolation-atmospheric-distillation
- https://github.com/ArturTask/HysysExcel
- https://github.com/cityfamer/HyPy
- https://github.com/robfox92/matlab-fitness-hysys
- https://upcommons.upc.edu/entities/publication/35e0b9f9-59ec-472f-8b4d-4d9dd5ae143d
- https://upcommons.upc.edu/entities/publication/a5a9b824-75d8-4611-8f08-f8a82f294e06

## License And Public Access Notes

- No login, paid access, institutional credentials, customer-support portal, or non-public source was used.
- GitHub repositories with no explicit license were not downloaded, even when `.hsc` filenames were visible.
- MIT-licensed GitHub hits without HYSYS model files were not downloaded as benchmark cases.
- UPCommons records were publicly visible and include `.hsc` attachment names, but the rights/license presentation indicates all rights reserved or no reusable license, so no PDF or HYSYS file was saved.

## Recommended Automation Uses

- Keep using already archived licensed GitHub cases for automation smoke tests; do not re-download them.
- Add UPCommons ethylbenzene and CO2 absorption records to a manual permission-review list if these process themes are important.
- Treat UPCommons search as a useful non-GitHub mine, but only archive when the page has an explicit reusable license or written permission.

## Residual Risks

- GitHub code search via API was not available in this environment for direct `extension:hsc` REST queries; repository search and tree inspection were used instead.
- UPCommons pages may permit personal download for reading, but the current archival bot rules require redistribution/research-archive clarity before saving files.
- Some high-value HYSYS cases may be hidden behind release assets or supplementary ZIPs without clear metadata.

## Next Suggestions

- Add targeted queries for `site:upcommons.upc.edu ".hsc" "Hysys"` and manually screen rights before any download.
- Continue GitHub search for `license:mit HYSYS .hsc` style repository leads, but expect many duplicates.
- Keep a separate permission backlog for no-license GitHub `.hsc` repositories and all-rights-reserved university repository records.
