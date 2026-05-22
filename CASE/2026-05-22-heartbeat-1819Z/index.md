# Aspen HYSYS Case Discovery Heartbeat - 2026-05-22 18:19Z

## Run Context

- Automation ID: `ai-hysys-case-2`
- Trigger time: `2026-05-22T18:19:25.854Z`
- Repository: `D:\CODEX\AI-HYSYS-Skill`
- Branch gate: `main`
- Git gate: `git pull --ff-only origin main` completed with `Already up to date.`
- Model run status: `not_run`

## Search Mines

- GitHub repository search sorted by recent updates.
- GitHub tree inspection for repositories mentioning Aspen HYSYS, HYSYS automation, `.hsc`, `.hscz`, XML, and validation data.
- Zenodo API search for `"Aspen HYSYS" hsc`, `"Aspen HYSYS" hscz`, `"Aspen HYSYS" "simulation files"`, and `"Aspen HYSYS" "HYSYS files"`.
- Mendeley Data and Figshare metadata checks for public Aspen HYSYS datasets.
- Web search for Mendeley, Figshare, Dataverse, GitLab, and GitHub HYSYS case leads.

## Keywords

- `Aspen HYSYS`
- `HYSYS hsc`
- `extension:hsc`
- `extension:hscz`
- `HYSYS XML Cases`
- `Aspen HYSYS simulation files`
- `Aspen HYSYS HYSYS files`
- `Python-COM HYSYS`
- `MATLAB HYSYS`
- `Excel validation HYSYS`

## Downloaded Case List

No new case was downloaded in this run.

The highest-confidence public model-bearing hits were already archived in earlier `CASE` runs. Newly inspected or refreshed candidates either lacked a redistributable license, did not expose a HYSYS main simulation file, or matched existing dedupe keys.

## Candidate Review

| Candidate | Source page | Download URL | Local path | Selection decision | Quality |
|---|---|---|---|---|---|
| lihaijie1228/hysys_python_GA Decarbonization HYSYS candidate | https://github.com/lihaijie1228/hysys_python_GA | https://raw.githubusercontent.com/lihaijie1228/hysys_python_GA/main/simulaton_file/Decarbonization/Decarbonization.hsc | Not downloaded | Contains `simulaton_file/Decarbonization/Decarbonization.hsc`, but repository has no license and was already recorded as a candidate. | D |
| Galigeigei-Z/HDA-Surrogate-Optimization | https://github.com/Galigeigei-Z/HDA-Surrogate-Optimization | https://codeload.github.com/Galigeigei-Z/HDA-Surrogate-Optimization/zip/refs/heads/main | Not downloaded | MIT-licensed HYSYS automation and heat-network data, but inspected tree exposes notebooks, README, and XLSX only; no `.hsc`, `.hscz`, HYSYS XML case, or `.compound`. | D |
| GaboTalero/HYSYS-Python-Case-Builder | https://github.com/GaboTalero/HYSYS-Python-Case-Builder | https://codeload.github.com/GaboTalero/HYSYS-Python-Case-Builder/zip/refs/heads/main | Not downloaded | MIT-licensed COM case-building scripts, but no packaged HYSYS model file was found in the tree. | D |
| Mendeley 9384yj4xg3 geothermal HYSYS simulation data | https://data.mendeley.com/datasets/9384yj4xg3/5 | https://data.mendeley.com/public-api/datasets/9384yj4xg3 | Not downloaded | Public CC BY 4.0 dataset contains XLSX, DOCX, and PNG simulation outputs, but no HYSYS main case file. Previously logged as metadata/no-model candidate. | D |

## Source Notes

- `lihaijie1228/hysys_python_GA` contains a plausible Aspen HYSYS `.hsc` model, but absence of a repository license prevents preservation or redistribution in this archive.
- `Galigeigei-Z/HDA-Surrogate-Optimization` and `GaboTalero/HYSYS-Python-Case-Builder` are useful automation leads under MIT, but fail the lock standard because no main HYSYS simulation file is included.
- `Mendeley 9384yj4xg3` is a public DOI dataset with CC BY 4.0 terms, but it provides HYSYS-derived data and figures rather than a HYSYS case.
- Zenodo latest HSC hits remained dominated by non-HYSYS `HSC` astronomy/biology records, PDF-only records, or previously archived model packages such as Zenodo `18806107`.

## License / Public Access Notes

- No files were downloaded.
- No candidate with both a qualifying HYSYS main model and acceptable preservation rights was found.
- No login, paywall, institutional, customer support, or commercial training resource was accessed.

## Recommended Automation Use

- Use `lihaijie1228/hysys_python_GA` only as a manual permission-follow-up candidate, not as an automated test asset.
- Use MIT automation-only repositories as possible code-pattern leads for future HYSYS COM control research, not as case archives.
- Use Mendeley `9384yj4xg3` as a possible data-only validation reference for geothermal flash-cycle calculations, not as a HYSYS model source.

## Dedupe Basis

- Existing source pages and filenames were read from prior `CASE/**/sources.json` records.
- `https://github.com/lihaijie1228/hysys_python_GA` and `Decarbonization.hsc` overlap earlier candidate records.
- `https://data.mendeley.com/datasets/9384yj4xg3/5` overlaps earlier metadata/no-model records.
- Known already archived model-bearing packages such as Figshare `25202060`, Zenodo `18806107`, Zenodo `10966344`, Mendeley `8r8ztbkfjj`, Mendeley `r3875vhrjs`, and GitHub `edgarsmdn/Aspen_HYSYS_Python` were not re-downloaded.

## Residual Risks

- GitHub code search for bare `.hsc` returns many unrelated Haskell `.hsc` false positives, so repository tree inspection remains necessary.
- Some public repositories may add licenses or HYSYS model files later; this run reflects the inspected state at `2026-05-22T18:19Z`.
- Metadata-only records can mention Aspen HYSYS while exposing only derived tables or screenshots.

## Follow-Up Suggestions

1. Recheck no-license model-bearing GitHub candidates only if a license is added or author permission is documented.
2. Continue prioritizing DOI-backed data repositories because they have clearer public-access metadata, but require file-list verification before download.
3. Keep a separate watchlist for MIT automation repositories without `.hsc` files; they may be useful for script patterns but should not enter the model corpus.
