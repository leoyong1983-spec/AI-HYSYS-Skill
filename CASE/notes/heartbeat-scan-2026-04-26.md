# AI-HYSYS 心跳扫描记录：2026-04-26

## 扫描目的

自动测试每日心跳闭环：搜索 AI 控制 Aspen HYSYS、HYSYS 自动化、Industrial AI、Hybrid Models、online digital twin、plant data、AI Model Builder 相关资料；判断是否足以影响 AI-HYSYS-Skill 的项目规则；有价值则保存进 `CASE/`、更新项目、校验、提交并推送。

## 新增资料已保存

| 类别 | 本地文件 | 原始来源 | 价值判断 |
|---|---|---|---|
| 官方 | [../official/aspentech-whats-new-v15-industrial-ai-2026.html](../official/aspentech-whats-new-v15-industrial-ai-2026.html) | [AspenTech V15 What's New](https://solutions.aspentech.com/en/whats-new) | 证明 AspenTech 当前产品语境已经把 Industrial AI、AI Model Builder、Aspen HYSYS/Plus、Aspen OnLine 和 HYSYS/Plus online workflows 放在同一产品路线中。 |
| 官方 | [../official/aspentech-university-hysys-hybrid-ai-online-course-2026.html](../official/aspentech-university-hysys-hybrid-ai-online-course-2026.html) | [AspenTech University EHM105](https://esupport.aspentech.com/UniversityCourse?id=a3pUn0000028hg9IAA) | 官方培训页说明从 HYSYS/Aspen Plus 离线模型、plant data、Hybrid Models 到 online digital twin 的工作流，适合补强 skill 的 digital twin 边界。 |
| 官方 | [../official/aspentech-ehm105-ai-powered-digital-twin-agenda.pdf](../official/aspentech-ehm105-ai-powered-digital-twin-agenda.pdf) | [EHM105 course agenda PDF](https://www.aspentech.com/-/media/aspentech/home/support-and-training/training-agendas/ehm105-course-agenda.pdf) | 课程议程明确覆盖 Aspen HYSYS Workbook、Microsoft Excel and Aspen HYSYS、Plant Data、AI Model Builder、Hybrid Models、Aspen OnLine 发布。 |
| 官方 | [../official/aspen-hybrid-models-customer-faq.pdf](../official/aspen-hybrid-models-customer-faq.pdf) | [Aspen Hybrid Models FAQ PDF](https://www.aspentech.com/-/media/aspentech/home/resources/faq-documents/pdfs/fy22/q2/at-06496-hybrid-models-customer-faq.pdf?sc_lang=en) | FAQ 强调 Hybrid Models 是 AI + first principles + simulation/plant data 的组合，可用于约束“hybrid AI 不能替代 HYSYS baseline”的项目边界。 |

## 对项目的实际改进

1. [../../references/digital-twin-boundary.md](../../references/digital-twin-boundary.md) 已补入 offline model、plant data、AI Model Builder、Hybrid Models、Aspen OnLine 的边界说明。
2. [../source-index.md](../source-index.md) 已加入本轮新增官方来源。
3. 校验脚本改为自动检查根目录、`references/` 和 `CASE/notes/` 下的 Markdown 文件，避免未来每日新增心跳记录时还要手工维护校验列表。

## 边界结论

这些资料增强的是“AI-HYSYS-Skill 可以服务 HYSYS online/digital-twin/hybrid-AI 工作流的前置整理、通道判断、KPI 导出、报告和审计”这一主张。

它们仍不支持把仓库宣传为：

- AI 可稳定从零创建复杂 HYSYS 工艺模型。
- Hybrid Model 可替代 HYSYS baseline、物性包、设备拓扑或人工审核。
- Aspen OnLine / AI Model Builder 等商业产品可由本开源 skill 自动复刻。

## 自动化结果

- 仓库验证：`.\scripts\validate_repo.ps1` 已通过。
- Python 语法检查：`scripts/hysys_automation.py` 与 `scripts/validate_repo.py` 已通过 `py_compile`。
- 安全检查：未发现明显密钥/凭证文件，未发现超过 50MB 的文件。
- 待完成：提交并推送到 GitHub。
