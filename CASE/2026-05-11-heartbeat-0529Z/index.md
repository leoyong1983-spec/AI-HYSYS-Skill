# Aspen HYSYS CASE Heartbeat (2026-05-11-0529Z)

- 运行时间(UTC): 2026-05-11T05:45:13Z
- 运行目录: D:\CODEX\AI-HYSYS-Skill
- 本次新增下载案例数: **0**
- 本次候选记录数: **3**

## 检索矿区

1. Zenodo API (/api/records, /api/records/{id})
2. Figshare API (/v2/articles/search, /v2/articles/{id})
3. OSF API (/v2/nodes，命中为 0)
4. Dataverse (Harvard API 文件级搜索，命中为 0)
5. GitHub/GitLab 公开检索（本轮未获得可确认公开且含 HYSYS case 的新来源）

## 关键词

- "Aspen HYSYS" "case file"
- "Aspen HYSYS" ".hsc"
- "HYSYS XML Cases" ".xml"
- "process simulation" "model validation" "experimental data"
- "LNG" "CO2 capture" "hydrogen" "ammonia" "methanol"

## 下载案例清单

- 无新增下载。
- 依据：本轮可确认来源中未发现满足“公开可归档 + 含 .hsc/.xml 或可明确还原工程包 + 非重复”的新目标。

## 候选与来源

1. Figshare 31477552
- 来源页面: https://curate.curtin.edu.au/articles/journal_contribution/An_adaptable_steady_state_aspen_hysys_model_for_the_methane_fuelled_solid_oxide_fuel_cell/31477552
- 下载 URL: https://api.figshare.com/v2/articles/31477552/files
- 本地路径: CASE/2026-05-11-heartbeat-0529Z/artifacts/figshare-31477552-metadata.json
- 质量评级: D
- 选择理由: 标题直接指向 Aspen HYSYS 模型主题，适合持续跟踪。
- 许可证/公开访问说明: All rights reserved, written permission required，且未暴露可下载模型文件。
- 推荐自动化用途: 暂不纳入自动化基准库；仅可用于后续人工联系作者。

2. Figshare 32085284
- 来源页面: https://acs.figshare.com/articles/journal_contribution/Comparative_Analysis_of_MEA_Absorption_and_Membrane_Separation_for_FCCU_CO_sub_2_sub_Capture_Process_Simulation_and_Techno-Economic_Evaluation/32085284
- 下载 URL: https://api.figshare.com/v2/articles/32085284/files
- 本地路径: CASE/2026-05-11-heartbeat-0529Z/artifacts/figshare-32085284-metadata.json
- 质量评级: D
- 选择理由: CO2 capture 主题匹配，但附件表现为 PDF 补充材料，不含模型文件。
- 许可证/公开访问说明: CC BY-NC 4.0（非商业约束），模型可复现性不足。
- 推荐自动化用途: 仅可提取参数假设，不可直接做 HYSYS 案例自动化测试。

3. Zenodo 7787405
- 来源页面: https://zenodo.org/records/7787405
- 下载 URL: https://zenodo.org/api/records/7787405/files
- 本地路径: CASE/2026-05-11-heartbeat-0529Z/artifacts/zenodo-7787405-metadata.json
- 质量评级: D
- 选择理由: 主题与船载碳捕集相关，属于优先方向。
- 许可证/公开访问说明: CC-BY-4.0 公开，但仅见 XLSX 数据，不含 .hsc/.xml。
- 推荐自动化用途: 可作为数据对照候选，不能直接作为 HYSYS 基准模型。

## 去重依据

已读取并去重基线文件:
- CASE/2026-05-11-heartbeat-0026Z/sources.json
- CASE/2026-05-11-heartbeat-0222Z/sources.json

已存在来源（本轮不重复下载）:
- https://zenodo.org/records/10966344
- https://zenodo.org/records/14882867
- https://zenodo.org/records/15338007
- https://zenodo.org/records/18806107
- https://zenodo.org/records/19469917
- https://github.com/andr1976/dwsim-paper

## 残余风险

- 多个公开条目只提供论文/PDF/表格，无 HYSYS 模型文件，无法满足 A/B/C 级纳入标准。
- 个别候选许可为 NC 或 All Rights Reserved，公共仓库再分发边界需人工确认。
- 本轮未运行 Aspen HYSYS，不对模型可计算性做任何运行声明。

## 后续建议

1. 下一轮把检索重点转向“论文补充包中明确给出 .hsc/.xml 的 DOI 记录”。
2. 增加人工许可白名单策略（例如明确接受的 CC 许可证集合），减少反复候选筛选。
3. 继续优先跟踪 LNG/CO2 capture/hydrogen 主题的 Zenodo 与高校公开仓库。
