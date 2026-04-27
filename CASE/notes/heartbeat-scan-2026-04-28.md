# AI-HYSYS 心跳扫描记录：2026-04-28

## 扫描目的

按既定闭环执行：搜索 AI 控制 Aspen HYSYS、HYSYS COM/Python/Spreadsheet/Workbook 自动化、LLM 工艺模拟 agent、HYSYS digital twin / hybrid AI / surrogate model 资料；与 [../source-index.md](../source-index.md) 比对；有价值则保存到 CASE，必要时更新项目规则，校验后提交推送。

## 新增资料已保存

| 类别 | 本地文件 | 原始来源 | 价值判断 |
|---|---|---|---|
| 官方 | [../official/aspen-hysys-online-simulation-models-webinar-2026.html](../official/aspen-hysys-online-simulation-models-webinar-2026.html) | [AspenTech on-demand webinar](https://www.aspentech.com/en/resources/on-demand-webinars/deploy-simulation-models-online-easily-gain-unrivaled-process-insights) | 官方页面明确把 Aspen HYSYS models、online simulations、KPI monitoring、process insights、energy efficiency、emissions reduction 和 troubleshooting 放在同一叙事中，补强 online digital twin / Aspen OnLine 边界。 |
| 官方 | [../official/aspen-hysys-dynamics-product-page-2026.html](../official/aspen-hysys-dynamics-product-page-2026.html) | [Aspen HYSYS Dynamics product page](https://www.aspentech.com/en/products/engineering/aspen-hysys-dynamics) | 官方页面说明 HYSYS Dynamics 支持动态仿真、瞬态条件分析和内置模板；这补强“动态任务必须从已验证 steady-state baseline 受控转换”的边界。 |
| 研究 | [../research/hysys-lng-surrogate-jcp-2026-metadata.html](../research/hysys-lng-surrogate-jcp-2026-metadata.html) | [Sultan Qaboos University metadata](https://squ.elsevierpure.com/en/publications/artificial-intelligence-driven-surrogate-modeling-for-computation/), [DOI](https://doi.org/10.1016/j.jclepro.2026.148110) | 2026 Journal of Cleaner Production LNG surrogate 论文元数据；公开摘要显示用仿真数据训练 Random Forest 代理模型，在 LNG 优化中降低计算时间/数字碳足迹，适合补强 LNG surrogate 任务边界。 |

## 有价值但未保存全文的资料

| 来源 | 访问状态 | 价值判断 |
|---|---|---|
| On the use of Surrogate Models to enhance the production planning of sustainable aviation fuels via the hydroprocessed esters and fatty acids process | SSRN 页面和 PDF 匿名下载被 Cloudflare / JavaScript / cookie challenge 阻断；不保存伪 PDF。 | 有价值。公开搜索结果显示该工作使用 Aspen AI Model Builder、Aspen HYSYS simulation、Aspen PIMS-AO 和 HEFA 路线，说明 surrogate 可以服务生产计划优化，但不等同于本 skill 可替代 PIMS、AI Model Builder 或商业计划系统。 |

## 重复或暂不入库

- `Data-driven simulation of crude distillation using Aspen HYSYS and comparative machine learning models` 已在 [heartbeat-test-2026-04-27-cjce-hysys-ml.md](heartbeat-test-2026-04-27-cjce-hysys-ml.md) 登记，本轮不重复保存。
- 搜索到的课程营销页、软件选型页和泛泛博客没有新增工程证据，不入库。

## 对项目的实际改进

1. [../source-index.md](../source-index.md) 增加两个 AspenTech 官方快照、一个 LNG surrogate 元数据快照和本次心跳笔记。
2. [hysys-source-digest.md](hysys-source-digest.md) 增加 2026-04-28 结论：online deployment、dynamic simulation 和 surrogate planning 都应拆成边界清楚的工程层。
3. [../../references/digital-twin-boundary.md](../../references/digital-twin-boundary.md) 增加 online simulation、HYSYS Dynamics、LNG surrogate 和 planning surrogate 的边界条目。
4. [../../SKILL.md](../../SKILL.md) 增加 dynamic simulation、production planning / PIMS、distributed control / online deployment 的拆分要求。
5. [../../README.md](../../README.md) 增加新官方页和研究链接，方便访客核验。

## 边界结论

本轮资料继续增强同一条主线：AI-HYSYS-Skill 最可靠的定位仍是接管已有可运行 HYSYS case，做参数接管、验证、导出、报告和受控数据集生成。

它们不支持把本仓库宣传为：

1. 可从零自动构建生产级 HYSYS 模型。
2. 可复刻 Aspen OnLine、Aspen AI Model Builder、Aspen PIMS-AO 或商业 Hybrid Models。
3. 可把 surrogate / soft sensor / digital twin 输出直接用于生产闭环控制。
4. 可跳过 HYSYS runtime、人类工程审核或项目既有批准流程。
