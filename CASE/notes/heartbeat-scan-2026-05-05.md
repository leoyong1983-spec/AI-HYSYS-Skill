# AI-HYSYS 心跳扫描记录：2026-05-05

## 扫描目的

按既定闭环执行：搜索 AI 控制 Aspen HYSYS、HYSYS COM/Python/Spreadsheet/Workbook 自动化、LLM 工艺模拟 agent、HYSYS digital twin / hybrid AI 资料；与 [../source-index.md](../source-index.md) 比对；有价值则保存到 CASE，必要时更新项目规则，校验后提交推送。

## 新增资料已保存

| 类别 | 本地文件 | 原始来源 | 价值判断 |
|---|---|---|---|
| 官方 | [../official/aspen-hysys-mysep-live-process-digital-twin-2026.html](../official/aspen-hysys-mysep-live-process-digital-twin-2026.html) | [AspenTech MySep live process digital twin webinar](https://www.aspentech.com/en/resources/on-demand-webinars/apac-webinar-en-driving-throughput-and-efficiency-with-digital-twin) | 有价值。官方页面明确描述 live process digital twin 集成 Aspen HYSYS 与 MySep Engine 严谨分离器模型，用于 brownfield operations、real-time performance、carryover risk、throughput、energy efficiency 和 KPI limits。 |
| 官方 | [../official/aspen-hysys-saudi-aramco-plant-digital-twin-2026.html](../official/aspen-hysys-saudi-aramco-plant-digital-twin-2026.html) | [AspenTech Saudi Aramco plant digital twin case study](https://www.aspentech.com/en/resources/case-studies/saudi-aramco-increases-capacity-by-100000-barrels-day-and-upgrades-bottom-of-the-barrel-products) | 有价值。官方页面说明 Saudi Aramco 使用 Aspen HYSYS 建立多个装置 plant digital twins，用于炼厂改造可行性分析和处理能力提升方案评估。 |
| 官方 | [../official/aspen-hysys-indian-oil-barauni-process-digital-twins-2026.html](../official/aspen-hysys-indian-oil-barauni-process-digital-twins-2026.html) | [AspenTech Indian Oil Barauni process digital twins webinar](https://www.aspentech.com/en/resources/on-demand-webinars/apac-webinar-en-learn-how-a-major-indian-refinery-gained-substantial-benefits) | 有价值。官方页面说明 Indian Oil Barauni Refinery 部署 Aspen HYSYS-based process digital twins，用于炼厂运行优化和不可实时测量 KPI 的工程场景。 |

## 重复或暂不入库

- arXiv LLM process simulation 论文已在 [heartbeat-scan-2026-05-02.md](heartbeat-scan-2026-05-02.md) 登记，本轮不重复。
- HYSYS V12 + Python COM 氢液化论文已在 [heartbeat-scan-2026-05-01.md](heartbeat-scan-2026-05-01.md) 登记，本轮不重复。
- 搜索到的泛泛营销页和无 HYSYS 技术细节的内容不入库。

## 对项目的实际改进

1. [../source-index.md](../source-index.md) 增加三份 AspenTech 官方 digital twin 快照和本次心跳记录。
2. [hysys-source-digest.md](hysys-source-digest.md) 增加 live process digital twin / multi-unit plant digital twin / refinery process digital twins 的项目化结论。
3. [../../references/digital-twin-boundary.md](../../references/digital-twin-boundary.md) 增加第三方严谨模型、brownfield live operation、多装置数字孪生和不可实时测量 KPI 的边界。
4. [../../SKILL.md](../../SKILL.md) 增加第三方模型和多装置 digital twin 任务的拆分要求。
5. [../../README.md](../../README.md) 增加三条 AspenTech 官方引用。

## 边界结论

本轮资料增强了 AI-HYSYS-Skill 的官方证据链：HYSYS 可以参与 live process digital twin、multi-unit plant digital twin 和 refinery process digital twins。

它支持以下主张：

1. AI-HYSYS-Skill 可帮助整理已有 HYSYS baseline、外部模型接口、KPI、实时数据口径和审计报告。
2. 当 HYSYS 与 MySep、historian、dashboard、Aspen OnLine 或其他外部系统结合时，必须把外部系统列为边界。
3. 多装置数字孪生任务应拆成 unit-level model、site-level scenario、data source、KPI、validation 和 human acceptance。

它不支持以下主张：

1. 开源 skill 可以复刻 AspenTech/第三方商业 live digital twin 产品。
2. AI 可以绕过 HYSYS runtime、第三方模型、现场数据治理或人工工程审核。
3. live KPI 或 carryover risk 建议可以默认自动回写生产控制系统。
