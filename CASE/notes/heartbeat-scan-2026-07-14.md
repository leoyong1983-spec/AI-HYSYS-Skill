# Heartbeat Scan 2026-07-14

## Search Scope

Searched for recent credible papers, official documentation, technical articles, and public code about AI controlling Aspen HYSYS, HYSYS COM/Python automation, MCP/tool-server interfaces, digital twins, operator training, and hybrid AI workflows.

## Valuable Finding

The valuable new source is the open-access paper "Neural Network Prediction of Mass Transfer Coefficients in Distillation Columns Using Aspen Hysys," published in the July 2026 issue of the Journal of Engineering and Sustainable Development.

Saved evidence:

- `CASE/research/hysys-distillation-mass-transfer-ann-jeasd-2026.pdf`

Value grade: B-

Reason:

- Directly uses Aspen HYSYS to generate data for an ANN surrogate.
- Defines a narrow, inspectable variable schema: reflux ratio, feed molar flow, and benzene feed mole fraction as inputs; gas-side volumetric mass-transfer coefficient as output.
- Uses a small 3:4:1 multilayer perceptron and reports 95.3% training performance after 1,000 iterations.
- The source is peer-reviewed, open access, and licensed CC BY 4.0.

Limitations:

- The study is limited to a benzene-toluene binary distillation case using NRTL.
- It does not clearly report an independent train/validation/test split, external validation, uncertainty bounds, extrapolation tests, or failed HYSYS samples.
- No reusable dataset, HYSYS case, automation script, or model code was identified.
- The reported training percentage is not sufficient evidence for production control or generalization to other columns.

## Project Impact

The paper strengthens the existing rule that HYSYS-generated data can support a bounded surrogate or soft-sensor layer, but the surrogate must remain subordinate to the validated HYSYS workcopy and human review.

For similar distillation tasks, require:

- HYSYS case provenance and property-package basis.
- Explicit input/output schema and engineering units.
- Design-space bounds and sample identifiers.
- Train/validation/test separation and error metrics on unseen samples.
- Extrapolation and failed-sample handling.
- HYSYS readback for accepted candidates and a human acceptance record.

`SKILL.md` was not changed because it already requires these controls for surrogate, ML, hybrid-model, and digital-twin tasks.

## Rejected Or Deferred Items

- Aspen Operator Training results were duplicates of the official evidence saved on 2026-07-13.
- Previously indexed PINN, cryogenic heat-exchanger digital-twin, ML-aided flash, MCP, wrapper, and process-simulation-agent sources were not duplicated.
- General training-course listings and social-media discussions were excluded because they do not add technical implementation evidence.
