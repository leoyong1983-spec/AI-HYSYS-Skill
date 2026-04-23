# 基础工艺包交付层规则

## 目标

本技能的目标不是单独跑一个 Aspen HYSYS case，而是把 HYSYS 运行结果稳定转成可审计、可发审的基础工艺包交付链。

## 默认交付分层

### 1. 机器可读源层

先导出：

- `case_summary.json`
- `key_streams.csv`
- `key_operations.csv`
- `utility_summary.csv`
- `solver_status.md`
- `assumptions.md`
- `open_issues.md`

如果项目采用 spreadsheet / workbook bridge，也可以附：

- `named_cells.csv`
- `dashboard_inputs.csv`
- `dashboard_outputs.csv`

这层是正式 `Word / Excel / PowerPoint` 的数据源层。

### 2. 正式 Office 层

当项目进入基础工艺包审查版时，正式件通常包括：

- 物料衡算工作簿
- 热量衡算工作簿
- 主要设备表
- 公用工程汇总表
- 人工裁决登记表
- 基础工艺包主文稿
- 交付清单与问题说明
- 发审传递说明
- 审查汇报材料

### 3. 审查支持层

进入发审准备后，应补齐：

- 审查会首读指引
- 发审范围说明
- 审查意见登记表
- 审查意见闭环流程
- 需要后补的接口范围说明

## 默认边界

如果项目已经进入 review-stage basic process package：

- 不再继续自由调优
- 不再改 frozen baseline
- layout 副本只允许视觉微调
- 可以补做 reader-friendly workbook / dashboard，但不能伪装成新的计算真源

## 发布门禁

### Release blocker

如果发现冻结 case 真实对象，与导出层或包件文本不一致：

1. 立即建立 `RB-xx`
2. 暂停新增增强类工作
3. 优先做只读 inventory、export refresh、package 刷新和 QA 复核

### 人工裁决

可以存在 `OPEN human decisions`，但不能存在“未登记的 release blocker”。

## 中文交付约束

如果项目要求中文交付：

- 提交目录名、文件名、读者可见正文优先中文
- 必要英文术语应加中文注释
- 路径、位号、流股标签、API 名称可保留
- 不要把终端显示乱码误判为文件真损坏

## HYSYS 专项提醒

- 若 direct COM 与 spreadsheet bridge 同时存在，以 machine-readable export 为正式源，以 dashboard/workbook 为可读辅助层
- 不要把 workbook 中的手工改值历史当成正式审计记录；正式记录要回写到 case、日志或导出文件
- 若 case 分为 steady-state 与 dynamic 两套，必须显式说明交付基于哪一套，不得混用
