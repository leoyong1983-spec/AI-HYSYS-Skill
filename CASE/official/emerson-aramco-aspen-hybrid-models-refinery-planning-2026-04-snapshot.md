# Emerson / Aramco Aspen Hybrid Models refinery planning snapshot

Source URL: https://www.aspentech.com/en/resources/press-releases/emerson-and-aramco-deploy-ai-solution-aimed-at-higher-refinery-yield-volume-and-efficiencies

Published: 2026-04-27

Captured by heartbeat: 2026-05-18 Asia/Shanghai

## Why this source matters

This official Emerson/AspenTech release documents Aramco deploying Aspen Hybrid Models in an existing refinery planning framework. It is useful evidence for the AI-HYSYS-Skill boundary around hybrid AI, refinery planning, rigorous first-principles simulation cases, plant-data calibration, and planning optimizer integration.

It does not prove that an open-source Codex skill can reproduce Aspen Hybrid Models, AspenTech Manufacturing and Supply Chain tools, or production planning writeback. It also does not prove reliable from-scratch HYSYS model generation.

## Technical points to preserve

- The deployment integrates Aspen Hybrid Models into Aramco's existing refinery planning framework.
- The work targets multi-site, multi-period refinery planning rather than direct HYSYS COM control.
- Emerson describes the method as combining first-principles models, industrial AI, and deep domain expertise.
- The release reports yield and quality prediction accuracy up to 98.5% in key refinery units.
- CCR and platformer units are mentioned as implemented areas; hydrocracker expansion is described as a current focus.
- The models are described as using thousands of converged simulation cases built on rigorous first-principles models calibrated with actual plant data.
- The relevant product boundary spans Aspen Hybrid Models, AspenTech Performance Engineering, and AspenTech Manufacturing and Supply Chain suites.

## Project interpretation

For this repository, the correct takeaway is:

1. Keep HYSYS or other rigorous simulation cases as the validated baseline.
2. Treat hybrid AI and surrogate planning models as advisory or planning layers with explicit validity ranges.
3. Require plant data provenance, model versioning, objective functions, constraints, and human acceptance before using recommendations.
4. Do not claim this skill can replace PIMS, APC, DCS, Aspen Hybrid Models, or closed-loop production planning systems.
5. When a user asks for refinery planning support, produce candidate scenarios, KPI tables, validation evidence, and audit notes, then require HYSYS/runtime or project-approved planning-system review before any operational use.

## Value judgment

Quality: A

Reason: official vendor/customer deployment evidence; directly relevant to hybrid AI and refinery planning boundaries; not a runnable HYSYS automation example.
