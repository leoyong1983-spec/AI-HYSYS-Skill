# 手动心跳测试记录：2026-04-27 - HYSYS 原油蒸馏与 ML 代理模型

## 搜索命中

本轮按“搜索资料 -> 判断价值 -> 保存到 CASE -> 必要时修改项目 -> 校验 -> commit/push/PR”流程手动测试，命中一篇新的 HYSYS + 机器学习论文线索：

- 题名：Data-driven simulation of crude distillation using Aspen HYSYS and comparative machine learning models
- 期刊：The Canadian Journal of Chemical Engineering
- 日期：2026-02
- DOI：`10.1002/cjce.70297`
- 来源页：[ResearchGate metadata](https://www.researchgate.net/publication/400895104_Data-driven_simulation_of_crude_distillation_using_Aspen_HYSYS_and_comparative_machine_learning_models)
- DOI 入口：[https://doi.org/10.1002/cjce.70297](https://doi.org/10.1002/cjce.70297)

## 保存状态

本轮尝试保存 Wiley PDF 与 ResearchGate HTML 快照，但匿名访问被站点访问控制阻断：

- Wiley PDF 入口返回 Cloudflare / JavaScript / cookie challenge。
- ResearchGate 页面下载返回 access denied / 1020。

因此本仓库不保存伪 PDF，也不绕过门禁抓取全文。本文件仅保存可核验的书目信息、公开摘要层面的技术判断、项目价值和边界结论。

## 技术摘要

该论文使用 Aspen HYSYS 对原油蒸馏过程做仿真，并把 HYSYS 结果作为机器学习模型的数据来源。公开摘要层面的信息显示，研究比较了线性回归、随机森林、支持向量回归和人工神经网络等模型，用于预测蒸馏产品性质或相关输出。

对 AI-HYSYS-Skill 来说，关键不是复刻论文模型，而是吸收它的工程范式：

1. 先有可信 HYSYS case 或仿真基线。
2. 在明确设计空间内批量生成仿真数据。
3. 再训练 ML surrogate / soft sensor / 快速估算层。
4. 所有 ML 输出都要保留有效范围、误差指标和人工复核要求。

## 价值判断

有价值，值得影响项目。

它补强了“AI-HYSYS-Skill 可以帮助 HYSYS 项目走向 surrogate model / soft sensor / KPI 预测前置整理”的证据链。它也支持我们在项目里新增一个明确边界：HYSYS 仍是可信仿真基线，ML 代理模型只是加速评估、筛选或报告层，不应在未复核时替代 HYSYS runtime。

## 不支持的宣传

这条资料不支持以下说法：

1. AI 可以可靠地从零创建复杂 HYSYS 工厂模型。
2. ML surrogate 可以替代已验证 HYSYS baseline。
3. 代理模型可以在训练范围外自动外推并用于生产决策。
4. 本开源 skill 已具备 Aspen AI Model Builder、Aspen OnLine 或商业 Hybrid Models 的完整能力。
5. 只凭论文摘要就能声明已经复现论文结果。

## 对项目的改进动作

本轮据此补充项目规则：

1. 在 [../../references/digital-twin-boundary.md](../../references/digital-twin-boundary.md) 增加 surrogate / ML 代理模型默认边界。
2. 在 [hysys-source-digest.md](hysys-source-digest.md) 增加 HYSYS 仿真数据训练 ML 的项目化结论。
3. 在 [../source-index.md](../source-index.md) 登记本条来源与访问限制。
4. 在 [../../SKILL.md](../../SKILL.md) 增加 surrogate / data-driven simulation 任务的执行约束。
