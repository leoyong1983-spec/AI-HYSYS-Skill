# 权威路径与执行通道选择

## 结论先行

把 Aspen HYSYS 交给 AI 控制时，推荐把执行通道分成三层：

1. `HYSYS.Application / COM` 作为主控制层
2. `Spreadsheet / Aspen Simulation Workbook` 作为稳定 tagged IO 层
3. `Python / PowerShell` 作为 orchestration、批量试算、导出和审计层

不要反过来。

如果需要在 direct COM、spreadsheet/workbook、data tables、indirect communication、GUI fallback 之间做具体选择，先读 [control-lane-decision-matrix.md](control-lane-decision-matrix.md)。这份文件把 2022 HYSYS interconnection 论文和 2025 Python-HYSYS automation 论文转成了可执行决策规则。

原因很直接：

- 官方 AspenTech 产品页明确把 HYSYS 放在 steady-state、dynamic studies、process safety、optimization 这一整套工程工作流里，而不是单一黑箱算例工具。
- 官方 Aspen Simulation Workbook 产品页明确证明了 “把仿真变量稳定映射到 Excel / workbook 工作流” 是 Aspen 官方支持的路径。
- 官方支持站公开文章页面给出了 `Jump Start` 和 `Customization Guide` 入口，说明 HYSYS 的自动化、对象访问和基础建模学习路径是长期存在的。
- 社区公开仓库 `Aspen_HYSYS_Python` 明确采用 “HYSYS spreadsheet 作为 Python 控制桥” 来绕开脆弱的对象路径访问。
- 2022 年 HYSYS interconnection 论文明确把通信方式拆成 direct communication、indirect communication、internal spreadsheets、data tables 四类。
- 2025 年 Python-HYSYS 论文进一步说明，真实自动化会碰到对象层级、特殊对象、backdoor variables、优化和技术经济工具等问题。
- 当前仓库内置的 [`scripts/hysys_automation.py`](../scripts/hysys_automation.py) 已经证明 direct COM 这条路可以稳定处理启动、开 case、保存、ASCII staging 和基础对象操作。

## 外部权威依据

### 1. Aspen HYSYS 官方产品定位

来源：

- [Aspen HYSYS product page](https://www.aspentech.com/en/products/engineering/aspen-hysys)
- 本地快照：[CASE/official/aspen-hysys-product-page.html](../CASE/official/aspen-hysys-product-page.html)

这页最重要的信号不是营销词，而是它公开展示了 HYSYS 的工作域：

1. steady-state 与 dynamic studies 都在同一产品族内
2. process safety analysis 被明确挂在 HYSYS 应用场景下
3. optimization、integrated workflows、AI positioning 都已经公开绑定到这个产品叙事里
4. 这意味着 AI-HYSYS-Skill 不能只定位成 “读写几个变量”，而要定位成 “可接管工程工作流”

### 2. Aspen Simulation Workbook 官方桥接层

来源：

- [Aspen Simulation Workbook product page](https://www.aspentech.com/en/products/engineering/aspen-simulation-workbook)
- 本地快照：[CASE/official/aspen-simulation-workbook-product-page.html](../CASE/official/aspen-simulation-workbook-product-page.html)

这条来源最关键的价值：

1. 官方明确支持把 simulation data 和 process data 映射到 Microsoft Excel
2. 官方强调 intuitive workflow、visual dashboards、non-simulator users 也能消费模型
3. 对 AI 代理来说，这意味着 workbook / spreadsheet 不是旁门，而是合法的稳定接口层

### 3. AspenTech 支持站公开入口

来源：

- [Aspen HYSYS V8.0 Jump Start article](https://esupport.aspentech.com/S_Article?id=000060539)
- [Aspen HYSYS V7.3 Customization Guide article](https://esupport.aspentech.com/s_Article?key=131879)
- 本地快照：
  - [CASE/official/aspen-hysys-python-spreadsheet-article.html](../CASE/official/aspen-hysys-python-spreadsheet-article.html)
  - [CASE/official/aspen-hysys-customization-guide-article.html](../CASE/official/aspen-hysys-customization-guide-article.html)

当前公开可匿名访问的是文章页与附件入口信息。

从文章页可以确认：

1. `Jump Start` 是官方面向基础建模的公开入口
2. `Customization Guide` 作为正式文档条目长期存在
3. 这为对象模型、变量路径、自动化接口的存在性提供了官方背书

注意：

- 截至 2026-04-21，AspenTech 支持站附件直链在匿名下载时返回门户 HTML，而不是真 PDF。
- 所以仓库里保留的是文章页与附件编号，而不是伪装成 PDF 的无效文件。

### 4. AspenTech 培训目录

来源：

- [AspenTech course catalog PDF](https://www.aspentech.com/-/media/aspentech/home/customer-help/aspentech-course-catalog.pdf?hash=35328F62068FD84D73AB9A55D8197071&sc_lang=en)
- 本地快照：[CASE/official/aspentech-course-catalog.pdf](../CASE/official/aspentech-course-catalog.pdf)
- [EHY2311: Developing Automation Solutions for Aspen HYSYS](https://esupport.aspentech.com/UniversityCourse?id=a3p0B0000004Yn6QAE)
- 本地快照：[CASE/official/aspentech-ehy2311-hysys-automation-course-2026-07-16.html](../CASE/official/aspentech-ehy2311-hysys-automation-course-2026-07-16.html)

这份目录至少说明：

1. HYSYS 官方培训覆盖 optimization、dynamic analysis、LNG modeling、process safety 等场景
2. Excel/workbook 类工作流在 Aspen 培训体系里本来就是正式主题
3. AI-HYSYS-Skill 的定位可以理直气壮地放在 “工程工作流接管”，而不是只放在 “小脚本玩具”
4. EHY2311 进一步明确覆盖 HYSYS Type Library、Excel Object Browser、VBA、User Variables、User Operations、调试和跨 simulation 信息连接
5. 这些官方主题支持本仓库的通道分类，但不能替代项目本地 runtime smoke test、单位/求解器检查和人工验收

### 5. AspenTech 平台支持与版本前提

来源：

- [AspenTech Platform Support](https://www.aspentech.com/en/platform-support)
- [V15 Engineering Platform Specifications PDF](https://www.aspentech.com/-/media/aspentech/home/platform-support/v15/v15engspecs.pdf)
- 本地快照：
  - [CASE/official/aspentech-platform-support-2026-05.html](../CASE/official/aspentech-platform-support-2026-05.html)
  - [CASE/official/aspentech-v15-engineering-platform-specifications-2026.pdf](../CASE/official/aspentech-v15-engineering-platform-specifications-2026.pdf)

这条来源用于 readiness 和版本迁移，不用于宣称自动化能力。

它要求本 skill 把以下问题分开：

1. HYSYS 或 Aspen Engineering Suite 是否安装、授权并可启动。
2. 当前 Windows、Office、Python、pywin32 和 COM 注册是否满足项目需要。
3. Aspen OnLine、AI Model Builder、Hybrid Models、PIMS、APC/GDOT 等是否是当前项目实际可用资产，还是外部商业产品边界。
4. 如果平台前提不满足，先报告环境 blocker，不要把它包装成 AI prompt 或脚本调参问题。

### 6. 同行评议的 HYSYS interconnection 与 Python-HYSYS automation

来源：

- [hysys-interconnection-methodologies-sim2-2022.pdf](../CASE/research/hysys-interconnection-methodologies-sim2-2022.pdf)
- [hysys-coding-platforms-jglobal-2025.html](../CASE/research/hysys-coding-platforms-jglobal-2025.html)

这两条来源把“能不能连上 HYSYS”推进到“如何选择正确控制通道”：

1. 2022 年论文把 HYSYS 通信方式拆成 direct communication、indirect communication、internal spreadsheets、data tables。
2. 这说明 spreadsheet bridge 不是孤立技巧，而是可以纳入正式 interconnection taxonomy 的通道。
3. 2025 年论文强调 Python 与 Aspen HYSYS 的对象层级、特殊对象、backdoor variables、仿真优化和技术经济工具。
4. 这要求 AI-HYSYS-Skill 在写入参数前先做 lane decision，而不是直接把所有变量都当成普通对象属性。

## 社区与项目内的可执行依据

### 1. 社区 spreadsheet bridge 示例

来源：

- [edgarsmdn/Aspen_HYSYS_Python](https://github.com/edgarsmdn/Aspen_HYSYS_Python)
- 本地快照：
  - [CASE/community/Aspen_HYSYS_Python-README.md](../CASE/community/Aspen_HYSYS_Python-README.md)
  - [CASE/community/HYSYS_python_spreadsheets.py](../CASE/community/HYSYS_python_spreadsheets.py)
  - [CASE/community/Test_1.py](../CASE/community/Test_1.py)

这个示例的核心不是代码风格，而是策略：

1. 它明确说 HYSYS 变量路径访问有时会很麻烦
2. 它因此选择 spreadsheet 作为 Python 控制桥
3. 它还明确提醒要控制 solver 开关并等待求解完成

这对 AI 代理非常重要，因为：

- direct COM 适合 authoritative control
- spreadsheet bridge 适合稳定批量 IO 和低摩擦参数注入

### 2. 第三方 HYSYS Python wrapper 候选

来源：

- [aspen_pysys PyPI JSON](../CASE/community/aspen-pysys-pypi-json-2026-05-22.json)
- [CacklingTanuki/aspen-pysys Codeberg page](../CASE/community/aspen-pysys-codeberg-page-2026-05-22.html)

这条来源说明社区开始出现更直接的 HYSYS Python wrapper，但当前只能作为候选，不应直接升级为默认依赖。

原因：

1. 2026-05-22 扫描时版本为 `0.1.0a0`，属于 alpha。
2. PyPI 元数据要求 Python `>=3.12.12` 和 `pywin32>=311`，与项目现场常见 Python 环境未必一致。
3. 许可为 `GPL-3.0-or-later`，不能不经评估就并入本 MIT 仓库的默认运行依赖。
4. README 仍以已有或可打开的 HYSYS simulation case 为前提，不证明从零建模或生产级自动化可靠。
5. 未在当前本地 Aspen HYSYS runtime 上做 smoke test 前，只能作为参考实现或候选线索。

因此默认策略仍是：先用本仓库 direct COM starter 和 spreadsheet/workbook bridge 证明控制通道，再按项目许可和运行环境决定是否单独试用第三方 wrapper。

2026-05-22 源码核查补充：`aspen_pysys` 的当前公开快照值得学习的是 typed wrapper / object factory / primitive adapter 这类分层思想，而不是直接并入代码。核查时未发现单独 `.pyi` 类型存根文件，也未确认存在可直接复用的跨进程路径哈希缓存树；不应把它描述成已验证的生产级高性能执行层。

本仓库吸收的低风险工程点是：

1. 在 `scripts/hysys_automation.py` 中保持会话内 operation / spreadsheet 对象缓存，减少同一 case 内的重复 COM 对象查找。
2. 在 spreadsheet readback 后先执行 COM 返回值标准化，把常见 tuple/list/array-like 值转成普通 Python 容器，再交给后续 JSON、Pydantic 或报告层处理。
3. 明确 HYSYS empty-value sentinel `-32767` 的处理位置，但不把第三方 GPL 代码复制进 MIT 仓库。

### 3. 仓库内 direct COM 包装层

来源：

- [`scripts/hysys_automation.py`](../scripts/hysys_automation.py)

它已经体现出几个关键工程判断：

1. 启动要有 retry
2. `.hsc` 文件在非 ASCII 路径下要考虑 staging
3. `TEMP/TMP` 目录要可控
4. save / save as / close / quit 要显式管理

这说明 direct COM 不只是 “能连上”，而是可以被整理成可审计执行通道。

## 推荐执行通道

### 主通道

`PowerShell / Python orchestration -> HYSYS.Application / COM -> Aspen HYSYS`

适用场景：

- 环境接管
- smoke test
- 现有 case 加载
- 读写对象属性
- 计算与收敛
- 冻结基线
- 导出 `CSV / JSON / Markdown`
- 发布前一致性检查

### 稳定桥接通道

`Python / PowerShell -> Spreadsheet or Aspen Simulation Workbook -> Aspen HYSYS`

适用场景：

- 变量路径太深、太脆弱、不适合直接 object-path 操作
- 需要人类也能看懂的参数面板
- 需要批量读取 KPI、报表值、设计变量
- 需要给非 HYSYS 深度用户一个受控操作面

### 辅助通道

`Excel / VBA -> Workbook / Spreadsheet -> Aspen HYSYS`

只在以下条件成立时启用：

1. 项目里已经有成熟桥接层
2. 用户明确要求保留这个遗留工作流
3. direct COM 或脚本化桥接不适合当前任务

### 补充通道

`HYSYS data tables / special objects -> controlled read-write workflow`

适用场景：

- HYSYS case 中已经配置了 Data Table、Design Spec、Optimizer、Column、Spreadsheet 等特殊对象
- 这些对象已经有稳定名称、单位和读写边界
- 任务是读取表格化结果、做窄范围扫描或配合既有模型结构调参

注意：

- Data tables 和特殊对象不能替代 case baseline。
- 每次使用前都要记录 schema、单位、读写方向和 solver policy。
- 若需要 backdoor variables，必须先做单点 smoke test，不允许直接批量写入。

## fallback 顺序

1. 复用项目内已验证 runner
2. 直接 `HYSYS.Application`
3. Spreadsheet / Workbook bridge
4. Data tables / special-object lane
5. Excel / VBA / Matlab / C# / intermediate-file 既有桥
6. GUI

## 不建议的误区

- 不要因为 spreadsheet bridge 更容易看懂，就把它误当成唯一权威执行层
- 不要在没有验证 `HYSYS.Application` 启动和开 case 能力前，直接假设 Python 包一定能控住 HYSYS
- 不要把 GUI 点击当成生产主路径
- 不要在没有冻结命名和结构前，让 AI 直接大规模改 flowsheet topology

## 技能内的默认判断

如果同时存在多条可行路径，默认选择：

1. 当前项目里已经证明成功的 runner
2. 否则选择 direct COM
3. 如果 direct COM 对变量访问太脆弱，而 spreadsheet/workbook 已经成型，则把它作为稳定 IO 层
4. GUI 只保留给 visual sign-off 或 unavoidable checks
