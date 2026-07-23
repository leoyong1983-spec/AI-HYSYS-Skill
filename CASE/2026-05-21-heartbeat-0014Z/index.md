# Aspen HYSYS Case Discovery Heartbeat - 2026-05-21 0014Z

## Run Time

- Trigger time UTC: 2026-05-21T00:14:19.683Z
- Workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-21-heartbeat-0014Z
- Artifacts directory: not created; no files were downloaded this run.
- Model run status: not_run. No Aspen HYSYS model was opened, solved, executed, or validated.

## Repository Gate

- Current branch: main.
- `git pull --ff-only origin main`: completed successfully; repository was already up to date.
- Working tree before CASE write: clean, with one prior CASE commit ahead of origin/main from the 2026-05-20 2314Z heartbeat push failure.
- Git LFS rule observed: no ZIP or large binary files were added this run.

## Search Mines

- GitHub code search with `gh search code` for `.hsc` and `.hscz` files.
- GitHub repository search with `gh search repos` for licensed and recently updated Aspen HYSYS repositories.
- GitHub API tree inspection for selected duplicate candidates.
- Zenodo API and web search for open HYSYS dataset records.
- Existing `CASE/**/sources.json`, `CASE/**/index.md`, and `CASE/source-index.md` searched for source-page/title/file dedupe.

## Keywords Used

- `HYSYS filename:*.hsc`
- `Aspen filename:*.hsc`
- `HYSYS filename:*.hscz`
- `Aspen HYSYS license:mit`
- `HYSYS case file pushed:>=2026-05-01`
- `site:zenodo.org Aspen HYSYS .hsc`
- `edgarsmdn/Aspen_HYSYS_Python`
- `shahria-sunny/Natural-Gas-Sweetening`
- `zenodo 14882867`

## Downloaded Case List

No new HYSYS cases were downloaded. Direct GitHub code search returned no qualifying `.hsc` or `.hscz` hits. Repository search found several public HYSYS-related repositories, but the only model-bearing candidates reviewed in detail were already archived in prior CASE runs. The Zenodo high-quality dataset hit was also already archived, including its HYSYS `.hsc` files, DOI metadata, license metadata, spreadsheets, and notebooks.

## Candidate And Duplicate Review

| Title | Source page | Download URL | Local path | Selection reason | Quality | License / public access note | Recommended automation use | Dedupe basis | Residual risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GitHub code search for HYSYS `.hsc/.hscz` files | https://github.com/search?q=HYSYS+filename%3A*.hsc&type=code | Not used | Not downloaded | Direct GitHub code search for `.hsc` and `.hscz` returned no qualifying model-file hits for download. | D | Public GitHub search only; no case payload found. | Keep as negative evidence for code-search coverage; continue repository tree inspection. | No source_page, SHA256, or filename suitable for CASE archival was found. | GitHub code search can miss binary or large files; repo-level searches remain necessary. |
| edgarsmdn/Aspen_HYSYS_Python | https://github.com/edgarsmdn/Aspen_HYSYS_Python | Not used | Not downloaded | MIT repository containing `Test_1.hsc`, README, license, and Python automation script. It is a valid HYSYS automation/model source but already archived. | D | Public MIT repository; no new download because it is duplicate. | Regression fixture for spreadsheet/Python COM automation only via existing archived copy. | `source_page` and `Test_1.hsc` already recorded in CASE/2026-05-11-heartbeat-1057Z and CASE/source-index.md; tree file SHA `3c1044e6d310ca784bee6f25dba59aaf41a9f04b`. | GitHub `updatedAt` changed recently, but repository `pushedAt` and inspected tree evidence indicate no new case payload. |
| shahria-sunny/Natural-Gas-Sweetening | https://github.com/shahria-sunny/Natural-Gas-Sweetening | Not used | Not downloaded | MIT repository containing `Gas Sweetening.hsc`, report PDF, README, and license. It is a valid natural-gas sweetening case but already archived. | D | Public MIT repository; no new download because it is duplicate. | Existing archived copy remains suitable for gas sweetening and acid-gas removal automation testing. | `source_page`, title, and `Gas Sweetening.hsc` already recorded in CASE/2026-05-11-heartbeat-0741Z. | HYSYS V14 is inferred from repository metadata/README; model was not opened in this run. |
| Zenodo 14882867 - Onboard carbon capture for circular marine fuels | https://zenodo.org/records/14882867 | Not used | Not downloaded | High-quality open dataset with DOI, CC-BY-4.0 license, HYSYS `.hsc` files, spreadsheets, and notebooks. It is already archived in the CASE corpus. | D | Open Zenodo record, DOI 10.5281/zenodo.14882867, CC-BY-4.0; no new download because it is duplicate. | Existing archived copy remains a high-value CCUS/methanol/LNG benchmark and validation-data source. | `source_page`, DOI, title, and HYSYS filenames already recorded in CASE/2026-05-11-heartbeat-0026Z and later duplicate sweeps. | HYSYS version remains unknown because no model was opened; large `.apw` file should remain managed as an archived artifact only. |

## Source Pages Checked

- https://github.com/search?q=HYSYS+filename%3A*.hsc&type=code
- https://github.com/search?q=Aspen+filename%3A*.hsc&type=code
- https://github.com/search?q=HYSYS+filename%3A*.hscz&type=code
- https://github.com/search?q=Aspen+HYSYS+license%3Amit&type=repositories
- https://github.com/search?q=HYSYS+case+file+pushed%3A%3E%3D2026-05-01&type=repositories
- https://github.com/edgarsmdn/Aspen_HYSYS_Python
- https://github.com/shahria-sunny/Natural-Gas-Sweetening
- https://zenodo.org/records/14882867

## License And Public Access Notes

- No login, paid access, institutional credential, customer-support portal, or private source was used.
- Public GitHub code search produced no qualifying model payload.
- MIT repositories with model files were not redownloaded because they were exact or near-exact duplicates already archived.
- The Zenodo record is openly accessible under CC-BY-4.0 and already archived; no duplicate download was made.
- No executable, macro, script, HYSYS model, workbook, notebook, or unknown binary was run.

## Recommended Automation Uses

- Use the existing `edgarsmdn/Aspen_HYSYS_Python` archive for Python/HYSYS spreadsheet automation fixture work.
- Use the existing `shahria-sunny/Natural-Gas-Sweetening` archive for gas sweetening and acid-gas-removal benchmark exploration.
- Use the existing Zenodo 14882867 archive for CCUS, methanol, LNG, spreadsheet-validation, and dataset/DOI metadata workflows.
- Continue prioritizing model-bearing public repositories with explicit licenses and tree evidence before download.

## Residual Risks

- GitHub code search may not index all binary HYSYS files.
- Some repository metadata can update without a new model payload.
- Duplicate checks rely on source pages, filenames, and recorded archive metadata; unopened HYSYS files were not solver-validated.
- The Zenodo record includes a large Aspen Plus `.apw` file; this run did not re-download or inspect binary contents.

## Next Suggestions

- Add a crawler rule that treats `updatedAt`-only GitHub repository changes as low priority unless `pushedAt` or tree SHA changes.
- Continue periodic Zenodo API checks for new records containing `.hsc`, `.hscz`, or explicit Aspen HYSYS case files.
- Keep GitHub tree inspection focused on MIT/Apache/BSD/CC-licensed repositories that expose actual model payloads, not automation-only code.
