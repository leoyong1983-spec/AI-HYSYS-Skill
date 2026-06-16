# Heartbeat Scan - 2026-06-17

## Search Scope

Searched for recent credible papers, official pages, technical posts, and public examples about AI controlling Aspen HYSYS, HYSYS automation via COM/Python/spreadsheets/workbooks, LLM agents for process simulation, and HYSYS digital twin or hybrid AI workflows.

## Valuable Finding

**ddtlxc001/aspen-mcp**

- Source: https://github.com/ddtlxc001/aspen-mcp
- Local README snapshot: `CASE/community/aspen-mcp-ddtlxc001-readme-2026-06-17.md`
- Local metadata snapshot: `CASE/community/aspen-mcp-ddtlxc001-metadata-2026-06-17.md`
- README SHA256: `3f7dcbe82f631a773bd0ac186da86bb1d58bc4cf8006837dcb68bfbddbc1ffc3`

## Value Judgment

Grade: **B adjacent implementation evidence**

The repository is useful because it is a public MIT-licensed Aspen Plus v15 MCP server using COM automation. It is adjacent rather than direct evidence: Aspen Plus is not Aspen HYSYS, and the repository does not validate AI-HYSYS-Skill in a local HYSYS runtime.

Its engineering patterns are still useful for AI-HYSYS-Skill's MCP boundary: explicit lifecycle tools, status/probe operations, convergence diagnostics, stdio MCP transport, dedicated STA COM ownership, auto-retry/reconnection behavior, and a clear tool catalogue.

## Adopted Project Change

- Updated `CASE/source-index.md` with the README and metadata snapshots.
- Updated `references/literature-patterns.md` with an adjacent Aspen MCP/COM implementation pattern.
- Updated `SKILL.md` to require lifecycle/status/probe tools, single COM-owner or STA-thread behavior, retry/reconnect boundaries, and audit/rollback controls when designing HYSYS MCP wrappers.
- Updated `README.md` references.

## Not Adopted

- No dependency on `aspen-mcp` was added.
- No Aspen Plus tool names were copied into HYSYS as if they were portable.
- No claim was added that Aspen Plus MCP automation proves HYSYS runtime readiness or reliable from-scratch HYSYS model generation.

