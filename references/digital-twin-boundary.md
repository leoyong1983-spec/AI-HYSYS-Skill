# HYSYS 数字孪生与 AI 边界

## 何时读取

当用户把 HYSYS 与 digital twin、hybrid model、Industrial AI、soft sensor、实时监控、收益优化或排放优化放在一起讨论时，先读这份边界说明。它用于防止把“过程模拟数字孪生”误说成“AI 已经可以自由操控 HYSYS”。

## 新增官方证据

| 来源 | 本地文件 | 项目价值 |
|---|---|---|
| Energy Company Saves $6M USD with a Performance Engineering Digital Twin | [CASE/official/aspen-hysys-performance-digital-twin-case-study.pdf](../CASE/official/aspen-hysys-performance-digital-twin-case-study.pdf) | AspenTech 官方案例明确把 Aspen HYSYS 用于性能工程数字孪生、故障识别、避免非计划停车和经济收益。 |
| Utilize a Process Simulation Digital Twin to Optimize Condensate Yield | [CASE/official/aspen-hybrid-model-condensate-digital-twin-article-2025.pdf](../CASE/official/aspen-hybrid-model-condensate-digital-twin-article-2025.pdf) | 官方文章展示 hybrid model、AI、first-principles、historian、soft sensor、condensate yield 和 GHG reduction 的工程链路。 |
| AspenTech V15 What's New | [CASE/official/aspentech-whats-new-v15-industrial-ai-2026.html](../CASE/official/aspentech-whats-new-v15-industrial-ai-2026.html) | 官方 V15 页面把 Industrial AI、AI Model Builder、Aspen HYSYS/Plus、Aspen OnLine for HYSYS and Aspen Plus 放在同一产品语境中。 |
| EHM105 - Unlock Operational Excellence with AI-Powered Digital Twins | [CASE/official/aspentech-ehm105-ai-powered-digital-twin-agenda.pdf](../CASE/official/aspentech-ehm105-ai-powered-digital-twin-agenda.pdf) | 官方培训议程明确覆盖 HYSYS Workbook、Microsoft Excel and Aspen HYSYS、Plant Data、AI Model Builder、Hybrid Models、Aspen OnLine 发布。 |
| Aspen Hybrid Models Customer FAQ | [CASE/official/aspen-hybrid-models-customer-faq.pdf](../CASE/official/aspen-hybrid-models-customer-faq.pdf) | FAQ 强调 Hybrid Models 是 AI、first principles、simulation/plant data 和领域知识的组合，适合约束 hybrid AI 的工程边界。 |

## 应该如何影响本项目

这些资料增强了 AI-HYSYS-Skill 的工程价值叙事：

1. HYSYS 不只是静态算例工具，可以支撑性能工程、数字孪生、监控、优化和问题诊断。
2. AI / hybrid model 的价值在于把 first-principles simulation、现场数据、soft sensor 和工程目标连接起来。
3. 对本 skill 来说，最现实的切入点仍是已有 HYSYS case 的受控接管、参数更新、KPI 导出、状态检查和报告生成。
4. 如果项目已有 historian、soft sensor、dashboard 或 hybrid model，AI-HYSYS-Skill 应先识别这些现成资产，再决定是否接入。
5. 如果项目要从 offline simulation 走向 online digital twin，应把 plant data、Excel/HYSYS Workbook、AI Model Builder、Hybrid Models、Aspen OnLine 发布和人工校验责任拆开，不要混成一个“AI 自动完成”的黑箱。

## 不应该如何使用

不要把这些官方案例解读成：

1. AI 可以可靠地从零创建复杂 HYSYS 工厂模型。
2. digital twin 自动等同于 direct COM 控制。
3. hybrid model 可以替代 case baseline、物性包、设备拓扑和人工审核。
4. 官方案例的经济收益可以直接套用到本项目。
5. 开源 skill 可以复刻 Aspen OnLine、AI Model Builder 或商业 Hybrid Models 产品能力。

## 推荐项目输出

当用户要求 HYSYS digital twin / Industrial AI / hybrid model 支持时，输出应包含：

1. 当前 HYSYS case 是否是已验证 baseline 或 audited workcopy。
2. 可接入的数据源：HYSYS spreadsheet/workbook、historian、CSV、Excel、人工导出或数据库。
3. soft sensor 或 KPI 的定义、单位、刷新频率和人工校验责任。
4. 该任务属于监控、优化、故障诊断、调参、报告生成还是正式包文件交付。
5. 明确说明哪些工作已由 HYSYS runtime 验证，哪些只是资料支持的设计建议。
6. 若涉及 online deployment，明确 Aspen OnLine / AI Model Builder / Hybrid Models 是否只是外部商业系统入口，还是当前项目里已经配置好的可访问资产。

## Offline 到 Online 的拆分

不要把数字孪生写成一个动作。至少拆成：

1. Offline model：已验证的 HYSYS/Aspen Plus case、workcopy、物性包、设备拓扑和报告 schema。
2. Plant data：Excel、historian、CSV 或数据库数据源，以及清洗、采样、单位和时间戳规则。
3. Hybrid model：AI + first principles 的建模边界、训练数据范围、外推限制和人工验收标准。
4. Online deployment：Aspen OnLine、dashboard、soft sensor 或其他发布层。
5. Audit loop：每次数据更新、模型更新、参数回写、KPI 报告都要保留可审计记录。

## 与控制通道矩阵的关系

[control-lane-decision-matrix.md](control-lane-decision-matrix.md) 回答“用什么通道控制 HYSYS”；本文件回答“digital twin / hybrid AI 证据能支持什么项目主张”。两者要一起用，不能互相替代。
