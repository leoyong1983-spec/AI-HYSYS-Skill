# LNG 液化路线选择比较模板

## 1. 本轮继承清单

### 1.1 路线层级规则

| 类别 | 已继承规则 |
|---|---|
| 主模板层级 | `A1` = `N2 expander` 最小模板；`A2` = `SMR/PRICO` 最小模板；`B` = `50万 Nm3/d` 扩展工程模板；`C` = 系统级概念模板 |
| 适用顺序 | 先选路线，再选模板层级，再决定是否加载接口子模板 |
| 首轮默认优先级 | 若目标是稳健、简洁、教学或逻辑验证，优先 `A1`；若目标是更接近 50 万方/天工程化表达，优先 `A2/B` |
| 禁止事项 | 不得把大型复杂 LNG 路线不加裁剪地直接作为中小型模板；不得把概念级模板伪装成工艺包级模型 |

### 1.2 高 N2 触发规则

| 类别 | 已继承规则 |
|---|---|
| 普通处理禁区 | `N2` 不能只当普通组分处理，因为它会影响 LNG 热值、闪蒸损失、甲烷回收率和单位液化能耗 |
| 触发条件 | 若 `N2 > 常规商品气范围` 且已明显影响 LNG 成品质量、末端闪蒸损失或 fuel gas 负荷，不得默认走常规 `SMR/PRICO` 主模板 |
| 必要动作 | 必须单列 `NRU Interface`，而不是在主冷箱内“顺便处理” |
| 接口输出 | `N2-depleted feed to liquefaction`、`nitrogen-rich offgas/vent`、甲烷损失估计、NRU 功耗/冷量接口 |

### 1.3 BOG / end flash gas / fuel gas / vent 边界规则

| 类别 | 已继承规则 |
|---|---|
| 必须分开 | `END_FLASH_GAS`、`TANK_BOG_RETURN`、`BOG_TO_COMP`、`FUEL_GAS_TO_HEADER`、`VENT_GAS`、`BOG_TO_RECONDENSER`（如有） |
| 禁止合并 | 不得把 `end flash gas` 与 `tank BOG` 合并成一股“总回气” |
| 稳态边界要求 | 稳态模板必须显式给出 `fuel gas`、`vent/flare` 去向，不得省略 |
| 子模板触发 | 当方案边界包含储罐/装船返回蒸气，或需要估算 fuel gas 回收/flare 负荷时，必须加载 `BOG` 子模板 |

### 1.4 模板 A/B/C 修订规则

| 模板 | 已继承修订 |
|---|---|
| `A1/A2` | 默认增加可选接口：`NRU-101 Nitrogen Rejection Interface`、`BOG-401 BOG Return Interface` |
| `B` | 新增：`NRU-101`、`K-401`、`E-401`、`D-401`（可选）、`FG-401`、`FLR-401` |
| `C` | 必须写清 `high-N2 feed branch`、`nitrogen-rich offgas branch`、`end flash gas branch`、`tank BOG branch`、`fuel gas sink`、`vent/flare sink` |

### 1.5 人类可读规范规则

| 类别 | 已继承规则 |
|---|---|
| 命名 | 物流名必须反映功能和状态；设备名必须反映编号和功能 |
| 分区 | 至少分为原料气区、预处理区、主循环区、制冷剂区、冷箱区、末端闪蒸与产品区、flash gas/fuel gas/vent 区 |
| 表达方式 | 优先 `Sub-Flowsheet`，`Design Spec` 和 `Recycle` 必须命名，`Spreadsheet` 不得隐藏关键逻辑 |
| 输出规范 | 必须支持设计基础表、主要物流表、主要设备表、关键假设表、负荷统计、收敛说明、局限性说明 |

---

## 2. 路线选择总表

| 路线/子模板 | 适用原料气特征 | 典型产能适配 | 是否适合 50万方/天 | 物性与边界复杂度 | 收敛难度 | 人类可读性难度 | 是否需要 NRU Interface | 是否需要单列 BOG 子模板 | 可用于什么阶段 | 不适用场景 | 主要风险提醒 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `A1_N2_EXPANDER_MIN` | 已净化干燥、低到中等复杂度、非高 N2 主导 | 小型到中小型 | `是，可作最小入口模板` | 低到中 | 低 | 低 | `通常否` | `按边界触发` | 教学、概念验证、方案预研 | 追求更高能效且边界已明确的工程方案 | 易被误当成最终工程路线；能耗通常高于优质 SMR |
| `A2_SMR_PRICO_MIN` | 已净化干燥、常规商品气、N2 不高、希望接近工程化 | 中小型 | `是，优先推荐` | 中到高 | 中 | 中 | `通常否；高 N2 时改走 B-N` | `按边界触发` | 概念方案、方案比选、扩展模板前置骨架 | 高 N2、高重烃风险未澄清、预处理边界不明 | MR 组成和 MSHE 自由度敏感；容易过约束 |
| `B_LNG_500K_ENGINEERING` | 已明确设计基础、预处理出口规格明确、目标是 50 万方/天方案表达 | 中小型 | `是，主模板` | 高 | 中到高 | 中到高 | `按高 N2 规则触发` | `按站场边界触发` | 方案研究、TEA 前处理、接近工艺包草稿 | 原料气边界不完整、产品边界未锁定 | 若输入不完整，容易把方案模板误用为细化设计模板 |
| `BN_HIGH_N2_NRU_ENGINEERING` | 高 N2、N2 已明显影响产品规格/闪蒸/回收率/fuel gas | 中小型到中型 | `是，但需专题触发` | 高 | 高 | 高 | `必须是` | `按站场边界触发` | 高 N2 方案研究、路线比选、概念到方案级 | 把 NRU 当作默认配置的常规商品气场景 | 若误判 N2 风险，会高估液化率或低估甲烷损失 |
| `SUB_BOG_STEADY_STATE` | 边界包含 tank BOG、loading return、BOG 回收需求 | 不限 | `是，作为附加子模板` | 中 | 中 | 中 | `否` | `这是 BOG 子模板本体` | 方案边界完善、fuel gas/flare 估算 | 不含罐区/装船边界的纯主液化教学模型 | 不能把 BOG 当作一股总回气；不能代替瞬态储罐模型 |
| `SUB_FUEL_GAS_INTERFACE` | 需要明确 flash gas/BOG 去燃料系统的条件 | 不限 | `是，按需附加` | 低到中 | 低 | 低 | `否` | `与 BOG 子模板联动更常见` | 概念方案、方案比选、工艺包草稿边界 | 没有 fuel gas 消纳边界时 | 富氮 offgas 不一定能作 fuel gas |
| `SUB_VENT_FLARE_INTERFACE` | 需要核定 vent/flare 去向、异常气处理 | 不限 | `是，按需附加` | 低到中 | 低 | 低 | `否` | `常与 BOG 子模板同时触发` | 方案边界、风险说明、局限性说明 | 把 vent/flare 当常规正常去向的场景 | 若省略该接口，会掩盖边界失配和异常工况 |

---

## 3. 路线选择决策树

### 3.1 可执行判断流程

```text
STEP 1 读取原料气与任务边界
IF 缺少以下任一关键输入：
  - 原料气组成
  - 原料气压力/温度/流量
  - LNG 产品边界
  - 是否包含 tank BOG / loading return
THEN
  仅允许输出 C_LNG_SYSTEM_CONCEPT
  标记 = "不可进入接近工艺包草稿级模板"
  STOP

STEP 2 判断是否高 N2 专题
IF N2 已知明显高于常规商品气范围
  OR N2 已导致下列任一现象：
    - LNG 产品热值/规格风险
    - 末端 flash gas 显著偏高
    - 甲烷回收率明显下降
    - fuel gas 负荷或组成异常
THEN
  触发 = NRU-101
  主模板候选 = BN_HIGH_N2_NRU_ENGINEERING
ELSE
  进入 STEP 3

STEP 3 判断目标阶段
IF 目标 = 教学/逻辑验证/快速建立稳健基础
THEN 主模板 = A1_N2_EXPANDER_MIN
ELSE IF 目标 = 中小型 LNG 概念方案 / 方案比选 / 50万方/天工程骨架
THEN 主模板 = A2_SMR_PRICO_MIN 或 B_LNG_500K_ENGINEERING

STEP 4 判断是否允许进入 B 级模板
IF 已有：
  - 原料气设计基础完整
  - 预处理出口规格明确
  - LNG 产品边界明确
  - 主要能耗统计口径明确
THEN
  可升级主模板 = B_LNG_500K_ENGINEERING
ELSE
  保持 A1/A2 或 C

STEP 5 判断是否必须加载 BOG 子模板
IF 方案边界包含以下任一项：
  - tank BOG
  - loading return gas
  - 需估算 fuel gas 回收
  - 需估算 vent / flare 负荷
THEN
  附加模板 += SUB_BOG_STEADY_STATE
  附加模板 += SUB_FUEL_GAS_INTERFACE
  附加模板 += SUB_VENT_FLARE_INTERFACE

STEP 6 判断是否只能输出概念级模型
IF 存在以下任一项：
  - 原料气边界未确认
  - 预处理出口规格缺失
  - LNG 产品压力/温度未确认
  - BOG 边界仅知道“有回气”但未区分来源
THEN
  降级 = C_LNG_SYSTEM_CONCEPT
  标记 = "禁止直接进入接近工艺包草稿级模板"

STEP 7 输出建模入口对象包
输出 = 主模板 + 附加接口模板 + 必须人工确认项 + 禁止自动决定项
```

### 3.2 关键判据写死规则

| 判断题 | 固化规则 |
|---|---|
| 原料气中 N2 到什么水平时，不得默认走常规 `SMR/PRICO` 主模板 | 当 `N2` 已明显高于常规商品气范围，且已影响 LNG 产品规格、闪蒸损失、甲烷回收率或 fuel gas 组成时，不得默认走常规 `SMR/PRICO` |
| 哪些原料气条件下优先考虑 `A1` | 边界尚不复杂、目标是稳健收敛与教学验证、预处理后可视作已净化干燥、暂不处理高 N2 专题 |
| 哪些条件下优先进入 `A2/B` | 原料气为常规商品气或等效处理气、目标是 50 万方/天中小型 LNG 方案表达、希望接近工程化路线 |
| 哪些条件下必须触发 `B-N` | 高 N2 已构成产品/闪蒸/回收率/fuel gas 风险，或需要明确 NRU 前后物流与甲烷损失 |
| 哪些条件下必须加载 `BOG/fuel gas/vent` 子模板 | 边界涉及 tank BOG、loading return、fuel gas 回收估算、vent/flare 负荷估算 |
| 哪些条件下只能输出概念级模型 | 原料气设计基础不完整、预处理出口规格未给、LNG 产品边界未锁定、BOG 来源未区分 |

---

## 4. 模板调用矩阵

| 输入条件 | 触发规则 | 选中的主模板 | 需附加的接口模板 | 必须人工确认项 | 禁止自动决定项 | 输出给下一线程的对象包名称 |
|---|---|---|---|---|---|---|
| 已净化干燥、边界简单、目标是教学或最小逻辑验证 | 教学/最小可行优先 | `A1_N2_EXPANDER_MIN` | `可选 BOG-401` | 原料气是否真已满足进冷箱规格 | 不得自动假定其为最终工程路线 | `PKG_ENTRY_A1_BASE` |
| 常规商品气、目标为中小型 LNG 方案骨架 | 常规路线优先 | `A2_SMR_PRICO_MIN` | `按边界附加 BOG/FG/FLR` | MR 是否允许作为首轮路线；预处理出口规格是否确认 | 不得自动做 MR 组成优化 | `PKG_ENTRY_A2_BASE` |
| 50万方/天、设计基础完整、需要设备表和物流表接口 | 可升级工程模板 | `B_LNG_500K_ENGINEERING` | `按边界附加 NRU/BOG/FG/FLR` | 压缩机效率、MITA、压降假设、产品边界 | 不得自动给出采购级设备定值 | `PKG_ENTRY_B_500K` |
| 高 N2 已明显影响产品/闪蒸/回收率 | 强制高 N2 路线 | `BN_HIGH_N2_NRU_ENGINEERING` | `NRU-101`；必要时再加 `BOG/FG/FLR` | 是否必须做 NRU；NRU 后目标 N2 规格；富氮气去向 | 不得自动选择单塔/双塔 NRU 详细方案 | `PKG_ENTRY_BN_HIGH_N2` |
| 边界含 tank BOG 或 loading return | 强制气体去向子模板 | `原主模板不变` | `SUB_BOG_STEADY_STATE` + `SUB_FUEL_GAS_INTERFACE` + `SUB_VENT_FLARE_INTERFACE` | BOG 来源、温度窗口、是否允许送压缩机、fuel gas 消纳能力 | 不得自动把 end flash gas 与 tank BOG 合并 | `PKG_ADDON_BOG_BOUNDARY` |
| 原料气信息缺失或产品边界未确认 | 降级保护 | `C_LNG_SYSTEM_CONCEPT` | `仅保留占位接口` | 缺失输入清单 | 不得自动升级到 B 或 B-N | `PKG_ENTRY_C_CONCEPT_ONLY` |

---

## 5. 后续建模线程交接包

### 5.1 必须先拿到的输入

| 类别 | 必填项 | 说明 |
|---|---|---|
| 原料气设计基础 | 流量、压力、温度、组分 | 没有这组信息，不允许进入 B/B-N |
| 风险标记 | `N2` / `CO2` / `C2+` / `C5+` / `H2O` / `Hg` | 至少要形成高风险/常规/未知三级标记 |
| 目标产能 | `Nm3/d` 或其他统一口径 | 需明确是否是 50 万方/天级 |
| LNG 产品边界 | 产品压力、温度、是否允许 end flash、目标质量边界 | 决定是否能进入接近工艺包草稿级模板 |
| 预处理边界 | 是否已满足进冷箱规格 | 未明确时只能概念级 |
| 高 N2 专题 | 是/否/未定 | 触发 NRU 判断 |
| BOG 专题 | 无 / tank BOG / loading return / 二者都有 | 决定是否附加 BOG 子模板 |

### 5.2 交接包模板

```yaml
handoff_package_name: PKG_ENTRY_<ROUTE_CODE>_<CASE_ID>

feed_design_basis:
  flowrate:
  pressure:
  temperature:
  composition:

feed_risk_flags:
  nitrogen_risk:
  co2_risk:
  h2o_risk:
  hg_risk:
  c2plus_risk:
  c5plus_freeze_risk:

capacity_target:
  value:
  unit:

lng_product_boundary:
  product_pressure:
  product_temperature:
  end_flash_allowed:
  quality_notes:

pretreatment_boundary:
  acid_gas_spec_defined:
  dehydration_spec_defined:
  mercury_spec_defined:
  heavy_hc_control_defined:

special_topics:
  high_n2_topic:
  nru_interface_required:
  bog_required:
  fuel_gas_interface_required:
  vent_flare_interface_required:

recommended_route:
  main_template:
  add_on_templates:

uncertainties:
  - 

manual_decisions_required:
  - 

auto_decision_prohibited:
  - 
```

### 5.3 需人工拍板项

| 项目 | 原因 |
|---|---|
| 是否将项目升级到 `B` 或 `B-N` | 这取决于输入完整性与目标深度，不应自动升级 |
| NRU 是否必须设置 | 需要结合产品规格、甲烷损失容忍度和项目路线取舍 |
| BOG 去向主策略 | `fuel gas`、`recondensation`、`vent/flare` 涉及站场边界与业主策略 |
| LNG 产品边界最终值 | 这会直接影响 flash、能耗和回收率 |
| 是否接受 `A1` 仅作教学/基线模型 | 防止被误当最终路线 |

---

## 6. 统一命名建议

### 6.1 主模板命名

| 对象 | 建议命名 |
|---|---|
| A1 | `TPL_A1_N2_EXPANDER_MIN` |
| A2 | `TPL_A2_SMR_PRICO_MIN` |
| B | `TPL_B_LNG_500K_ENGINEERING` |
| B-N | `TPL_BN_HIGH_N2_NRU_ENGINEERING` |
| C | `TPL_C_LNG_SYSTEM_CONCEPT` |

### 6.2 接口与子模板命名

| 对象 | 建议命名 |
|---|---|
| NRU 接口 | `IFC_NRU_101` |
| end flash gas 接口 | `IFC_END_FLASH_GAS_201` |
| tank BOG 接口 | `IFC_TANK_BOG_401` |
| BOG 子模板 | `SUB_BOG_STEADY_STATE_401` |
| fuel gas 接口 | `IFC_FUEL_GAS_401` |
| vent/flare 接口 | `IFC_VENT_FLARE_401` |
| BOG 再冷凝接口 | `IFC_BOG_RECOND_401` |

### 6.3 交接包命名

| 对象 | 建议命名 |
|---|---|
| 通用入口包 | `PKG_ENTRY_<ROUTE_CODE>_<CASE_ID>` |
| A1 包 | `PKG_ENTRY_A1_<CASE_ID>` |
| A2 包 | `PKG_ENTRY_A2_<CASE_ID>` |
| B 包 | `PKG_ENTRY_B_<CASE_ID>` |
| B-N 包 | `PKG_ENTRY_BN_<CASE_ID>` |
| BOG 附加包 | `PKG_ADDON_BOG_<CASE_ID>` |

### 6.4 禁止使用的含糊命名

| 禁止命名 | 问题 |
|---|---|
| `route1` | 看不出路线类型 |
| `final_model` | 看不出层级与适用边界 |
| `gas_return` | 看不出是 end flash gas 还是 tank BOG |
| `nru_case` | 看不出是接口、子模板还是主模板 |
| `vent1` | 看不出是否为 flare/vent/interface |
| `real_template_v2` | 模糊且不可审查 |

---

## 7. 风险与误用警示

| 误用场景 | 为什么危险 | 纠正动作 |
|---|---|---|
| 把高 N2 原料气误导入常规 `SMR/PRICO` 模板 | 会错误低估闪蒸损失、错误高估甲烷回收率，并掩盖产品规格风险 | 先执行高 N2 判断，再决定是否触发 `IFC_NRU_101` |
| 把 `end flash gas` 与 `tank BOG` 合并为一股“总回气” | 会抹掉温度、压力、压缩可行性和 flare 条件差异 | 强制拆分 `IFC_END_FLASH_GAS_201` 与 `IFC_TANK_BOG_401` |
| 把概念级模板结果当工程定值 | 会把概念能耗误当采购或保证值 | 明确标记为概念级，仅作 TEA/方案比选输入 |
| 在未确认原料气边界前就加载复杂主模板 | 会产生伪精细模型，输入不稳而结构过深 | 降级到 `TPL_C_LNG_SYSTEM_CONCEPT` |
| 用单一能耗指标粗暴否定路线适配性 | 会忽视可读性、稳健性、边界适配性和高 N2 风险 | 同时查看能耗、回收率、边界复杂度、收敛难度 |
| 自动决定 NRU 详细工艺方案 | 这涉及产品规格、甲烷损失、排放与投资权衡 | 只允许自动触发 `NRU Interface`，不允许自动拍板详细 NRU 方案 |
| 自动把 BOG 默认送 fuel gas | 可能不满足温度、压力、组分或消纳条件 | 强制检查 `fuel gas sink` 条件和 `vent/flare` 后备去向 |
| 用接收站 BOG 再冷凝方案直接套液化厂罐区 | 站场边界不同，冷量来源和设备职责不同 | 仅允许作为 `BOG` 子模板参考，不得默认化 |

---

## 8. 最终输出结构

### 8.1 可直接用于后续自动建模入口的资产列表

| 资产 | 用途 |
|---|---|
| `路线选择总表` | 先粗选主模板与子模板 |
| `路线选择决策树` | 将判断逻辑转成可执行入口规则 |
| `模板调用矩阵` | 输入条件到模板调用的映射 |
| `建模线程交接包模板` | 给下一线程传递结构化输入 |
| `风险警示清单` | 防止自动建模线程误用模板 |

### 8.2 下一线程调用顺序

1. 读取 `建模线程交接包`
2. 执行 `路线选择决策树`
3. 按 `模板调用矩阵` 选主模板和附加接口模板
4. 生成人工确认项清单
5. 仅在确认项完成后，进入 HYSYS 建模线程

### 8.3 默认入口规则摘要

```text
默认主路径：
  常规商品气 + 50万方/天 + 边界完整 -> TPL_B_LNG_500K_ENGINEERING

默认教学路径：
  边界简单 + 快速稳健验证 -> TPL_A1_N2_EXPANDER_MIN

默认工程骨架路径：
  常规商品气 + 方案级 -> TPL_A2_SMR_PRICO_MIN

强制专题路径：
  高N2显著影响产品/闪蒸/回收率 -> TPL_BN_HIGH_N2_NRU_ENGINEERING + IFC_NRU_101

强制附加路径：
  存在 tank BOG / loading return / fuel gas回收 / vent-flare估算
  -> SUB_BOG_STEADY_STATE_401 + IFC_FUEL_GAS_401 + IFC_VENT_FLARE_401

保护降级路径：
  输入不完整 -> TPL_C_LNG_SYSTEM_CONCEPT
```
