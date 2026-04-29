# AI-HYSYS 心跳扫描记录：2026-04-30

## 扫描目的

按既定闭环执行：搜索 AI 控制 Aspen HYSYS、HYSYS COM/Python/Spreadsheet/Workbook 自动化、LLM 工艺模拟 agent、HYSYS digital twin / hybrid AI / surrogate model 资料；与 [../source-index.md](../source-index.md) 比对；有价值则保存到 CASE，必要时更新项目规则，校验后提交推送。

## 新增判断

| 类别 | 来源 | 保存状态 | 价值判断 |
|---|---|---|---|
| 研究 | [ScienceDirect: On the use of Surrogate Models for the Production Planning of biofuels via Hydro-processed Esters and Fatty Acids (HEFA) process](https://www.sciencedirect.com/science/article/pii/S009813542600102X) | ScienceDirect / AIChE / SSRN 匿名下载均被访问控制或 TLS/Cloudflare 挡住；不保存伪 HTML/PDF。本笔记保存可核验元数据与项目判断。 | 有价值。搜索摘要显示该工作面向 HEFA / SAF 生产计划，连接 process simulation、surrogate model 和 planning optimization；它补强“surrogate 可以服务计划优化层，但不替代 HYSYS、PIMS 或商业优化系统”的边界。 |
| 官方 | [Aspen HYSYS product page](https://www.aspentech.com/en/products/engineering/aspen-hysys) | 已有快照：[../official/aspen-hysys-product-page.html](../official/aspen-hysys-product-page.html) | 有价值但不新增文件。已有快照中包含 Aspen Hybrid Models、Powerful Optimization with AI、plant-calibrated predictive models、real-time data 等表述，可进一步支撑本项目把 AI 放在“已有模型 + 数据 + 审计”的工程边界内。 |

## 访问限制记录

本轮尝试保存以下页面失败，因此不把挑战页或错误页入库：

- AIChE proceedings 页面返回 Cloudflare JavaScript / cookie challenge。
- ScienceDirect 摘要页 `https://www.sciencedirect.com/science/article/pii/S009813542600102X` 连接被关闭。
- SSRN 页面和 PDF 入口此前已返回 Cloudflare / JavaScript / cookie challenge。

## 对项目的实际改进

1. [../source-index.md](../source-index.md) 登记 2026-04-30 心跳笔记，并增强 Aspen HYSYS 产品页在 Hybrid Models / plant-calibrated predictive models 方面的说明。
2. [hysys-source-digest.md](hysys-source-digest.md) 增加 HEFA / SAF production planning surrogate 的边界结论。
3. [../../references/digital-twin-boundary.md](../../references/digital-twin-boundary.md) 将 HEFA / production planning surrogate 证据指向本笔记，并新增 planning surrogate 默认边界。
4. [../../README.md](../../README.md) 增加 ScienceDirect HEFA surrogate 链接，方便访客核验。

## 边界结论

本轮资料不改变仓库主定位。AI-HYSYS-Skill 仍聚焦已有可运行 HYSYS case 的接管、参数更新、验证、导出和报告。

HEFA / SAF surrogate 证据只能支持以下主张：

1. HYSYS 或其他严谨仿真模型可以作为 surrogate / planning model 的数据来源。
2. surrogate 可作为生产计划、情景筛选或候选方案评估的加速层。
3. 若连接 PIMS、AI Model Builder、APC、DCS 或在线系统，必须把这些商业系统作为外部边界。
4. surrogate 输出必须保留训练范围、误差指标、目标函数、约束、适用工况和人工验收记录。

它不支持以下主张：

1. AI-HYSYS-Skill 可以替代 Aspen PIMS-AO、Aspen AI Model Builder、Aspen OnLine 或商业优化器。
2. AI 可以从零可靠构建生产级 HYSYS 模型。
3. surrogate 结果可以绕过 HYSYS runtime 和人工工程审核直接进入生产闭环。
