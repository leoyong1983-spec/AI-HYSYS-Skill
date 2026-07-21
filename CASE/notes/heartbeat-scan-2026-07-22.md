# Heartbeat Scan 2026-07-22

## Public Search Scope

Searched for recent credible sources on AI controlling Aspen HYSYS, HYSYS COM/Python/spreadsheet/workbook automation, MCP and LLM process-simulation agents, digital twins, hybrid AI, surrogate modeling, and optimization. Findings were compared against `CASE/source-index.md` through the 2026-07-20 entry.

This note contains public-source analysis only. No local project file, path, case, screenshot, operating value, or identifying detail is included.

## Valuable Finding

Title: `Active learning-driven process modeling and optimization of crude oil to chemicals coupled with carbon capture`

- DOI: `10.1016/j.compchemeng.2026.109707`
- Journal: `Computers & Chemical Engineering`
- Grade: B+ direct research evidence
- Saved evidence: `CASE/research/hysys-active-learning-cotc-pcc-crossref-2026-07-22.json`

The public publisher abstract and introduction describe an Aspen HYSYS mechanistic model connected by bidirectional COM exchange to an uncertainty-driven active-learning workflow. The workflow selects informative simulator evaluations instead of relying only on random sampling and then uses a surrogate for multi-objective decision support.

## Adopted Safeguards

- Define and retain the initial experimental design.
- Record the acquisition or uncertainty metric, batch size, stopping rule, and sample IDs.
- Keep failed HYSYS evaluations rather than silently dropping them.
- Maintain an untouched validation set and report unseen-sample metrics.
- Count only solved and read-back HYSYS runs as simulator evidence.
- Revalidate final surrogate or optimizer candidates in the approved HYSYS workcopy before human acceptance.

## Limitations

- No public source code, HYSYS case, reusable dataset, or downloadable full text was identified.
- The Crossref snapshot has bibliographic metadata but no abstract; the methodological details were independently checked on the public publisher page.
- Reported sample savings and process-performance results are case-specific and were not adopted as project claims.
- Active learning remains an advisory sampling layer, not permission for autonomous production writeback.

## Rejected Or Deferred Results

- Previously indexed HYSYS pressure-swing-distillation, ANN, ML-flash, HDA surrogate, PINN, Sketch2Simulation, and APS/MCP papers were not duplicated.
- Tracked HYSYS MCP and wrapper repositories had no newer code push that changed their assessment.
- `aspen-pysys` remains at alpha `0.1.0a5` and is not a default dependency.
- General cloud MCP gateway work is architecture-adjacent and does not prove HYSYS runtime behavior.
