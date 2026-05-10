# AI-HYSYS 心跳扫描记录：2026-05-11

## 扫描目的

按既定闭环执行：搜索 AI 控制 Aspen HYSYS、HYSYS COM/Python/Spreadsheet/Workbook 自动化、LLM 工艺模拟 agent、HYSYS digital twin / hybrid AI 资料；与 [../source-index.md](../source-index.md) 比对；有价值则保存到 CASE，必要时更新项目规则，校验后提交推送。

## 新增资料已保存

| 类别 | 本地文件 | 原始来源 | 价值判断 |
|---|---|---|---|
| 研究 | [../research/hysys-scadabr-python-supervisory-control-mdpi-2026.pdf](../research/hysys-scadabr-python-supervisory-control-mdpi-2026.pdf) | [Supervisory Monitoring and Control Using Chemical Process Simulators and SCADA Systems](https://doi.org/10.3390/methane5010008) | 高价值。2026 年 Methane 论文直接描述 Aspen HYSYS/Python 与 ScadaBR 通过 Modbus 做实时监控、监督和动态模型验证，是本仓库目前最贴近“仿真模型接入外部监督系统”的公开证据。 |
| 研究 | [../research/hysys-scadabr-python-supervisory-control-mdpi-2026-crossref.json](../research/hysys-scadabr-python-supervisory-control-mdpi-2026-crossref.json) | [Crossref metadata](https://api.crossref.org/works/10.3390/methane5010008) | 有价值。保留题名、DOI、发布日期、摘要、引用和开放许可元数据，避免只依赖下载 PDF。 |
| 社区 | [../community/SCADABR-PYTHON-README.md](../community/SCADABR-PYTHON-README.md) | [LizandroCloud/SCADABR-PYTHON](https://github.com/LizandroCloud/SCADABR-PYTHON) | 有价值但边界有限。该仓库是 Python-SCADABR/Modbus 教程，不是 HYSYS API 文档；用于解释 SCADA bridge 层，不作为 HYSYS 直接控制证据。 |
| 社区 | [../community/SCADABR-PYTHON-servidor.py](../community/SCADABR-PYTHON-servidor.py) | [raw servidor.py](https://raw.githubusercontent.com/LizandroCloud/SCADABR-PYTHON/main/tutorial/servidor.py) | 有价值但边界有限。展示 Python 端 Modbus server/bridge 写法，可为 SCADA 测试台、培训或 digital twin dashboard 接口提供参考。 |
| 社区 | [../community/SCADABR-PYTHON-teste-scada.py](../community/SCADABR-PYTHON-teste-scada.py) | [raw teste-scada.py](https://raw.githubusercontent.com/LizandroCloud/SCADABR-PYTHON/main/tutorial/teste-scada.py) | 有价值但边界有限。展示 Python 与 SCADA 通信的测试脚本节奏，不代表可直接回写真实生产控制系统。 |
| 研究 | [../research/reasoning-agent-distillation-nature-2026.pdf](../research/reasoning-agent-distillation-nature-2026.pdf) | [Reasoning-agent-driven process simulation, optimization, carbon accounting and decarbonization of distillation](https://doi.org/10.1038/s44172-025-00583-3) | 有价值。Nature Communications Engineering 2026 论文展示 LLM reasoning agent 自动化流程仿真、优化、碳核算和节能方案构建；属于 Aspen Plus 相邻证据，不是 HYSYS 直接证据。 |
| 研究 | [../research/reasoning-agent-distillation-nature-2026.html](../research/reasoning-agent-distillation-nature-2026.html) | [Nature article page](https://www.nature.com/articles/s44172-025-00583-3) | 有价值。保留开放文章页面快照，便于核对 DOI、发布日期、摘要、授权状态和参考文献。 |

## 重复或暂不入库

- Sketch2Simulation、Text to Simulation、LLM agent process simulation 三类 agentic simulation 证据已在前序心跳记录和 `source-index.md` 中登记，本轮不重复保存。
- 泛泛讨论 AI、digital twin 或 Aspen 产品营销但没有 HYSYS、Python/COM、SCADA、Workbook 或 agent 工作流细节的页面不入库。
- MDPI 常规 HTML 页面匿名下载返回 Access Denied 阻断页，已删除伪快照；仅保留真实 PDF 和 Crossref 元数据。

## 对项目的实际改进

1. [../source-index.md](../source-index.md) 增加 HYSYS/Python/ScadaBR 论文、SCADABR-PYTHON 社区教程、Nature reasoning-agent 论文和本次心跳记录。
2. [hysys-source-digest.md](hysys-source-digest.md) 增加 SCADA/Modbus bridge 和 reasoning-agent 的项目化结论。
3. [../../references/control-lane-decision-matrix.md](../../references/control-lane-decision-matrix.md) 增加 SCADA/Modbus/OPC-style 外部监督通道边界。
4. [../../references/digital-twin-boundary.md](../../references/digital-twin-boundary.md) 增加 dynamic monitoring、operator training、supervisory validation 和 agent decarbonization 的默认边界。
5. [../../SKILL.md](../../SKILL.md) 增加 SCADA/Modbus、external supervisory interface 和 reasoning-agent 碳核算任务的拆分要求。
6. [../../README.md](../../README.md) 增加本轮两条研究引用，并明确 SCADA/Modbus 不等于生产闭环接管。

## 边界结论

本轮资料增强了 AI-HYSYS-Skill 的两个方向：

1. HYSYS 可以通过 Python 与 SCADA/Modbus 风格外部系统做动态监控、监督和控制策略验证。
2. LLM reasoning agent 已经可在严谨流程模拟器上组织仿真、优化和碳核算工作流。

它支持以下主张：

1. AI-HYSYS-Skill 可以帮助整理 HYSYS baseline、变量 schema、Modbus/SCADA tag、KPI、数据时间戳、运行日志和审计报告。
2. 对 operator training、dynamic monitoring、dashboard 或 digital twin testbed，AI 可以生成接入清单、测试脚本、数据字典和人工验收项。
3. 对碳核算和节能优化类 agent 工作流，可以借鉴“仿真 -> 优化 -> 碳/能耗评价 -> 人工复核”的分段模式。

它不支持以下主张：

1. SCADA/Modbus 接入等于 AI 可以接管真实生产控制系统。
2. 开源 skill 可以替代 Aspen OnLine、DCS、APC、SIS、PIMS 或现场批准流程。
3. Aspen Plus 上的 reasoning-agent 成功可以直接等同为 HYSYS 从零建模可靠。
