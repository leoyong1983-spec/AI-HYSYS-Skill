# AI-HYSYS 心跳扫描记录：2026-05-12

## 扫描目的

按既定闭环执行：搜索 AI 控制 Aspen HYSYS、HYSYS COM/Python/Spreadsheet/Workbook 自动化、LLM 工艺模拟 agent、HYSYS digital twin / hybrid AI 资料；与 [../source-index.md](../source-index.md) 比对；有价值则保存到 CASE，必要时更新项目规则，校验后提交推送。

## 新增资料已保存

| 类别 | 本地文件 | 原始来源 | 价值判断 |
|---|---|---|---|
| 官方 | [../official/aspen-hysys-tupras-column-performance-2026.html](../official/aspen-hysys-tupras-column-performance-2026.html) | [Control Column Performance Using Aspen HYSYS](https://www.aspentech.com/en/resources/case-studies/control-column-performance-using-aspen-hysys) | 有价值。AspenTech 官方案例说明 Tüpraş 使用 Aspen HYSYS column analysis 及 Aspen Exchanger Design & Rating 集成来提升塔能力并满足产品规格，补强“已有模型诊断、瓶颈分析、报告输出”的工程价值。 |
| 官方 | [../official/aspen-hysys-tupras-column-performance-2019.pdf](../official/aspen-hysys-tupras-column-performance-2019.pdf) | [AspenTech PDF](https://www.aspentech.com/-/media/aspentech/home/resources/case-study/pdfs/fy19/q3/at-05656-tupras-case-study.pdf?sc_lang=en) | 有价值。保留官方英文 PDF，作为 column hydraulics、tray rating、plant digital twin / column performance 场景的可核验证据。 |
| 研究 | [../research/hysys-psd-xgboost-pso-springer-2026.html](../research/hysys-psd-xgboost-pso-springer-2026.html) | [Springer article page](https://link.springer.com/article/10.1007/s11814-026-00646-x) | 有价值。2026 Korean Journal of Chemical Engineering 论文展示 Aspen HYSYS 压力摆动精馏模型结合 XGBoost 与 PSO 做热负荷预测和工况优化，适合作为 HYSYS baseline -> ML surrogate -> optimization 的新证据。 |
| 研究 | [../research/hysys-psd-xgboost-pso-springer-2026.pdf](../research/hysys-psd-xgboost-pso-springer-2026.pdf) | [Springer PDF](https://link.springer.com/content/pdf/10.1007/s11814-026-00646-x.pdf) | 有价值。保存开放 PDF，便于后续核对模型变量、误差指标、优化边界和 HYSYS 验证责任。 |

## 重复或暂不入库

- 2026-05-11 已保存的 HYSYS/Python/ScadaBR 与 reasoning-agent 资料，本轮不重复保存。
- 搜索结果中的普通博客、泛 AI 营销页和没有 HYSYS 技术细节的 closed-loop AI 宣传不入库，避免把未验证闭环控制说成项目能力。
- Tüpraş 页面曾出现西班牙语 PDF 线索，本轮只保留官方英文 PDF，删除重复语言版本以保持 CASE 轻量。

## 对项目的实际改进

1. [../source-index.md](../source-index.md) 增加 Tüpraş 官方案例、Springer HYSYS+XGBoost/PSO 论文和本次心跳记录。
2. [hysys-source-digest.md](hysys-source-digest.md) 增加 column performance / plant digital twin 与 HYSYS surrogate optimization 的项目化结论。
3. [../../references/digital-twin-boundary.md](../../references/digital-twin-boundary.md) 增加 column hydraulics、tray rating、surrogate optimization 和 PSO 候选工况的默认边界。
4. [../../README.md](../../README.md) 增加两条引用，方便访客从首页追溯证据。

## 边界结论

本轮资料增强的是“已有 HYSYS 模型的诊断、代理模型和优化辅助”，不是 AI 从零建模能力。

它支持以下主张：

1. AI-HYSYS-Skill 可以帮助围绕已有 HYSYS case 整理 column performance、瓶颈、KPI、候选优化变量和审计报告。
2. HYSYS 仿真数据可以训练 ML surrogate，并用 PSO 等优化器生成候选工况。
3. 任何 surrogate / optimizer 建议都必须回到 HYSYS runtime 或人工工程审核验证。

它不支持以下主张：

1. ML surrogate 可以替代 HYSYS baseline。
2. PSO 输出可以直接写回生产控制。
3. 官方案例收益可以未经项目数据验证直接套用。
