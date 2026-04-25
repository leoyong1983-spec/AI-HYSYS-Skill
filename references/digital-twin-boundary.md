# HYSYS 数字孪生与 AI 边界

## 何时读取

当用户把 HYSYS 与 digital twin、hybrid model、Industrial AI、soft sensor、实时监控、收益优化或排放优化放在一起讨论时，先读这份边界说明。它用于防止把“过程模拟数字孪生”误说成“AI 已经可以自由操控 HYSYS”。

## 新增官方证据

| 来源 | 本地文件 | 项目价值 |
|---|---|---|
| Energy Company Saves $6M USD with a Performance Engineering Digital Twin | [CASE/official/aspen-hysys-performance-digital-twin-case-study.pdf](../CASE/official/aspen-hysys-performance-digital-twin-case-study.pdf) | AspenTech 官方案例明确把 Aspen HYSYS 用于性能工程数字孪生、故障识别、避免非计划停车和经济收益。 |
| Utilize a Process Simulation Digital Twin to Optimize Condensate Yield | [CASE/official/aspen-hybrid-model-condensate-digital-twin-article-2025.pdf](../CASE/official/aspen-hybrid-model-condensate-digital-twin-article-2025.pdf) | 官方文章展示 hybrid model、AI、first-principles、historian、soft sensor、condensate yield 和 GHG reduction 的工程链路。 |

## 应该如何影响本项目

这些资料增强了 AI-HYSYS-Skill 的工程价值叙事：

1. HYSYS 不只是静态算例工具，可以支撑性能工程、数字孪生、监控、优化和问题诊断。
2. AI / hybrid model 的价值在于把 first-principles simulation、现场数据、soft sensor 和工程目标连接起来。
3. 对本 skill 来说，最现实的切入点仍是已有 HYSYS case 的受控接管、参数更新、KPI 导出、状态检查和报告生成。
4. 如果项目已有 historian、soft sensor、dashboard 或 hybrid model，AI-HYSYS-Skill 应先识别这些现成资产，再决定是否接入。

## 不应该如何使用

不要把这些官方案例解读成：

1. AI 可以可靠地从零创建复杂 HYSYS 工厂模型。
2. digital twin 自动等同于 direct COM 控制。
3. hybrid model 可以替代 case baseline、物性包、设备拓扑和人工审核。
4. 官方案例的经济收益可以直接套用到本项目。

## 推荐项目输出

当用户要求 HYSYS digital twin / Industrial AI / hybrid model 支持时，输出应包含：

1. 当前 HYSYS case 是否是已验证 baseline 或 audited workcopy。
2. 可接入的数据源：HYSYS spreadsheet/workbook、historian、CSV、Excel、人工导出或数据库。
3. soft sensor 或 KPI 的定义、单位、刷新频率和人工校验责任。
4. 该任务属于监控、优化、故障诊断、调参、报告生成还是正式包文件交付。
5. 明确说明哪些工作已由 HYSYS runtime 验证，哪些只是资料支持的设计建议。

## 与控制通道矩阵的关系

[control-lane-decision-matrix.md](control-lane-decision-matrix.md) 回答“用什么通道控制 HYSYS”；本文件回答“digital twin / hybrid AI 证据能支持什么项目主张”。两者要一起用，不能互相替代。
