# MCP Design Strategies For AI Agents In The Chemical Engineering Industry - Metadata Snapshot

## Source

- Title: MCP Design Strategies for AI Agents in the Chemical Engineering Industry
- Author listed on ResearchGate: Byunghyun Ban
- Venue/status: ResearchGate preprint
- Date shown by source: May 2026
- DOI shown by source: `10.13140/RG.2.2.14152.69125`
- Source page: https://www.researchgate.net/publication/404500792_MCP_Design_Strategies_for_AI_Agents_in_the_Chemical_Engineering_Industry

## Access Note

Direct automated download of the ResearchGate page from PowerShell returned HTTP `1020`, so this repository stores a metadata snapshot rather than a full HTML/PDF copy. Treat this as a candidate source record, not a preserved full-text archive.

## Project-Relevant Content

The source proposes a field-validated MCP ecosystem for chemical-engineering agents, including Process Data MCP, SOP and Work Instruction MCP, Safety and Hazard MCP, Process Simulation MCP, Maintenance MCP, Quality and Laboratory Data MCP, Environmental and Carbon Accounting MCP, and Operator Knowledge Capture MCP.

It is relevant because it reinforces the project boundary that industrial chemical-engineering agents should act through validated, auditable, access-controlled tools and human approval paths rather than through a generic agent framework alone.

## Value Judgment

Grade: **B-/C+ candidate architecture evidence**

Reasons:

- Relevant to AI-HYSYS-Skill's MCP and process-simulation tool-contract boundary.
- Chemical-engineering specific rather than generic AI-agent material.
- Useful for reinforcing read-only-first deployment, access control, audit logging, safety constraints, and human approval.
- Not peer-reviewed and not direct Aspen HYSYS runtime validation.

## Adopted Boundary

For any MCP-style HYSYS task, prefer read-only and dry-run tools first. Any write-capable tool must expose explicit authorization, object schema, units, bounds, rollback behavior, audit log, failure behavior, and human acceptance.

