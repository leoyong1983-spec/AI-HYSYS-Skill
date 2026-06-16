# Aspen Plus MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/platform-Windows-lightgrey)](https://www.microsoft.com/windows)

**Talk to Aspen Plus in natural language.** An MCP (Model Context Protocol) server that bridges AI agents with Aspen Plus v15 via COM automation. 85 tools for parameter tuning, sensitivity analysis, convergence diagnostics, and result reading.

> **English** · **中文 (见下方)**

---

## Features

- **85 MCP tools** for blocks, streams, components, reactions, columns, utilities, sensitivity
- **No GUI interaction needed** — control Aspen Plus entirely through code
- **Smart parameter categorization** — `find_incomplete_inputs()` knows what matters per block type and operating mode
- **Convergence diagnostics** — `diagnose()` with built-in knowledge base
- **Reaction kinetics** — POWERLAW, LHHW, EQUILIBRIUM, RStoic, RPLUG/RCSTR reaction sets
- **Sensitivity analysis** — variable sweep with linked feed parameters
- **Safe COM threading** — dedicated STA thread, auto-retry with reconnection

## Quick Start

### Requirements

- **Windows** (COM automation is Windows-only)
- **Aspen Plus v15** (GUI 41.0 / 40.0)
- **Python 3.10+**

### Installation

```bash
git clone https://github.com/ddtlxc001/aspen-mcp.git
cd aspen-mcp
python -m venv venv
venv\Scripts\pip install -e .
venv\Scripts\aspen-mcp
```

The server communicates over **stdio** (standard MCP transport) — compatible with any MCP client.

### MCP Client Configuration

**Reasonix** (reasonix.toml):
```toml
[[plugins]]
name    = "aspen-mcp"
command = "path\\to\\aspen-mcp\\venv\\Scripts\\python.exe"
args    = ["-m", "aspen_mcp.server"]
```

**Claude Desktop / VS Code** (mcpServers):
```json
{
  "mcpServers": {
    "aspen-mcp": {
      "command": "path\\to\\aspen-mcp\\venv\\Scripts\\python.exe",
      "args": ["-m", "aspen_mcp.server"]
    }
  }
}
```

### Typical Workflow

```
# 1. Open or create
open_file("my_simulation.apw")      # or: new_simulation()

# 2. Add components
add_component("WATER")
add_component("ETHANOL")

# 3. Set property method
set_property_method("NRTL")

# 4. Build topology
add_block("MIXER", "M-1")
add_block("HEATER", "H-1")
connect("M-1", "H-1", "S-1")

# 5. Set parameters
set_param("H-1", "TEMP", 150)             # block param
set_stream_param("S-1", "TEMP", 100)      # stream param
set_stream_param("S-1", "PRES", 5)

# 6. Run & get results
reinit_and_run()
get_block("H-1")
get_stream("S-1")
```

---

## Tool Reference

### Simulation Lifecycle
| Tool | Description |
|------|-------------|
| open_file(path) | Open .apw file |
| new_simulation() | Create blank sim from clean template |
| close_file() | Close current file |
| run() | Run simulation (sync) |
| run_async() | Run asynchronously |
| stop_simulation() | Stop running simulation |
| reinit() | Clear results (call before re-running) |
| reinit_and_run() | Reinit + Run in one step (recommended) |
| save(path?) | Save / SaveAs |
| status() | Connection & engine status |
| probe() | COM health check (app/root/tree) |
| visible(show) | Show/hide Aspen GUI window |
| batch_refresh(off) | Toggle GUI refresh (faster bulk ops) |
| run_script(path) | Execute a Python script inside Aspen |

### Flowsheet Topology
| Tool | Description |
|------|-------------|
| add_block(name, type) | Add a block (HEATER, RPLUG, FLASH2, MIXER, etc.) |
| remove_block(name) | Remove a block |
| add_stream(name) | Add a stream |
| remove_stream(name) | Remove a stream |
| connect(source, dest, stream?) | Connect blocks via auto-created stream |
| connect_port(block, port, stream) | Connect to a specific port |
| disconnect(stream_name) | Disconnect & remove stream |
| list_all_blocks() | List all blocks |
| list_all_streams() | List all streams |
| list_all_ports() | All ports & connections at a glance |
| list_block_ports(block) | List a block's ports & connections |
| flowsheet_topology() | Full topology: source --[stream]--> dest |

### Parameters & Streams
| Tool | Description |
|------|-------------|
| set_param(block, param, value) | Set a block parameter |
| set_stream_param(stream_name, param, value, basis?) | Set a stream parameter (TEMP, PRES, TOTAL), optional basis |
| set_stream_composition(stream_name, component, flow) | Set a component's molar flow |
| set_stream_composition_batch(stream_name, components, basis?, total_flow?) | Batch-set composition with BASIS control |
| get_block(name) | Read block specs & results |
| get_stream(name) | Read stream output properties |
| block_status(name) | Block convergence status (BLKSTAT/BLKMSG) |
| get_stream_composition_info(name) | Stream composition metadata |

### Components & Properties
| Tool | Description |
|------|-------------|
| add_component(id) | Add a component (WATER, ETHANOL, etc.) |
| remove_component(id) | Remove a component |
| list_components() | List all components |
| get_property_method() | Get current global property method |
| set_property_method(method) | Set property method (NRTL, PENG-ROB, UNIQUAC, IDEAL) |

### Reactions
| Tool | Description |
|------|-------------|
| add_reaction_set(name, type) | Create reaction set (POWERLAW/LHHW/EQUILIBRIUM) |
| remove_reaction_set(name) | Remove a reaction set |
| add_reaction(set, no, reactants, products, phase?, exponents?) | Add a reaction with stoichiometry |
| remove_reaction(set, no) | Remove a single reaction |
| list_reaction_sets() | List all reaction sets |
| setup_block_reaction(block, reactants?, products?, ...) | Set RStoic block stoichiometry |

### Columns (RadFrac)
| Tool | Description |
|------|-------------|
| set_column_stages(block, nstage) | Set number of stages |
| set_column_pressure(block, top_pres, dp_stage?) | Set pressure profile |
| set_condenser_type(block, type) | Set condenser (NONE/TOTAL/PARTIAL-V/...) |
| set_reboiler_type(block, type) | Set reboiler (NONE/KETTLE/THERMOSIPHON/...) |
| set_feed_stage(block, stream, stage) | Set feed stage |
| set_product_stage(block, stream, stage, phase?) | Set product draw stage |
| add_side_duty(block, stage, duty) | Add side heater/cooler duty |
| remove_side_duty(block, stage) | Remove side duty |

### Utilities
| Tool | Description |
|------|-------------|
| add_utility(name, type, block?, params?) | Add WATER/STEAM/ELECTRICITY utility |
| batch_add_utilities([]) | Add multiple utilities atomically |
| get_utility(name) | Read utility parameters |
| list_utilities() | List all utilities |
| remove_utility(name) | Remove a utility |

### Recycle / Tear Streams
| Tool | Description |
|------|-------------|
| list_tear_streams() | List all tear streams (recycle loops) |
| set_tear_estimate(stream, temp?, pres?, total_flow?) | Set tear stream initial estimate |
| configure_fsplit(block, outlet, frac) | Configure FSPLIT outlet split fraction |

### Diagnostics & Analysis
| Tool | Description |
|------|-------------|
| find_incomplete_inputs() | Scan unset inputs (per-block smart categorization) |
| fill_trivial_params() | Fill infrastructure params with defaults |
| validate_block(name) | Check block input completeness |
| diagnose(keywords) | Convergence diagnosis + knowledge base search |
| search_convergence_knowledge(keywords) | Verbose knowledge base search |
| simulation_warnings() | Scan for common config issues |
| sensitivity(block, variable, values, unit?) | Manual sensitivity sweep |
| sensitivity_advanced(block, variable, values, linked_params?, ...) | Advanced sweep with linked feed params |
| deep_probe(block_name?) | Deep-probe block input nodes for validation info |
| export_report_file(path) | Export .rep report |
| generate_input_summary(path, mode?) | Export .bkp input summary |
| readback(path, mode?) | Read back .bkp file into simulation |

### Low-level Path Access
| Tool | Description |
|------|-------------|
| explore(path) | Explore Aspen object tree at backslash path |
| get_value(path) | Read value by backslash path |
| set_value(path, value, unit?) | Write value by backslash path |
| insert_row(path, dimension?) | Insert row in a table node |
| set_label(path, index, label, dimension?) | Set row/column label in a 2D table |

### Discovery & Help
| Tool | Description |
|------|-------------|
| help(topic?) | Get usage guide for any workflow topic |

---

## Documentation

Detailed block parameter documentation for 70+ Aspen Plus block types is available under `docs/blocks/`.

## License

MIT — see [LICENSE](LICENSE).


---

# Aspen Plus MCP

通过自然语言操控 Aspen Plus 进行化工流程模拟——参数调优、批量运行、读取结果，全部由 AI 代理完成。

## 工作模式

```
你在 GUI 里搭好流程拓扑 → MCP 接管参数调优和运行分析
```

**MCP 不负责画流程图。** 你可以在 Aspen Plus GUI 中手动放置模块和物流，也可以用 `connect`/`connect_port` 工具通过代码建立连接。搭建完成后，MCP 用来：

- ✅ 批量改参数、跑灵敏度分析
- ✅ 运行模拟、检查收敛状态
- ✅ 读取物流和模块结果数据
- ✅ 导出报告

---

## 安装

### 环境要求

- Windows（COM 自动化依赖）
- Aspen Plus v15 已安装（GUI 41.0 / 40.0）
- Python 3.10+

### 步骤

```bash
# 1. 克隆项目
git clone https://github.com/ddtlxc001/aspen-mcp.git
cd aspen-mcp

# 2. 创建虚拟环境
python -m venv venv

# 3. 激活虚拟环境并安装依赖
venv\Scripts\pip install -e .

# 4. 启动（验证安装）
venv\Scripts\aspen-mcp
```

启动后 MCP 服务器通过 stdio 通信，适用于任何支持 MCP 协议的客户端（Reasonix、Claude Desktop、VS Code 等）。

### 在 Reasonix 中使用

在 `reasonix.toml` 中添加：

```toml
[[plugins]]
name    = "aspen-mcp"
command = "path\\to\\aspen-mcp\\venv\\Scripts\\python.exe"
args    = ["-m", "aspen_mcp.server"]
```

### 在 Claude Desktop / VS Code 中使用

```json
{
  "mcpServers": {
    "aspen-mcp": {
      "command": "path\\to\\aspen-mcp\\venv\\Scripts\\python.exe",
      "args": ["-m", "aspen_mcp.server"]
    }
  }
}
```

---

## 常见工作流

### 1. 打开文件并运行

```
open_file("甲醇.apw")
run()
status()
```

### 2. 改参数后重新运行

```
set_param("HEATER", "TEMP", 150)
set_param("HEATER", "PRES", 5)
run()
get_stream("C-OUT")
```

### 3. 从零搭建流程

```
# 添加模块
add_block("MIXER", "MIXER")
add_block("REACTOR", "RPLUG")
add_block("SEP", "FLASH2")

# 连接
connect("MIXER", "REACTOR", "FEED")
connect("REACTOR", "SEP", "R-OUT")

# 设参数
set_param("MIXER", "TEMP", 100)
set_stream_param("FEED", "TEMP", 150)
set_stream_param("FEED", "PRES", 5)
set_stream_param("FEED", "TOTAL", 100)

# 运行
reinit_and_run()
get_stream("R-OUT")
```

### 4. 添加组分并切换物性方法

```
add_component("METHANE")
add_component("ETHANOL")
list_components()
set_property_method("NRTL")
```

---

## 工具总览

### 模拟生命周期

| 工具 | 说明 |
|---|---|
| open_file(path) | 打开 .apw 文件 |
| new_simulation() | 创建空白新模拟（复制纯净模板到临时文件） |
| close_file() | 关闭当前文件 |
| run() | 运行模拟（同步） |
| run_async() | 异步运行 |
| stop_simulation() | 停止当前运行 |
| save(path?) | 保存或另存文件 |
| reinit() | 重置结果（重新运行前调用） |
| reinit_and_run() | Reinit + Run 一步完成（推荐） |
| status() | 查看连接和引擎状态 |
| probe() | 诊断 COM 状态（app/root/tree 三级检查） |
| visible(show) | 显示/隐藏 Aspen 窗口 |
| batch_refresh(off) | 开关 GUI 刷新（批量操作加速） |
| run_script(path) | 在 Aspen 内部执行 Python 脚本 |

### 流程拓扑

| 工具 | 说明 |
|---|---|
| add_block(name, type) | 添加模块（HEATER, RPLUG, FLASH2, MIXER 等） |
| remove_block(name) | 删除模块 |
| add_stream(name) | 添加物流 |
| remove_stream(name) | 删除物流 |
| connect(source, dest, stream?) | 连接源块到目标块（自动创建流） |
| connect_port(block, port, stream) | 连接到指定端口 |
| disconnect(stream_name) | 断开流并从流程中移除 |
| list_all_blocks() | 列出所有模块 |
| list_all_streams() | 列出所有物流 |
| list_all_ports() | 查看所有模块端口和连接 |
| list_block_ports(block) | 查看块的端口和连接情况 |
| flowsheet_topology() | 显示完整流程拓扑 |

### 参数与结果

| 工具 | 说明 |
|---|---|
| set_param(block, param, value) | 设置模块参数 |
| set_stream_param(stream_name, param, value, basis?) | 设置物流参数（TEMP, PRES, TOTAL），可选 basis |
| set_stream_composition(stream_name, component, flow) | 设置物流中某组分的摩尔流量 |
| set_stream_composition_batch(stream_name, components, basis?, total_flow?) | 批量设置组分（支持 BASIS 控制） |
| get_block(name) | 读取模块规格和结果 |
| get_stream(name) | 读取物流属性（温度、压力、流量等） |
| get_stream_composition_info(name) | 读取物流组成信息 |
| block_status(name) | 读取模块收敛状态（BLKSTAT/BLKMSG） |

### 组分与物性

| 工具 | 说明 |
|---|---|
| list_components() | 列出所有组分 |
| add_component(id) | 添加组分（如 WATER, ETHANOL） |
| remove_component(id) | 删除组分 |
| get_property_method() | 读取当前全局物性方法 |
| set_property_method(method) | 设置物性方法（NRTL, PENG-ROB, UNIQUAC, IDEAL） |

### 反应与动力学

| 工具 | 说明 |
|---|---|
| add_reaction_set(name, type) | 创建反应集（POWERLAW/LHHW/EQUILIBRIUM） |
| remove_reaction_set(name) | 删除反应集 |
| add_reaction(set, no, reactants, products, phase?, exponents?) | 添加反应及计量系数 |
| remove_reaction(set, no) | 删除单个反应 |
| list_reaction_sets() | 列出所有反应集 |
| setup_block_reaction(block, reactants?, products?, ...) | 设置 RStoic 块计量反应 |

### 塔器（RadFrac）

| 工具 | 说明 |
|---|---|
| set_column_stages(block, nstage) | 设置理论板数 |
| set_column_pressure(block, top_pres, dp_stage?) | 设置压力分布 |
| set_condenser_type(block, type) | 设置冷凝器类型 |
| set_reboiler_type(block, type) | 设置再沸器类型 |
| set_feed_stage(block, stream, stage) | 设置进料位置 |
| set_product_stage(block, stream, stage, phase?) | 设置产品采出位置 |
| add_side_duty(block, stage, duty) | 设置侧线换热 |
| remove_side_duty(block, stage) | 删除侧线换热 |

### 公用工程

| 工具 | 说明 |
|---|---|
| add_utility(name, type, block?, params?) | 添加公用工程（WATER/STEAM/ELECTRICITY） |
| batch_add_utilities([]) | 批量添加公用工程（原子操作） |
| get_utility(name) | 读取公用工程参数 |
| list_utilities() | 列出所有公用工程 |
| remove_utility(name) | 删除公用工程 |

### 回流撕裂流股

| 工具 | 说明 |
|---|---|
| list_tear_streams() | 列出所有撕裂流股 |
| set_tear_estimate(stream, temp?, pres?, total_flow?) | 设置撕裂流股初值 |
| configure_fsplit(block, outlet, frac) | 配置 FSPLIT 出口分配比例 |

### 分析诊断

| 工具 | 说明 |
|---|---|
| find_incomplete_inputs() | 扫描未填写的输入节点 |
| fill_trivial_params() | 填充基础设施/UI 参数 |
| validate_block(name) | 验证模块输入完整性 |
| diagnose(keywords) | 收敛诊断 + 知识库搜索 |
| search_convergence_knowledge(keywords) | 详细收敛知识搜索 |
| simulation_warnings() | 扫描常见配置问题 |
| sensitivity(block, variable, values, unit?) | 手动灵敏度分析 |
| sensitivity_advanced(block, variable, values, linked_params?, ...) | 高级灵敏度分析（支持关联进料参数） |
| deep_probe(block_name?) | 深度探测块输入节点验证信息 |
| export_report_file(path) | 导出 .rep 报告 |
| generate_input_summary(path, mode?) | 导出 .bkp 输入摘要 |
| readback(path, mode?) | 回读 .bkp 文件 |

### 通用路径访问

| 工具 | 说明 |
|---|---|
| explore(path) | 探索 Aspen 对象树 |
| get_value(path) | 按反斜杠路径读值 |
| set_value(path, value, unit?) | 按反斜杠路径写值 |
| insert_row(path, dimension?) | 在表节点中插入行 |
| set_label(path, index, label, dimension?) | 设置二维表的行/列标签 |

### 帮助入口

| 工具 | 说明 |
|---|---|
| help(topic?) | 获取任意工作流主题的详细用法指南 |

---

## 操作要点

### 删除块和物流的顺序 ⚠️

**先删块，再清物流。** 绝不能反过来。

✅ 正确：
```
remove_block B1          # 块先删，连接自动断裂
disconnect CL2           # 清理残余孤儿物流
disconnect H2O
```

❌ 错误（会导致 COM 服务器异常）：
```
disconnect CL2           # 块还在但进料少了一条
disconnect H2O           # 块完全孤零零
remove_block B1          # COM 服务器异常
```

### COM 错误分级

| 错误现象 | 含义 | 应对 |
|---|---|---|
| 尚未调用 CoInitialize。 | 子线程未初始化 COM | 修复代码即可 |
| 发生意外。 | 参数/操作型错误 | 可重试 |
| 服务器出现异常情况。 | COM 状态已脏 | close_file → open_file |
| 远程过程调用失败。 | Aspen Plus 未运行 | 检查 Aspen Plus |
| 对象没有连接到服务器 | COM 代理已过期 | 重启 MCP 插件 |

**close_file() → open_file() 可解决绝大多数 COM 稳定性问题。**

### 流股参数设置（MIXED 子节点）⚠️

**`set_param` 只能设模块参数。** 物流参数（TEMP、PRES、TOTAL 等）必须用 **`set_stream_param`**。

为什么？Aspen COM 的流股参数节点都有一个 `MIXED` 子节点：

```
Data\Streams\H2O\Input\TEMP       ← 直接 SetValue 会报 AE_UNDERSPEC
Data\Streams\H2O\Input\TEMP\MIXED  ← 必须在这里写入值
```

✅ 正确用法：
```
set_stream_param("H2O", "TEMP", 140)
set_stream_param("H2O", "PRES", 1)
set_stream_param("H2O", "TOTAL", 200)
```

### 运行策略：Reinit + Run2

修改参数或拓扑后，正确的流程是：

```
reinit()           # 清空旧计算结果和引擎缓存
run()              # 执行计算
```

或一步到位：
```
reinit_and_run()   # Reinit() + Run2() 组合
```

**Reinit() 会强制 Aspen 引擎重建计算顺序和撕裂流股。**

### 启动策略

`new_simulation()` 不使用 `InitNew()`（COM 引用不稳定），而是：
1. `close_file()`
2. 复制纯净空白模板到 `%TEMP%`（带 PID 后缀）
3. `open_file()` 打开副本

**模板初始状态：** METCBAR 单元制、0 组分、PENG-ROB 物性、空拓扑。

### HEATER 的温度设置

HEATER 默认 `HEATOPT=CONST-DUTY`。要用温度设参需先改为 `CONST-TEMP`：
```
set_value(r"\Data\Blocks\PREHEAT\Input\HEATOPT", "CONST-TEMP")
```

### 流连接

物流连接不走 `Connections`（只读），而走 **`Block → Ports → {port名} → Elements.Add(流名)`**。
- 标准端口名：`F(IN)` 输入、`P(OUT)` 输出、`V(OUT)` 汽相、`L(OUT)` 液相
- 不确定端口名时用 `list_block_ports("模块名")` 查看

### 保存文件

- `save()` — 原地保存
- `save("路径.apw")` — 另存为新文件

### 批量操作加速

大批量改参数前调 `batch_refresh(True)` 关闭 GUI 刷新，改完 `batch_refresh(False)` 恢复。

### 模块参数文档

`docs/blocks/` 目录下有 70 种 Aspen Plus 模块的详细参数文档。

---

## Requirements

- Windows（COM 自动化依赖）
- Aspen Plus v15 已安装（GUI 41.0 / 40.0）
- Python 3.10+
