# HYSYS Case Discovery Heartbeat - 2026-05-22 00:18Z

## Run Context

- Automation ID: `ai-hysys-case-2`
- Trigger time (UTC): `2026-05-22T00:18:26.222Z`
- Local folder: `CASE/2026-05-22-heartbeat-0018Z/`
- Repository gate: `main` branch confirmed; `git pull --ff-only origin main` returned already up to date.
- Model run status: no HYSYS models were opened, executed, solved, or validated.

## Search Mines

- GitHub code and repository search
- Figshare and institutional Figshare API search
- Zenodo record search
- Harvard Dataverse public search
- Wiley companion/instructor resource page
- Local CASE archive dedupe scan

## Keywords And Query Patterns

- `Aspen HYSYS README`
- `HYSYS Aspen`
- `extension:hsc Aspen HYSYS`
- `Aspen HYSYS hsc`
- `Aspen HYSYS simulation files`
- `Aspen HYSYS Mendeley Data .hsc`
- `Aspen HYSYS figshare .hsc`
- `Aspen HYSYS supplementary .hsc`
- `site:gitlab.com Aspen HYSYS hsc`
- `site:bitbucket.org Aspen HYSYS hsc`

## Downloaded Cases

No cases were downloaded in this run. Current hits either did not contain a qualifying HYSYS main simulation file, required instructor/commercial access, or exposed only paper/PDF/DOCX metadata.

## Candidate Records

| Title | Source Page | Download URL | Local Path | Quality | Selection Reason | License/Public Access | Recommended Automation Use | Dedupe Basis | Residual Risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Natividade02/three-phase-separator-simulation | https://github.com/Natividade02/three-phase-separator-simulation | https://codeload.github.com/Natividade02/three-phase-separator-simulation/zip/refs/heads/main | Not downloaded | D | MIT repository for a dynamic three-phase separator simulation, but tree inspection found Python files only and no `.hsc`, `.hscz`, HYSYS XML case, or `.compound` file. | Public GitHub repository with MIT license, but no qualifying HYSYS model file. | Do not archive as a HYSYS case; possible background reference for separator dynamics only. | Repository URL plus absence of qualifying HYSYS model files. | README mentions simulation but not a HYSYS case; no Aspen runtime evidence. |
| RHorsley80/tank_heat_balance | https://github.com/RHorsley80/tank_heat_balance | https://codeload.github.com/RHorsley80/tank_heat_balance/zip/refs/heads/main | Not downloaded | D | MIT repository for tank heat-balance calculations; README mentions process-simulator inputs such as Aspen HYSYS, but no HYSYS main model file was found. | Public GitHub repository with MIT license, but no qualifying HYSYS model file. | Do not archive as a HYSYS case; possible method reference for tank heat balance calculations. | Repository URL plus absence of qualifying HYSYS model files. | May depend on external process simulator values; not a HYSYS model package. |
| Figshare/Curtin recent Aspen HYSYS metadata sweep | https://api.figshare.com/v2/articles/search | not_downloaded_no_qualifying_hysys_model_files | Not downloaded | D | Recent Figshare/Curtin hits include Aspen HYSYS article metadata, PDFs, DOCX files, or empty file lists, but no exposed `.hsc`, `.hscz`, HYSYS XML case, `.compound`, or model archive. | Mixed public metadata; some records are CC BY/CC BY-NC, several Curtin records are all-rights-reserved/written-permission-required. No model files were downloaded. | Use as literature-lead backlog only; not usable for automated model tests. | Article IDs inspected: `32085284`, `31601266`, `31477552`, `31668241`, `31667302`, `31654579`, `31868278`, `31769227`, `31762477`, `31707634`, `31701994`, `31525141`, `31239679`; several were already seen in prior CASE sweeps. | Metadata quality varies; API search matched HYSYS papers but not downloadable cases. |
| Wiley Haydary companion/instructor resources | https://bcs.wiley.com/he-bcs/Books?action=resource&bcsId=11642&chapterId=137707&itemId=1119089115&resourceId=46274 | not_downloaded_password_protected_instructor_assets | Not downloaded | D | Wiley companion resource appears tied to book/instructor assets for Aspen Plus/HYSYS examples and is password protected; not an open public model archive. | Requires instructor/password-protected access; commercial textbook companion context. Skipped under no-login/no-commercial-training rule. | Do not use for automated archive. Revisit only if a public, explicitly licensed download is provided by the publisher/author. | New local query key: `wiley-haydary-companion-password-protected`; no previous CASE hit found for this exact source. | Potentially relevant HYSYS examples may exist behind access controls, but they are not openly archivable. |

## Safety Notes

- No archive files were downloaded.
- No executable, macro, script, installer, or HYSYS model was run.
- No SHA256 values were generated because no new artifacts were saved.
- No existing CASE assets were removed, moved, or overwritten.

## Follow-Up Suggestions

- Suppress code-only GitHub repositories unless a tree-level check finds `.hsc`, `.hscz`, HYSYS XML, or `.compound`.
- Keep Figshare/Curtin records as literature leads only when file lists are PDF/DOCX/empty.
- Do not use password-protected Wiley/instructor assets without explicit public license and access rights.
- Continue searching for DOI-backed repositories where the model file itself is exposed under CC BY, MIT, or similarly clear terms.
