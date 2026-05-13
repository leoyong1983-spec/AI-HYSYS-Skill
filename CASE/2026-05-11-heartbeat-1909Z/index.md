# Aspen HYSYS CASE Discovery Heartbeat (2026-05-11-heartbeat-1909Z)

## 1) 运行信息
- 运行目录: CASE/2026-05-11-heartbeat-1909Z
- 运行时间 (UTC): 2026-05-11T19:09Z -> 2026-05-11T19:18:08Z
- 运行时间 (Asia/Shanghai): 2026-05-12 03:18:08 +08:00
- 执行模式: Discovery & Fetch（本轮以许可合规优先，候选侦察为主）

## 2) 检索矿区与关键词
- 科学数据仓储:
  - Zenodo API: "Aspen HYSYS", "Aspen HYSYS" "case file"
  - Mendeley Data 页面/API: wzd6j2pd4v 文件清单与许可核验
  - Figshare API: Aspen HYSYS
- 开源代码托管:
  - GitHub repo search: Aspen HYSYS
  - GitHub tree inspection: .hsc, .xml, README, LICENSE, xlsx/csv/pdf
- 官方/社区公开资源:
  - 本轮仅做检索入口核查，未发现可直接公开下载且许可清晰的新 HYSYS 模型包

## 3) 去重基线
- 读取并汇总现有 CASE/**/sources.json:
  - source files: 11
  - records: 40
  - unique source_page: 38
  - unique download_url: 37
  - unique title: 40
  - unique filename: 144
  - unique sha256: 142
- 去重键: source_page, download_url, 	itle, ilenames, sha256
- 本轮重复命中示例:
  - https://data.mendeley.com/datasets/wzd6j2pd4v/1（历史已记录，且内容无 .hsc/.xml，本轮不重复下载）

## 4) 下载结果（本轮）
- 新增下载案例数: **0**
- 说明: 本轮新命中的含 .hsc 仓库均缺少明确再分发许可声明；依据约束“无法确认下载权利则仅记录候选”，未执行包下载。

## 5) 候选清单（已落盘到 sources.json）

### A) SinaGhanbarii/HDA-Plant-Simulation
- 来源页面: https://github.com/SinaGhanbarii/HDA-Plant-Simulation
- 下载 URL（未执行）: https://github.com/SinaGhanbarii/HDA-Plant-Simulation/archive/refs/heads/main.zip
- 本地证据: rtifacts/metadata_SinaGhanbarii__HDA-Plant-Simulation.json
- 选择理由: 含多份 .hsc + Excel + 报告，工程包完整度较高。
- 质量评级: D（候选）
- 许可证/公开访问说明: 仓库公开可访问，但未检测到明确 LICENSE 文件，归档再分发权利不清晰。
- 推荐自动化用途: 获授权后可用于多阶段 HYSYS case 批处理与灵敏度流程脚本基准。

### B) masoud-abdi/The-simulation-of-Acetic-Acid-process
- 来源页面: https://github.com/masoud-abdi/The-simulation-of-Acetic-Acid-process
- 下载 URL（未执行）: https://github.com/masoud-abdi/The-simulation-of-Acetic-Acid-process/archive/refs/heads/main.zip
- 本地证据: rtifacts/metadata_masoud-abdi__The-simulation-of-Acetic-Acid-process.json
- 选择理由: 含 .hsc + 报告 PDF，README 提及 HYSYS v10。
- 质量评级: D（候选）
- 许可证/公开访问说明: 仓库公开可访问，但未检测到明确 LICENSE 文件，归档再分发权利不清晰。
- 推荐自动化用途: 获授权后可用于单案例读取、流股表抽取和报告生成测试。

### C) royhanikbarr/Gas-Turbine-Hysys
- 来源页面: https://github.com/royhanikbarr/Gas-Turbine-Hysys
- 下载 URL（未执行）: https://github.com/royhanikbarr/Gas-Turbine-Hysys/archive/refs/heads/main.zip
- 本地证据: rtifacts/metadata_royhanikbarr__Gas-Turbine-Hysys.json
- 选择理由: 含 .hsc + 报告 PDF + README，主题与能量系统仿真相关。
- 质量评级: D（候选）
- 许可证/公开访问说明: 仓库公开可访问，但未检测到明确 LICENSE 文件，归档再分发权利不清晰。
- 推荐自动化用途: 获授权后可用于设备对象遍历、能量平衡报表抽取与接口稳定性测试。

## 6) 残余风险
- 许可风险: 3 个候选均缺少明确再分发许可声明。
- 可重复性风险: 未下载原始包，仅记录元数据证据，后续源仓库可能变更。
- 运行风险: 未执行任何 HYSYS 模型求解；不声明模型可计算状态。

## 7) 后续建议
1. 继续优先检索带明确开放许可（MIT/Apache/CC-BY）且含 .hsc/.xml 的仓库或数据集。
2. 对高潜候选向作者发起许可确认（允许研究归档/再分发）后再下载入库。
3. 加强 Mendeley/Zenodo DOI 反向检索策略，优先筛选 iles 清单中直接出现 .hsc 的记录。
