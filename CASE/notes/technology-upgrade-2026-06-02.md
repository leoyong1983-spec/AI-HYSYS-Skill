# 2026-06-02 技术升级笔记：Text-to-Flowsheet、MCP 与 Graph-IR 边界

## 本轮价值判断

Text-to-Flowsheet 属于 A- 级相邻研究证据：它是 2026 年 RSC Digital Discovery 正式论文，公开代码库，且明确把自然语言流程描述转换为流程图中间结构，再进入严格流程模拟器，并用黑箱优化补齐不确定参数以争取收敛。

APS + MCP agent 属于 B+ 级相邻架构证据：它说明 MCP 可以成为 LLM 与严谨流程模拟器之间的标准工具边界，但案例软件是 AVEVA Process Simulation，不是 HYSYS。

Sketch2Simulation 属于 B+ 级 HYSYS 相关研究证据：它支持多智能体、图/草图到 HYSYS Python COM 脚本的研究路线，但仍不能替代本仓库的默认生产边界。

## 对 AI-HYSYS-Skill 的改进结论

1. Text-to-flowsheet / diagram-to-simulation 任务必须先形成可审计的 Graph-IR 或等价中间表示，再允许转换成 HYSYS 写入动作。
2. 黑箱优化只能作为局部收敛辅助，不得默认改变拓扑、物性包或冻结边界；变量、范围、目标函数、残差、迭代次数和失败样本必须记录。
3. MCP 应作为协议层和工具边界，而不是新的模拟器控制通道本身；底层仍要落到 direct COM、workbook/spreadsheet、data table 或既有 runner。
4. HYSYS COM 自动化仍按单 workcopy / 单写入队列 / 明确启动关闭边界执行，不共享 live COM handle 到并发线程或进程。

## 本轮没有采纳的做法

- 没有新增 SciPy 依赖。原因：仓库当前定位是轻量、可安装、可审计的 HYSYS skill；优化器应先作为项目工作流规则，而不是默认依赖。
- 没有新增 MCP server。原因：MCP 是合理演进方向，但 HYSYS 本地 runtime、鉴权、锁、schema、审计日志和回滚流程需要独立实现后才能变成可执行组件。
- 没有宣称 AI-HYSYS-Skill 已能可靠从文本生成生产级 HYSYS flowsheet。当前默认路径仍是接管已存在、可运行、可验证的 HYSYS case。

## Sources

- Text-to-Flowsheet: https://pubs.rsc.org/en/content/articlehtml/2026/dd/d6dd00060f
- Text2Flowsheet code/data: https://github.com/LLM4ChemEng/Text2Flowsheet
- LLM Agent for User-friendly Chemical Process Simulations: https://arxiv.org/abs/2601.11650
- Sketch2Simulation: https://arxiv.org/abs/2603.24629

