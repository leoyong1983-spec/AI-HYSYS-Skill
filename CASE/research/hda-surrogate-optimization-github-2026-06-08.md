# HDA Surrogate Optimization GitHub Metadata Snapshot

Snapshot date: 2026-06-08 Asia/Shanghai

## Source

- Repository: Galigeigei-Z/HDA-Surrogate-Optimization
- URL: https://github.com/Galigeigei-Z/HDA-Surrogate-Optimization
- License observed from repository page: MIT
- Cited paper: Sustainability assessment and optimization of a toluene hydrodealkylation process using surrogate models
- Venue: Chemical Engineering Science 332 (2026) 124158
- DOI: 10.1016/j.ces.2026.124158

## Why It Matters

This source is valuable for AI-HYSYS-Skill because it is public, recent, HYSYS-adjacent, and includes a HYSYS automation demo. The repository describes:

- a Python-based interface for Aspen HYSYS
- connection to an already-open HYSYS case through `win32com`
- mapping of material stream and unit-operation names
- structured parameter changes and result inspection
- mock mode when HYSYS is not available
- heat-network supertargeting, pinch-analysis workflow, surrogate modeling, Bayesian optimization, and sustainability metrics

## Boundary For This Repository

This source supports existing-case automation, teaching demos, and sustainability/HEN workflow design. It does not prove that AI can reliably build a production HYSYS model from scratch.

For AI-HYSYS-Skill, use this source to reinforce:

- connect to an existing open/loadable HYSYS case before automation
- map stream and unit-operation names before writes
- separate HYSYS runtime validation from mock-mode or notebook-only demonstrations
- treat surrogate/BO/HEN supertargeting outputs as advisory candidates until HYSYS workcopy readback and human review pass

