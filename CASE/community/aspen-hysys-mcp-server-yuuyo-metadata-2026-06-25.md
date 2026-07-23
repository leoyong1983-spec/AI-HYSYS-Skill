# yuuyo-arobet/AspenHYSYS-MCP-Server Metadata

- Source: https://github.com/yuuyo-arobet/AspenHYSYS-MCP-Server
- Snapshot date: 2026-06-25 Asia/Shanghai
- Local README snapshot: `CASE/community/aspen-hysys-mcp-server-yuuyo-readme-2026-06-25.md`
- Local GitHub metadata: `CASE/community/aspen-hysys-mcp-server-yuuyo-metadata-2026-06-25.json`
- Local tree metadata: `CASE/community/aspen-hysys-mcp-server-yuuyo-tree-2026-06-25.json`
- Local license metadata: `CASE/community/aspen-hysys-mcp-server-yuuyo-license-2026-06-25.json`
- License detected by GitHub API: MIT
- Repository description: Control Aspen HYSYS from Claude Code / Claude Desktop via MCP. 51 tools with a safe mode gate, read-only by default, real-machine verified on HYSYS V14.
- Observed tags/topics: Aspen HYSYS, COM automation, MCP, process simulation, Claude.
- Grade: B+/B direct community implementation evidence.

## Value Judgment

This repository is valuable because it is HYSYS-specific rather than Aspen Plus-only. The README and metadata describe a Windows Python MCP server over `HYSYS.Application` COM with read/session/write/build tool classes, explicit `HYSYS_MCP_MODE` gating, read-only-first behavior, and claimed HYSYS V14 real-machine verification.

It should influence AI-HYSYS-Skill as an implementation precedent for MCP tool-contract design, especially:

- separate read, session, write, and build tools;
- read-only/default mode before enhanced write mode;
- lifecycle and health tools before write tools;
- explicit Windows native Python and `pywin32` assumptions;
- HYSYS case/workcopy validation before writes.

## Adoption Boundary

Do not install, vendor, or make this MCP server a default dependency in AI-HYSYS-Skill until local HYSYS runtime validation, tool-permission review, error recovery behavior, and license compatibility are checked in a controlled workcopy.

Do not treat the existence of a public MCP server as proof that AI-HYSYS-Skill itself has a configured MCP runtime, production writeback authorization, or reliable from-scratch HYSYS model generation.

## Snapshot Hashes

- README: `48039CAA23CB6005457161686268EF4EB34357CB41B8BD8D1159C3D1C6C35F03`
- GitHub metadata: `D8003D29AF96A7501444EAC367A7C5D2A3EF1D6A308E22898C77DF7DC9269464`
- GitHub tree metadata: `3B0BE598B0ACDBAF9508DD39D4F7B8ADE0DCF095808A351DA4DEB072658055C0`
- GitHub license metadata: `02AD57A3D7AAA87A24E4D7974D6D39AC1E0D7D488491C8458CB59387B53FED2E`
