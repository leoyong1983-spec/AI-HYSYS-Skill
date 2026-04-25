# AI-HYSYS 心跳扫描记录：2026-04-25

## 扫描目的

手动测试每天 1 点心跳任务：搜索并保存 AI 控制 Aspen HYSYS、HYSYS 自动化、Aspen 官方 AI / Hybrid Models、HYSYS 数字孪生相关的新资料；只保留对 AI-HYSYS-Skill 定位、证据链或后续开发有价值的信息。

## 新增资料已保存

| 类别 | 本地文件 | 原始来源 | 价值判断 |
|---|---|---|---|
| 官方 | [../official/aspen-hysys-2025-brochure-page.html](../official/aspen-hysys-2025-brochure-page.html) | [Aspen HYSYS brochure page](https://www.aspentech.com/en/resources/brochure/aspen-hysys) | 补强 HYSYS 在全生命周期、经济、能耗、安全、排放和 model-backed intelligence 中的官方定位。 |
| 官方 | [../official/aspen-hybrid-models-product-page.html](../official/aspen-hybrid-models-product-page.html) | [Aspen Hybrid Models](https://www.aspentech.com/en/solutions/aspen-hybrid-models) | 证明 Aspen 官方已经把 Industrial AI / Hybrid Models 与 Aspen HYSYS、Aspen Plus 等过程模拟器联系起来。 |
| 官方 | [../official/aspen-elearning-catalog-2025-04.pdf](../official/aspen-elearning-catalog-2025-04.pdf) | [Aspen eLearning catalog 2025-04](https://www.aspentech.com/-/media/aspentech/home/knowledge/elearning/aspen_elearning_catalog_040525.pdf) | 补强 HYSYS 基础、分析报告、Simulation Workbook、自动化方案、动态仿真、LNG 等培训证据。 |
| 研究 | [../research/pinn-digital-twin-arxiv-2603.24644-abstract.html](../research/pinn-digital-twin-arxiv-2603.24644-abstract.html) | [arXiv 2603.24644 abstract](https://arxiv.org/abs/2603.24644) | 证明 HYSYS 生成的动态数据可进入 PINN / digital twin / soft sensing / MPC / anomaly detection 研究链路。 |
| 研究 | [../research/pinn-digital-twin-arxiv-2603.24644.pdf](../research/pinn-digital-twin-arxiv-2603.24644.pdf) | [arXiv 2603.24644 PDF](https://arxiv.org/pdf/2603.24644.pdf) | 保存完整论文，供后续提炼数字孪生扩展方向。 |

## 对 AI-HYSYS-Skill 的影响

1. 继续坚持主定位：AI 接管已有可运行 HYSYS case 的参数、边界、求解、检查和报告，而不是默认承诺从零自动建模。
2. 官方 Hybrid Models 资料可以用于 README / CASE 叙事：Aspen 自身已经把 AI、first-principles models、过程模拟器和工程决策放在同一条线上。
3. arXiv 2603.24644 应作为“围绕 HYSYS 的 AI 数字孪生”证据，不应混同为“AI 直接操控 HYSYS COM”的证据。
4. eLearning 目录说明 HYSYS 自动化、Simulation Workbook、动态仿真和 LNG 都是可公开引用的官方学习入口，适合支撑 skill 的控制通道分层。

## 已同步更新

- [source-index.md](../source-index.md) 已加入新增来源索引。
- [hysys-source-digest.md](hysys-source-digest.md) 已加入本次心跳测试结论。
- 仓库验证命令 `.\scripts\validate_repo.ps1` 已通过。

## 第二轮手动测试补充

第二轮检索继续围绕 AI-HYSYS-Skill 的真实控制通道寻找更强证据。新增资料如下：

| 类别 | 本地文件 | 原始来源 | 价值判断 |
|---|---|---|---|
| 官方 | [../official/aspen-hysys-brochure-2025-05.pdf](../official/aspen-hysys-brochure-2025-05.pdf) | [Aspen HYSYS brochure PDF](https://www.aspentech.com/-/media/aspentech/home/resources/brochure/pdfs/fy25/q4/at-4162_bro_aspen-hysys_final_0525.pdf) | 官方 PDF 明确强化 Industrial AI、model-backed intelligence、经济、能耗、安全和排放叙事，比 HTML 快照更适合长期留档。 |
| 研究 | [../research/hysys-coding-platforms-jglobal-2025.html](../research/hysys-coding-platforms-jglobal-2025.html) | [J-GLOBAL article metadata](https://jglobal.jst.go.jp/en/public/202502285695228497) | 2025 年 Computers & Chemical Engineering 论文书目信息，主题覆盖 Python-HYSYS 对象层级、特殊对象、backdoor variables、仿真优化和技术经济工具；原文 DOI 为 `10.1016/j.compchemeng.2025.109247`。 |
| 研究 | [../research/hysys-interconnection-methodologies-sim2-2022.pdf](../research/hysys-interconnection-methodologies-sim2-2022.pdf) | [SIM2 public PDF](https://papers.sim2.be/assets/uploads/files/1c6ba-communicationarticle.pdf) | 同行评议论文对比 HYSYS direct communication、indirect communication、internal spreadsheets、data tables 四类连接方式，直接支撑本 skill 的通道选择逻辑；ScienceDirect DOI 为 `10.1016/j.compchemeng.2022.107785`。 |

第二轮额外结论：`direct COM` 不应被写成唯一通道，而应写成主通道；`spreadsheet/workbook` 不只是权宜之计，而是经过论文和社区实践共同支持的稳定桥接层；`data tables` 和间接通信可以作为特定场景下的降级或补充通道，但不应喧宾夺主。

注意：ScienceDirect 页面用命令行下载时返回了无效壳页，已删除，未纳入 CASE。Mindat 页面被 Cloudflare 拦截，也未保存为有效资料。
