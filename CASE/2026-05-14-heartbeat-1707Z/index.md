# CASE Heartbeat 2026-05-14 1707Z

## 1. Run Time

- Trigger time (UTC): 2026-05-14T17:07:08.461Z
- Local repository: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-14-heartbeat-1707Z
- Model execution status: not_run for all entries. No Aspen HYSYS case was opened, executed, or solved.

## 2. Searched Mine Areas

- GitHub-first repository search: Aspen HYSYS, HYSYS Python, HYSYS simulation, Aspen HYSYS license:mit.
- GitHub tree inspection for candidate repositories with possible .hsc payloads.
- Zenodo API search for Aspen HYSYS / HYSYS simulation / .hsc / hydrogen / CO2 capture combinations.
- No login-gated, paid, customer-support, institutional, private training, executable, or unknown binary payload was used.

## 3. Keywords Used

- `Aspen HYSYS`
- `HYSYS Python`
- `HYSYS simulation`
- `Aspen HYSYS license:mit`
- `HYSYS hsc license:mit`
- `"Aspen HYSYS" ".hsc"`
- `"Aspen HYSYS" "HYSYS"`
- `"HYSYS simulation" ".hsc"`
- `"Aspen HYSYS" "hydrogen"`
- `"Aspen HYSYS" "CO2 capture"`

## 4. Downloaded Case List

No new high-quality, non-duplicate Aspen HYSYS case file was downloaded in this heartbeat.

Reason: new GitHub model-bearing hits lack explicit licenses, while MIT-licensed model/data hits found this round are already archived or do not contain a HYSYS model file.

## 5. Candidate And Duplicate Findings

| Title | Source page | Download URL | Local path | Reason | Quality | License / public access | Recommended use | Dedupe basis | Residual risk |
|---|---|---|---|---|---|---|---|---|---|
| afabrild/HYSYS-MATLAB-LINK | https://github.com/afabrild/HYSYS-MATLAB-LINK | Raw HSC URL recorded, not downloaded | artifacts/github-afabrild__HYSYS-MATLAB-LINK-* | Contains `Distill_Example.hsc` and MATLAB COM script, but no explicit license. | D | Public repository metadata only; no license detected. | Manual permission candidate for distillation and MATLAB-HYSYS link tests. | source_page, raw HSC URL, filename, metadata SHA256. | Cannot archive model without license/author permission. |
| Rus-tam/hysys_observer | https://github.com/Rus-tam/hysys_observer | Raw HSC URL recorded, not downloaded | artifacts/github-Rus-tam__hysys_observer-* | Contains `example.hsc` and Python observer code, but no explicit license. | D | Public repository metadata only; no license detected. | Manual permission candidate for observer-style automation tests. | source_page, raw HSC URL, filename, metadata SHA256. | Cannot archive model without license/author permission. |
| Anikesh31/simulator_codingplatform_integration | https://github.com/Anikesh31/simulator_codingplatform_integration | Raw HSC URL recorded, not downloaded | artifacts/github-Anikesh31__simulator_codingplatform_integration-* | Contains `Test_file_hysys_python.hsc`, Python/MATLAB scripts, and README, but no explicit license. | D | Public repository metadata only; no license detected. | Manual permission candidate for Python/MATLAB HYSYS integration tests. | source_page, raw HSC URL, filename, metadata SHA256. | Cannot archive model without license/author permission. |
| lihaijie1228/hysys_python_GA | https://github.com/lihaijie1228/hysys_python_GA | Raw HSC URL recorded, not downloaded | artifacts/github-lihaijie1228__hysys_python_GA-* | Contains `Decarbonization.hsc`, CSV, README, and GA automation scripts, but no explicit license. | D | Public repository metadata only; no license detected. | Manual permission candidate for decarbonization optimization and GA tests. | source_page, raw HSC URL, filename, metadata SHA256. | Cannot archive model without license/author permission. |
| Duplicate: edgarsmdn/Aspen_HYSYS_Python | https://github.com/edgarsmdn/Aspen_HYSYS_Python | Not downloaded this run | artifacts/github-edgarsmdn__Aspen_HYSYS_Python-* | MIT repository with `Test_1.hsc`, already archived in CASE/2026-05-11-heartbeat-1057Z. | D | MIT; duplicate of existing archive. | Use existing archived copy for spreadsheet bridge and Python-COM smoke tests. | source_page, codeload URL, known filenames. | Re-downloading would duplicate existing CASE assets. |
| Zenodo search sweep | https://zenodo.org/search?q=Aspen%20HYSYS | Not downloaded | artifacts/zenodo-search-results.json | Search returned known HYSYS model records already archived plus paper/data-only false positives. | D | Search metadata only; individual records vary by license. | Duplicate-control audit trail. | search artifact SHA256, known DOI/source pages. | Search aggregate includes non-HYSYS false positives. |

## 6. Structured Source File

See `sources.json` in this folder for SHA256 values and machine-readable metadata.

## 7. Follow-Up Recommendations

- Ask authors of the four unlicensed GitHub HSC repositories for explicit archive/research-use permission before downloading model payloads.
- Add a `license_required` flag to the CASE intake checklist so no-license HSC repositories go straight to manual review.
- Keep GitHub-first search, but filter candidates by repository license before payload download.
- Retry pushing local commits if GitHub HTTPS connectivity is stable; this run starts from local main already ahead by the prior heartbeat commit.
