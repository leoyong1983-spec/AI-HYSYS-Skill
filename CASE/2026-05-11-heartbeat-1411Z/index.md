# Aspen HYSYS CASE Heartbeat (2026-05-11 1411Z)

- 运行时间（UTC）：2026-05-11T14:11:00Z ~ 2026-05-11T14:59:44Z（约 -431.3 分钟）
- 心跳目录：CASE/2026-05-11-heartbeat-1411Z
- 触发策略：优先高质量矿区（Mendeley Data / Zenodo / Figshare / GitHub），并执行严格去重与许可检查。

## 检索矿区与关键词

- 科学数据仓储：Mendeley Data、Zenodo API、Figshare API、Dataverse (Harvard)、OSF API
- 开源托管：GitHub repository search + tree probe
- 关键词：Aspen HYSYS、.hsc、HYSYS XML、supplementary material、LNG、oil-off gas、hydrogen、CO2 capture、process simulation、lowsheet

## 去重基线与判重

- 读取了 CASE/**/sources.json 与 index.md，按 source_page、download_url、	itle、ilenames、sha256 去重。
- 对本次主目标 https://data.mendeley.com/datasets/8r8ztbkfjj/1 判重结果：
  - source_page：未命中既有记录
  - download_url：未命中既有记录
  - 主包 SHA256 417f3c0c8bcf381fd5bae591cf55ab18e75a03943d72c00d8b44a6a1c99068bf：未命中既有记录

## 下载案例清单（本次新增）

### 1) Data for: Optimization model and application for the recondensation process of boil-off gas in a liquefied natural gas receiving terminal

- 质量评级：A
- 来源页面：<https://data.mendeley.com/datasets/8r8ztbkfjj/1>
- 下载 URL：<https://data.mendeley.com/public-files/datasets/8r8ztbkfjj/files/939edba8-4b16-441d-b0bc-7609c2688f18/file_downloaded>
- 本地路径：
  - CASE/2026-05-11-heartbeat-1411Z/artifacts/Research data.zip
  - CASE/2026-05-11-heartbeat-1411Z/artifacts/mendeley-8r8ztbkfjj-metadata.json
  - CASE/2026-05-11-heartbeat-1411Z/artifacts/Research-data-zip-listing.txt
- 模型与配套：压缩包清单显示 2 个 .hsc（April to October.hsc、November to March.hsc）和大量 Excel/CSV 数据。
- 许可证/公开访问说明：Mendeley Data 元数据声明 CC BY 4.0，DOI 10.17632/8r8ztbkfjj.1。
- 选择理由：同时具备 HYSYS 模型、论文关联 DOI、结构化数据，且公开可下载，适合作为 LNG/BOG 高价值基准案例。
- 推荐自动化用途：
  - BOG 重冷凝工况回放与参数接管
  - 月度环境温度/周期敏感性分析
  - 代理模型训练数据提取（从表格与关键节点数据）

## 候选但未下载（D）

1. https://github.com/bpalotai/Flowsheet-toolbox
- 依据：早先树探测到 Cases/HX-model-V1/HysysModel/SampleModel_V2.hsc，但许可证不明确（本轮并遇到 GitHub API rate-limit）。
- 建议：人工确认许可后再归档。

2. https://data.mendeley.com/datasets/9384yj4xg3/5
- 依据：CC BY 4.0，含 Excel/图/Docx，但未暴露 .hsc/.xml。
- 建议：仅可作为验证数据参考，暂不纳入可复现 HYSYS 模型库。

3. https://data.mendeley.com/datasets/mg3rgk9xkm/1
- 依据：公共 API 返回 404（dataset not found），无法验证可用性与许可。
- 建议：后续复查版本 URL 或作者主页。

## 安全检查

- 已对下载压缩包进行清单化检查，未执行任何压缩包内 exe/脚本/宏。
- 清单中未检测到可执行文件扩展名。
- 未打开、运行或求解任何 HYSYS 模型（model_run_status = not_run）。

## 残余风险

- 大体量压缩包（205 MB）含大量表格，后续解析建议按目录与字段白名单处理。
- 仅完成“获取与静态核查”，未进行本机 HYSYS 版本兼容与收敛验证。
- GitHub 公共 API 在本轮触发限流，个别候选的许可核验需要后续补充。

## 后续建议

1. 对新入库 A 级案例补做 manifest.csv（内含 case/data 索引、相对路径、单位/字段说明）。
2. 针对 Flowsheet-toolbox 向作者确认 license，确认后可补抓该 .hsc 案例。
3. 扩展检索词："Aspen HYSYS" "CC BY" "dataset" "hsc"、"HYSYS files" "Mendeley Data"、"LNG receiving terminal" "HYSYS case"。
