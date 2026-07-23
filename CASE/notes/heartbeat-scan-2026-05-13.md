# AI-HYSYS 心跳扫描记录：2026-05-13

## 扫描目的

按既定闭环执行：搜索 AI 控制 Aspen HYSYS、HYSYS COM/Python/Spreadsheet/Workbook 自动化、LLM 工艺模拟 agent、HYSYS digital twin / hybrid AI 资料；与 [../source-index.md](../source-index.md) 比对；有价值则保存到 CASE，必要时更新项目规则，校验后提交推送。

## 新增资料已保存

| 类别 | 本地文件 | 原始来源 | 价值判断 |
|---|---|---|---|
| 官方 | [../official/aspen-online-product-page-2026.html](../official/aspen-online-product-page-2026.html) | [Aspen OnLine product page](https://www.aspentech.com/en/products/engineering/aspen-online) | 高价值。官方页面明确把 live data、process simulation、plant historian / lab data、Aspen Plus 和 Aspen HYSYS project files 放在 Aspen OnLine 工作流中，补齐本仓库对 online deployment 商业系统边界的证据链。 |
| 研究 | [../research/first-principles-modeling-age-ai-crossref-2026.json](../research/first-principles-modeling-age-ai-crossref-2026.json) | [Crossref metadata](https://api.crossref.org/works/10.1021/acs.iecr.5c04156) | 高价值。IECR 2026 综述《Perspectives on the Essential Role of First-Principles Modeling in the Age of AI》从方法论上支持“AI/hybrid/surrogate 不能替代 first-principles baseline”的项目边界。 |
| 研究 | [../research/first-principles-modeling-age-ai-tudelft-2026.html](../research/first-principles-modeling-age-ai-tudelft-2026.html) | [TU Delft Research Portal](https://research.tudelft.nl/en/publications/perspectives-on-the-essential-role-of-first-principles-modeling-i/) | 有价值。保存可访问的高校研究门户页面，用于核对题名、作者、期刊、DOI、页码和 peer-review 类型；不保存 ACS 正文 PDF。 |

## 重复或暂不入库

- `Aspen OnLine` 已在前序资料中被提到，但此前主要来自 webinar/course agenda；本轮新增的是官方产品页，价值更高。
- ACS 页面匿名访问返回 Cloudflare challenge，已删除伪快照；只保留 Crossref 元数据和 TU Delft 研究门户页面。
- 泛泛 AI marketing、未说明 HYSYS/COM/Workbook/Online/Hybrid boundary 的搜索结果不入库。

## 对项目的实际改进

1. [../source-index.md](../source-index.md) 增加 Aspen OnLine 官方产品页、IECR 2026 第一性原理建模综述和本次心跳记录。
2. [hysys-source-digest.md](hysys-source-digest.md) 增加 online model deployment 与 first-principles baseline 的项目化结论。
3. [../../references/digital-twin-boundary.md](../../references/digital-twin-boundary.md) 增加 Aspen OnLine、plant historian/lab data、first-principles model、hybrid/surrogate 层之间的边界。
4. [../../README.md](../../README.md) 增加两条高层引用，方便访客从首页追溯证据。

## 边界结论

本轮资料进一步强化了当前项目定位：AI-HYSYS-Skill 负责已有 HYSYS case 的接管、变量映射、验证、KPI、报告和审计输出，不复刻 Aspen OnLine，也不让 AI 取代第一性原理模型。

它支持以下主张：

1. 如果项目进入 online / live data / historian 场景，应把 HYSYS/Aspen Plus 模型、plant historian/lab data、Aspen OnLine 发布层、KPI 和人工验收责任拆开。
2. First-principles baseline 仍是 AI、hybrid model、surrogate model、soft sensor 和 optimizer 的工程锚点。
3. AI-HYSYS-Skill 可以输出上线前检查清单、tag/KPI schema、模型校验记录、审计报告和人工复核项。

它不支持以下主张：

1. 开源 skill 可以替代 Aspen OnLine 或自动发布在线模型。
2. AI/hybrid/surrogate 可以绕过 HYSYS runtime、物性包、模型验证或人工审核。
3. 只要有 live data 就可以默认闭环回写生产系统。
