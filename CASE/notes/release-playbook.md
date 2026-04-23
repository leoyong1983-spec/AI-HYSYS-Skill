# AI-HYSYS-Skill 发布打法

## 目标

借鉴 AI-DWSIM-Skill 已经验证过的成功思路，把 AI-HYSYS-Skill 发布成一个同时具备：

- 明确定位
- 清晰证据
- 可安装 skill
- 可复用资料包
- GitHub 开源卫生

的仓库。

## 为什么 AI-DWSIM-Skill 那套思路有效

AI-DWSIM-Skill 成功的关键，不是“资料很多”，而是四件事同时成立：

1. 有清楚的 authoritative control lane
2. 有可执行的 `SKILL.md`
3. 有 GitHub 开源仓库该有的 README / AGENTS / CI / Issue 模板
4. 有一条可讲清楚的价值链：环境接管 -> 建模/调优 -> 导出 -> 基础工艺包

AI-HYSYS-Skill 也应该保持这四件事。

## AI-HYSYS-Skill 的推荐定位

### 一句话定位

`AI-HYSYS-Skill is an auditable, script-first Aspen HYSYS takeover kit that combines direct COM control, spreadsheet/workbook bridges, and source-backed process package delivery.`

### 中文版定位

`AI-HYSYS-Skill 是一个可审计、脚本优先的 Aspen HYSYS 接管工具包：用 direct COM 做主执行层，用 spreadsheet/workbook 做稳定桥接层，并把计算结果落成可交付的基础工艺包输出。`

## README 首页建议强调的三点

### 1. 不是空泛 AI，而是真正的控制通道选择

首屏就讲：

- project-local runner
- direct COM / `HYSYS.Application`
- spreadsheet / workbook bridge
- GUI last

### 2. 不是孤证，而是 CASE 证据包

首屏就给：

- 官方 Aspen 页面
- 官方支持文章页
- 社区 bridge 代码
- 最新 AI 论文

### 3. 不是只会聊天，而是会留下 artifacts

首屏就给：

- `case_summary.json`
- `key_streams.csv`
- `key_operations.csv`
- `utility_summary.csv`
- `assumptions.md`
- `run_status.md`

## 适合公开展示的 3 个 demo

### Demo 1: 环境与控制通道判定

主题：

- 让 AI 判断本机是 direct COM 更稳，还是 spreadsheet bridge 更稳

价值：

- 这是最容易让人瞬间理解 skill 价值的入口 demo

### Demo 2: 打开现有 HYSYS case 并导出关键表

主题：

- 读 case、跑一遍、导出关键流股和设备表

价值：

- 这能证明 AI 不只是会写说明，而是真的在接管 HYSYS 工作流

### Demo 3: 冻结基线并生成 review-stage 资料

主题：

- workcopy、freeze、export、review support

价值：

- 这会把仓库从 “自动化脚本库” 提升到 “工艺包交付工具包”

## GitHub 发布时的具体动作

1. 仓库 About 按 [../../GITHUB_REPO_SETTINGS.md](../../GITHUB_REPO_SETTINGS.md) 填好。
2. README 首屏保留 badges、控制通道、CASE 入口。
3. 仓库里保留 `CASE/`，不要删。
4. 至少上传一次 README 截图或 demo 结果到 issue / discussion / release 说明里。
5. 首发时优先讲 “AI 控制 HYSYS 的可执行路径”，不要先把范围吹到“自动完成所有化工设计”。

## 首发文案方向

### 英文短文案

`AI-HYSYS-Skill helps AI agents take over Aspen HYSYS with auditable COM automation, spreadsheet/workbook bridges, bounded tuning rules, and process-package-ready exports.`

### 中文短文案

`AI-HYSYS-Skill 不是教 AI 去乱点 HYSYS，而是给 AI 一条可审计的接管路径：什么时候走 direct COM，什么时候走 spreadsheet/workbook bridge，什么时候只能退回人工可视检查。`

## 首发时不要做的事

- 不要声称已经覆盖所有 HYSYS 场景
- 不要把 community bridge 说成官方 API 文档
- 不要把匿名抓不到的 Aspen 附件伪装成 PDF 上传
- 不要只有宏大愿景，没有本地可运行脚本或 CASE 证据
