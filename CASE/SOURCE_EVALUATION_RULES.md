# Source Evaluation Rules / 资料评价规则

These rules are the default gate for AI-HYSYS-Skill heartbeat maintenance and can be reused by sibling engineering skills such as AI-DWSIM-Skill, AI-Phast-Skill, and AI-PyPSA-Skill.

这些规则用于判断论文、官网资料、GitHub 仓库、博客、论坛贴、wrapper、数据集或二进制资产是否值得保存、引用或影响项目规则，也可作为其他工程技能维护时的通用模板。

## Core Rule / 核心规则

Grade every source before saving, adopting, or changing project claims. Do not let a weak source inflate runtime, safety, production-control, or from-scratch modeling claims.

任何资料进入 CASE、README、SKILL 或 references 前，必须先评级。低等级资料不能把项目宣传边界抬高，尤其不能证明生产运行、自动闭环、安全审批或从零建模可靠性。

## Grades / 等级

| Grade | English rule | 中文规则 |
|---|---|---|
| A | Official vendor documentation, official product/support/training pages, or locally verified runtime evidence for the exact target software. Strongly allowed to influence skill rules. | 官方厂商文档、官方产品/支持/培训页面，或当前目标软件的本地真实运行验证证据。可以强影响技能规则。 |
| B+ | Peer-reviewed papers or high-quality technical sources directly involving the target software, automation route, runtime validation, case execution, digital twin, optimization, or reporting workflow. | 同行评审论文或高质量技术资料，并且直接涉及目标软件、自动化通道、运行验证、case 执行、数字孪生、优化或报告工作流。 |
| B | Adjacent but engineering-relevant evidence, such as Aspen Plus for a HYSYS skill, DWSIM for general process-simulation automation, MCP/COM examples, or process-systems-engineering agent papers. Use as architecture precedent only. | 相邻但工程相关的证据，例如 HYSYS 技能中的 Aspen Plus 资料、通用流程模拟自动化中的 DWSIM 资料、MCP/COM 示例或流程系统工程 agent 论文。只能作为架构借鉴。 |
| B-/C+ | Candidate sources such as preprints, small GitHub repositories, alpha wrappers, ResearchGate metadata, or lightly validated community examples. Track carefully; do not adopt as defaults. | 候选资料，例如预印本、小型 GitHub 仓库、alpha wrapper、ResearchGate 元数据或轻验证社区示例。可跟踪，不作为默认依赖或核心结论。 |
| C | Blogs, forum posts, snippets, marketing pages, or informal examples. Use only as background unless corroborated by stronger evidence. | 博客、论坛、代码片段、营销页或非正式示例。除非有更强证据交叉验证，否则只作背景信息。 |
| D | Unsafe, unclear, polluted, or unsuitable sources, including installers, unknown binaries, proprietary plant files, unclear licenses, private case files, suspicious archives, unrelated assets, or duplicates already captured. | 不安全、不清晰、污染或不适合的来源，包括安装器、未知二进制、专有工厂文件、许可证不明、私有 case、可疑压缩包、无关资产或已保存重复资料。 |

## Adoption Actions / 采纳动作

| Grade | Action |
|---|---|
| A or B+ | Save a safe snapshot when allowed, update the source index, and update SKILL/README/references if it materially improves the project. |
| B | Save metadata or a lightweight snapshot if useful, update boundaries, and explicitly label it adjacent rather than direct proof. |
| B-/C+ | Save only lightweight metadata or candidate notes unless uniquely useful. Do not add as a default dependency. |
| C | Usually do not change project rules. Record only when it explains a search or rejection decision. |
| D | Do not ingest into the normal CASE benchmark. Quarantine or reject, and record the reason when useful. |

## Required Fields / 必填字段

For every adopted or tracked source, record:

- source URL
- local path if saved
- license or access status when known
- value grade
- direct or adjacent relationship to AI-HYSYS-Skill
- why adopted
- why not adopted or not promoted
- safety, license, runtime, and boundary warnings

## Default Boundary / 默认边界

AI-HYSYS-Skill remains focused on existing runnable Aspen HYSYS cases, controlled parameter takeover, validation, audit logs, rollback, and human acceptance.

Adjacent evidence does not prove HYSYS runtime validation. Wrapper availability, code generation success, text-to-flowsheet research, or an agent framework does not prove safe production writeback or reliable from-scratch HYSYS model generation.
