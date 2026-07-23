# Heartbeat Scan - 2026-06-13

## Search Scope

Searched for recent credible papers, official pages, technical posts, and public examples about AI controlling Aspen HYSYS, HYSYS Python/COM automation, LLM agents for process simulation, and HYSYS digital twin or hybrid AI workflows.

## Valuable Finding

**Large Language Models in Process Systems Engineering: Opportunities, Architectures, and Industrial Deployment Challenges** (`arXiv:2606.11589v1`)

- Source: https://arxiv.org/html/2606.11589v1
- Local HTML snapshot: `CASE/research/llm-pse-survey-arxiv-2606.11589v1.html`
- Local PDF: `CASE/research/llm-pse-survey-arxiv-2606.11589v1.pdf`
- PDF SHA256: `abe501a1023a14f1fe66b00ea1b973d04ce52446e629fd190c12aa0547c6c06d`

## Value Judgment

Grade: **B+ adjacent PSE architecture evidence**

This survey is valuable because it organizes LLM use in process design, simulation, digital twins, optimization, control, and safety. It supports AI-HYSYS-Skill's boundary that LLMs should be treated as constrained interface, orchestration, reasoning, and reporting layers around authoritative simulators and engineering review, not as replacements for validated HYSYS cases, deterministic solver evidence, plant writeback procedures, or process-safety approval.

## Adopted Project Change

- Updated `CASE/source-index.md` with local snapshots.
- Updated `references/literature-patterns.md` with a PSE-wide LLM deployment pattern.
- Updated `SKILL.md` to require tool contracts, deterministic simulator readback, validation metrics, and human acceptance when tasks cite broad PSE LLM architectures.
- Updated `README.md` references.

## Not Adopted

- No dependency or framework was added.
- No claim was added that a general LLM can directly replace HYSYS, APC/DCS, SIS, or qualified process-safety review.
- No code path was changed because the source is architectural evidence rather than a tested HYSYS automation implementation.
