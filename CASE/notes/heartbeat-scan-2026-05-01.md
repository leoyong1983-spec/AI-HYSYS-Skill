# AI-HYSYS 心跳扫描记录：2026-05-01

## 扫描目的

按既定闭环执行：搜索 AI 控制 Aspen HYSYS、HYSYS COM/Python/Spreadsheet/Workbook 自动化、LLM 工艺模拟 agent、HYSYS digital twin / hybrid AI / surrogate model 资料；与 [../source-index.md](../source-index.md) 比对；有价值则保存到 CASE，必要时更新项目规则，校验后提交推送。

## 新增判断

| 类别 | 来源 | 保存状态 | 价值判断 |
|---|---|---|---|
| 研究 | [ScienceDirect: Design and optimization of a stand-alone hydrogen liquefaction process via LNG regasification, SMR waste heat recovery, and CO valorization](https://www.sciencedirect.com/science/article/abs/pii/S0360319925061464) | ScienceDirect 摘要页下载失败，未保存伪 HTML。本笔记保存可核验元数据和项目判断。 | 有价值。公开摘要明确写到 Aspen HYSYS V12 与 Python scripts 通过 COM automation interface 集成，用于 systematic data extraction、modular simulations、automated sensitivity and optimization analyses。该证据直接补强 direct COM 主通道。 |

## 访问限制记录

本轮尝试保存 ScienceDirect 摘要页失败：

- `Invoke-WebRequest` 连接被关闭，未获得可保存正文。
- 不保存挑战页、错误页或伪快照。

## 对项目的实际改进

1. [../source-index.md](../source-index.md) 登记本次心跳笔记和 ScienceDirect 论文链接。
2. [hysys-source-digest.md](hysys-source-digest.md) 增加 HYSYS V12 + Python COM 的项目化结论。
3. [../../references/control-lane-decision-matrix.md](../../references/control-lane-decision-matrix.md) 增加模块化仿真、数据提取、敏感性和优化任务的 COM 控制边界。
4. [../../README.md](../../README.md) 增加该 HYSYS automation 论文链接，方便访客核验。

## 边界结论

这条资料强化的是“已有 HYSYS 模型 + Python COM 自动化”的工程路线。

它支持以下主张：

1. Direct COM 可作为 HYSYS 自动化主通道，用于系统化数据提取、模块化仿真、敏感性和优化分析。
2. 复杂系统可以拆成子系统运行，但每个子系统都需要清楚的输入输出、单位、收敛状态和数据导出 schema。
3. 批量敏感性或优化前必须先完成单点 smoke test、solver 策略和失败分类。

它不支持以下主张：

1. AI 可以可靠地从零创建生产级 HYSYS 工厂模型。
2. COM 自动化可以绕过 HYSYS runtime、模型收敛、物性包、人工工程审核或项目批准流程。
3. 优化脚本可以默认直接写回生产操作参数。
