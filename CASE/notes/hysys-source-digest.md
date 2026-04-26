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
