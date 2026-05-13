# CASE Heartbeat Index (2026-05-11-heartbeat-2213Z)

## Run Time
- UTC run timestamp: 2026-05-11T22:33:24Z
- Workspace: D:/CODEX/AI-HYSYS-Skill
- Heartbeat folder: D:/CODEX/AI-HYSYS-Skill/CASE/2026-05-11-heartbeat-2213Z

## Search Mines Covered
1. Scientific repositories: Zenodo API, Figshare API (high noise), OSF API probe.
2. Open-source hosting: GitHub repository API + tree introspection for .hsc/.xml + license filters.
3. Official/community open pages only (no login/protected portal bypass).
4. OA references: README DOI/论文链接探测。

## Keywords Used
- Aspen HYSYS case file
- Aspen HYSYS .hsc
- HYSYS XML cases .xml
- process simulation flowsheet
- model validation experimental data
- CO2 capture LNG hydrogen ammonia methanol
- GitHub API queries: hysys, Aspen HYSYS, simulation, in:readme,description

## Downloaded Cases (Non-duplicate)

### 1) COSMO Automated HYSYS Optimization Case Bundle (GitHub)
- Quality: B
- Source page: https://github.com/may3rd/COSMO
- Download URL: https://codeload.github.com/may3rd/COSMO/zip/refs/heads/main
- Local path: D:/CODEX/AI-HYSYS-Skill/CASE/2026-05-11-heartbeat-2213Z/artifacts/COSMO-main
- Key evidence: Test_1.hsc + Python automation scripts + CSV/XLSX test data + LICENSE
- License/public access note: GPL-3.0, public access.
- Recommended automation use: HYSYS COM 接口回归、案例加载冒烟、换热网络优化脚本联调。

### 2) pythonHysys Minimal Aspen HYSYS COM Case Bundle (GitHub)
- Quality: C
- Source page: https://github.com/tinchofiuba/pythonHysys
- Download URL: https://codeload.github.com/tinchofiuba/pythonHysys/zip/refs/heads/main
- Local path: D:/CODEX/AI-HYSYS-Skill/CASE/2026-05-11-heartbeat-2213Z/artifacts/pythonHysys-main
- Key evidence: case.hsc、inal.hsc + Python scripts + LICENSE
- License/public access note: MIT, public access.
- Recommended automation use: 最小 COM 连接与 case 打开/属性读写测试。

## Candidate-only (Not Downloaded/Not Admitted)
1. https://github.com/nikitrian/Reduced-space_Bayesian_Optimization (D)
   - 包内 .hsc 为 Git LFS pointer，缺少可直接获取的二进制模型本体。
2. https://zenodo.org/records/10782839 (D)
   - 当前仅公开 PDF，无 .hsc/.xml 模型文件。

## Dedupe Basis
- Baseline: all prior CASE/*/sources.json loaded.
- Keys checked: source_page, download_url, 	itle, ilenames, sha256.
- This run’s downloaded sources are new by source_page/download_url; no known hash collision with prior ingested case files.

## Safety & Integrity
- Raw zip packages preserved; no executable/script/macro execution.
- Zip entry safety scan for dangerous extensions (.exe/.dll/.bat/.cmd/.ps1/...): none found.
- No Aspen HYSYS runtime load/solve performed in this run.

## Residual Risks
- COSMO 与 pythonHysys 文档对工艺验证边界说明有限，需人工补充。
- 下载包中若含本地路径痕迹/历史脚本假设，迁移时需清理与复核。

## Next Suggestions
1. 在受控 HYSYS 环境做只读加载验证并记录版本/求解器状态。
2. 统一提取 case 元信息（关键单元、物流、设计变量）形成可检索清单。
