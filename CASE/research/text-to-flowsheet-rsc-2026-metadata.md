# Text-to-Flowsheet RSC 2026 Metadata Snapshot

Snapshot date: 2026-06-02 Asia/Shanghai

## Source

- Title: Text-to-Flowsheet: autonomous flowsheet generation from natural language process descriptions
- Venue: Digital Discovery, Royal Society of Chemistry
- First published: 2026-05-25
- DOI: 10.1039/D6DD00060F
- Article page: https://pubs.rsc.org/en/content/articlehtml/2026/dd/d6dd00060f
- Code/data repository: https://github.com/LLM4ChemEng/Text2Flowsheet

## Why It Matters

The paper is valuable for AI-HYSYS-Skill as adjacent, source-backed evidence that modern text-to-simulation work is moving toward:

- an explicit graph or intermediate representation before simulator writes
- simulator-specific translation rather than direct one-shot prompting
- validation stages before accepting a generated simulation
- black-box optimization for uncertain or missing parameters when trying to reach a converged simulation

## Boundary For This Repository

This is not direct proof that AI can reliably create production Aspen HYSYS cases from scratch. The reported simulator path is Aspen Plus, not a validated local HYSYS runtime in this repository.

AI-HYSYS-Skill should use this source to strengthen research/prototype guidance:

- keep topology and parameter intent in an auditable intermediate representation before writing to HYSYS
- use bounded numerical optimization only as local convergence assistance on approved variables
- keep final acceptance tied to an existing HYSYS workcopy, solver status, exported KPIs, and human engineering review

