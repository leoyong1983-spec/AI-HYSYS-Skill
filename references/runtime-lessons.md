# Runtime Lessons / 实际执行经验

Use for case migration, repeated scenario calculations, connection disputes, or a result that looks stable but has incomplete convergence evidence. These rules were distilled from local scripts, readbacks and engineer feedback. Private evidence stays in the originating project; the examples below contain no project values or object tags.

## 1. 先确认计算连接，再相信图面

图面上两条线相接、流股同名或设备数量一致，都不能证明计算端口相同。迁移或改接前，记录源模型每个相关单元的实际进出口对象身份、所属 flowsheet、端口方向及 ignored 状态。按目标版本实际暴露的专用端口或集合读取；一个通用集合为空，不足以证明没有连接。

Compare the upstream outlet with the downstream inlet using flowsheet-qualified stream identities. Recheck after save/close/reopen. Inspect the native PFD separately; disagreement between graphical endpoints and calculation ports is a finding, not permission to reconnect automatically. A connected mother case from another scenario is only a candidate topology until its inputs and boundary differences are mapped.

## 2. 数值稳定与回路闭合要分别验收

本地 V14 重算记录曾出现功率连续回读与重开后不变，但 recycle 进出口流量仍不同；单纯增加最大迭代次数或执行一次 ReStart 并未消除该差异。不要机械重复这些动作。检查 tear 绑定、初值、允许的求解策略，以及质量、温度、绝压、焓和组成的批准残差。

Keep `results_readable`, `repeated_readback_stable`, `reopened`, `recycle_residuals_verified`, and `engineering_accepted` distinct. Report a limited KPI check when residuals or approved tolerances are unavailable. Never turn missing residuals into zero or true.

If COM does not expose a unit's solved state, a same-object `<Name>`/`<IsSolved>` pair in a current `GetXMLForCase()` diagnostic export can supplement the check after validating that runtime's XML structure. Do not assume a global XML search has found the intended unit. XML status and solver idle cannot replace numerical residuals.

## 3. 区分诊断 XML 与原生交换文件

`GetXMLForCase()` 审计内容与原生 Save As XML 在已检查的案例中不是同一种可导入文件，不能只改扩展名互换。需要 V15 到 V14 迁移时，先在独立副本验证源版本原生导出、目标版本导入、另存 HSC 和重开。保留导出警告，逐项核查组件顺序、物性方法及配置、设备规格、连接与 ignored 状态；仅物性包名称相同不等于全部物性设置等效。

Imported cases may have a paused solver and unavailable cached values. Preserve that state in the migration record. Recalculation is a separate approved stage: reapply the same boundary, check finite readbacks and phases, then perform the full convergence contract. A successful import/reopen proves persistence, not solved equivalence. Special property packages, extensions and each runtime version require their own checks.

## 4. 迁移、统一连接、变更边界分开记账

原模型与计算书可能原本不一致。先记录两者版次、哈希、逐工况输入、来源与压力基准；只有输入、拓扑及求解策略相同时，才可分析版本迁移对结果的影响。不能把边界变化造成的差异称为“版本误差”。

When a model is deliberately reconnected, downstream flow may become a calculated result instead of an independent input. If preserving the old flow conflicts with preserving approved upstream conditions, record the conflict and use the engineer's chosen boundary. Do not silently tune unrelated feeds to reproduce an old filename or power label. After any change, recheck phase, utility requirements and material/energy closure; a lower duty alone does not establish a better design.

## 5. 批量母版只复用结构，不继承其他工况的验收

为每个工况建立输入映射与独立 workcopy。采用另一个稳定工况作初始化时，记录 seed 来源、可迁移状态和必须恢复的本工况规格；最终逐项核对全部批准输入，防止工况复制后遗留来料、环境、公用工程或压力边界。非零出口去向不明时保留为 open issue，不自动回接或删除。

Reconcile the expected scenario IDs, case hashes and result rows before aggregation. Keep warnings and failed trials alongside later candidates. User acceptance of a mother case's connections applies to those connections; it does not automatically accept revised duties, other scenarios or unverified tolerances.

## 6. 读取不到属性与软件故障分别处理

属性不可读时，保留成员名、单位和异常，先核查当前版本的对象类型与类型库；不要猜一个相似名称，或将错误值转成零。若窗口有响应但设备对话框不见了，先核对目标 HYSYS 窗口与显示器工作区，确认离屏后再移动该窗口。此类显示恢复不需要重启整个计算会话，也不能作为收敛证据。

## Evidence Scope / 证据范围

Historical V14/V15 source scripts and structured readbacks support the connection, migration, repeated-readback and scenario-boundary lessons above. The window recovery rule is supported by an existing bounded local recovery record. This skill update itself runs deterministic regression tests; it does not rerun private plant models or certify general XML downsave compatibility. Keep exact source pointers and hashes in the local maintenance work item.
