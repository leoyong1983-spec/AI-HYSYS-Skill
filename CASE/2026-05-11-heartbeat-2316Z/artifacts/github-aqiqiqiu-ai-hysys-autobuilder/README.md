# AI HYSYS Autobuilder

AI 驱动的 Aspen HYSYS 反应器智能建模系统。根据自然语言描述自动选择反应器类型（Conversion / Equilibrium / Gibbs），并生成模拟配置 JSON。

## 项目分支

- **dryrun** – 离线选型演示（仅生成 JSON，不连接 HYSYS），适合快速验证 AI 逻辑。
- **manual-param** – 混合模式（手动搭建 + Python 参数控制），用于权限受限环境。

## 功能特点

- 🤖 基于大模型（阿里云百炼）的自然语言理解，自动提取反应器类型、温度、压力、转化率。
- 📄 输出结构化 JSON（选型结果 + 建议参数）。
- 🖥️ 交互式命令行 – 用户输入任意反应描述，实时返回选型结果。
- 🔌 预留 HYSYS COM 接口，可扩展为全自动模拟（需适当权限）。

## 安装与配置

### 环境要求
- Python 3.8+
- pip

### 安装依赖
```bash
# 使用清华镜像
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 或使用阿里云镜像
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```



`requirements.txt` 内容：

text

```
pywin32
openai
```

### 配置 API Key

系统使用阿里云百炼 API（兼容 OpenAI）。设置环境变量：

bash

```
# Windows PowerShell
$env:DASHSCOPE_API_KEY = "sk-你的Key"

# Windows CMD
set DASHSCOPE_API_KEY=sk-你的Key

# Linux / Mac
export DASHSCOPE_API_KEY="sk-你的Key"
```



## 快速开始

### 1. 交互式选型（推荐）

bash

```
cd src/ai_hysys_autobuilder
python interactive_selector.py
```



输入自然语言描述（例如："乙烷裂解，转化率60%"），按回车即可获得选型结果，并保存到 `selection_result.json`。

### 2. 批量 dry-run 演示（三个预设场景）

bash

```
cd src/ai_hysys_autobuilder
python runner.py --run-all --dry-run --out ../../test_output
```



输出 `test_output/` 目录包含每个场景的选型 JSON 和汇总文件。**无需 HYSYS 环境**。



### 3. 真实 HYSYS 联动（需环境权限）

bash

```
python runner.py --run-all --visible --out real_output
```



**前提：HYSYS 已安装且 COM 权限允许创建单元操作（否则会失败）。**







## 项目结构

text

```
src/ai_hysys_autobuilder/
├── __init__.py
├── __main__.py
├── hysys_com.py          # COM 客户端（真实 + dry-run mock）
├── logging_utils.py
├── models.py             # 数据模型
├── parameter_config.py
├── reactor_builders.py
├── reactor_selection.py  # 大模型选型核心（LLM 版）
├── runner.py             # 批量运行入口
└── interactive_selector.py # 交互式单输入选型
```



## 示例输出

交互式输入：

> "我需要模拟甲烷蒸汽重整。进料是甲烷和水蒸气（摩尔比 1:2.7），炉温温度 710°C，压力 13.5 bar..."

输出 JSON（部分）：

json

```
{
  "reactor_type": "Gibbs",
  "confidence": 0.65,
  "rationale": ["用户未给出转化率...", "反应路径复杂..."],
  "suggested_hysys": {
    "temperature_c": 710.0,
    "pressure_kpa": 1350.0
  }
}
```



## 注意事项

- 需要稳定的网络连接（调用云端大模型）。
- 大模型 API 会产生费用（使用阿里云百炼免费额度可覆盖测试）。
- 真实 HYSYS COM 调用可能受系统权限限制，建议先用 dry-run 验证逻辑。