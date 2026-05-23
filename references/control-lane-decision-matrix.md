# HYSYS 控制通道决策矩阵

## 何时读取

在真正修改 HYSYS case、写入参数、跑 sensitivity、冻结 baseline 或导出包文件之前，先用这份矩阵判断控制通道。不要只因为某条路“能连上”就直接进入批量调参。

## 来源到项目规则的转化

这份矩阵把 `CASE/` 里的优秀技术内容转成项目规则：

1. [hysys-interconnection-methodologies-sim2-2022.pdf](../CASE/research/hysys-interconnection-methodologies-sim2-2022.pdf) 把 HYSYS interconnection 拆成 direct communication、indirect communication、internal spreadsheets、data tables 四类。
2. [hysys-coding-platforms-jglobal-2025.html](../CASE/research/hysys-coding-platforms-jglobal-2025.html) 记录了 2025 年论文对 Python-HYSYS 对象层级、特殊对象、backdoor variables、优化和技术经济工具的讨论。
3. [heartbeat-scan-2026-05-01.md](../CASE/notes/heartbeat-scan-2026-05-01.md) 记录了 HYSYS V12 + Python COM 用于系统化数据提取、模块化仿真、自动敏感性和优化分析的公开论文线索。
4. [Aspen Simulation Workbook](../CASE/official/aspen-simulation-workbook-product-page.html) 和社区 spreadsheet bridge 示例证明，tagged IO 层是合理工程接口，不是临时凑合。
5. [text-to-simulation-arxiv-2601.06776.pdf](../CASE/research/text-to-simulation-arxiv-2601.06776.pdf) 和 [llm-agent-process-simulation-arxiv-2601.11650.pdf](../CASE/research/llm-agent-process-simulation-arxiv-2601.11650.pdf) 说明 LLM agent 可通过分步工具链生成、分析和优化仿真，但仍需要工具日志、收敛检查和专家监督。
6. [scripts/hysys_automation.py](../scripts/hysys_automation.py) 是本仓库内置 direct COM starter wrapper，用于把主通道固化成可审计代码。
7. [hysys-scadabr-python-supervisory-control-mdpi-2026.pdf](../CASE/research/hysys-scadabr-python-supervisory-control-mdpi-2026.pdf) 说明 HYSYS/Python 可与 ScadaBR/Modbus 类监督系统结合，但这应作为 external supervisory/testbed lane，而不是默认生产闭环控制。
8. [reasoning-agent-distillation-nature-2026.pdf](../CASE/research/reasoning-agent-distillation-nature-2026.pdf) 补强 LLM reasoning agent 的仿真、优化、碳核算和节能方案分步工作流；它是 Aspen Plus 相邻证据，不改变 HYSYS 生产默认边界。
9. [hysys-ccs-eor-python-automation-eksergi-2026.pdf](../CASE/research/hysys-ccs-eor-python-automation-eksergi-2026.pdf) 展示 Aspen HYSYS V14 与 Python 自动化用于 162 个 full-factorial CCS-EOR 技经敏感性场景，补强批量场景必须先定义变量 schema、KPI、失败样本和经济指标导出。

## 通道定义

| 通道 | 适用场景 | 优点 | 风险 | 本仓库默认态度 |
|---|---|---|---|---|
| Proven project runner | 项目已有成功脚本、日志、导出器或 workbook runner | 最贴近当前 case，复用风险最低 | 可能有项目私有假设 | 第一优先级 |
| Direct COM | 启动 HYSYS、打开/保存 case、访问对象、冻结 workcopy、导出审计件 | 权威性最强，能控制 case 生命周期 | 深层对象路径可能脆弱，特殊对象需要额外处理 | 主通道 |
| Spreadsheet / Workbook | 参数面板、KPI 面板、命名 IO、多人可读工作流 | 稳定、可审计、人机共用 | 可能隐藏对象模型问题；schema 需冻结 | 首选桥接层 |
| Data tables | 已在 case 内配置好表格或需要 HYSYS 原生表格扫描 | 与 HYSYS 内部分析对象贴近 | 通用性弱，表结构容易依赖模型 | 补充通道 |
| Indirect communication | 已存在 Excel/VBA、Matlab、C#、中间文件或 OPC/ActiveX 工作流 | 可复用遗留资产 | 多一层状态和单位风险 | 只在已有且验证通过时使用 |
| SCADA / Modbus / OPC-style supervisory bridge | 动态监控、operator training、dashboard、digital twin testbed 或控制策略验证，且桥接层已由项目配置 | 接近现场监督系统语境，适合训练和验证 | 可能被误用为生产闭环；涉及网络、tag、刷新频率和写权限风险 | 外部监督通道，默认只读或人工批准写入 |
| GUI | 布局确认、不可脚本化视觉检查、人工复核 | 人类直观 | 不可审计、难复现 | 最后退路 |

## 选择算法

1. 如果项目目录已有验证过的 runner、日志或导出器，先复用，不要另起炉灶。
2. 如果任务涉及 case 生命周期，例如 open/save/reopen/freeze/export，优先 direct COM。
3. 如果任务是大量参数/KPI 读写，且模型里已有命名 spreadsheet/workbook，优先 `direct COM + spreadsheet/workbook tagged IO`。
4. 如果对象是 Column、Spreadsheet、Design Spec、Data Table、Optimizer 或其他特殊对象，先查现有命名对象和 workbook/schema，再决定是否走 direct object path。
5. 如果变量只能通过 backdoor variables 或深层对象路径访问，先做单点 smoke test，确认单位、读写方向和 solver 状态，再允许批量写入。
6. 如果只有 Excel/VBA、Matlab、C# 或中间文件桥已经跑通，允许作为 indirect lane，但必须记录它不是主真源。
7. 如果任务涉及 ScadaBR、Modbus、OPC、SCADA、dashboard 或 live monitoring，先确认它是模拟测试台、培训系统、只读监控还是允许写回的工程批准系统；默认不允许自动闭环回写。
8. 如果以上都不稳定，只允许 GUI 做人工确认或临时诊断，不允许把 GUI 当生产自动化主路径。

## 敏感性和优化任务的附加规则

如果任务要用 Python COM 对 HYSYS 做系统化数据提取、模块化仿真、敏感性或优化分析，必须先补充：

1. 子系统边界：哪些 unit operation、streams、utilities 和循环属于本轮模块。
2. 数据 schema：每个输入、输出、KPI、单位、允许范围和缺失值处理规则。
3. 求解策略：是否暂停 solver、如何恢复、如何等待收敛、如何记录失败样本。
4. 批量策略：先跑单点 smoke test，再跑小批量，再进入全量敏感性或优化。
5. 写回策略：默认只写 HYSYS workcopy，不直接写生产操作参数；优化建议必须进入人工复核。
6. 场景策略：full-factorial、DOE、PSO、Bayesian optimization 或人工候选集都必须记录设计矩阵、样本编号、输入边界、输出 KPI、失败分类和重跑规则。

## LLM Agent 任务的附加规则

如果任务要用 LLM agent、text-to-simulation、diagram-to-simulation 或 autonomous flowsheet construction 控制流程模拟器，必须先补充：

1. 工具边界：agent 可以调用哪些 COM、spreadsheet、workbook、MCP 或脚本工具，哪些动作必须人工确认。
2. 分步策略：优先 task understanding、topology、parameter configuration、evaluation 分段执行，不默认单提示到底。
3. 证据链：保存 tool call、输入输出 schema、收敛状态、错误日志和人工复核记录。
4. 适用范围：生产任务默认接管已有 HYSYS case；从零构建只允许作为研究、教学、草案或 smoke-test。
5. 拒绝条件：缺少物性包、设备拓扑、单位、边界条件或收敛验证时，不允许进入批量调参或正式导出。
6. 如果 agent 任务包含碳核算、节能方案或 decarbonization 评价，必须把模拟器结果、优化变量、能源情景、碳因子、适用区域和人工复核责任分开记录。

## 批量写入前检查

任何批量参数修改前都要记录：

1. 使用哪条通道，以及为什么不用更高优先级通道。
2. case 来源：frozen baseline、audited workcopy、mother case 或 smoke-test case。
3. 变量 schema：对象路径、spreadsheet 名称、cell 坐标、单位、允许范围、回滚值。
4. solver 节奏：是否暂停 solver、何时恢复 solver、如何等待 `IsSolving` 结束。
5. 失败分类：launch、open、binding、unit mismatch、solver、export。

## 输出模板

每次进入真实 case 写入前，至少输出一段 lane decision：

```text
Control lane: direct COM + spreadsheet bridge
Reason: existing workcopy loads through COM; target variables are exposed through named HYSYS spreadsheets.
Rejected lanes: GUI rejected because not auditable; raw deep object path rejected until one-cell smoke test passes.
Case source: audited workcopy, copied from frozen baseline.
Solver policy: pause solver, batch-write inputs, resume solver, wait for IsSolving=False, then read KPIs.
Rollback: restore saved workcopy if binding or solver failure occurs.
```

## 对当前 skill 的具体约束

1. `direct COM` 是主通道，但不是唯一通道。
2. `spreadsheet/workbook` 是稳定 tagged IO 层，不是低级替代品。
3. `data tables` 和 `indirect communication` 要写进 fallback 体系，但不能压过 direct COM 与 workbook bridge。
4. SCADA / Modbus / OPC-style bridge 是外部监督和测试台通道，不是默认生产控制通道。
5. AI 从零创建复杂 HYSYS flowsheet 仍只适合研究或 smoke test，不适合默认工程交付。
