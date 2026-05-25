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

2026-05-13 自动心跳补强 online deployment 与 first-principles baseline 边界：[official/aspen-online-product-page-2026.html](../official/aspen-online-product-page-2026.html) 明确 Aspen OnLine 使用 live data matched with process simulation，并可在 Aspen Plus / Aspen HYSYS simulation environment 中生成用 plant historian 或 lab data 校验的项目文件；[research/first-principles-modeling-age-ai-tudelft-2026.html](../research/first-principles-modeling-age-ai-tudelft-2026.html) 记录 IECR 2026 综述，强调 AI 时代第一性原理建模仍有核心作用。项目结论是：AI-HYSYS-Skill 可以帮助准备 online/historian/KPI/schema/审计材料，但不能复刻 Aspen OnLine，也不能让 AI、hybrid model 或 surrogate 替代 HYSYS 机理基线和人工工程审核。

2026-05-17 自动心跳补强 AspenTech AVA / Industrial AI 边界：[official/aspentech-industrial-ai-ava-2026.html](../official/aspentech-industrial-ai-ava-2026.html)、[official/emerson-aspentech-ava-launch-2026-05-snapshot.md](../official/emerson-aspentech-ava-launch-2026-05-snapshot.md) 和 [official/emerson-aspentech-optimize26-ai-hybrid-modeling-2026-05-snapshot.md](../official/emerson-aspentech-optimize26-ai-hybrid-modeling-2026-05-snapshot.md) 说明 Emerson/AspenTech 正在把 AVA、Industrial AI、first-principles context、数据平台、LLM-style assistance、process digital twins 和 hybrid modeling 放到同一运营工作流叙事中。项目结论是：AI-HYSYS-Skill 可以准备既有 HYSYS case、变量/KPI schema、验证记录和审计报告，但不能声称复刻 AVA、Aspen OnLine、AI Model Builder、DMC/APC/PIMS 或生产运营 AI 平台。`aspen-pysys` 仅保存为社区候选线索，因为扫描时没有可用 release。

2026-05-18 自动心跳新增 Emerson / Aramco Aspen Hybrid Models 炼厂计划优化官方证据：[official/emerson-aramco-aspen-hybrid-models-refinery-planning-2026-04-snapshot.md](../official/emerson-aramco-aspen-hybrid-models-refinery-planning-2026-04-snapshot.md) 说明 Aspen Hybrid Models 可接入既有炼厂计划框架，并基于严谨第一性原理仿真案例和实际工厂数据校准，用于多站点、多周期炼厂计划优化。项目结论是：这强化了 AI-HYSYS-Skill 对 production planning、PIMS、hybrid AI、surrogate planning 和人类验收边界的处理方式；本 skill 仍应输出候选情景、KPI 表、验证证据和审计记录，不能替代 Aspen Hybrid Models、商业计划优化器、APC/DCS/PIMS 或生产闭环决策。

2026-05-19 自动心跳新增 AspenTech AI / AVA portfolio 证据：[official/aspentech-ai-ava-portfolio-2026-05-snapshot.md](../official/aspentech-ai-ava-portfolio-2026-05-snapshot.md) 说明 AspenTech 正在把 AVA、Industrial AI、HYSYS/HYSYS Dynamics、Hybrid Models、Aspen OnLine、Unified PIMS、DMC3、GDOT、Mtell 和 sustainability planning 放进同一企业级工业决策叙事。项目结论是：AI-HYSYS-Skill 可以承接 AVA-style 任务的前置整理、变量/KPI schema、候选情景、验证记录和审计输出，但必须把 AVA、PIMS、APC/DMC、GDOT、online deployment 和生产闭环控制视为外部商业系统边界。

2026-05-20 自动心跳新增 AspenTech 官方平台支持证据：[official/aspentech-platform-support-2026-05.html](../official/aspentech-platform-support-2026-05.html) 和 [official/aspentech-v15-engineering-platform-specifications-2026.pdf](../official/aspentech-v15-engineering-platform-specifications-2026.pdf) 说明 HYSYS 自动化任务必须先区分 Aspen 运行环境、Windows/Office/Python 前提、COM 注册、产品版本和外部商业套件边界。项目结论是：readiness/version migration 任务不能只看 Python 脚本是否能跑，还要把平台不兼容、未安装组件、无授权组件和本 skill 的逻辑错误分开报告。

2026-05-22 自动心跳更新 `aspen_pysys` 社区候选状态：[community/aspen-pysys-pypi-json-2026-05-22.json](../community/aspen-pysys-pypi-json-2026-05-22.json) 和 [community/aspen-pysys-codeberg-page-2026-05-22.html](../community/aspen-pysys-codeberg-page-2026-05-22.html) 说明该包已经有 `0.1.0a0` alpha release、Codeberg 仓库、`pywin32>=311` 依赖和 `GPL-3.0-or-later` 许可。项目结论是：它值得作为第三方 wrapper 候选跟踪，但不能默认纳入 MIT skill，也不能替代本仓库内置 direct COM / spreadsheet bridge 工作流；使用前必须检查许可、Python 版本、HYSYS runtime、现有 case 和实际 API 行为。

2026-05-24 自动心跳新增 Eksergi CCS-EOR 技经敏感性论文：[research/hysys-ccs-eor-python-automation-eksergi-2026.pdf](../research/hysys-ccs-eor-python-automation-eksergi-2026.pdf) 和 [research/hysys-ccs-eor-python-automation-eksergi-2026.html](../research/hysys-ccs-eor-python-automation-eksergi-2026.html) 记录 Aspen HYSYS V14 自动化结合 Python，用 full-factorial 参数组合生成 162 个 CCS-EOR 场景。项目结论是：HYSYS + Python 自动化适合已有模型的批量场景、敏感性、技经 KPI 和报告导出；但必须先冻结变量 schema、样本编号、solver 策略、失败分类和人工复核，不能把批量优化直接等同于生产闭环写回。

2026-05-26 自动心跳新增 Viva Energy / Anukoolan 官方 webinar：[official/aspen-hysys-viva-energy-cdu-eo-hybrid-digital-twin-2026.html](../official/aspen-hysys-viva-energy-cdu-eo-hybrid-digital-twin-2026.html) 说明 Aspen HYSYS 可用 first-principles Equation Oriented models 和 Reduced Order Hybrid Models 建立 CDU、Prefractionation、Hydrotreater 数字孪生优化场景。项目结论是：这补强炼厂装置级 operational optimization / hybrid digital twin 证据，但本 skill 仍应限定为整理已有 HYSYS case、变量/KPI schema、候选工况、校验记录和审计报告，不能宣称自动复刻商业 hybrid digital twin 或生产闭环控制。

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
