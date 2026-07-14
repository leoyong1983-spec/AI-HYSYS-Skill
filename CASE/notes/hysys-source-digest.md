# HYSYS 资料摘要

## 一句话结论

AI-HYSYS-Skill 最有说服力的定位，不是“AI 会点 HYSYS”，而是：

`AI 可以沿着 Aspen 官方承认的工作流，使用 direct COM 作为主执行层、spreadsheet/workbook 作为稳定桥接层，在可审计边界内接管 Aspen HYSYS。`

## 2026-04-25 心跳测试新增结论

这次手动试跑没有推翻原定位，反而把证据链补强了：HYSYS 最适合让 AI 接管“已有可运行模型”的参数、边界、求解、检查和报告，不应把默认卖点写成从零自动建模。

新增官方材料显示，AspenTech 仍在把 HYSYS 放在工程模拟、经济、能耗、安全、排放、全生命周期决策和 Industrial AI / Hybrid Models 的语境里；这支持我们继续把 AI-HYSYS-Skill 定位为“工程工作流接管层”，而不是孤立的脚本玩具。

新增研究材料显示，HYSYS 还可以作为高保真动态数据源，支撑 PINN / digital twin / soft sensing / MPC / anomaly detection 方向。但这条线是“围绕 HYSYS 的 AI 建模与数字孪生”，不是“AI 直接控制 HYSYS COM”的替代证据，所以在 README 和 SKILL 中应保持边界清楚。

第二轮手动测试又补到两条更贴近控制通道的证据：[research/hysys-coding-platforms-jglobal-2025.html](../research/hysys-coding-platforms-jglobal-2025.html) 证明 2025 年已有论文系统讨论 Python 与 Aspen HYSYS 的对象层级、特殊对象和 backdoor variables；[research/hysys-interconnection-methodologies-sim2-2022.pdf](../research/hysys-interconnection-methodologies-sim2-2022.pdf) 则把 HYSYS 连接方式拆成 direct communication、indirect communication、internal spreadsheets、data tables 四类并对比。它们共同支持本仓库保留“direct COM 主通道 + spreadsheet/workbook 稳定桥接 + 其他连接方式按需降级”的设计。

第三轮手动测试新增两类官方数字孪生证据：[official/aspen-hysys-performance-digital-twin-case-study.pdf](../official/aspen-hysys-performance-digital-twin-case-study.pdf) 展示 Aspen HYSYS 在性能工程数字孪生、故障识别和经济收益中的应用；[official/aspen-hybrid-model-condensate-digital-twin-article-2025.pdf](../official/aspen-hybrid-model-condensate-digital-twin-article-2025.pdf) 展示 hybrid model、AI、first-principles、historian、soft sensor 和凝析油收益优化的链路。它们增强的是“工程价值和 digital twin 边界”，不是“AI 直接控制 HYSYS COM”的证据；对应项目规则见 [references/digital-twin-boundary.md](../../references/digital-twin-boundary.md)。

2026-04-26 自动心跳继续补强官方 online/digital-twin 证据：[official/aspentech-whats-new-v15-industrial-ai-2026.html](../official/aspentech-whats-new-v15-industrial-ai-2026.html) 显示 AspenTech V15 把 Industrial AI、AI Model Builder、Aspen HYSYS/Plus 和 Aspen OnLine 放在同一产品路线中；[official/aspentech-ehm105-ai-powered-digital-twin-agenda.pdf](../official/aspentech-ehm105-ai-powered-digital-twin-agenda.pdf) 明确覆盖 HYSYS Workbook、Microsoft Excel and Aspen HYSYS、Plant Data、AI Model Builder、Hybrid Models、Aspen OnLine 发布。项目结论是：AI-HYSYS-Skill 可以帮助整理 offline model、plant data、KPI、控制通道和审计输出，但不能宣称复刻 Aspen OnLine 或 AI Model Builder。

2026-04-27 自动心跳新增 HPCL 官方案例：[official/aspen-hpcl-industrial-ai-quality-soft-sensors-2026.pdf](../official/aspen-hpcl-industrial-ai-quality-soft-sensors-2026.pdf) 显示 Aspen AI Model Builder 与 Aspen HYSYS 可用于部署 AI soft sensors，按分钟级预测炼厂产品质量参数。它对本项目的价值是补强“soft sensor / real-time KPI / quality prediction”边界，而不是扩大到自动闭环控制；因此默认仍应输出 KPI 定义、数据源、模型有效范围、人工验收和审计记录。

2026-04-27 手动测试补充一条 HYSYS + ML 代理模型证据：[notes/heartbeat-test-2026-04-27-cjce-hysys-ml.md](heartbeat-test-2026-04-27-cjce-hysys-ml.md) 记录了 CJCE 2026 原油蒸馏论文的书目信息与访问限制。它的项目价值是说明 HYSYS 可作为仿真数据源，为 surrogate model、soft sensor 和快速估算层提供训练基础；但它仍不支持从零自动建模，也不支持未复核代理模型替代 HYSYS baseline。

2026-04-28 自动心跳新增三类证据：[official/aspen-hysys-online-simulation-models-webinar-2026.html](../official/aspen-hysys-online-simulation-models-webinar-2026.html) 补强 HYSYS models online deployment、KPI monitoring、process insights 和节能减排场景；[official/aspen-hysys-dynamics-product-page-2026.html](../official/aspen-hysys-dynamics-product-page-2026.html) 补强 HYSYS Dynamics 与瞬态分析边界；[research/hysys-lng-surrogate-jcp-2026-metadata.html](../research/hysys-lng-surrogate-jcp-2026-metadata.html) 补强 LNG surrogate / 低数字碳足迹优化研究证据。项目结论是：online deployment、dynamic simulation、surrogate planning 都可以纳入“已有 HYSYS case 的受控接管和审计输出”，但必须拆开商业系统、动态模型转换、代理模型有效范围和人工验收责任。

2026-04-30 自动心跳补强 HEFA / SAF production planning surrogate 证据：[notes/heartbeat-scan-2026-04-30.md](heartbeat-scan-2026-04-30.md) 记录了 ScienceDirect、AIChE 和 SSRN 访问限制以及可核验元数据。项目结论是：surrogate 可作为计划优化和情景筛选的加速层，但 AI-HYSYS-Skill 不替代 Aspen PIMS-AO、AI Model Builder、Aspen OnLine、APC/DCS 或人类工程审核。

2026-05-01 自动心跳补强 direct COM 主通道证据：[notes/heartbeat-scan-2026-05-01.md](heartbeat-scan-2026-05-01.md) 记录了氢液化论文的公开摘要信息。其关键价值是明确展示 Aspen HYSYS V12 可通过 Python scripts 与 COM automation interface 集成，用于系统化数据提取、模块化仿真、自动敏感性和优化分析。这支持本仓库把 direct COM 作为正式主通道，但仍要求单点 smoke test、solver 策略、schema 冻结和人工审核。

2026-05-02 自动心跳补强 LLM agent / text-to-simulation 证据：[research/text-to-simulation-arxiv-2601.06776.pdf](../research/text-to-simulation-arxiv-2601.06776.pdf) 展示从文本过程规格到可计算仿真配置的多智能体工作流；[research/llm-agent-process-simulation-arxiv-2601.11650.pdf](../research/llm-agent-process-simulation-arxiv-2601.11650.pdf) 展示 LLM agent 通过 MCP server 和 Python 与严谨流程模拟器交互。项目结论是：agentic simulation 可以借鉴工具边界、分步构建、数据提取、优化和专家监督模式，但 AI-HYSYS-Skill 的生产默认仍是接管已有可运行 HYSYS case，不是单提示从零建模。

2026-05-05 自动心跳新增三类 AspenTech 官方 digital twin 证据：[official/aspen-hysys-mysep-live-process-digital-twin-2026.html](../official/aspen-hysys-mysep-live-process-digital-twin-2026.html) 展示 Aspen HYSYS 与 MySep Engine 集成形成 live process digital twin；[official/aspen-hysys-saudi-aramco-plant-digital-twin-2026.html](../official/aspen-hysys-saudi-aramco-plant-digital-twin-2026.html) 展示 Saudi Aramco 使用 HYSYS 建立多个装置 plant digital twins 做炼厂改造可行性分析；[official/aspen-hysys-indian-oil-barauni-process-digital-twins-2026.html](../official/aspen-hysys-indian-oil-barauni-process-digital-twins-2026.html) 展示 Indian Oil Barauni Refinery 部署 HYSYS-based process digital twins。项目结论是：AI-HYSYS-Skill 可以服务 live/multi-unit/refinery digital twin 的前置整理、KPI schema、外部系统边界和审计输出，但不能宣称复刻商业 live digital twin 或自动闭环控制。

2026-05-11 自动心跳新增两条更贴近“外部监督系统”和“agentic simulation”的证据：[research/hysys-scadabr-python-supervisory-control-mdpi-2026.pdf](../research/hysys-scadabr-python-supervisory-control-mdpi-2026.pdf) 展示 Aspen HYSYS/Python 与 ScadaBR 通过 Modbus 做实时监控、监督和动态模型验证；[research/reasoning-agent-distillation-nature-2026.pdf](../research/reasoning-agent-distillation-nature-2026.pdf) 展示 LLM reasoning agent 自动化流程仿真、优化、碳核算和节能方案构建。项目结论是：SCADA/Modbus 只能作为外部监督、培训、dashboard 或 digital twin testbed 通道，不能默认写回生产控制；Aspen Plus reasoning-agent 论文可借鉴分步工具链和碳核算模式，但不证明 HYSYS 从零建模已经可靠。

2026-05-12 自动心跳新增两类证据：[official/aspen-hysys-tupras-column-performance-2019.pdf](../official/aspen-hysys-tupras-column-performance-2019.pdf) 展示 Tüpraş 使用 Aspen HYSYS column analysis 与 Aspen EDR 集成进行塔性能诊断和能力提升；[research/hysys-psd-xgboost-pso-springer-2026.pdf](../research/hysys-psd-xgboost-pso-springer-2026.pdf) 展示 Aspen HYSYS 压力摆动精馏模型结合 XGBoost 与 PSO 做热负荷预测和工况优化。项目结论是：AI-HYSYS-Skill 可以服务已有 HYSYS case 的诊断、KPI schema、候选优化变量和报告输出；ML surrogate / optimizer 只能作为候选建议层，不能替代 HYSYS runtime 或人工审核。

## 三条可发布的主线

### 1. 官方主线：HYSYS 本来就不是只做静态算例

[official/aspen-hysys-product-page.html](../official/aspen-hysys-product-page.html) 显示：

- HYSYS 覆盖 steady-state
- HYSYS 覆盖 dynamic studies
- HYSYS 明确挂着 process safety
- HYSYS 页面公开使用了 AI / optimization / workflow 叙事

这意味着 AI-HYSYS-Skill 可以把自己定位为：

- 可接管工程工作流的 HYSYS AI skill

而不是：

- 只会改几个变量的小脚本

### 2. 桥接主线：Spreadsheet / Workbook 是合法接口层

[official/aspen-simulation-workbook-product-page.html](../official/aspen-simulation-workbook-product-page.html) 和 [community/Aspen_HYSYS_Python-README.md](../community/Aspen_HYSYS_Python-README.md) 共同说明：

1. Aspen 官方支持把 simulation data 映射进 Excel/workbook
2. 社区实践也在用 spreadsheet 规避复杂对象路径
3. 所以 AI-HYSYS-Skill 最稳的宣传方式不是 “我完全绕开 HYSYS”，而是 “我用 HYSYS 原生能力和稳定桥接层协同工作”

### 3. AI 主线：最新研究已经开始直接生成 HYSYS 可执行脚本

[research/sketch2simulation-arxiv-2603.24629.pdf](../research/sketch2simulation-arxiv-2603.24629.pdf) 的关键价值不是要我们马上复刻整篇论文，而是它证明：

- Aspen HYSYS 已进入多智能体 LLM 自动建模研究视野
- 研究路线明确使用 Python automation script 去调用 Aspen HYSYS COM
- “AI 读图/读描述 -> 生成 HYSYS 脚本 -> 验证执行” 这件事已经不是空想

这会给 AI-HYSYS-Skill 一个很强的时代感。

[research/pinn-digital-twin-arxiv-2603.24644.pdf](../research/pinn-digital-twin-arxiv-2603.24644.pdf) 补充了另一条 AI-HYSYS 证据链：HYSYS 生成的动态过程数据可以训练物理约束神经网络数字孪生，用于实时软测量、预测控制和异常检测。这适合作为未来扩展方向，但不能用来宣称本仓库已经完成端到端动态孪生控制。

## 对技能设计的直接启发

### 1. 技能默认主通道必须是 direct COM

原因：

- 权威性最强
- 可做启动、开 case、保存、对象访问
- 最适合承接正式冻结、导出、审查支持

对应仓库实现：

- [`scripts/hysys_automation.py`](../../scripts/hysys_automation.py)

### 2. 技能必须内建 spreadsheet/workbook 备选通道

原因：

- HYSYS 变量路径可能很深
- 命名好的 spreadsheet 更利于人机共用
- 更适合快速搭 AI 参数面板或受控 dashboard

### 3. 技能必须强调“可审计导出链”

这是 AI-DWSIM-Skill 成功的重要原因之一：

- 不是只给建议
- 而是要求留下 workcopy、日志、导出表、状态说明

AI-HYSYS-Skill 也必须延续这条思路。

## 对发布打法的直接启发

### 1. 先讲执行通道，不先讲大而空的 AI 口号

用户最容易相信的不是：

- “AI 很聪明”

而是：

- “这个技能知道什么时候用 direct COM，什么时候用 spreadsheet bridge，什么时候只能退回 GUI”

### 2. 先给公开证据，再给宏大愿景

最有效的证据链应是：

1. Aspen 官方产品页
2. Aspen 官方支持页
3. 公开社区桥接代码
4. 最新 AI 研究论文
5. 你自己的本地可运行包装层

### 3. README 要同时服务两类人

1. 想直接装 skill 的 AI 用户
2. 想判断这仓库是否可信的工艺工程师

所以 README 既要有安装指引，也要有控制通道选择逻辑和 CASE 资料入口。

## 不应走的误区

- 不要把 AI-HYSYS-Skill 写成纯理论调研仓库
- 不要只讲 GPT 或 agent，而不讲 HYSYS 的真实控制通道
- 不要把 spreadsheet bridge 吹成唯一真源
- 不要在没有 CASE 证据包时就宣称“全网首个”

## 推荐下一步

发布前重点检查：

1. README 首屏是否一眼讲清 direct COM + spreadsheet bridge + CASE 资料包
2. `SKILL.md` 是否真的可触发并指导 Codex 做事
3. `CASE/source-index.md` 是否能让访客快速看到官方证据
4. 是否准备了 2 到 3 个真实演示任务或截图

## 2026-07-01 换热器 AI/HYSYS 结论

新增 [heat-exchanger-ai-control-patterns-2026-07-01.md](heat-exchanger-ai-control-patterns-2026-07-01.md) 和 [references/heat-exchanger-ai-patterns.md](../../references/heat-exchanger-ai-patterns.md)。本轮结论是：换热器、HEN、Aspen EDR、`Delta Tmin`、LNG 冷箱和低温换热器任务可以纳入 AI-HYSYS-Skill，但必须表述为“已有 HYSYS/EDR case 的候选优化、回算验证和报告支持”。ML、灰箱、GA、BO、PSO 等算法只负责提出候选条件，最终接受必须依赖 HYSYS/EDR workcopy 回算、KPI 导出、失败样本记录和人工验收。不得宣称 AI 已能可靠从零生成 HYSYS 换热器模型，也不得把外部预测或 Excel-only 计算说成 HYSYS-native 结果。

## 2026-07-03 MCP / wrapper / text-to-flowsheet 结论

新增 [heartbeat-scan-2026-07-03.md](heartbeat-scan-2026-07-03.md)。本轮检索没有改变项目主边界，但补强三类证据：`aspen-pysys` 0.1.0a3 是 HYSYS Python wrapper 候选，因 alpha、GPL-3.0-or-later、Python/pywin32 要求高且未本地验证，不能作为默认依赖；`gsi-lab/APS-Agent` 是 AVEVA Process Simulation 的 MCP 相邻实现，只能用于学习 tool schema、read-only-first、single-workcopy lock、audit log 和 rollback 设计，不能当成 HYSYS API；RSC/Zenodo `Text-to-flowsheet` 是 Graph-IR 和黑箱优化相邻证据，只能支持“候选意图 -> 显式中间表示 -> simulator 回算 -> 人工验收”的规则，不支持宣称 HYSYS 从零建模已可靠。

## 2026-07-04 HYSYS-specific MCP server 结论

新增 [heartbeat-scan-2026-07-04.md](heartbeat-scan-2026-07-04.md)。`yuuyo-arobet/AspenHYSYS-MCP-Server` 是当前 CASE 中更直接的 HYSYS MCP 社区证据：它明确以 Windows Python、pywin32 和 HYSYS COM 为执行层，README 声称提供 51 个工具、`HYSYS_MCP_MODE` 安全模式门、默认不公开写入工具，并有 HYSYS V14 实机验证记录。项目应吸收它的架构经验：MCP 适合作为 COM / spreadsheet / workbook lane 上方的工具编排层，必须坚持 read-only-first、mode gate、dry-run、single-workcopy lock、audit log、失败回滚和人工验收。它不能成为默认依赖，因为这是第三方社区仓库、公开采用信号很低，且本仓库没有对它做本地 HYSYS runtime smoke test。

## 2026-07-05 HYSYS coding-platform / wrapper 结论

新增 [heartbeat-scan-2026-07-05.md](heartbeat-scan-2026-07-05.md)。`Anikesh31/simulator_codingplatform_integration` 补强了已入库 2025 Computers & Chemical Engineering 论文的公开代码侧证据，适合学习 HYSYS 对象读取、backdoor variables、方法参数检查、Python/MATLAB 连接和 TEA 示例；`DanielVazVaz/PySIS` 补强了 HYSYS COM 抽象层的社区 wrapper 证据，README 声称覆盖 HYSYS V11/V12/V14。两者都不作为默认依赖：GitHub API 未识别许可证，本仓库未做本地 HYSYS runtime smoke test，且外部 wrapper 不能替代 direct COM / spreadsheet / workbook lane 的可审计控制规则。

## 2026-07-06 `ap-python` wrapper 结论

新增 [heartbeat-scan-2026-07-06.md](heartbeat-scan-2026-07-06.md)。`bsha0/ap-python` 是 MIT 许可的 Aspen Plus / Aspen HYSYS Python automation package，README 展示了 HYSYS moniker、`find_node`、`get_units`、`get_value`、`set_value`、`save` 和 `saveas` 包装模式。它补强了“变量 moniker + 单位感知 get/set wrapper”是公开存在的 HYSYS 自动化模式，但仓库较老、采用信号有限且本仓库未做 runtime smoke test，因此只进入 wrapper watchlist，不作为默认依赖。本轮还核对了 2026 LNG cold energy GA 论文；因原文未包含明确 Aspen/HYSYS 证据，未作为 HYSYS source pack 资料入库。

## 2026-07-07 HYSYS automation / LLM-agent 期刊元数据结论

新增 [heartbeat-scan-2026-07-07.md](heartbeat-scan-2026-07-07.md)。`Automation in the simulation of processes with Aspen HYSYS: An academic approach` 的 Crossref 元数据确认，HYSYS 自动化本身已经是可发表、可教学、可结构化的工程教育主题；这补强了本项目把 Excel/VBA/spreadsheet bridge 视为合法稳定 IO 层的依据。项目规则不变：direct COM 或 proven project runner 仍是 case 生命周期主通道，Excel/VBA/spreadsheet 更适合作为变量面板和批量 IO 桥，所有写入都必须落在 workcopy、solver policy、schema、日志和人工验收框架内。

`Large language model agent for user-friendly chemical process simulations` 的 Crossref 元数据确认了 Digital Chemical Engineering 期刊版 DOI `10.1016/j.dche.2026.100312`。它继续支持 MCP / tool server / step-by-step simulator-agent 架构，但仍属于相邻流程模拟证据，不是 HYSYS 专属 API，也不支持把 AI 从零建模写成生产默认能力。

## 2026-07-10 PSE/LLM 综述结论

新增 [heartbeat-scan-2026-07-10.md](heartbeat-scan-2026-07-10.md)。`Large Language Models in Process Systems Engineering: Opportunities, Architectures, and Industrial Deployment Challenges` 是一篇 2026-06-10 提交的 PSE/LLM 综述，覆盖 process modeling and simulation、optimization and scheduling、process control、fault detection and diagnosis 等方向。它对本项目最有用的不是扩大能力边界，而是强化边界：LLM 对文档查询、非结构化知识综合、人机交互和报告解释有明确价值；但实时执行、约束满足和形式化安全保证仍然困难。因此 AI-HYSYS-Skill 继续保持“已有 HYSYS case 接管 + 脚本化验证 + 人工验收”的定位，不把广义 PSE 综述解读为 HYSYS 生产级从零建模已经可靠。

## 2026-07-12 OTS / HYSYS Dynamics fertilizer evidence conclusion

New note: [heartbeat-scan-2026-07-12.md](heartbeat-scan-2026-07-12.md). The useful new signal is not a new AI-control paper; it is industry evidence that Aspen HYSYS Dynamics and HYSYS-based OTS are being used in OPTIMIZE 26 operating contexts, including ammonia/urea facilities and first-principles urea-plant operator training.

Project conclusion: this strengthens AI-HYSYS-Skill for existing HYSYS Dynamics case takeover, OTS scenario documentation, DCS/SIS loop mapping review, KPI export, and training/reporting support. It does not change the core boundary: embedded DCS/SIS logic inside a simulator is training and validation evidence, not authorization for production writeback or autonomous AI control. For ammonia/urea or `NH3-CO2-H2O` dynamic tasks, the skill should require the property-package basis, dynamic case provenance, scenario list, failure behavior, and human acceptance before any engineering conclusion.

## 2026-07-13 Aspen Operator Training official evidence conclusion

New note: [heartbeat-scan-2026-07-13.md](heartbeat-scan-2026-07-13.md). The useful new source is AspenTech's official Aspen Operator Training product page and its linked OTS FAQ PDF. This upgrades the 2026-07-12 Inprocess / OPTIMIZE 26 evidence with official AspenTech product-level support for DCS-agnostic OTS, dynamic simulation, Inprocess OTS software, and Aspen HYSYS Dynamic Lifecycle.

Project conclusion: AI-HYSYS-Skill can support OTS-adjacent engineering work by organizing existing HYSYS Dynamics cases, scenario lists, tag/KPI schemas, DCS/SIS loop mapping evidence, replay/audit logs, and operator-training reports. It must not claim to replace commercial OTS platforms, HYSYS Dynamics model-build expertise, DCS/SIS engineering, production writeback approval, or from-scratch HYSYS model generation.

## 2026-07-14 HYSYS distillation ANN surrogate conclusion

New note: [heartbeat-scan-2026-07-14.md](heartbeat-scan-2026-07-14.md). The new B- source is a July 2026 peer-reviewed paper that uses Aspen HYSYS data to train a 3:4:1 ANN for a benzene-toluene distillation mass-transfer coefficient. It provides a concrete, narrow example of the `HYSYS baseline -> bounded dataset -> surrogate` pattern, but reports only training performance and does not provide a clear independent test split, reusable code/data, uncertainty bounds, or extrapolation evidence.

Project conclusion: surrogate and soft-sensor work must preserve HYSYS case provenance, property-package basis, variable units, design-space bounds, sample IDs, train/validation/test separation, unseen-sample metrics, failed-sample logs, extrapolation limits, HYSYS readback, and human acceptance. This source does not justify production control, replacement of the HYSYS baseline, or transfer of the model to unrelated columns.
