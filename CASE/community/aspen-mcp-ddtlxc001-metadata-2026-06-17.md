# ddtlxc001/aspen-mcp - Metadata Snapshot

## Source

- Repository: `ddtlxc001/aspen-mcp`
- URL: https://github.com/ddtlxc001/aspen-mcp
- Description: MCP server for Aspen Plus v15. 85 tools for process simulation via COM automation.
- Default branch: `master`
- License shown by GitHub: MIT
- Topics shown by GitHub: `aspen-plus`, `chemical-engineering`, `com-automation`, `fastmcp`, `mcp`, `process-simulation`, `python`, `pywin32`
- Updated at scan time: 2026-06-16T09:52:18Z
- Local README snapshot: `CASE/community/aspen-mcp-ddtlxc001-readme-2026-06-17.md`
- README SHA256: `3f7dcbe82f631a773bd0ac186da86bb1d58bc4cf8006837dcb68bfbddbc1ffc3`

## Value Judgment

Grade: **B adjacent implementation evidence**

This repository is valuable because it is an active MIT-licensed public implementation of an MCP server around a commercial Aspen simulator through COM automation. It is not HYSYS-specific, but it demonstrates useful engineering patterns for AI-HYSYS-Skill: explicit lifecycle tools, health probes, convergence diagnostics, stdio MCP transport, dedicated STA COM threading, retry/reconnection behavior, and clear separation between tool calls and simulator execution.

## Boundary

Do not treat this source as Aspen HYSYS runtime validation. Aspen Plus object paths, file formats, solver behavior, and unit operation APIs are not automatically portable to HYSYS.

For AI-HYSYS-Skill, adopt only the safe architecture lessons: explicit tool contracts, lifecycle probes, single-session locks, STA COM ownership, retry/reconnect boundaries, dry-run/read-only-first behavior, audit logs, rollback, and human acceptance before any write-capable HYSYS workflow.

