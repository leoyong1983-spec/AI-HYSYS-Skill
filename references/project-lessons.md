# 项目经验沉淀

以下规则来自当前仓库内外已经验证过的 HYSYS 控制路径，而不是纸面建议。

## 1. 先接管环境，再谈建模

第一关必须是：

- Aspen HYSYS 安装与版本
- `HYSYS.Application` 是否可启动
- case 能否 `open / save / reopen`
- 输出目录是否可写
- 若采用 spreadsheet / workbook，绑定是否能读到命名对象

这关没过，不进入 case 层。

## 2. 最稳的主通道是 `direct COM + orchestration`

当前仓库自带的 [`scripts/hysys_automation.py`](../scripts/hysys_automation.py) 已经表明：

- direct COM 可以做启动、开 case、少量对象操作、保存、关闭
- 这条路最适合作为权威执行主通道
- `Python / PowerShell` 更适合做外层 orchestration，而不是替代 HYSYS 本体

这里要特别区分：

- `能创建最小 case 或最小对象`
- 和
- `能从零稳定搭出生产可用的复杂 HYSYS 工艺模型`

前者可以成立，后者当前不应当作为默认承诺。

## 3. spreadsheet bridge 适合做稳定 IO，不适合取代主真源

社区示例 [`CASE/community/HYSYS_python_spreadsheets.py`](../CASE/community/HYSYS_python_spreadsheets.py) 的最大启发不是“怎么写 COM”，而是：

1. 当对象路径复杂时，spreadsheet 是稳定桥
2. 当多人要消费同一批变量时，spreadsheet / workbook 比深层对象路径更可读
3. 但它仍应服务于 case，而不是替代 case

## 4. 必须区分四类失败

至少要分开记录：

- HYSYS 启动失败
- case 打开失败
- 对象绑定失败
- solver 失败

否则后续会误判问题层级。

## 5. 求解器节奏必须受控

如果通过 spreadsheet / object path 批量改值：

1. 先考虑暂停 solver
2. 成批写入
3. 再恢复 solver
4. 等待 `IsSolving` 结束

不要边写边盲读结果。

当前 [`scripts/hysys_automation.py`](../scripts/hysys_automation.py) 已把这条经验落成 helper：

- `SpreadsheetCellBinding` 用于记录 spreadsheet、行列、标签和单位
- `batch_write_spreadsheet_cells(...)` 用于暂停 solver、批量写入、恢复 solver、等待求解结束
- `wait_for_solver_idle(...)` 用于避免读到中间状态

这不是替代工程判断，而是把社区示例和论文中的 solver 节奏固化成默认安全动作。

## 6. workcopy 要优先于母版

排序依据应该是：

1. frozen baseline
2. 最新 loadable audited workcopy
3. 最新 loadable mother case
4. 没有可用 case 时，最多只做最小实验模板用于 smoke test 或接口验证

不要直接在 accepted baseline 上执行可写变更。

也不要把最小实验模板误当成真实工程基线。

## 7. 非 ASCII 路径要提前处理

当前 direct COM 包装层已经显式处理了：

- `.hsc` 非 ASCII 路径 staging
- `TEMP/TMP` 目录固定化

这说明路径编码不是小问题，而是必须在技能规则里写死的环境门槛。

## 8. 调优必须分层推进

推荐顺序：

1. 先证明 case 能开、能算、能保存
2. 再做单变量或单变量族的 bounded tuning
3. 再做导出与审查支持

禁止在 control lane 还没稳定时就直接做多参数乱扫。

## 8.1 你的当前项目经验需要写死

结合你在本地沉淀的“AI辅助人类已建 HYSYS 模型”和 “AI一键调配 LNG 液化 HYSYS 模型”三份操作文档，以及当前仓库的 `CASE/notes/` 材料：

当前更可靠的结论应写成：

1. AI 接管人类已建且可运行的 HYSYS 模型，替换参数、边界、规模并重算，这条路是合适的
2. AI 从零新建复杂 HYSYS LNG 工艺模型，这条路当前不稳，不应当作为默认执行口径
3. 所以默认流程应是：读取已有模型 -> 识别控制归属 -> 替换边界 -> 阶梯调产 -> 导出结果

## 9. 动态 case 要单列说明

官方 HYSYS 产品定位明确包含 dynamic studies，但这不代表：

- steady-state 与 dynamic case 可以混当同一真源
- 同一套导出能直接跨两种 case 使用

如果用户要做动态分析或 OTS 支撑，必须单独写清：

1. 当前控制对象是哪一个 case
2. 当前导出属于 steady-state 还是 dynamic
3. 是否允许回写到 review-stage baseline

## 10. 每次自动运行都要留下机器可审计件

至少包括：

- `case_summary.json`
- `key_streams.csv`
- `key_operations.csv`
- `assumptions.md`
- `open_issues.md`
- `run_status.md`

不要把“成功”只留在聊天里。

## 11. AI 研究可以当增强路线，但不能压过工程主通道

[Sketch2Simulation](../CASE/research/sketch2simulation-arxiv-2603.24629.pdf) 这类研究说明：

- 多智能体 + LLM + Python COM 脚本生成，已经开始进入 Aspen HYSYS 可执行建模
- 这对 AI-HYSYS-Skill 的叙事很有价值

但默认主路径仍应是：

- 先有可控、可审计、可验证的 direct COM / bridge lane
- 再谈更激进的 diagram-to-simulation 自动化

## 12. 新论文带来的项目化改进

第二轮心跳测试新增的 2022/2025 资料带来三个必须进入项目规则的点：

1. HYSYS interconnection 不止 direct COM 和 spreadsheet，还包括 indirect communication 与 data tables；它们应进入 fallback 体系。
2. Python-HYSYS 自动化会遇到特殊对象和 backdoor variables；因此写入前必须先做 lane decision 和单点 smoke test。
3. 控制通道选择应写成可复用矩阵，而不是散落在 README 里的口号。

对应落地文件：

- [control-lane-decision-matrix.md](control-lane-decision-matrix.md)
- [`scripts/hysys_automation.py`](../scripts/hysys_automation.py)
