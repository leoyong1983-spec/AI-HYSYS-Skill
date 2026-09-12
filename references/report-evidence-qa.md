# Report Evidence QA / 报告同源与可读性验收

Use for a HYSYS-based process explanation or Office deliverable, not for every solver call. Follow the project's chosen template and final formats. Report preparation does not by itself authorize recalculation or a topology change.

## One Accepted Snapshot / 一份报告对应一个可追溯状态

报告建立在明确的案例哈希、软件版本、运行模式和验收记录上。正文、表格及图中数据从同一份已核实快照取数，统一单位与舍入。源文件哈希与快照不符时，不能只更新记录里的哈希继续称为“已验证”；应重新取证或说明仅讨论历史版本。

Explain the process by function and flow before presenting object inventories. Identify separate material networks and their energy coupling using actual bindings; label any simplified illustration as explanatory, not as a replacement for the native PFD.

Before publication, check that the report distinguishes fresh feed from internal circulation, gross product from target-component output, composition bases, shaft duty from electrical demand, and circulating inventory from makeup consumption. Do not infer missing boundaries or convert unknown native values into zero.

## Independent Gates / 分开记录验收结果

| Gate | Evidence needed | Does not establish |
| --- | --- | --- |
| Data consistency | Case identity, accepted snapshot, units and report-to-table checks | Current plant or equipment performance |
| Document integrity | DOCX structure and required sections, resolvable MD assets | Visual readability |
| Native application check | Open, update fields where applicable, save, close and reopen in the intended office application | All pages visually inspected |
| Visual review | Render and inspect the actual pages, including tables, figures and changed pagination | Engineering acceptance |

默认工程报告提供 DOCX 与 MD，过程图及校验记录按项目目录约定存放。面向 Microsoft Word 的交付，优先在可用的 Word 中做最终保存重开与排版检查；只管理本任务创建的文档和实例，不结束用户会话。工具不可用时说明未完成哪道检查，不能用结构检查代替视觉检查。项目明确选择其他渲染路线时记录工具和限制，不照搬别的项目的软件禁用偏好。

For visual QA, inspect the complete document at a readable scale: clipped figures, crowded tables, page breaks, fields/TOC, placeholders and Chinese glyphs. After a fix, recheck every page affected by repagination. Keep QA PDF/images as local process evidence; they are not extra final deliverables unless requested. Check Markdown image paths from the delivered location.

Report calculation verification, document QA and remaining engineering decisions separately. Do not mark unperformed checks as passed. This reference defines the acceptance workflow; it does not install a Word renderer or claim a report was generated in the current task.
