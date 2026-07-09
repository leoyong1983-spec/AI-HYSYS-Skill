# CASE Source Index

准备日期：2026-04-21（Asia/Shanghai）
最近心跳测试：2026-05-12（Asia/Shanghai）

这个目录不是“随手存链接”，而是 AI-HYSYS-Skill 的公开素材底座。建议先读 [notes/hysys-source-digest.md](notes/hysys-source-digest.md)，再按需要下钻到具体文件。

## 使用原则

1. `official/` 里的 AspenTech 页面用于证明 HYSYS、Workbook、培训入口和支持入口是真实存在的官方能力。
2. `community/` 里的公开仓库用于证明 Python 控制 HYSYS 的 spreadsheet bridge 路径已经有人公开落地。
3. `research/` 里的论文用于证明 AI + HYSYS 的公开研究路径，包括生成可执行建模脚本、用 HYSYS 仿真数据训练代理模型/数字孪生，但不能自动等同于生产闭环。
4. `notes/` 里的中文文件用于把这些来源压缩成可发布、可讲述、可复用的话术和方法论。
5. SCADA / Modbus / OPC-style 资料只用于外部监督、培训、dashboard 或 digital twin testbed 边界，不等同于生产闭环控制授权。

## 索引表

| 类别 | 本地文件 | 作用 | 原始链接 | 备注 |
|---|---|---|---|---|
| 官方 | [official/aspen-hysys-product-page.html](official/aspen-hysys-product-page.html) | 证明 HYSYS 官方覆盖 steady-state、dynamic studies、process safety、AI optimization、Hybrid Models、plant-calibrated predictive models 和 real-time data 等工作流 | [Aspen HYSYS product page](https://www.aspentech.com/en/products/engineering/aspen-hysys) | HTML 快照 |
| 官方 | [official/aspen-hysys-dynamics-product-page-2026.html](official/aspen-hysys-dynamics-product-page-2026.html) | 证明 AspenTech 官方把 HYSYS Dynamics 定位为动态仿真、瞬态条件分析和控制方案验证能力；用于约束动态任务必须从已验证 baseline 受控转换 | [Aspen HYSYS Dynamics product page](https://www.aspentech.com/en/products/engineering/aspen-hysys-dynamics) | HTML 快照 |
| 官方 | [official/aspen-hysys-2025-brochure-page.html](official/aspen-hysys-2025-brochure-page.html) | 补充 2026 可访问的 HYSYS brochure 页面，强调经济、能耗、安全、排放、全生命周期和 model-backed intelligence | [Aspen HYSYS brochure page](https://www.aspentech.com/en/resources/brochure/aspen-hysys) | HTML 快照 |
| 官方 | [official/aspen-hysys-brochure-2025-05.pdf](official/aspen-hysys-brochure-2025-05.pdf) | 保存 2025-05 官方 HYSYS brochure PDF，补强 Industrial AI、model-backed intelligence、经济、能耗、安全、排放等产品叙事 | [Aspen HYSYS brochure PDF](https://www.aspentech.com/-/media/aspentech/home/resources/brochure/pdfs/fy25/q4/at-4162_bro_aspen-hysys_final_0525.pdf) | 真 PDF |
| 官方 | [official/aspen-hysys-performance-digital-twin-case-study.html](official/aspen-hysys-performance-digital-twin-case-study.html) | 官方案例页面：Aspen HYSYS 用于性能工程数字孪生，识别热虹吸系统液压不稳定并支撑经济收益叙事 | [AspenTech performance engineering digital twin case study](https://www.aspentech.com/en/resources/case-studies/energy-company-saves-%246m-usd-with-a-performance-engineering-digital-twin) | HTML 快照 |
| 官方 | [official/aspen-hysys-performance-digital-twin-case-study.pdf](official/aspen-hysys-performance-digital-twin-case-study.pdf) | 官方案例 PDF：保存 HYSYS + Aspen EDR 数字孪生案例全文，支持“现有模型接管 + 诊断/报告/优化”的工程价值定位 | [AspenTech performance engineering digital twin PDF](https://www.aspentech.com/-/media/aspentech/home/resources/case-study/pdfs/fy21/q2/at-06386--cs-english-v9.pdf?sc_lang=en) | 真 PDF |
| 官方/研究 | [notes/heat-exchanger-ai-control-patterns-2026-07-01.md](notes/heat-exchanger-ai-control-patterns-2026-07-01.md) | 换热器 AI/HYSYS 知识沉淀：已有 HYSYS/EDR case、变量 schema、surrogate/optimizer 候选、HYSYS/EDR 回算与人工验收 | [Aspen EDR](https://www.aspentech.com/en/products/engineering/aspen-exchanger-design-and-rating), [HDA surrogate program](https://github.com/Galigeigei-Z/HDA-Surrogate-Optimization), [STHE AI paper](https://doi.org/10.1049/cit2.12393) | CASE 笔记；用于技能规则，不等同于 runtime 验证 |
| 官方 | [official/aspen-hysys-tupras-column-performance-2026.html](official/aspen-hysys-tupras-column-performance-2026.html) | 官方案例页面：Tüpraş 使用 Aspen HYSYS column analysis 与 Aspen Exchanger Design & Rating 集成提升塔能力并满足产品规格 | [Control Column Performance Using Aspen HYSYS](https://www.aspentech.com/en/resources/case-studies/control-column-performance-using-aspen-hysys) | HTML 快照 |
| 官方 | [official/aspen-hysys-tupras-column-performance-2019.pdf](official/aspen-hysys-tupras-column-performance-2019.pdf) | 官方案例 PDF：保留 column hydraulics、tray rating、column performance 和 plant digital twin 场景的英文全文 | [AspenTech Tüpraş PDF](https://www.aspentech.com/-/media/aspentech/home/resources/case-study/pdfs/fy19/q3/at-05656-tupras-case-study.pdf?sc_lang=en) | 真 PDF |
| 官方 | [official/aspen-hybrid-model-condensate-digital-twin-article.html](official/aspen-hybrid-model-condensate-digital-twin-article.html) | 官方文章页面：ADNOC 使用 hybrid model 和 process simulation digital twin 优化凝析油收益 | [AspenTech condensate digital twin article](https://www.aspentech.com/en/resources/articles/utilize-a-process-simulation-digital-twin-to-optimize-condensate-yield) | HTML 快照 |
| 官方 | [official/aspen-hybrid-model-condensate-digital-twin-article-2025.pdf](official/aspen-hybrid-model-condensate-digital-twin-article-2025.pdf) | 官方文章 PDF：补强 hybrid model、AI、first-principles、historian、soft sensor、condensate yield 和 GHG reduction 的工程链路 | [AspenTech condensate digital twin PDF](https://www.aspentech.com/-/media/aspentech/home/resources/articles/pdfs/fy25/q2/at-3653-art_hp-adnoc-digital-twin.pdf) | 真 PDF |
| 官方 | [official/aspen-hpcl-industrial-ai-quality-soft-sensors-2026.html](official/aspen-hpcl-industrial-ai-quality-soft-sensors-2026.html) | 官方案例页面：HPCL 使用 Aspen AI Model Builder 和 Aspen HYSYS 部署 AI soft sensors 做实时质量控制 | [AspenTech HPCL Industrial AI case study](https://www.aspentech.com/en/resources/case-studies/real-time-quality-control-how-hpcl-uses-industrial-ai-to-improve-refining-processes) | HTML 快照 |
| 官方 | [official/aspen-hpcl-industrial-ai-quality-soft-sensors-2026.pdf](official/aspen-hpcl-industrial-ai-quality-soft-sensors-2026.pdf) | 官方案例 PDF：保存 HPCL soft sensor 全文，补强 HYSYS + AI Model Builder + 实时质量/KPI 预测的工程证据 | [AspenTech HPCL Industrial AI PDF](https://www.aspentech.com/-/media/aspentech/home/resources/case-study/pdfs/fy25/q5/at-4331_cs_hpcl_real_time_quality_control_v3.pdf) | 真 PDF |
| 官方 | [official/aspentech-whats-new-v15-industrial-ai-2026.html](official/aspentech-whats-new-v15-industrial-ai-2026.html) | AspenTech V15 页面，补强 Industrial AI、AI Model Builder desktop、Aspen HYSYS/Plus green H2、Aspen OnLine for HYSYS and Aspen Plus 等当前产品语境 | [AspenTech V15 What's New](https://solutions.aspentech.com/en/whats-new) | HTML 快照 |
| 官方 | [official/aspen-hysys-online-simulation-models-webinar-2026.html](official/aspen-hysys-online-simulation-models-webinar-2026.html) | 官方 on-demand webinar 页面：用 Aspen HYSYS models 部署 online simulations，支撑 KPI monitoring、process insights、节能减排和 troubleshooting 边界 | [Deploy Simulation Models Online Easily](https://www.aspentech.com/en/resources/on-demand-webinars/deploy-simulation-models-online-easily-gain-unrivaled-process-insights) | HTML 快照 |
| 官方 | [official/aspen-hysys-mysep-live-process-digital-twin-2026.html](official/aspen-hysys-mysep-live-process-digital-twin-2026.html) | 官方 on-demand webinar 页面：Aspen HYSYS 与 MySep Engine 严谨分离器模型集成，形成 live process digital twin，用于 brownfield operations、carryover risk、throughput、energy efficiency 和 KPI limits | [AspenTech MySep live process digital twin webinar](https://www.aspentech.com/en/resources/on-demand-webinars/apac-webinar-en-driving-throughput-and-efficiency-with-digital-twin) | HTML 快照 |
| 官方 | [official/aspen-hysys-saudi-aramco-plant-digital-twin-2026.html](official/aspen-hysys-saudi-aramco-plant-digital-twin-2026.html) | 官方案例页面：Saudi Aramco 使用 Aspen HYSYS 建立多个装置 plant digital twins，用于炼厂改造可行性分析和产能提升方案评估 | [AspenTech Saudi Aramco plant digital twin case study](https://www.aspentech.com/en/resources/case-studies/saudi-aramco-increases-capacity-by-100000-barrels-day-and-upgrades-bottom-of-the-barrel-products) | HTML 快照 |
| 官方 | [official/aspen-hysys-indian-oil-barauni-process-digital-twins-2026.html](official/aspen-hysys-indian-oil-barauni-process-digital-twins-2026.html) | 官方 webinar 页面：Indian Oil Barauni Refinery 部署 Aspen HYSYS-based process digital twins，用于炼厂运行优化和不可实时测量 KPI 场景 | [AspenTech Indian Oil Barauni process digital twins webinar](https://www.aspentech.com/en/resources/on-demand-webinars/apac-webinar-en-learn-how-a-major-indian-refinery-gained-substantial-benefits) | HTML 快照 |
| 官方 | [official/aspentech-university-hysys-hybrid-ai-online-course-2026.html](official/aspentech-university-hysys-hybrid-ai-online-course-2026.html) | 官方培训页，说明 HYSYS/Aspen Plus 离线模型可结合 plant data、Hybrid Models 和 online digital twins 做监控、优化、洞察和故障支持 | [AspenTech University EHM105 course](https://esupport.aspentech.com/UniversityCourse?id=a3pUn0000028hg9IAA) | HTML 快照 |
| 官方 | [official/aspentech-ehm105-ai-powered-digital-twin-agenda.pdf](official/aspentech-ehm105-ai-powered-digital-twin-agenda.pdf) | EHM105 课程议程，覆盖 HYSYS Workbook、Microsoft Excel and Aspen HYSYS、Plant Data、AI Model Builder、Hybrid Models、Aspen OnLine 发布 | [EHM105 course agenda PDF](https://www.aspentech.com/-/media/aspentech/home/support-and-training/training-agendas/ehm105-course-agenda.pdf) | 真 PDF |
| 官方 | [official/aspen-hybrid-models-customer-faq.pdf](official/aspen-hybrid-models-customer-faq.pdf) | Hybrid Models FAQ，补强 AI + first principles + simulation/plant data 的边界说明，适合约束 hybrid AI 不替代 HYSYS baseline | [Aspen Hybrid Models FAQ PDF](https://www.aspentech.com/-/media/aspentech/home/resources/faq-documents/pdfs/fy22/q2/at-06496-hybrid-models-customer-faq.pdf?sc_lang=en) | 真 PDF |
| 官方 | [official/aspen-simulation-workbook-product-page.html](official/aspen-simulation-workbook-product-page.html) | 证明 Aspen 官方支持 Excel / workbook 桥接仿真变量与流程数据 | [Aspen Simulation Workbook product page](https://www.aspentech.com/en/products/engineering/aspen-simulation-workbook) | HTML 快照 |
| 官方 | [official/aspentech-course-catalog.pdf](official/aspentech-course-catalog.pdf) | 证明 Aspen 培训体系覆盖 HYSYS 优化、动态分析、LNG、Excel/workbook 等主题 | [AspenTech course catalog PDF](https://www.aspentech.com/-/media/aspentech/home/customer-help/aspentech-course-catalog.pdf?hash=35328F62068FD84D73AB9A55D8197071&sc_lang=en) | 真 PDF |
| 官方 | [official/aspen-elearning-catalog-2025-04.pdf](official/aspen-elearning-catalog-2025-04.pdf) | 补充 2025-04 eLearning 目录，覆盖 HYSYS 基础、分析报告、Simulation Workbook、自动化方案、动态仿真和 LNG 课程入口 | [Aspen eLearning catalog PDF](https://www.aspentech.com/-/media/aspentech/home/knowledge/elearning/aspen_elearning_catalog_040525.pdf) | 真 PDF |
| 官方 | [official/aspen-hybrid-models-product-page.html](official/aspen-hybrid-models-product-page.html) | 证明 Aspen 官方已经把 Industrial AI / Hybrid Models 与 Aspen HYSYS、Aspen Plus 等过程模拟器放在同一叙事中 | [Aspen Hybrid Models product page](https://www.aspentech.com/en/solutions/aspen-hybrid-models) | HTML 快照 |
| 官方 | [official/aspen-hysys-python-spreadsheet-article.html](official/aspen-hysys-python-spreadsheet-article.html) | 公开支持站文章页，确认 Jump Start 入口与附件编号 | [Aspen HYSYS V8.0 Jump Start article](https://esupport.aspentech.com/S_Article?id=000060539) | 匿名可取文章页，附件需额外门禁 |
| 官方 | [official/aspen-hysys-customization-guide-article.html](official/aspen-hysys-customization-guide-article.html) | 公开支持站文章页，确认 Customization Guide 条目与附件编号 `a0g0B00000GfJSC` | [Aspen HYSYS V7.3 Customization Guide article](https://esupport.aspentech.com/s_Article?key=131879) | 匿名可取文章页，附件直链返回门户 HTML |
| 社区 | [community/Aspen_HYSYS_Python-README.md](community/Aspen_HYSYS_Python-README.md) | 说明社区公开采用 spreadsheet 作为 Python 控制桥 | [edgarsmdn/Aspen_HYSYS_Python](https://github.com/edgarsmdn/Aspen_HYSYS_Python) | MIT 仓库 |
| 社区 | [community/HYSYS_python_spreadsheets.py](community/HYSYS_python_spreadsheets.py) | 直接展示 `win32com` + spreadsheet 连接方式 | [raw file](https://raw.githubusercontent.com/edgarsmdn/Aspen_HYSYS_Python/main/HYSYS_python_spreadsheets.py) | 代码快照 |
| 社区 | [community/Test_1.py](community/Test_1.py) | 展示 solver 开关和等待求解完成的控制节奏 | [raw file](https://raw.githubusercontent.com/edgarsmdn/Aspen_HYSYS_Python/main/Test_1.py) | 代码快照 |
| 社区 | [community/Test_1.hsc](community/Test_1.hsc) | 公开样例 case，可作为 bridge 演示输入 | [raw file](https://raw.githubusercontent.com/edgarsmdn/Aspen_HYSYS_Python/main/Test_1.hsc) | 真 HSC 文件 |
| 社区 | [community/SCADABR-PYTHON-README.md](community/SCADABR-PYTHON-README.md) | 公开 Python-SCADABR/Modbus 教程，辅助理解 HYSYS/Python/ScadaBR 论文中的外部监督桥接层 | [LizandroCloud/SCADABR-PYTHON](https://github.com/LizandroCloud/SCADABR-PYTHON) | 不是 HYSYS API 文档；只作 SCADA bridge 参考 |
| 社区 | [community/SCADABR-PYTHON-servidor.py](community/SCADABR-PYTHON-servidor.py) | 展示 Python 端 Modbus server/bridge 写法，可为培训、dashboard 或 testbed 提供接口参考 | [raw file](https://raw.githubusercontent.com/LizandroCloud/SCADABR-PYTHON/main/tutorial/servidor.py) | 代码快照 |
| 社区 | [community/SCADABR-PYTHON-teste-scada.py](community/SCADABR-PYTHON-teste-scada.py) | 展示 Python 与 SCADA 通信测试脚本节奏 | [raw file](https://raw.githubusercontent.com/LizandroCloud/SCADABR-PYTHON/main/tutorial/teste-scada.py) | 代码快照 |
| 研究 | [research/sketch2simulation-arxiv-2603.24629.pdf](research/sketch2simulation-arxiv-2603.24629.pdf) | 证明多智能体 LLM 已开始面向 Aspen HYSYS 生成可执行 Python COM 脚本 | [Sketch2Simulation PDF](https://arxiv.org/pdf/2603.24629.pdf) | 真 PDF |
| 研究 | [research/sketch2simulation-arxiv-2603.24629-abstract.html](research/sketch2simulation-arxiv-2603.24629-abstract.html) | 保留论文摘要页面与原始编号 | [Sketch2Simulation abstract](https://arxiv.org/abs/2603.24629) | HTML 快照 |
| 研究 | [research/text-to-simulation-arxiv-2601.06776.pdf](research/text-to-simulation-arxiv-2601.06776.pdf) | 证明 LLM 多智能体已开始从文本过程规格生成可计算仿真配置；用于约束 greenfield 自动仿真仍属研究/原型路径 | [Text to Simulation PDF](https://arxiv.org/pdf/2601.06776) | 真 PDF；不等同于 HYSYS 生产级从零建模 |
| 研究 | [research/text-to-simulation-arxiv-2601.06776-abstract.html](research/text-to-simulation-arxiv-2601.06776-abstract.html) | 保留 text-to-simulation 论文摘要页面与原始编号 | [Text to Simulation abstract](https://arxiv.org/abs/2601.06776) | HTML 快照 |
| 研究 | [research/llm-agent-process-simulation-arxiv-2601.11650.pdf](research/llm-agent-process-simulation-arxiv-2601.11650.pdf) | 记录 LLM agent 通过 MCP server 和 Python 与严谨流程模拟器交互的跨模拟器证据；用于补强工具边界、step-by-step 模式和专家监督要求 | [LLM agent process simulation PDF](https://arxiv.org/pdf/2601.11650) | 真 PDF；AVEVA APS 案例，不是 HYSYS 直接证据 |
| 研究 | [research/llm-agent-process-simulation-arxiv-2601.11650-abstract.html](research/llm-agent-process-simulation-arxiv-2601.11650-abstract.html) | 保留 LLM agent process simulation 论文摘要页面与原始编号 | [LLM agent process simulation abstract](https://arxiv.org/abs/2601.11650) | HTML 快照 |
| 研究 | [research/hysys-coding-platforms-jglobal-2025.html](research/hysys-coding-platforms-jglobal-2025.html) | 记录 2025 Computers & Chemical Engineering 论文书目信息：Python-HYSYS 对象层级、特殊对象、backdoor variables 和仿真优化/技术经济工具 | [J-GLOBAL article metadata](https://jglobal.jst.go.jp/en/public/202502285695228497) | HTML 元数据；原文 DOI `10.1016/j.compchemeng.2025.109247` |
| 研究 | [research/hysys-interconnection-methodologies-sim2-2022.pdf](research/hysys-interconnection-methodologies-sim2-2022.pdf) | 对比 HYSYS direct communication、indirect communication、internal spreadsheets、data tables 四类连接方式，为控制通道选择提供同行评议依据 | [SIM2 public PDF](https://papers.sim2.be/assets/uploads/files/1c6ba-communicationarticle.pdf) | 真 PDF；ScienceDirect DOI `10.1016/j.compchemeng.2022.107785` |
| 研究 | [research/hysys-scadabr-python-supervisory-control-mdpi-2026.pdf](research/hysys-scadabr-python-supervisory-control-mdpi-2026.pdf) | 2026 Methane 论文，描述 Aspen HYSYS/Python 与 ScadaBR 通过 Modbus 连接，用于实时监控、监督和动态模型验证 | [MDPI DOI](https://doi.org/10.3390/methane5010008) | 真 PDF；高价值直接 HYSYS/Python/SCADA 证据 |
| 研究 | [research/hysys-scadabr-python-supervisory-control-mdpi-2026-crossref.json](research/hysys-scadabr-python-supervisory-control-mdpi-2026-crossref.json) | 保存 HYSYS/Python/ScadaBR 论文的 Crossref 元数据、摘要、发布日期和开放许可 | [Crossref metadata](https://api.crossref.org/works/10.3390/methane5010008) | JSON 元数据 |
| 研究 | [notes/heartbeat-scan-2026-05-01.md](notes/heartbeat-scan-2026-05-01.md) | 记录 2026 International Journal of Hydrogen Energy 氢液化论文线索：Aspen HYSYS V12 + Python COM automation interface 用于系统化数据提取、模块化仿真、自动敏感性和优化分析 | [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0360319925061464) | ScienceDirect 摘要页下载失败；仅保存 CASE 笔记，不保存伪快照 |
| 研究 | [research/pinn-digital-twin-arxiv-2603.24644.pdf](research/pinn-digital-twin-arxiv-2603.24644.pdf) | 证明 HYSYS 生成动态数据后可进入 PINN / digital twin / soft sensing / MPC / anomaly detection 研究链路 | [PINN digital twin PDF](https://arxiv.org/pdf/2603.24644.pdf) | 真 PDF，不等同于直接 COM 控制 |
| 研究 | [research/pinn-digital-twin-arxiv-2603.24644-abstract.html](research/pinn-digital-twin-arxiv-2603.24644-abstract.html) | 保留 PINN 数字孪生论文摘要页面与原始编号 | [PINN digital twin abstract](https://arxiv.org/abs/2603.24644) | HTML 快照 |
| 研究 | [notes/heartbeat-test-2026-04-27-cjce-hysys-ml.md](notes/heartbeat-test-2026-04-27-cjce-hysys-ml.md) | 记录 2026 CJCE HYSYS 原油蒸馏 + 机器学习代理模型论文的元数据、访问限制、价值判断和边界结论 | [ResearchGate metadata](https://www.researchgate.net/publication/400895104_Data-driven_simulation_of_crude_distillation_using_Aspen_HYSYS_and_comparative_machine_learning_models), [DOI](https://doi.org/10.1002/cjce.70297) | Wiley/ResearchGate 匿名抓取受访问控制阻断；仅保存 CASE 笔记，不保存伪 PDF |
| 研究 | [research/hysys-lng-surrogate-jcp-2026-metadata.html](research/hysys-lng-surrogate-jcp-2026-metadata.html) | 记录 2026 Journal of Cleaner Production LNG surrogate 论文元数据，补强“仿真数据 -> ML surrogate -> LNG 优化/低数字碳足迹”的研究证据 | [SQU metadata](https://squ.elsevierpure.com/en/publications/artificial-intelligence-driven-surrogate-modeling-for-computation/), [DOI](https://doi.org/10.1016/j.jclepro.2026.148110) | HTML 元数据；ScienceDirect 摘要页显示使用 Aspen HYSYS V14，不保存全文 |
| 研究 | [research/hysys-psd-xgboost-pso-springer-2026.html](research/hysys-psd-xgboost-pso-springer-2026.html) | 2026 Korean Journal of Chemical Engineering 论文页面：Aspen HYSYS 压力摆动精馏模型结合 XGBoost 与 PSO 做热负荷预测和工况优化 | [Springer article](https://link.springer.com/article/10.1007/s11814-026-00646-x) | HTML 快照 |
| 研究 | [research/hysys-psd-xgboost-pso-springer-2026.pdf](research/hysys-psd-xgboost-pso-springer-2026.pdf) | 论文 PDF：补强“HYSYS baseline -> ML surrogate -> optimizer -> HYSYS/人工复核”的边界证据 | [Springer PDF](https://link.springer.com/content/pdf/10.1007/s11814-026-00646-x.pdf) | 真 PDF；不等同于 surrogate 替代 HYSYS baseline |
| 研究 | [notes/heartbeat-scan-2026-04-30.md](notes/heartbeat-scan-2026-04-30.md) | 记录 HEFA / SAF production planning surrogate 论文线索、访问限制和项目边界；补强 surrogate 与 PIMS/计划优化系统之间的边界 | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S009813542600102X), [SSRN DOI](https://doi.org/10.2139/ssrn.5373950) | ScienceDirect/AIChE/SSRN 匿名访问受限；仅保存 CASE 笔记，不保存伪快照 |
| 研究 | [research/reasoning-agent-distillation-nature-2026.pdf](research/reasoning-agent-distillation-nature-2026.pdf) | 2026 Nature Communications Engineering 论文，展示 LLM reasoning agent 自动化流程仿真、优化、碳核算和节能方案构建 | [Nature DOI](https://doi.org/10.1038/s44172-025-00583-3) | 真 PDF；Aspen Plus 相邻证据，不是 HYSYS 直接证据 |
| 研究 | [research/reasoning-agent-distillation-nature-2026.html](research/reasoning-agent-distillation-nature-2026.html) | 保存 reasoning-agent distillation 论文页面，用于核对 DOI、发布日期、摘要和开放状态 | [Nature article page](https://www.nature.com/articles/s44172-025-00583-3) | HTML 快照 |
| 本地沉淀 | [notes/local-lng-hysys-study.md](notes/local-lng-hysys-study.md) | 你自己已有的 HYSYS LNG 学习与模板提炼沉淀 | 本地文件复制 | 不是公网来源，但很适合并入技能经验层 |
| 本地沉淀 | [notes/local-lng-route-template.md](notes/local-lng-route-template.md) | 你自己已有的液化路线选择模板 | 本地文件复制 | 用于后续场景化扩展 |
| 中文总结 | [notes/hysys-source-digest.md](notes/hysys-source-digest.md) | 把官方、社区、研究三类资料压缩成技能设计结论 | 本仓库 | 推荐先读 |
| 心跳记录 | [notes/heartbeat-scan-2026-04-25.md](notes/heartbeat-scan-2026-04-25.md) | 记录 2026-04-25 手动心跳测试保存的新资料、价值判断和边界结论 | 本仓库 | 后续每日扫描可沿用此格式 |
| 心跳记录 | [notes/heartbeat-scan-2026-04-26.md](notes/heartbeat-scan-2026-04-26.md) | 记录 2026-04-26 自动心跳保存的新资料、价值判断、项目改进和推送状态 | 本仓库 | 每日自动化闭环样例 |
| 心跳记录 | [notes/heartbeat-scan-2026-04-27.md](notes/heartbeat-scan-2026-04-27.md) | 记录 2026-04-27 自动心跳保存的新资料、价值判断、项目改进和推送状态 | 本仓库 | 每日自动化闭环样例 |
| 心跳记录 | [notes/heartbeat-scan-2026-04-28.md](notes/heartbeat-scan-2026-04-28.md) | 记录 2026-04-28 自动心跳保存的新资料、价值判断、项目改进和推送状态 | 本仓库 | 每日自动化闭环样例 |
| 心跳记录 | [notes/heartbeat-scan-2026-04-30.md](notes/heartbeat-scan-2026-04-30.md) | 记录 2026-04-30 自动心跳保存的新资料、价值判断、项目改进和推送状态 | 本仓库 | 每日自动化闭环样例 |
| 心跳记录 | [notes/heartbeat-scan-2026-05-01.md](notes/heartbeat-scan-2026-05-01.md) | 记录 2026-05-01 自动心跳保存的新资料、价值判断、项目改进和推送状态 | 本仓库 | 每日自动化闭环样例 |
| 心跳记录 | [notes/heartbeat-scan-2026-05-02.md](notes/heartbeat-scan-2026-05-02.md) | 记录 2026-05-02 自动心跳保存的新资料、价值判断、项目改进和推送状态 | 本仓库 | 每日自动化闭环样例 |
| 心跳记录 | [notes/heartbeat-scan-2026-05-05.md](notes/heartbeat-scan-2026-05-05.md) | 记录 2026-05-05 自动心跳保存的新资料、价值判断、项目改进和推送状态 | 本仓库 | 每日自动化闭环样例 |
| 心跳记录 | [notes/heartbeat-scan-2026-05-11.md](notes/heartbeat-scan-2026-05-11.md) | 记录 2026-05-11 自动心跳保存的 HYSYS/Python/ScadaBR、SCADABR-PYTHON 和 reasoning-agent 资料、价值判断、项目改进和边界结论 | 本仓库 | 每日自动化闭环样例 |
| 心跳记录 | [notes/heartbeat-scan-2026-05-12.md](notes/heartbeat-scan-2026-05-12.md) | 记录 2026-05-12 自动心跳保存的 Tüpraş HYSYS column performance 官方案例和 Springer HYSYS+XGBoost/PSO 资料、价值判断、项目改进和边界结论 | 本仓库 | 每日自动化闭环样例 |
| 发布打法 | [notes/release-playbook.md](notes/release-playbook.md) | 借鉴 AI-DWSIM-Skill 的成功路径，为 AI-HYSYS-Skill 准备发布策略 | 本仓库 | 推荐发布前再读一遍 |

## 2026-07-03 新增索引

| 类别 | 本地文件 | 作用 | 原始链接 | 备注 |
|---|---|---|---|---|
| 社区 | [community/aspen-pysys-pypi-json-2026-07-03.json](community/aspen-pysys-pypi-json-2026-07-03.json) | `aspen-pysys` PyPI 0.1.0a3 元数据；HYSYS Python wrapper 候选，GPL-3.0-or-later、Python >=3.12.12、pywin32>=311，未做本地 HYSYS runtime 验证 | [aspen-pysys PyPI](https://pypi.org/project/aspen-pysys/) | B- 候选；不作为默认依赖 |
| 社区/相邻 | [community/aps-agent-gsi-lab-readme-2026-07-03.md](community/aps-agent-gsi-lab-readme-2026-07-03.md) | `gsi-lab/APS-Agent` README 快照；AVEVA Process Simulation MCP agent，相邻证明 MCP server 可包装严谨流程模拟器工具 | [gsi-lab/APS-Agent](https://github.com/gsi-lab/APS-Agent) | B 相邻架构证据；不是 HYSYS API |
| 社区/相邻 | [community/aps-agent-gsi-lab-metadata-2026-07-03.json](community/aps-agent-gsi-lab-metadata-2026-07-03.json) | `gsi-lab/APS-Agent` GitHub 元数据快照，MIT 许可证、Python、2026-06-11 更新 | [GitHub API](https://api.github.com/repos/gsi-lab/APS-Agent) | 配合 README/tree/license 快照使用 |
| 社区/相邻 | [community/aps-agent-gsi-lab-tree-2026-07-03.json](community/aps-agent-gsi-lab-tree-2026-07-03.json) | `gsi-lab/APS-Agent` tree 快照；用于确认 MCP server、tool 包、compiled modules 和 requirements 结构 | [GitHub tree](https://api.github.com/repos/gsi-lab/APS-Agent/git/trees/main?recursive=1) | 不下载或运行二进制 `.pyd` |
| 社区/相邻 | [community/aps-agent-gsi-lab-license-2026-07-03.txt](community/aps-agent-gsi-lab-license-2026-07-03.txt) | `gsi-lab/APS-Agent` MIT license 快照 | [raw license](https://raw.githubusercontent.com/gsi-lab/APS-Agent/main/LICENSE) | 许可证证据 |
| 研究/相邻 | [research/text-to-flowsheet-zenodo-19910216-2026-07-03.json](research/text-to-flowsheet-zenodo-19910216-2026-07-03.json) | Text-to-flowsheet RSC/Zenodo 元数据快照；LLM-assisted flowsheet digitization、Graph-IR、black-box optimization 相邻证据 | [RSC article](https://pubs.rsc.org/en/content/articlelanding/2026/dd/d6dd00060f), [Zenodo record](https://zenodo.org/records/19910216) | B 相邻；不证明 HYSYS greenfield 可靠 |
| 心跳记录 | [notes/heartbeat-scan-2026-07-03.md](notes/heartbeat-scan-2026-07-03.md) | 2026-07-03 心跳记录：aspen-pysys 0.1.0a3、APS-Agent、Text-to-flowsheet 的价值判断和项目边界更新 | 本仓库 | 本轮维护摘要 |

## 2026-07-04 新增索引

| 类别 | 本地文件 | 作用 | 原始链接 | 备注 |
|---|---|---|---|---|
| 社区/直接 | [community/aspen-hysys-mcp-server-readme-2026-07-04.md](community/aspen-hysys-mcp-server-readme-2026-07-04.md) | `yuuyo-arobet/AspenHYSYS-MCP-Server` README 快照；HYSYS-specific MCP + pywin32/COM 控制候选，包含 51 tools、只读/会话/写入模式门和 HYSYS V14 实机验证声明 | [yuuyo-arobet/AspenHYSYS-MCP-Server](https://github.com/yuuyo-arobet/AspenHYSYS-MCP-Server) | B+ 直接社区证据；不作为默认依赖 |
| 社区/直接 | [community/aspen-hysys-mcp-server-metadata-2026-07-04.json](community/aspen-hysys-mcp-server-metadata-2026-07-04.json) | GitHub 元数据快照，记录描述、许可证、更新时间和仓库状态 | [GitHub API](https://api.github.com/repos/yuuyo-arobet/AspenHYSYS-MCP-Server) | MIT；低公开采用信号，需本地复核 |
| 社区/直接 | [community/aspen-hysys-mcp-server-tree-2026-07-04.json](community/aspen-hysys-mcp-server-tree-2026-07-04.json) | 仓库 tree 快照；用于确认 `src/hysys_mcp`、tool 分层、registry、tests 和 docs 结构 | [GitHub tree](https://api.github.com/repos/yuuyo-arobet/AspenHYSYS-MCP-Server/git/trees/main?recursive=1) | 只记录结构，不下载整仓库 |
| 社区/直接 | [community/aspen-hysys-mcp-server-architecture-2026-07-04.md](community/aspen-hysys-mcp-server-architecture-2026-07-04.md) | 架构说明快照；用于学习 MCP server、COM client、tool registry、mode gate 和测试分层 | [architecture doc](https://raw.githubusercontent.com/yuuyo-arobet/AspenHYSYS-MCP-Server/main/docs/ARCHITECTURE.md) | 设计参考，不等同于本仓库 runtime 验证 |
| 社区/直接 | [community/aspen-hysys-mcp-server-license-2026-07-04.txt](community/aspen-hysys-mcp-server-license-2026-07-04.txt) | MIT license 快照 | [raw license](https://raw.githubusercontent.com/yuuyo-arobet/AspenHYSYS-MCP-Server/main/LICENSE) | 许可证证据 |
| 心跳记录 | [notes/heartbeat-scan-2026-07-04.md](notes/heartbeat-scan-2026-07-04.md) | 2026-07-04 心跳记录：HYSYS-specific MCP server 价值判断、未采纳默认依赖原因和项目边界更新 | 本仓库 | 本轮维护摘要 |

## 2026-07-05 新增索引

| 类别 | 本地文件 | 作用 | 原始链接 | 备注 |
|---|---|---|---|---|
| 社区/直接 | [community/simulator-codingplatform-integration-readme-2026-07-05.md](community/simulator-codingplatform-integration-readme-2026-07-05.md) | `Anikesh31/simulator_codingplatform_integration` README 快照；补强 HYSYS + Python/MATLAB 连接、对象/属性读取、backdoor variables、方法参数检查和 TEA 示例证据 | [Anikesh31/simulator_codingplatform_integration](https://github.com/Anikesh31/simulator_codingplatform_integration) | B+；与 DOI `10.1016/j.compchemeng.2025.109247` 对应，许可证未识别 |
| 社区/直接 | [community/simulator-codingplatform-integration-metadata-2026-07-05.json](community/simulator-codingplatform-integration-metadata-2026-07-05.json) | GitHub 元数据快照，记录公开状态、更新时间、星标和 license 字段 | [GitHub API](https://api.github.com/repos/Anikesh31/simulator_codingplatform_integration) | 只作证据，不作为默认依赖 |
| 社区/直接 | [community/simulator-codingplatform-integration-tree-2026-07-05.json](community/simulator-codingplatform-integration-tree-2026-07-05.json) | 仓库 tree 快照；用于确认教程代码结构 | [GitHub tree](https://api.github.com/repos/Anikesh31/simulator_codingplatform_integration/git/trees/main?recursive=1) | 不下载整仓库 |
| 社区/直接 | [community/pysis-readme-2026-07-05.md](community/pysis-readme-2026-07-05.md) | `DanielVazVaz/PySIS` README 快照；HYSYS COM 抽象层候选，README 声称支持 HYSYS V11/V12/V14 | [DanielVazVaz/PySIS](https://github.com/DanielVazVaz/PySIS) | B；许可证未识别，未做本地 runtime 验证 |
| 社区/直接 | [community/pysis-metadata-2026-07-05.json](community/pysis-metadata-2026-07-05.json) | GitHub 元数据快照，记录公开状态、更新时间、星标、fork 和 license 字段 | [GitHub API](https://api.github.com/repos/DanielVazVaz/PySIS) | Wrapper watchlist，不作为默认依赖 |
| 社区/直接 | [community/pysis-tree-2026-07-05.json](community/pysis-tree-2026-07-05.json) | 仓库 tree 快照；用于确认包结构和文档入口 | [GitHub tree](https://api.github.com/repos/DanielVazVaz/PySIS/git/trees/master?recursive=1) | 不下载整仓库 |
| 心跳记录 | [notes/heartbeat-scan-2026-07-05.md](notes/heartbeat-scan-2026-07-05.md) | 2026-07-05 心跳记录：HYSYS coding-platform companion repo、PySIS wrapper 的价值判断和未采纳默认依赖原因 | 本仓库 | 本轮维护摘要 |

## 2026-07-06 新增索引

| 类别 | 本地文件 | 作用 | 原始链接 | 备注 |
|---|---|---|---|---|
| 社区/直接 | [community/ap-python-readme-2026-07-06.md](community/ap-python-readme-2026-07-06.md) | `bsha0/ap-python` README 快照；Aspen Plus/HYSYS Python automation package，展示 HYSYS moniker、`get_units`、`get_value`、`set_value`、`save` 和 `saveas` 包装模式 | [bsha0/ap-python](https://github.com/bsha0/ap-python) | B；MIT，老仓库，未做本地 runtime 验证 |
| 社区/直接 | [community/ap-python-metadata-2026-07-06.json](community/ap-python-metadata-2026-07-06.json) | GitHub 元数据快照，记录公开状态、更新时间、星标、fork 和 license 字段 | [GitHub API](https://api.github.com/repos/bsha0/ap-python) | Wrapper watchlist，不作为默认依赖 |
| 社区/直接 | [community/ap-python-tree-2026-07-06.json](community/ap-python-tree-2026-07-06.json) | 仓库 tree 快照；用于确认包结构、测试和 HYSYS/Plus 子模块入口 | [GitHub tree](https://api.github.com/repos/bsha0/ap-python/git/trees/master?recursive=1) | 不下载整仓库 |
| 社区/直接 | [community/ap-python-license-2026-07-06.txt](community/ap-python-license-2026-07-06.txt) | MIT license 快照 | [raw license](https://raw.githubusercontent.com/bsha0/ap-python/master/LICENSE) | 许可证证据 |
| 心跳记录 | [notes/heartbeat-scan-2026-07-06.md](notes/heartbeat-scan-2026-07-06.md) | 2026-07-06 心跳记录：`ap-python` 价值判断、LNG 冷能 GA 论文未采纳原因和 wrapper watchlist 更新 | 本仓库 | 本轮维护摘要 |

## 2026-07-07 新增索引

| 类别 | 本地文件 | 作用 | 原始链接 | 备注 |
|---|---|---|---|---|
| 研究/直接 | [research/hysys-automation-aspen-excel-vba-cae-2023-crossref.json](research/hysys-automation-aspen-excel-vba-cae-2023-crossref.json) | Crossref 元数据：`Automation in the simulation of processes with Aspen HYSYS: An academic approach`，补强 HYSYS 自动化、Excel/VBA/外部脚本控制通道证据 | [DOI 10.1002/cae.22589](https://doi.org/10.1002/cae.22589) | B+；元数据可访问，PDF 下载返回非 PDF，未保存伪文件 |
| 研究/相邻 | [research/llm-agent-process-simulation-crossref-2026-07-07.json](research/llm-agent-process-simulation-crossref-2026-07-07.json) | Crossref 元数据：`Large language model agent for user-friendly chemical process simulations`，确认 Digital Chemical Engineering 期刊版 DOI、发布日期和许可信息 | [DOI 10.1016/j.dche.2026.100312](https://doi.org/10.1016/j.dche.2026.100312) | B；相邻 APS/MCP agent 证据，不是 HYSYS 专属 API |
| 心跳记录 | [notes/heartbeat-scan-2026-07-07.md](notes/heartbeat-scan-2026-07-07.md) | 2026-07-07 心跳记录：HYSYS 自动化 CAE 论文、LLM-agent 期刊元数据、未采纳官方课程/LinkedIn/泛 MCP 资料原因 | 本仓库 | 本轮维护摘要 |

## 2026-07-10 新增索引

| 类别 | 本地文件 | 作用 | 原始链接 | 备注 |
|---|---|---|---|---|
| 研究/相邻 | [research/llm-pse-survey-arxiv-2606.11589-abstract-2026-07-10.html](research/llm-pse-survey-arxiv-2606.11589-abstract-2026-07-10.html) | arXiv 摘要页：`Large Language Models in Process Systems Engineering`，确认 2026-06-10 提交、作者、摘要和 DOI | [arXiv 2606.11589](https://arxiv.org/abs/2606.11589) | B；PSE/LLM 相邻综述，不是 HYSYS 专属证据 |
| 研究/相邻 | [research/llm-pse-survey-arxiv-2606.11589.pdf](research/llm-pse-survey-arxiv-2606.11589.pdf) | 论文 PDF；用于沉淀 LLM 在 PSE 的机会、架构、工业部署挑战，以及“能力展示 vs 愿景主张”的边界 | [PDF](https://arxiv.org/pdf/2606.11589) | 真 PDF；用于边界规则，不用于声明 HYSYS 从零建模可靠 |
| 心跳记录 | [notes/heartbeat-scan-2026-07-10.md](notes/heartbeat-scan-2026-07-10.md) | 2026-07-10 心跳记录：PSE/LLM 综述的价值判断、未采纳重复资料原因和项目边界影响 | 本仓库 | 本轮维护摘要 |

## 访问说明

- AspenTech 支持站的文章页可以匿名抓到，但附件直链在匿名访问时会返回门户 HTML。因此仓库里保留文章页和附件编号，不保留伪 PDF。
- 课程目录和 arXiv 论文是可稳定落盘的真 PDF，因此直接作为 CASE 正式资料保留。
- 社区代码与样例 case 仅作为公开桥接示例，不等同于官方 HYSYS API 文档。
