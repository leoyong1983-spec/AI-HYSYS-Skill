# CASE Source Index

准备日期：2026-04-21（Asia/Shanghai）
最近心跳测试：2026-04-25（Asia/Shanghai）

这个目录不是“随手存链接”，而是 AI-HYSYS-Skill 的公开素材底座。建议先读 [notes/hysys-source-digest.md](notes/hysys-source-digest.md)，再按需要下钻到具体文件。

## 使用原则

1. `official/` 里的 AspenTech 页面用于证明 HYSYS、Workbook、培训入口和支持入口是真实存在的官方能力。
2. `community/` 里的公开仓库用于证明 Python 控制 HYSYS 的 spreadsheet bridge 路径已经有人公开落地。
3. `research/` 里的论文用于证明 “AI 直接生成 HYSYS 可执行建模脚本” 这条线已经进入公开研究。
4. `notes/` 里的中文文件用于把这些来源压缩成可发布、可讲述、可复用的话术和方法论。

## 索引表

| 类别 | 本地文件 | 作用 | 原始链接 | 备注 |
|---|---|---|---|---|
| 官方 | [official/aspen-hysys-product-page.html](official/aspen-hysys-product-page.html) | 证明 HYSYS 官方覆盖 steady-state、dynamic studies、process safety、AI optimization 等工作流 | [Aspen HYSYS product page](https://www.aspentech.com/en/products/engineering/aspen-hysys) | HTML 快照 |
| 官方 | [official/aspen-hysys-2025-brochure-page.html](official/aspen-hysys-2025-brochure-page.html) | 补充 2026 可访问的 HYSYS brochure 页面，强调经济、能耗、安全、排放、全生命周期和 model-backed intelligence | [Aspen HYSYS brochure page](https://www.aspentech.com/en/resources/brochure/aspen-hysys) | HTML 快照 |
| 官方 | [official/aspen-hysys-brochure-2025-05.pdf](official/aspen-hysys-brochure-2025-05.pdf) | 保存 2025-05 官方 HYSYS brochure PDF，补强 Industrial AI、model-backed intelligence、经济、能耗、安全、排放等产品叙事 | [Aspen HYSYS brochure PDF](https://www.aspentech.com/-/media/aspentech/home/resources/brochure/pdfs/fy25/q4/at-4162_bro_aspen-hysys_final_0525.pdf) | 真 PDF |
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
| 研究 | [research/sketch2simulation-arxiv-2603.24629.pdf](research/sketch2simulation-arxiv-2603.24629.pdf) | 证明多智能体 LLM 已开始面向 Aspen HYSYS 生成可执行 Python COM 脚本 | [Sketch2Simulation PDF](https://arxiv.org/pdf/2603.24629.pdf) | 真 PDF |
| 研究 | [research/sketch2simulation-arxiv-2603.24629-abstract.html](research/sketch2simulation-arxiv-2603.24629-abstract.html) | 保留论文摘要页面与原始编号 | [Sketch2Simulation abstract](https://arxiv.org/abs/2603.24629) | HTML 快照 |
| 研究 | [research/hysys-coding-platforms-jglobal-2025.html](research/hysys-coding-platforms-jglobal-2025.html) | 记录 2025 Computers & Chemical Engineering 论文书目信息：Python-HYSYS 对象层级、特殊对象、backdoor variables 和仿真优化/技术经济工具 | [J-GLOBAL article metadata](https://jglobal.jst.go.jp/en/public/202502285695228497) | HTML 元数据；原文 DOI `10.1016/j.compchemeng.2025.109247` |
| 研究 | [research/hysys-interconnection-methodologies-sim2-2022.pdf](research/hysys-interconnection-methodologies-sim2-2022.pdf) | 对比 HYSYS direct communication、indirect communication、internal spreadsheets、data tables 四类连接方式，为控制通道选择提供同行评议依据 | [SIM2 public PDF](https://papers.sim2.be/assets/uploads/files/1c6ba-communicationarticle.pdf) | 真 PDF；ScienceDirect DOI `10.1016/j.compchemeng.2022.107785` |
| 研究 | [research/pinn-digital-twin-arxiv-2603.24644.pdf](research/pinn-digital-twin-arxiv-2603.24644.pdf) | 证明 HYSYS 生成动态数据后可进入 PINN / digital twin / soft sensing / MPC / anomaly detection 研究链路 | [PINN digital twin PDF](https://arxiv.org/pdf/2603.24644.pdf) | 真 PDF，不等同于直接 COM 控制 |
| 研究 | [research/pinn-digital-twin-arxiv-2603.24644-abstract.html](research/pinn-digital-twin-arxiv-2603.24644-abstract.html) | 保留 PINN 数字孪生论文摘要页面与原始编号 | [PINN digital twin abstract](https://arxiv.org/abs/2603.24644) | HTML 快照 |
| 本地沉淀 | [notes/local-lng-hysys-study.md](notes/local-lng-hysys-study.md) | 你自己已有的 HYSYS LNG 学习与模板提炼沉淀 | 本地文件复制 | 不是公网来源，但很适合并入技能经验层 |
| 本地沉淀 | [notes/local-lng-route-template.md](notes/local-lng-route-template.md) | 你自己已有的液化路线选择模板 | 本地文件复制 | 用于后续场景化扩展 |
| 中文总结 | [notes/hysys-source-digest.md](notes/hysys-source-digest.md) | 把官方、社区、研究三类资料压缩成技能设计结论 | 本仓库 | 推荐先读 |
| 心跳记录 | [notes/heartbeat-scan-2026-04-25.md](notes/heartbeat-scan-2026-04-25.md) | 记录 2026-04-25 手动心跳测试保存的新资料、价值判断和边界结论 | 本仓库 | 后续每日扫描可沿用此格式 |
| 发布打法 | [notes/release-playbook.md](notes/release-playbook.md) | 借鉴 AI-DWSIM-Skill 的成功路径，为 AI-HYSYS-Skill 准备发布策略 | 本仓库 | 推荐发布前再读一遍 |

## 访问说明

- AspenTech 支持站的文章页可以匿名抓到，但附件直链在匿名访问时会返回门户 HTML。因此仓库里保留文章页和附件编号，不保留伪 PDF。
- 课程目录和 arXiv 论文是可稳定落盘的真 PDF，因此直接作为 CASE 正式资料保留。
- 社区代码与样例 case 仅作为公开桥接示例，不等同于官方 HYSYS API 文档。
