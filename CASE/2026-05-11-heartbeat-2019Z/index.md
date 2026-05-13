# CASE Heartbeat Index (2026-05-11-heartbeat-2019Z)

- 运行时间(UTC): 2026-05-11T20:19:00Z
- 执行目录: `D:\CODEX\AI-HYSYS-Skill`
- 检索矿区:
  - Zenodo API (`records`)
  - Mendeley Data (`public-api` + 数据集页)
  - GitHub API（仓库与树扫描，仅做公开元数据核验）
- 关键词:
  - `Aspen HYSYS`, `hsc`, `HYSYS XML case`, `process simulation`, `LNG`, `CO2 capture`, `Mendeley Data HYSYS`, `GitHub HYSYS .hsc`

## 下载案例清单

本次新增高质量非重复下载案例: **0**

原因:
- Zenodo 与 Mendeley 的高质量 HYSYS 目标命中均与既有 CASE 重复（按 `source_page/download_url/title/filename/sha256` 去重）。
- 新发现候选中，`f28wdd3g8m` 证据显示为 Aspen Plus `.apwz`，未证实 HYSYS `.hsc/.xml`。
- 新发现 GitHub `.hsc` 仓库未声明明确许可证，不满足可安全归档要求。

## 候选与去重记录

1. Duplicate: Zenodo 18806107
- 来源页面: https://zenodo.org/records/18806107
- 下载 URL: https://zenodo.org/api/records/18806107/files
- 本地去重依据: `CASE/2026-05-11-heartbeat-0222Z/sources.json`
- 选择理由: 已有完整 `.hsc + xlsx + EES` 资产，重复下载无收益。
- 质量评级: D（本轮为重复记录，不新增下载）
- 许可证/公开访问: CC BY 4.0（已在历史心跳归档）
- 推荐自动化用途: 使用历史已归档案例做 CCUS 场景回归。

2. Candidate: Mendeley `f28wdd3g8m`
- 来源页面: https://data.mendeley.com/datasets/f28wdd3g8m/2
- 下载 URL: https://data.mendeley.com/public-files/datasets/f28wdd3g8m/files/b250afda-4c6b-4db9-80ac-a677f66c46fb/file_downloaded
- 本地路径: `CASE/2026-05-11-heartbeat-2019Z/artifacts/candidate-f28wdd3g8m-metadata.json`
- 选择理由: 公开 CC BY 数据集，包含流程模拟包；但现有证据只见 Aspen Plus `.apwz`，不满足 HYSYS 基线条件。
- 质量评级: D（候选）
- 许可证/公开访问: CC BY 4.0
- 推荐自动化用途: 若未来扩展到 Aspen Plus，可转为跨平台样本。

3. Candidate set: GitHub unlicensed `.hsc`
- 来源页面: https://github.com/Rus-tam/hysys_observer
- 本地路径: `CASE/2026-05-11-heartbeat-2019Z/artifacts/candidate-github-unlicensed-hsc.json`
- 选择理由: 可见 `.hsc` 文件，但仓库许可证缺失（NOASSERTION），不满足安全归档。
- 质量评级: D（候选）
- 许可证/公开访问: 未明确
- 推荐自动化用途: 需作者授权后再纳入。

## 去重依据

- 主要键: `source_page`, `download_url`, `title`, `local_artifacts.filename`, `local_artifacts.sha256`
- 证据文件: `CASE/2026-05-11-heartbeat-2019Z/artifacts/dedupe-evidence.json`

## 残余风险

- 公开数据仓储中含 HYSYS 模型的新条目稀缺，检索结果易被非相关或低质量内容污染。
- GitHub 无许可证仓库即使含 `.hsc`，也存在再分发法律风险。
- Mendeley 某些数据集描述提及流程模拟，但实际文件可能为 Aspen Plus/图片/表格而非 HYSYS。

## 后续建议

1. 下次继续优先扫描 Zenodo/Mendeley，但加入“最近新增 DOI + `.hsc/.HSC` 文件名”硬过滤。
2. 增加人工许可判定白名单流程：仅纳入明确 MIT/Apache/BSD/CC BY/CC0。
3. 对候选数据集先做元数据与压缩包目录级检查，再决定是否正式下载归档。
