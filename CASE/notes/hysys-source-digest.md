# HYSYS 资料摘要

## 一句话结论

AI-HYSYS-Skill 最有说服力的定位，不是“AI 会点 HYSYS”，而是：

`AI 可以沿着 Aspen 官方承认的工作流，使用 direct COM 作为主执行层、spreadsheet/workbook 作为稳定桥接层，在可审计边界内接管 Aspen HYSYS。`

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
