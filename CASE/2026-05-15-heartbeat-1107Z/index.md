# CASE Heartbeat 2026-05-15 1107Z

## 1. Run Time

- Trigger UTC time: 2026-05-15T11:07:50.403Z
- Local workspace: D:\CODEX\AI-HYSYS-Skill
- Target directory: CASE/2026-05-15-heartbeat-1107Z
- Artifacts directory: CASE/2026-05-15-heartbeat-1107Z/artifacts
- Model run status: not_run for all entries; no HYSYS model, script, workbook, macro or executable was run.

## 2. Searched Mining Areas

- GitHub repository search, using README/license/topic queries and then repository-tree inspection for unseen high-signal candidates.
- Zenodo API targeted sweep for HYSYS hsc/hscz/simulation-file and methanol/hydrogen/ammonia/LNG supplementary-material queries.
- Existing CASE dedupe pass over 26 prior sources.json files and 139 source entries.

## 3. Keywords Used

- `Aspen HYSYS in:readme`, `HYSYS hsc in:readme`, `HYSYS hscz in:readme`
- `HYSYS "case file" in:readme`, `HYSYS "simulation file" in:readme`
- `HYSYS license:mit`, `HYSYS license:gpl-3.0`
- `HYSYS LNG`, `HYSYS CO2`, `HYSYS hydrogen`, `HYSYS ammonia`, `HYSYS methanol`
- Zenodo: `Aspen HYSYS hsc`, `Aspen HYSYS hscz`, `Aspen HYSYS simulation file`, and topic-specific supplementary material queries.

## 4. Downloaded Case List

No new HYSYS model payload was downloaded in this run.

Reason: no new source satisfied all requirements: public/legal, non-duplicate, clear license or archiving rights, and containing a qualifying HYSYS model file.

## 5. Candidate Findings

### D - Conceptual Design and Economic Feasibility of Valuable Substances Recovery Unit

- Source page: https://github.com/Pouria-MK/_Nov.2023_Conceptual-Design-and-Economic-Feasibility-of-Valuable-Substances-Recovery-Unit
- Download URL considered: https://github.com/Pouria-MK/_Nov.2023_Conceptual-Design-and-Economic-Feasibility-of-Valuable-Substances-Recovery-Unit
- Local evidence: `artifacts/github-Pouria-MK___Nov.2023_Conceptual-Design-and-Economic-Feasibility-of-Valuable-Substances-Recovery-Unit-repo.json`, `artifacts/github-Pouria-MK___Nov.2023_Conceptual-Design-and-Economic-Feasibility-of-Valuable-Substances-Recovery-Unit-tree.json`
- HYSYS files found in tree: `SIM/compressor and cooling water.hsc`, `SIM/no compressor and cooling cycle.hsc`
- Companion material in tree: XML files, Excel workbook, PDF reports and README.
- Selection reason: relevant to hydrogen/methanol recovery and compressor/cooling-cycle alternative process benchmarking.
- License/public access note: public GitHub metadata is accessible, but no License was detected; payloads were not downloaded.
- Recommended automation use: after license or author permission review, use for compressor/cooling-cycle alternative case comparison and report/data extraction tests.
- Dedupe basis: source URL and tree filenames only; no SHA calculated because payloads were not downloaded.
- Residual risk: license/redistribution rights unresolved; no model was opened or solved.

## 6. Duplicate / Skipped Sources

- Zenodo 14882867 (`Dataset for publication "Onboard carbon capture for circular marine fuels"`) remains a high-quality CC-BY-4.0 HYSYS source, but it is already archived in the CASE library.
- Zenodo records surfaced in this sweep were otherwise spreadsheet/PDF-only, known duplicates, Aspen Plus `.apw`, `.lnr`, or non-qualifying for the HYSYS model-file requirement.
- GitHub search surfaced this repository itself (`leoyong1983-spec/AI-HYSYS-Skill`); it was treated as a self-hit and excluded from candidate sources.
- Several MIT repositories were HYSYS-adjacent but contained no qualifying `.hsc`, `.hscz`, HYSYS XML `.xml`, or `.compound` file.

## 7. Quality Ratings

- A duplicate: Zenodo 14882867, already archived.
- D candidate: the Pouria-MK recovery-unit repository, due to missing License.
- No B/C new downloads were added.

## 8. Safety Notes

- No model payload, PDF, spreadsheet or script was downloaded in this run.
- Final committed artifacts are JSON metadata plus `index.md` and `sources.json` only.
- Security inventory reports no executable or macro-like files in final run artifacts.

## 9. Residual Risks

- GitHub search can miss binary `.hsc/.hscz` files; repository-tree inspection is still required.
- Some candidate repositories may later add a license and should be rechecked.
- Tree metadata confirms filenames only, not model integrity or HYSYS version.

## 10. Follow-up Recommendations

1. Put the Pouria-MK recovery-unit repository into a manual license/author-permission queue.
2. Add self-hit filtering for `leoyong1983-spec/AI-HYSYS-Skill` in future search scripts.
3. Keep Zenodo 14882867 on the duplicate allowlist.
4. Continue using GitHub repository-tree scanning rather than relying on code search for HYSYS binary extensions.
