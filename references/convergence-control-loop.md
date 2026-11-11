# Mandatory HYSYS Convergence Control Loop

## 中文说明

本规则适用于任何会修改 HYSYS 输入、运行求解、调整 recycle、执行灵敏度或声称“模型已收敛”的 AI 任务。它的核心原则是：

> `Solver.IsSolving == False` 只表示求解器当前空闲，不表示模型已经收敛。

### 1. 写入前冻结验收合同

在首次写入之前，必须把本次任务的验收条件落成机器可读检查项。至少确认：

1. 哪些 recycle 必须启用，以及各自预期的 `IsIgnored` 状态；
2. recycle 的 feed/product/tear-stream 绑定是否完整；
3. 要检查哪些 tear-stream 残差、单位和项目批准容差；
4. 哪些物料衡算、能量衡算、相态、警告和 KPI 必须通过；
5. AI 允许调整哪些变量、上下限、步长、回退点、最大迭代次数和最长运行时间；
6. 谁负责批准工程容差和最终接受。

不得由 AI 自行编造残差容差。缺少必要读回路径、单位或批准容差时，终态只能是 `UNVERIFIED` 或 `BLOCKED`，不能是 `CONVERGED`。

### 2. 强制状态机

每次执行必须按下列顺序推进：

```text
BASELINE
  -> WRITE_APPROVED_INPUTS
  -> SOLVE_OR_CONTINUE
  -> WAIT_IDLE
  -> READBACK
  -> EVALUATE_ALL_REQUIRED_CHECKS
      -> FAIL: ADJUST_WITHIN_BOUNDS or ROLLBACK, then repeat
      -> PASS: repeat readback/solve cycle for stability confirmation
  -> TWO_OR_MORE_CONSECUTIVE_PASSES
  -> SAVE
  -> CLOSE_AND_REOPEN
  -> RECHECK_THE_SAME_CONTRACT
  -> ACCEPT
```

以下任一情况都必须判为失败或未验证：

- 必需 recycle 为 ignored；
- feed/product/tear-stream 绑定缺失或语义不清；
- 任一必需残差缺失、单位未知或超过批准容差；
- 物料/能量闭合、相态、警告或关键 KPI 未通过；
- 只完成一次求解或一次读回；
- 保存重开后检查结果漂移；
- 达到迭代、时间、变量边界、重复失败状态或无改进停止条件。

### 3. Recycle 特别规则

发现 recycle 被忽略时，不得简单把 `IsIgnored` 改成 `False` 后把下一次空闲状态当作修复成功。必须先确认其被忽略的原因、tear 初值、回路绑定、求解顺序以及项目批准的 continuation、damping 或初始化策略。若启用后残差放大、流量跳到非物理解或进入重复失败状态，应立即回退到最后获批 workcopy，并报告为 `NOT_CONVERGED`。

### 4. HERMES / DeepSeek 执行合同

调用本技能的代理不得在第一次 HYSYS 工具返回后自行结束。它必须持续调用工具，直到收敛守卫产生下列机器终态之一：

- `ACCEPTED`: 所有必需检查连续至少两次通过，并且保存、关闭、重开后同一合同再次通过；
- `NOT_CONVERGED`: 已达到停止条件或出现发散、振荡、无改进；
- `BLOCKED`: 缺少批准容差、对象绑定、读回能力或工程决策；
- `ERROR`: COM、求解、读回、调整、保存或重开失败，保留原始错误。

自然语言“看起来正常”“求解完成”“有结果了”不能覆盖机器终态。输出必须包含每轮检查、残差、调整、停止原因和最终状态。

### 5. 代码入口

[`scripts/hysys_convergence_guard.py`](../scripts/hysys_convergence_guard.py) 提供无第三方依赖的循环守卫：

- `ConvergenceObservation` 把 `False` 和缺失的 `None` 都按失败处理；
- `ConvergencePolicy` 强制至少两个连续通过读回，并限制迭代、时间和重复失败状态；
- `run_convergence_loop(...)` 执行 solve/wait/read/evaluate/adjust 循环并返回可序列化审计记录；
- `require_accepted()` 让下游发布步骤在非接受状态下直接失败。

调用方仍需用项目批准的对象、单位和容差实现 `observe`，并用批准变量与边界实现 `adjust`。该 helper 不替代工程判断，也不会自动决定 HYSYS 的 recycle 策略。

### 6. 固定检查清单，禁止运行中缩减

首次执行前，必须显式构造 `ConvergencePolicy(required_checks=(...))`，字段名称来自本次获批合同。空清单返回 `acceptance_contract_required`，不会调用求解回调。每轮和保存重开后的读回都检查同一清单：遗漏字段会被补为 `None` 并判为未通过，不能靠少提交检查项取得接受状态。

```python
policy = ConvergencePolicy(required_checks=(
    "solver_idle", "ports_match_approved_map", "required_recycles_active",
    "tear_residuals_within_approved_tolerance", "mass_energy_closure",
    "required_kpis_valid",
))
```

这些是示例检查名，不是可以直接置为 True 的模板。各项都要由实际读回和批准容差计算；任务不适用的项目在写入前说明理由，不能在失败后删除。调用 `verify_iterative_convergence(..., policy=policy)` 或 `run_convergence_loop(..., policy=policy)`，检查返回结果并调用 `require_accepted()` 后再生成“已收敛”交付状态。`require_reopen_verification=False` 不再允许产生接受状态。

守卫在求解、读回、重开回调返回后再核对时间限制，超时不能报成功；最后一轮失败后不再写入没有下一轮可验证的调整。此时间检查不能打断阻塞中的 COM 调用，项目 runner 仍须实现有时限的等待或已有的独立工作进程恢复机制，不能据此杀掉用户会话。

兼容性说明：旧调用只提供观察结果、不传固定清单时，现在会明确阻塞。迁移已有 runner 时，先依据工程合同补齐 policy，再运行正常与缺项负例，不从第一次观测反推验收标准。参见[实际执行经验](runtime-lessons.md)。

## English Summary

`IsSolving == False` means **IDLE**, not **CONVERGED**. Before any write, freeze a machine-readable acceptance contract covering required recycle states and bindings, approved residual tolerances and units, balance/KPI checks, allowed variables and bounds, rollback, and execution limits. Run solve/wait/read/evaluate/adjust cycles until every required check passes at least twice consecutively, then save, close, reopen, and re-evaluate the same contract. Missing evidence fails closed. Never fix an ignored recycle by blindly enabling it; validate initialization and continuation strategy and roll back on divergence. An agent may report convergence only when the guard returns an accepted terminal state.
