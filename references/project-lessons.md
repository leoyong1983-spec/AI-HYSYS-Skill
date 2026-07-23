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
- `read_spreadsheet_cells(...)` 用于按 binding label 批量读回机器可消费的 KPI 字典
- `batch_write_spreadsheet_cells(...)` 用于暂停 solver、批量写入、恢复 solver、等待求解结束
- `wait_for_solver_idle(...)` 用于避免读到中间状态

这不是替代工程判断，而是把社区示例和论文中的 solver 节奏固化成默认安全动作。

第三方 wrapper 候选 `aspen_pysys` 的可借鉴点是“把 COM 边界显式包装”，不是把 alpha / GPL 包变成默认依赖。因此当前仓库只吸收两类安全设计：会话内对象缓存，以及 spreadsheet readback 后的 COM 值标准化。不要跨进程共享 HYSYS COM 句柄；多工况并发应使用独立 workcopy、独立进程和明确的启动/关闭边界。

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

## 13. 原生 PFD 整理必须设备优先并做计算指纹回归

真实 V15 case 的布局整理表明，PFD 不是普通二维画布：流股、能量流、标签和设备之间存在吸附及反向牵引。稳定做法是：

1. 从验证基线复制 layout workcopy，冻结 solver 后再写 PFD。
2. 按正式 PFD 的工艺阅读顺序先定位全部非流股对象；并联机组分泳道，回流在上、液相回罐在下，检查表移出主线。
3. 流股只执行 `AutoPosition()`，不要给所有流股逐一写绝对坐标。
4. 设备使用 `PFD.MoveBy((item,), dx, dy)`，并在流股、标签处理后再次正向/反向定位；短连接对用显式优先顺序收口。
5. `PFD.Centre()` 不等于 GUI `ZoomToFit`；最终人工打开后用 `Home` 做 Fit to Window。
6. 保存后关闭重开，比较对象清单、物料流、能量流、recycle、solver 和目标坐标；任何计算指纹变化都视为布局失败。

详细 COM 行为、配置格式和验收条件见 [pfd-layout-workflow.md](pfd-layout-workflow.md)，可执行入口见 [`scripts/hysys_pfd_layout.py`](../scripts/hysys_pfd_layout.py)。

## 14. Recycle 收敛不能只看一个状态码

经脱敏的本地 HYSYS V15 direct COM 运行证据表明，复杂 case 中的 recycle 状态字段可能不能单独表达工程上需要的闭合质量。默认验收应组合检查：

1. solver 已结束且允许继续求解；
2. recycle 未被意外设为 `Ignored`；
3. feed/product 对象仍绑定到预期流股；
4. 质量、温度、压力、焓和组成等项目批准的 tear-stream 残差满足容差；
5. 关键物料衡算、能量衡算和对象数量没有漂移；
6. 保存、关闭、重开后再次读取，全部检查仍然通过。

如果某个 COM 状态值为空、未定义或语义不清，应把它记录为诊断信息，而不是自行解释为“已收敛”。残差验收规则及容差必须来自项目边界或工程师批准。

## 15. 计算完成与成果可发布是两个状态

一次自动运行可能已经得到可复核的 staged case，但随后在策略、导出或最终封装阶段报错。此时不得删除错误后直接把结果改成 `PASS`。更稳妥的处理是：

1. 保留原始错误、traceback 和失败阶段；
2. 不覆盖母版，独立重开 staged workcopy；
3. 重新执行对象绑定、solver、残差、KPI 和关闭重开验证；
4. 核对母版哈希没有变化；
5. 在独立 finalization 记录中保留 previous errors；
6. 只有复核全部通过后，才复制或提升经过验证的成果文件。

这样可以区分“仿真结果本身有效”和“自动化流水线完整成功”，避免通过清空错误字段制造假成功。

## 16. 所有压力写入都必须显式处理表压与绝压

经脱敏的本地 HYSYS V15 direct COM 脚本和结构化回读表明，外部计算书常使用表压，而 HYSYS 流股压力写入和回读应明确按绝压处理。稳定流程是：

1. 在输入 schema 中分别保存原始压力值、`gauge/absolute` 基准和工程单位；
2. 表压转绝压时记录采用的大气压，不把换算常数隐藏在脚本中；
3. 向 HYSYS 写入带显式绝压单位的值，并在 solver 结束后从同一控制对象回读；
4. 输出同时保留原始表压、换算绝压、HYSYS 回读绝压和允许偏差；
5. 如果控制归属不清、回读不一致或 COM/RPC 会话失败，不得保存为已接受成果，也不得把设备名称中的压力数字当成真实压力基准。

该规则已由本地性质计算、压缩计算和独立 JSON 回读证据支持。一次设备对象写入后的 RPC 失败只作为失败样本保留，不能据此宣称设备级自动恢复或替代控制路径已经验证。

## 17. 外部估算与 HYSYS 回读不一致时不得强行对表

经脱敏的本地 HYSYS V15 工况派生脚本、原生 case 和保存关闭重开回读表明，从已有验证模型派生新工况时，外部工作簿、线性估算或经验比例结果可能与 HYSYS 严格计算存在偏差。此时应：

1. 保留外部估算值、HYSYS 回读值、绝对偏差、相对偏差和各自计算基准；
2. 确认物性包、边界、流股定义、循环结构、单位和设备效率是否一致；
3. 在差异原因和允许偏差由工程师确认前，把该项保留为 open issue；
4. 不为匹配工作簿而反向篡改已收敛的 HYSYS 结果，也不静默用 HYSYS 数值覆盖原估算；
5. 每个派生工况都从同一获批母版哈希或冻结基线开始，使用独立 workcopy，禁止把前一个工况串联为下一个工况的起点；
6. 每个工况保留独立的 `RUNNING / PASS / ERROR` 审计记录、输出目录和最后成功阶段；只有保存、关闭、重开并复核通过的工况才能晋级为交付候选；
7. 批量任务中单个工况失败时，保留其错误与中间证据，但不得污染其他工况；恢复执行时应核对母版哈希，只复用已经重开验证通过的成果，其余工况从获批基线重新运行。

该规则已有多个本地派生工况的真实 HYSYS 保存重开、逐工况审计和结构化回读支持，可标记为本地验证；它证明的是“已有 case 的受控派生、批量恢复与差异治理”，不是从零建模能力。

## 18. 已有 case 内重建子系统时必须冻结未改动侧

经脱敏的本地 HYSYS 脚本、原生 case、结构化检查点和保存关闭重开回读表明，在已有模型内替换或重建一个获批子系统时，不能只检查新子系统是否收敛。稳定流程是：

1. 操作前记录母版哈希，并复制临时 workcopy，禁止直接覆盖源 case；
2. 冻结未改动侧的物料流、能量流、对象清单和 solver 指纹，明确允许变化的拓扑边界；
3. 需要蒸发或冷凝等热力压力边界时，优先使用临时 HYSYS 性质或饱和探针计算，并记录组成、温度、汽相分率和单位，不使用来源不明的硬编码常数；
4. 仅在批准边界内重建拓扑和有限调参，失败运行及其 solver 状态继续保留；
5. 保存、关闭并重开 workcopy 后，重新读取新子系统和未改动侧，核对母版哈希未变且未改动侧指纹没有漂移；
6. 设备选型、厂家确认和项目专属验收项仍保持为人工 open issue，不因仿真收敛而自动关闭。

该规则已有真实 HYSYS 执行、保存重开和机器可读回读证据，可标记为本地验证。它适用于“已有可运行 case 内的受控子系统重建”，不支持宣称从零生成完整 HYSYS 模型已经可靠。

## 2026-06-02 Text-To-Flowsheet And MCP Lessons

Recent text-to-flowsheet and process-simulation-agent papers add useful engineering patterns, but they do not change this repository's default execution boundary.

1. Use Graph-IR before simulator writes. For text-to-flowsheet, diagram-to-simulation, or sketch-to-simulation tasks, keep a normalized intermediate representation of topology, variables, units, and uncertain parameters before any HYSYS write. This makes AI intent reviewable before COM or workbook execution.
2. Treat black-box optimization as local convergence assistance. Optimizers may help tune uncertain parameters, but only on approved workcopies, approved variables, documented bounds, logged residual objectives, and final HYSYS readback.
3. Treat MCP as a tool-contract layer. MCP can make tools cleaner for agents, but it still has to wrap direct COM, spreadsheet/workbook, data table, or proven runner lanes with locks, schemas, audit logs, and rollback.

Do not add SciPy, an MCP server, or a third-party HYSYS wrapper as a default dependency until a real project runner proves runtime value, license compatibility, and recovery behavior.
