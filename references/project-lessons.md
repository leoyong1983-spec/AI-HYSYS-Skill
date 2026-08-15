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

## 19. 新增陌生单元操作前先探测 COM 注册类型

经脱敏的本地 HYSYS V15 direct COM 脚本、逐候选错误记录和对象类型回读表明，界面显示名称不一定等于 `Flowsheet.Operations.Add(...)` 接受的注册类型标识。稳定流程是：

1. 只在一次性 workcopy 上探测，操作前冻结 solver，不覆盖母版或已接受成果；
2. 候选类型必须是有限、可审查的清单，禁止无限猜测或在正式 case 中反复试写；
3. 每次尝试记录候选标识、异常信息、返回对象类型和 `VisibleTypeName`；
4. 仅把真实创建且类型回读一致的标识带入获批变更边界，失败候选继续保留为诊断证据；
5. 探测成功只证明当前 HYSYS 运行环境能够发现该对象类型，不证明拓扑修改、参数设置、求解收敛或工程验收已经通过。

该规则有真实 HYSYS 执行和结构化回读支持，可标记为本地验证。它用于降低 COM 类型字符串猜测造成的失败风险，不扩大本技能“已有可运行 case 受控接管”的边界。

## 20. 相变边界和设备测点必须分开验证

经脱敏的本地 HYSYS V15 direct COM 脚本、分步求解历史、关闭重开结果和补充相态回读表明，温度要求必须先落实到明确的物理测点，不能把压缩机排气、后冷却器出口、冷凝器出口和饱和边界当成同一个控制点。稳定流程是：

1. 写入前记录目标对应的 HYSYS 对象、测点位置、预期相态、控制归属和允许变化边界；
2. 对跨越较大的温压或相变边界，从获批基线按有限步长渐进写入，每一步都等待 solver 空闲并保留目标值、回读值、失败状态和回退点；
3. 在相变附近同时回读温度、绝压、汽相分率，并在设备容量相关时回读实际体积流量；仅温度命中不足以证明气相排气、液体产品或设备工况成立；
4. 验收时同时比较功率、热负荷、流量、COP、质量/能量残差及公用工程需求，禁止只因单一能耗指标改善就接受方案；
5. 循环水循环量不得写成新鲜水补水量；换热面积、污垢、压降、管口、泵和厂家性能保证继续作为人工 open issue；
6. 最终 workcopy 仍须保存、关闭、重开并复核源文件哈希、对象数量、solver、相态和关键 KPI。

该规则已有真实 HYSYS 执行和机器可读回读支持，可标记为本地验证。它强化的是已有模型的边界敏感性和相态验收，不证明设备选型、详细换热设计或生产写回已经完成。

## 21. 批量工况矩阵必须与输出清单逐项对账

经脱敏的本地 HYSYS V15 批量派生脚本、逐工况审计记录、原生 case 和保存关闭重开回读表明，仅有“全部运行完成”的汇总状态不足以证明批量成果完整。稳定流程是：

1. 执行前冻结工况矩阵、唯一工况 ID 和预期成果数量，明确每个矩阵单元对应的输入边界与验收项；
2. 每个矩阵单元使用独立 workcopy、审计记录、源 case 哈希、输出 case 哈希和结果命名空间，禁止跨工况复用未验证的实时 COM 状态；
3. 汇总前核对矩阵与输出清单一一对应，拒绝缺失、重复、孤立或串工况污染的 case、审计记录和结果行；
4. 每个 case 都必须保存、关闭、重开，并重新核对对象清单、solver、相态、物料/能量闭合和项目批准的 KPI；
5. 聚合 CSV、JSON 或报告只能纳入逐项 `PASS` 的结果；失败单元保留原始错误并从获批基线独立重跑，不得用汇总成功掩盖单项失败。

该规则已有真实 HYSYS 执行、逐工况机器可读审计和原生 case 回读支持，可标记为本地验证。它证明的是“已有模型批量派生的完整性治理”，不证明从零建模、设备详细设计或生产写回已经完成。

## 22. 实际设备流股与记账流股必须先分类再改连接

经脱敏的本地 HYSYS V15 direct COM 执行脚本和交付说明表明，已有模型可能同时包含实际设备连接流股、边界输入流股、仅用于计算书对账的记账流股，以及 recycle/tear stream。若不先分类就直接改连接，容易产生重复计量、重复进料或非零孤立流股。稳妥流程是：

1. 修改前冻结源 case 哈希，并建立“流股名称、对象路径、上游设备、下游设备、物理或记账角色、是否允许非零”的映射表；
2. 对同一物料来源，禁止实际设备流股与其记账替代流股同时以非零流量进入同一衡算边界；
3. 只在独立 workcopy 上暂停 solver 后成组修改连接；只有批准边界明确时，才能删除或归零记账流股，且不得误删真实边界流、recycle 或 tear stream；
4. 恢复 solver 后检查设备 feed/product 绑定、重复进料、非零孤立流股、对象清单以及项目批准的物料和能量闭合；
5. 保存、关闭、重开后重复拓扑和衡算回读，只有全部通过的 workcopy 才能晋级。

本轮监测目录包含执行脚本和交付说明，但未包含配套机器可读审计回读，因此本条作为高可信、低风险的工作流防护规则采纳，暂不标记为“本地运行验证”。它不证明新增拓扑已经通过工程审查，也不扩大从零建模或生产写回边界。

## 23. 外部边界基准变化时必须按依赖关系最小改参

经脱敏的本地 HYSYS V15 direct COM 脚本、原生 case、机器可读审计以及保存关闭重开回读表明，环境、季节或外部计算基准变化时，不应按比例重调整个模型。稳定流程是：

1. 冻结源 case 哈希并建立独立 workcopy，记录旧基准、新基准、来源、单位和获批目标；
2. 建立“外部基准 -> 受影响 HYSYS 对象和属性”的依赖表，明确受影响输入、独立贡献项和必须冻结的既有边界；
3. 暂停 solver 后只写入依赖表内的变量，禁止为强行命中目标而联动调整无关流股、设备或已接受贡献项；
4. 恢复求解并等待 solver 空闲，回读目标对象，同时检查受影响边界的物料衡算、能量衡算、相态、recycle 闭合和关键 KPI；
5. 审计记录必须同时列出已修改项和有意保持不变的项，并保留写入前后值、单位、对象路径、求解状态以及源文件和输出文件哈希；
6. 保存、关闭、重开后复核对象数量、solver 状态、衡算、关键 KPI 和冻结输入，只有全部保持一致的 workcopy 才能晋级；
7. 外部基准是否适用于项目以及最终工程验收仍由工程师确认，HYSYS 收敛不能替代基准来源审查。

该规则有真实 HYSYS V15 direct COM、原生 case、机器可读审计和保存重开回读支持，可标记为本地验证。它证明的是已有 case 的受控边界更新，不证明外部基准本身已获工程批准，也不扩大从零建模或生产写回边界。

## 24. 原生 XML 导出是审计通道，不是跨版本重建证明

经脱敏的本地 HYSYS V15 COM 批量执行、逐 case 日志、机器可读清单和源文件哈希复核表明，`SimulationCase.GetXMLForCase()` 可用于在不保存源 case 的情况下生成原生 XML 审计副本。稳定流程是：

1. 使用独立 HYSYS 自动化实例，按获批清单逐个打开源 case，不修改参数、不主动重算、不覆盖源文件；
2. 导出前后分别计算源 case SHA-256，任何变化都视为失败；
3. 使用 `GetXMLForCase()` 获取 XML，并以 UTF-8 写入独立交付目录；
4. 用禁止 DTD 和外部实体的标准 XML 解析器检查 XML 可解析、根元素符合预期，同时记录元素数量、文件大小、输出 SHA-256、HYSYS 版本和 solver 状态；
5. 单个 case 失败时删除不完整 XML，保留错误记录并继续按既定失败策略处理；结束后关闭 case 且不保存，释放 COM 对象并退出独立 HYSYS 实例；
6. 用唯一 case ID 对账源文件、XML 和审计记录，拒绝缺失、重复、孤立或哈希不一致的输出。

该流程已有真实 HYSYS V15 原生 case、COM 批量执行、机器可读审计和源文件哈希不变证据，可标记为本地验证。但“XML 可解析”只证明导出和结构完整性，不证明 XML 能在同版或跨版本 HYSYS 中无损重建原 case。任何导入、迁移或重建结论都必须在目标 HYSYS 环境另行执行官方应用或导入通道，并复核物性包、对象清单、连接关系、solver 状态和关键 KPI。

## 2026-06-02 Text-To-Flowsheet And MCP Lessons

Recent text-to-flowsheet and process-simulation-agent papers add useful engineering patterns, but they do not change this repository's default execution boundary.

1. Use Graph-IR before simulator writes. For text-to-flowsheet, diagram-to-simulation, or sketch-to-simulation tasks, keep a normalized intermediate representation of topology, variables, units, and uncertain parameters before any HYSYS write. This makes AI intent reviewable before COM or workbook execution.
2. Treat black-box optimization as local convergence assistance. Optimizers may help tune uncertain parameters, but only on approved workcopies, approved variables, documented bounds, logged residual objectives, and final HYSYS readback.
3. Treat MCP as a tool-contract layer. MCP can make tools cleaner for agents, but it still has to wrap direct COM, spreadsheet/workbook, data table, or proven runner lanes with locks, schemas, audit logs, and rollback.

Do not add SciPy, an MCP server, or a third-party HYSYS wrapper as a default dependency until a real project runner proves runtime value, license compatibility, and recovery behavior.

## 25. Solver 空闲不是收敛，AI 必须执行循环验收

经脱敏的本地 HYSYS V15 与 LLM 代理真实执行、COM 回读和事后核查表明，代理可能在一次参数写入后看到 `Solver.IsSolving == False` 和一组可读结果，就错误宣布“模型已收敛”。进一步检查发现，必需 recycle 仍可能处于 ignored 状态，tear-stream 残差没有闭合；而在没有初始化和 continuation 策略的情况下直接启用 recycle，又可能跳到错误分支或发散。

因此，所有参数更新和调优任务必须采用以下通用规则：

1. 把 `IsSolving == False` 仅记录为 `IDLE`，不得作为 `CONVERGED` 证据；
2. 写入前冻结项目批准的 recycle 状态、绑定、残差、单位、容差、衡算、KPI、调整边界和回退点；
3. 每轮执行求解、等待空闲、机器回读、全项判断，再决定有限调整或回退；
4. 任何缺失或语义不清的必需检查均按失败处理，并至少要求连续两次全项通过；
5. recycle 被忽略时先查明原因并建立批准的初始化或 continuation 策略，不得盲目切换状态；
6. 保存、关闭、重开后再次执行同一验收合同，只有机器终态为 `ACCEPTED` 才能对外称为已收敛。

该规则有真实本地 HYSYS 执行、代理工具调用和 COM 状态/残差回读支持，可标记为本地验证。公开规则仅保留通用失败模式，不包含项目名称、设备位号、工艺参数或私有 case。详细协议见 [convergence-control-loop.md](convergence-control-loop.md)，可执行守卫见 [`scripts/hysys_convergence_guard.py`](../scripts/hysys_convergence_guard.py)。

## 26. 获批计算书应转成权限合同，不能变成强行对表指令

经脱敏的本地 HYSYS V15 批量回归脚本、原生 case、结构化回读、失败记录、发布清单和保存关闭重开证据表明，工程师明确批准的计算书可以成为指定输入边界和验收比较值的权威来源，但不能替代 HYSYS 原生求解结果，也不能授权代理静默消除真实的相态、衡算或 solver 警告。稳定流程是：

1. 执行前把计算书转为机器可读的权限合同，冻结版本、SHA-256、获批输入、单位、容差、工况 ID、预期 case 清单和批准人；缺失、空白、重复或语义不清的字段按阻塞处理；
2. 明确区分“计算书批准的输入边界”“HYSYS 原生回读”“允许保留的已知偏差”和“必须关闭的失败项”，禁止把外部数值冒充 HYSYS 回读，也禁止为对表而联动修改合同外对象；
3. 每个工况从同一获批源哈希复制独立 workcopy，只写权限合同允许的边界，并证明源 case 在验证期间未改变；
4. 候选模型必须连续两次通过同一验收合同，保存、关闭、重开后再次通过；验收至少覆盖 solver、必要 recycle 状态和绑定、物料/能量闭合、相态、关键 KPI、对象或工况清单以及读回稳定性；
5. 发布前逐项对账预期工况与候选成果，任何缺失、失败、重复、孤立或哈希不一致都阻断整批发布，不得以汇总成功掩盖单项失败；
6. 覆盖正式目录前先逐文件备份并校验旧哈希，写入后校验候选哈希；失败运行必须保持“未发布”，并保留原始错误、回滚点和机器可读证据；
7. 若获批基准本身保留已知工程风险，应在结果中继续显式提示，不得为了让报告看起来干净而擅自增加能力、改变边界或消除警告。

该规则已有真实 HYSYS V15 批量执行、连续回读、保存关闭重开、失败即不发布、备份和发布哈希校验支持，可标记为本地验证。它证明的是“已有 case 按获批计算边界进行受控恢复和发布”，不证明计算书中的每个数值天然正确，也不扩大从零建模、详细设计或生产写回边界。

## 27. 模型文件名只能来自已验收回读，不能反过来证明模型内容

经脱敏的本地 HYSYS 原生 case、保存关闭重开回读、重命名脚本和机器可读清单表明，历史文件名可能与模型实际工况或关键 KPI 不一致。文件名便于人工识别，但不是模型内容、工况身份或收敛状态的权威证据。稳定流程是：

1. 先用 case SHA-256 将待处理文件唯一关联到已经 `PASS` 的验收记录，并确认验收记录中的工况 ID、保存关闭重开状态和目标 KPI 一致；
2. 只有已验收的 HYSYS 原生回读可以生成文件名中的工况或 KPI 标签，旧文件名、外部估算值和人工猜测不得作为重命名依据；
3. 文件名若采用取整值，只能用于快速识别；精确值、单位、压力基准和容差必须保留在 CSV 或 JSON 审计中；
4. 执行前生成完整的旧名到新名映射，核对预期 case 清单、唯一工况 ID、目标路径边界、目标名冲突、重复和孤立文件；任何异常均阻断执行；
5. 重命名必须支持事务回滚，执行后逐文件复核新旧 SHA-256 完全相同，并再次对账文件数量、唯一工况和命名规则；
6. 纯重命名没有打开、求解或保存 HYSYS，因此只能声明“元数据变更且内容哈希不变”，不得将其描述为新的收敛、计算或工程验收证据。

该规则已有真实原生 case、既有 HYSYS 保存关闭重开证据、哈希关联、冲突预检、事务回滚和重命名前后哈希一致性支持，可标记为本地验证。它强化的是交付物身份和发布可追溯性，不改变模型计算结果，也不扩大生产写回或从零建模边界。
