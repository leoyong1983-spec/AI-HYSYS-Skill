# Aspen HYSYS CASE Heartbeat (2026-05-11 0854Z)

## 运行时间
- 触发/执行 UTC: 2026-05-11T08:54:49Z
- 执行目录: `D:\CODEX\AI-HYSYS-Skill`
- 目标目录: `D:\CODEX\AI-HYSYS-Skill\CASE\2026-05-11-heartbeat-0854Z`

## 检索矿区
- 科学数据仓储: Zenodo API, Figshare API
- 开源代码托管: GitHub Repository/API（仅元数据与目录核查）
- 学术补充材料通道: Figshare supplemental/dataset 条目

## 本次关键词
- `Aspen HYSYS` `case file` `.hsc` `HYSYS XML Cases` `.xml`
- `LNG` `hydrogen` `ammonia` `methanol` `CO2 capture` `plantwide control`
- `supplementary material` `simulation file` `model validation` `experimental data`

## 下载案例清单（非重复）

### 1) Evaluation of plantwide control strategies implemented for an SO2 abatement plant
- 质量评级: `B`
- 来源页面: https://figshare.com/articles/25202060
- 下载 URL: https://api.figshare.com/v2/articles/25202060/files
- 本地路径:
  - `D:\CODEX\AI-HYSYS-Skill\CASE\2026-05-11-heartbeat-0854Z\artifacts\All_control_off_DMC.hsc`
  - `D:\CODEX\AI-HYSYS-Skill\CASE\2026-05-11-heartbeat-0854Z\artifacts\DMC_evaluation2.zip`
  - `D:\CODEX\AI-HYSYS-Skill\CASE\2026-05-11-heartbeat-0854Z\artifacts\DMC_evaluation2-zip-listing.txt`
  - `D:\CODEX\AI-HYSYS-Skill\CASE\2026-05-11-heartbeat-0854Z\artifacts\figshare-25202060-metadata.json`
- 选择理由:
  - 直接包含 Aspen HYSYS `*.hsc` 模型文件（`All_control_off_DMC.hsc`）
  - 数据集公开可下载，带 DOI（`10.25403/UPresearchdata.25202060.v1`）
  - 许可明确（CC BY 4.0），可用于研究归档与自动化基准
- 许可证/公开访问说明:
  - Figshare 公开页面可直接访问，无需登录
  - `license = CC BY 4.0`
- 推荐自动化用途:
  - HYSYS case 打开/参数抓取回归测试
  - 控制策略相关变量扫描与灵敏度分析
  - 大体积工程包的归档完整性与哈希追踪
- 去重依据:
  - 与已有 `CASE/*/sources.json` 的 `source_page`、`download_url`、标题、文件名、SHA256 均无匹配
  - 去重结果: `NO_DUPLICATE_MATCH`
- 安全检查:
  - 已生成压缩包清单 `DMC_evaluation2-zip-listing.txt`
  - 未发现 `.exe/.dll/.bat/.ps1/.vbs/.js/.msi` 等高风险可执行扩展名
  - 未运行任何压缩包内脚本、宏或可执行文件

## 候选但未下载（D）

### A) sour-gas-sweetening-hysys (GitHub)
- 来源页面: https://github.com/Mahdi-Arashian/sour-gas-sweetening-hysys
- 候选理由: 目录包含 `GTU Simulation.hsc` + PDF 报告 + README
- 未下载原因: 仓库未检测到明确 LICENSE，归档/再分发权限不清晰
- 建议: 如获得作者许可或补充许可证，可纳入天然气脱酸场景基准

### B) hysys_python_GA (GitHub)
- 来源页面: https://github.com/lihaijie1228/hysys_python_GA
- 候选理由: 目录包含 `Decarbonization.hsc` + `File.csv` + 自动化脚本
- 未下载原因: 仓库未检测到明确 LICENSE，归档/再分发权限不清晰
- 建议: 若权利明确，可作为“优化/代理模型训练”候选案例

## 主要文件 SHA256
- `All_control_off_DMC.hsc`: `2b7426874874269c51bf6cf950072b7abc8c2a424e3b9adcdce8acbe0232bfd8`
- `DMC_evaluation2.zip`: `6157de72f94afc4d4377d79283c1d4d525ed192f6d1645d2f365532437b4cc0e`
- `DMC_evaluation2-zip-listing.txt`: `755ffa35db88b8b068dd32abf0d3821ef93b4ec3683d1efeb45cdf0744e83a7c`
- `figshare-25202060-metadata.json`: `187d5d3de5e278c3e53e87d6e297c97f6fc999e1efd889398d0efc175b1011e0`

## 残余风险
- 未在本机 Aspen HYSYS 中加载/求解模型，`model_run_status = not_run`
- `DMC_evaluation2.zip` 为应用特定序列化结构（大量非常规扩展名），语义字段需人工二次解读
- 候选 GitHub 仓库许可证不明，暂不纳入下载归档

## 后续建议
1. 优先继续挖掘“带明确开源许可证 + .hsc + README/PDF/CSV”的仓库或数据集（目标 1-2 个/轮）。
2. 对本次 `DMC_evaluation2.zip` 做离线结构映射（仅解析目录/文本，不执行脚本）并补充字段字典。
3. 若可用本机 HYSYS 运行环境，后续增加“可加载性/求解状态”核验记录（版本、求解结果、关键流股/设备检查点）。
