# Heartbeat Scan - 2026-06-12

## Search Scope

Searched for recent credible sources on AI controlling Aspen HYSYS, Python/COM automation, LLM process-simulation agents, digital twins, and related text-to-flowsheet or graph-based flowsheet workflows.

## Valuable Finding

**Learning from flowsheets: A generative transformer model for autocompletion of flowsheets** (`arXiv:2208.00859v2`)

- Source: https://arxiv.org/abs/2208.00859
- Local abstract snapshot: `CASE/research/flowsheet-autocomplete-sfiles-arxiv-2208.00859v2-abstract.html`
- Local PDF: `CASE/research/flowsheet-autocomplete-sfiles-arxiv-2208.00859v2.pdf`
- PDF SHA256: `084625ceb0d4467bedbd4ca4ed353f903bc8aa79e1a0b48b6dd0d8546ac2ef8f`

## Value Judgment

Grade: **B-/C+ supporting evidence**

This source is useful because it shows a graph/string representation workflow for flowsheet learning and autocompletion using public Aspen Plus and DWSIM flowsheet data. It strengthens the project boundary that AI can propose or autocomplete topology candidates, but those candidates are not automatically HYSYS-valid engineering cases.

## Adopted Project Change

- Updated `CASE/source-index.md` with the local PDF and abstract snapshot.
- Updated `references/literature-patterns.md` to distinguish flowsheet autocompletion from simulator validation.
- Updated `SKILL.md` so SFILES/autocomplete outputs must be converted into an auditable object/stream map and validated through the existing HYSYS workcopy lane before engineering use.
- Updated `README.md` references.

## Not Adopted

- No dependency was added.
- No runtime path was changed.
- No claim was added that AI can reliably build production-ready HYSYS models from zero.
