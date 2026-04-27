# HYSYS 数字孪生与 AI 边界

## 何时读取

当用户把 HYSYS 与 digital twin、hybrid model、Industrial AI、soft sensor、实时监控、收益优化或排放优化放在一起讨论时，先读这份边界说明。它用于防止把“过程模拟数字孪生”误说成“AI 已经可以自由操控 HYSYS”。

## 新增官方证据

| 来源 | 本地文件 | 项目价值 |
|---|---|---|
| Energy Company Saves $6M USD with a Performance Engineering Digital Twin | [CASE/official/aspen-hysys-performance-digital-twin-case-study.pdf](../CASE/official/aspen-hysys-performance-digital-twin-case-study.pdf) | AspenTech 官方案例明确把 Aspen HYSYS 用于性能工程数字孪生、故障识别、避免非计划停车和经济收益。 |
| Utilize a Process Simulation Digital Twin to Optimize Condensate Yield | [CASE/official/aspen-hybrid-model-condensate-digital-twin-article-2025.pdf](../CASE/official/aspen-hybrid-model-condensate-digital-twin-article-2025.pdf) | 官方文章展示 hybrid model、AI、first-principles、historian、soft sensor、condensate yield 和 GHG reduction 的工程链路。 |
| Real-Time Quality Control: How HPCL Uses Industrial AI | [CASE/official/aspen-hpcl-industrial-ai-quality-soft-sensors-2026.pdf](../CASE/official/aspen-hpcl-industrial-ai-quality-soft-sensors-2026.pdf) | 官方案例展示 Aspen AI Model Builder + Aspen HYSYS 可用于部署 AI soft sensors，按分钟级预测质量参数，支持实时质量控制和成本优化。 |
| AspenTech V15 What's New | [CASE/official/aspentech-whats-new-v15-industrial-ai-2026.html](../CASE/official/aspentech-whats-new-v15-industrial-ai-2026.html) | 官方 V15 页面把 Industrial AI、AI Model Builder、Aspen HYSYS/Plus、Aspen OnLine for HYSYS and Aspen Plus 放在同一产品语境中。 |
| Deploy Simulation Models Online Easily Gain Unrivaled Process Insights | [CASE/official/aspen-hysys-online-simulation-models-webinar-2026.html](../CASE/official/aspen-hysys-online-simulation-models-webinar-2026.html) | 官方 webinar 页面把 Aspen HYSYS models、online simulations、KPI monitoring、process insights、节能减排和 troubleshooting 放在同一工作流中。 |
| Aspen HYSYS Dynamics | [CASE/official/aspen-hysys-dynamics-product-page-2026.html](../CASE/official/aspen-hysys-dynamics-product-page-2026.html) | 官方产品页说明 HYSYS Dynamics 支持动态仿真、瞬态条件分析和控制方案验证；用于约束动态任务的基线、转换和审核边界。 |
| EHM105 - Unlock Operational Excellence with AI-Powered Digital Twins | [CASE/official/aspentech-ehm105-ai-powered-digital-twin-agenda.pdf](../CASE/official/aspentech-ehm105-ai-powered-digital-twin-agenda.pdf) | 官方培训议程明确覆盖 HYSYS Workbook、Microsoft Excel and Aspen HYSYS、Plant Data、AI Model Builder、Hybrid Models、Aspen OnLine 发布。 |
| Aspen Hybrid Models Customer FAQ | [CASE/official/aspen-hybrid-models-customer-faq.pdf](../CASE/official/aspen-hybrid-models-customer-faq.pdf) | FAQ 强调 Hybrid Models 是 AI、first principles、simulation/plant data 和领域知识的组合，适合约束 hybrid AI 的工程边界。 |

## 新增研究证据

| 来源 | 本地文件 | 项目价值 |
|---|---|---|
| Data-driven simulation of crude distillation using Aspen HYSYS and comparative machine learning models | [CASE/notes/heartbeat-test-2026-04-27-cjce-hysys-ml.md](../CASE/notes/heartbeat-test-2026-04-27-cjce-hysys-ml.md) | 记录 2026 CJCE 论文元数据，补强“HYSYS 仿真数据 -> ML surrogate / soft sensor / 快速估算层”的研究证据，同时保留访问限制和不替代 HYSYS baseline 的边界。 |
| Artificial intelligence-driven surrogate modeling for computationally efficient and digitally decarbonized LNG process optimization under varying feed composition | [CASE/research/hysys-lng-surrogate-jcp-2026-metadata.html](../CASE/research/hysys-lng-surrogate-jcp-2026-metadata.html) | 记录 2026 JCP LNG surrogate 论文元数据，补强“仿真数据 -> Random Forest surrogate -> LNG 优化/计算时间与数字碳足迹降低”的证据。 |
| On the use of Surrogate Models to enhance the production planning of sustainable aviation fuels via the hydroprocessed esters and fatty acids process | [CASE/notes/heartbeat-scan-2026-04-28.md](../CASE/notes/heartbeat-scan-2026-04-28.md) | 记录 HEFA production planning surrogate 线索和 SSRN 访问限制；用于提醒 surrogate 可连接生产计划系统，但本 skill 不替代 Aspen PIMS-AO、AI Model Builder 或商业计划优化器。 |

## 应该如何影响本项目

这些资料增强了 AI-HYSYS-Skill 的工程价值叙事：

1. HYSYS 不只是静态算例工具，可以支撑性能工程、数字孪生、监控、优化和问题诊断。
2. AI / hybrid model 的价值在于把 first-principles simulation、现场数据、soft sensor 和工程目标连接起来。
3. 对本 skill 来说，最现实的切入点仍是已有 HYSYS case 的受控接管、参数更新、KPI 导出、状态检查和报告生成。
4. 如果项目已有 historian、soft sensor、dashboard 或 hybrid model，AI-HYSYS-Skill 应先识别这些现成资产，再决定是否接入。
5. 如果项目要从 offline simulation 走向 online digital twin，应把 plant data、Excel/HYSYS Workbook、AI Model Builder、Hybrid Models、Aspen OnLine 发布和人工校验责任拆开，不要混成一个“AI 自动完成”的黑箱。
6. 如果目标是 soft sensor 或在线质量预测，AI-HYSYS-Skill 应先定义 KPI、预测频率、数据源、HYSYS baseline、模型有效范围、报警/报告口径和人工验收责任。

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
7. 若涉及 soft sensor，明确它是只读预测、操作建议、还是允许回写到 HYSYS/workbook 的闭环控制建议；默认不允许自动闭环回写。

## Offline 到 Online 的拆分

不要把数字孪生写成一个动作。至少拆成：

1. Offline model：已验证的 HYSYS/Aspen Plus case、workcopy、物性包、设备拓扑和报告 schema。
2. Plant data：Excel、historian、CSV 或数据库数据源，以及清洗、采样、单位和时间戳规则。
3. Hybrid model：AI + first principles 的建模边界、训练数据范围、外推限制和人工验收标准。
4. Online deployment：Aspen OnLine、dashboard、soft sensor 或其他发布层。
5. Audit loop：每次数据更新、模型更新、参数回写、KPI 报告都要保留可审计记录。

## Soft Sensor 任务默认边界

HPCL 案例说明 HYSYS + AI Model Builder 可以支撑实时质量预测，但本开源 skill 的默认职责应限定为：

1. 整理已有 HYSYS case、Workbook/Spreadsheet、历史数据和 KPI 定义。
2. 输出 soft sensor 候选变量、单位、采样频率、模型有效范围和验证清单。
3. 生成审计报告、异常说明和人工复核项。
4. 不默认训练、部署或声称替代 Aspen AI Model Builder。
5. 不默认把 soft sensor 预测结果自动回写为 HYSYS 操作参数。

## Surrogate / 代理模型任务默认边界

当用户要求基于 HYSYS 做 data-driven simulation、ML surrogate、快速估算模型或软测量候选模型时，默认职责应限定为：

1. 把 HYSYS 视为可信仿真基线和数据来源，而不是被代理模型替代的对象。
2. 先定义设计空间、输入变量、输出 KPI、单位、采样策略、收敛失败记录和异常点处理规则。
3. 输出训练/验证/测试划分、误差指标、适用范围、外推禁区和人工复核清单。
4. 只把 surrogate 用作快速筛选、报告辅助或候选操作建议，不默认作为生产闭环控制器。
5. 任何超出训练范围的建议，都必须回到 HYSYS runtime 或人工工程审核重新验证。

## Dynamic / Online 任务默认边界

当用户要求 HYSYS Dynamics、online simulation、live process digital twin、KPI monitoring 或 Aspen OnLine 相关任务时，默认职责应限定为：

1. 先确认 steady-state baseline、dynamic case 或 online model 是否已经由人类工程师建立并验证。
2. 若只是 steady-state case，不默认自动转换成 dynamic model；先输出转换前提、缺失数据、控制结构、设备 holdup、压力流网络和验证清单。
3. 若涉及 online deployment，先识别 Aspen OnLine、dashboard、historian、DCS/APC、PIMS 或其他外部商业系统是否已存在，并把它们作为外部边界。
4. 本 skill 可以整理变量映射、KPI 定义、运行记录、异常解释和报告，但不默认发布在线模型或闭环接管生产控制。
5. 任何动态响应、在线预测或计划优化结果，都必须保留数据时间戳、模型版本、有效范围和人工验收记录。

## 与控制通道矩阵的关系

[control-lane-decision-matrix.md](control-lane-decision-matrix.md) 回答“用什么通道控制 HYSYS”；本文件回答“digital twin / hybrid AI 证据能支持什么项目主张”。两者要一起用，不能互相替代。
