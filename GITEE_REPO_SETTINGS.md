# Gitee 仓库设置建议

本文件仅用于 Gitee 备用镜像的中文展示与同步说明。GitHub 仍是本项目主线仓库，Gitee 只作为国内访问、备份和分发通道。

## 主线与备用线

- 主线仓库：GitHub
- 备用镜像：Gitee
- 代码、议题、PR、发布说明和自动化配置的权威来源仍以 GitHub 为准
- Gitee 侧尽量保持只同步，不在 Gitee 上单独维护分叉逻辑

## 仓库名称

`AI-HYSYS-Skill`

## 中文简介

面向 Aspen HYSYS 的 AI 自动化与基础工艺包工具包，采用 COM、Spreadsheet/Workbook 桥接、受限调参、可审计导出和公开资料支撑的 CASE 库，支持接管已有 HYSYS case 并生成复核阶段基础工艺包资料。

## 推荐标签

```text
hysys
aspen-hysys
流程模拟
化工过程
工艺包
基础工艺包
过程工程
自动化
人工智能
python
com自动化
数字化工程
```

## Gitee 页面说明

建议在 Gitee 仓库首页或项目简介中说明：

```text
本仓库是 AI-HYSYS-Skill 的 Gitee 备用镜像，便于国内访问与下载。项目主线仍在 GitHub；如需提交 issue、PR 或查看最新维护记录，请以 GitHub 仓库为准。
```

## 同步原则

1. GitHub 保持主线，不为 Gitee 修改 GitHub 专用文件。
2. Gitee 只同步已提交、已确认适合公开的内容。
3. 不在远端 URL、脚本、配置文件或提交记录中保存账号密码。
4. 如果需要认证推送，优先使用 Gitee 私人令牌或本机 Git Credential Manager。
5. 同步前先运行仓库校验：

```powershell
.\scripts\validate_repo.ps1
```

## 推送示例

创建 Gitee 空仓库后，将 `<gitee-repo-url>` 替换为实际 HTTPS 地址：

```powershell
git remote add gitee <gitee-repo-url>
git push gitee HEAD:main
```

如需同步当前工作分支而不是 `main`，请显式指定目标分支名，避免误覆盖 Gitee 默认分支。
