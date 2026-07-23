# Heartbeat scan 2026-07-10

## Scope

Searched for recent credible papers, official documentation, technical posts, and public examples about AI controlling Aspen HYSYS, HYSYS automation through COM/Python/spreadsheets/workbooks, LLM agents for process simulation, and HYSYS digital twin or hybrid AI workflows.

## Adopted source

### Large Language Models in Process Systems Engineering: Opportunities, Architectures, and Industrial Deployment Challenges

- Source: https://arxiv.org/abs/2606.11589
- PDF: https://arxiv.org/pdf/2606.11589
- Local snapshots:
  - `CASE/research/llm-pse-survey-arxiv-2606.11589-abstract-2026-07-10.html`
  - `CASE/research/llm-pse-survey-arxiv-2606.11589.pdf`
- Value grade: B adjacent PSE/LLM boundary evidence.
- Reason: The paper is a June 2026 survey of LLM applications in process systems engineering, including process modeling and simulation, optimization and scheduling, process control, and fault detection and diagnosis. Its abstract explicitly separates demonstrated capabilities from aspirational claims, which is directly useful for this repository's guardrails.
- Boundary: It is not HYSYS-specific and does not prove reliable from-scratch HYSYS model generation. It supports natural-language documentation/query/RAG/human-machine interaction uses more strongly than real-time execution, formal constraint satisfaction, or safety-guaranteed closed-loop control.

## Rejected or deferred findings

- Repeated Sketch2Simulation, PINN digital twin, APS-Agent, and HYSYS MCP references were not duplicated because the existing CASE index already covers them.
- Generic AI/digital-twin marketing pages without new HYSYS-specific runtime, COM, workbook, or validated simulation evidence were not saved.
- Search results that only repeated already-indexed wrapper repositories were not re-downloaded.

## Project impact

The source strengthens the current AI-HYSYS-Skill boundary:

1. Use LLMs for documentation querying, unstructured knowledge synthesis, workflow planning, report drafting, and human-facing explanation.
2. Keep HYSYS runtime, workcopy control, unit schemas, solver status, and exported results as the authoritative engineering evidence.
3. Treat real-time execution, constraint satisfaction, process control, and formal safety guarantees as high-risk areas requiring explicit project procedures and human acceptance.
4. Do not convert broad PSE LLM optimism into a claim that AI can reliably build production HYSYS cases from zero.
