# AI-HYSYS 心跳扫描记录：2026-05-02

## 扫描目的

按既定闭环执行：搜索 AI 控制 Aspen HYSYS、HYSYS COM/Python/Spreadsheet/Workbook 自动化、LLM 工艺模拟 agent、HYSYS digital twin / hybrid AI / surrogate model 资料；与 [../source-index.md](../source-index.md) 比对；有价值则保存到 CASE，必要时更新项目规则，校验后提交推送。

## 新增资料已保存

| 类别 | 本地文件 | 原始来源 | 价值判断 |
|---|---|---|---|
| 研究 | [../research/text-to-simulation-arxiv-2601.06776-abstract.html](../research/text-to-simulation-arxiv-2601.06776-abstract.html), [../research/text-to-simulation-arxiv-2601.06776.pdf](../research/text-to-simulation-arxiv-2601.06776.pdf) | [arXiv:2601.06776](https://arxiv.org/abs/2601.06776) | 有价值。论文提出从文本过程规格到可计算仿真配置的多智能体 LLM 工作流，强调 task understanding、topology generation、parameter configuration、evaluation analysis 和收敛率提升；用于补强“AI greenfield 仍是研究/原型路径，生产默认仍应接管已有 HYSYS case”的边界。 |
| 研究 | [../research/llm-agent-process-simulation-arxiv-2601.11650-abstract.html](../research/llm-agent-process-simulation-arxiv-2601.11650-abstract.html), [../research/llm-agent-process-simulation-arxiv-2601.11650.pdf](../research/llm-agent-process-simulation-arxiv-2601.11650.pdf) | [arXiv:2601.11650](https://arxiv.org/abs/2601.11650) | 有价值。论文展示 LLM agent 通过 MCP server 和 Python 与严谨流程模拟器交互，完成分析、优化、数据提取和引导式 flowsheet 构建；不是 HYSYS 证据，但适合作为工具边界、专家监督和 step-by-step 模式的跨模拟器参考。 |

## 重复或暂不入库

- HYSYS V12 + Python COM 氢液化论文已在 [heartbeat-scan-2026-05-01.md](heartbeat-scan-2026-05-01.md) 登记，本轮不重复。
- 2026 HEFA / SAF production planning surrogate 证据已在 [heartbeat-scan-2026-04-30.md](heartbeat-scan-2026-04-30.md) 登记，本轮不重复。
- 泛泛软件营销页、课程聚合页和未提供可核验技术细节的博客不入库。

## 对项目的实际改进

1. [../source-index.md](../source-index.md) 增加两篇 arXiv 论文和本次心跳笔记。
2. [hysys-source-digest.md](hysys-source-digest.md) 增加 LLM agent / text-to-simulation 的项目化结论。
3. [../../SKILL.md](../../SKILL.md) 增加 agentic / text-to-simulation 任务边界：生产默认仍是已有 HYSYS case 接管；单提示从零建模只适合研究或草案；step-by-step、工具日志、收敛状态和人工审核必须保留。
4. [../../references/control-lane-decision-matrix.md](../../references/control-lane-decision-matrix.md) 增加 LLM-agent 工具链附加规则。
5. [../../README.md](../../README.md) 增加两篇新论文链接，方便访客核验。

## 边界结论

本轮资料说明 LLM agent 正在进入严谨流程模拟软件的可执行工具链，但仍不能把 AI-HYSYS-Skill 宣传成“从零自动生成生产级 HYSYS 模型”的工具。

对本仓库而言，正确吸收方式是：

1. 把 LLM agent 作为有工具边界的执行层，而不是自由点击 GUI 的黑箱。
2. 对 topology generation、parameter configuration、evaluation analysis 分别留日志。
3. 单提示 flowsheet 构建只能作为教育、草案或 smoke-test；正式工程默认接管已有已验证 case。
4. 任何 AI 生成配置都必须通过 HYSYS runtime、收敛检查、物性包/设备拓扑复核和人工验收。
