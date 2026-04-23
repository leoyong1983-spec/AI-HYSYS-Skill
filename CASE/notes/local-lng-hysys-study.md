# HYSYS 的 LNG液化工艺案例学习与模板提炼

## 1）本轮学习对象

- 学习层级：`50万 Nm3/d 级中小型天然气液化厂`的`预处理 + 液化主循环 + LNG末端闪蒸/燃料气稳态边界`。
- 原料气类型假定：以`管道商品气/处理后井口气`为首轮模板对象，默认酸气和水已具备可达标处理条件，但必须保留 CO2/H2S/H2O/Hg/重烃冻结风险接口。
- 本轮路线对象：`N2 expander`、`SMR/PRICO 类`为主，`C3MR`仅作参考上限，不作为首轮默认模板。
- 本轮目标模型深度：`方案级 / 接近工艺包草稿级的稳态 HYSYS 模板基础`，不是采购级、施工级、动态开停车级模型。

## 2）案例收集范围

- Aspen HYSYS 官方能力与培训资料：重点看 LNG 集成、混合制冷、严格换热器模型、压缩机/动态接口能力。
- 公开论文与学位论文：重点看`SMR/PRICO`、`N2 dual expander`、小型/海上 LNG、优化研究中暴露出的关键变量与边界假设。
- 专利与工程公开资料：重点看`流程边界`、`预处理顺序`、`末端闪蒸/Fuel gas/Vent 处理`、`制冷剂回路结构`。
- 社区经验：重点看`MultiStream Heat Exchanger`、温差穿越、Recycle/Design Spec 冲突、换热器分段表达。

## 3）案例筛选标准

- 必须能识别`原料气边界`、`液化路线`、`流程边界`、`关键单元`。
- 优先保留对`50万 Nm3/d 中小型 LNG`可迁移的案例。
- 仅把`工程边界清晰`、`假设透明`、`HYSYS 表达可复核`的案例纳入模板候选。
- 纯教学流程、纯优化黑箱、纯甲烷示意流程，可收录但不得直接模板化。

## 4）质量评估方法

- `A级`：适合进入模板候选库。要求边界清楚、路线清楚、假设透明、HYSYS 表达具备可读性。
- `B级`：有明显参考价值，但存在边界不全、说明不足、命名不规范或输出不完整等缺陷。
- `C级`：只适合学 HYSYS 操作、收敛套路、单元设置，不适合学工程模板。
- `D级`：不建议学习，原因通常是把示意流程伪装成工程模型、默认值过多、关键假设缺失。

## 5）预期模板输出内容

- `模板A`：最小可行 LNG液化模型
- `模板B`：扩展版 `50万 Nm3/d` 工程模板
- `模板C`：系统级 LNG 概念模型
- 配套输出：命名规范、假设清单、输出报表结构、审查清单、路线选择模板

## 6）开始收集与分析

本轮先完成`第一轮代表性案例库 + 模板提炼`。重点不是“把单个案例复刻到 HYSYS”，而是建立后续自动建模代理可直接调用的人类可审查模板骨架。

---

## 1. 本轮学习对象

- 主题：`中小型 LNG 全流程概念模型（预处理边界 + 液化主循环 + 末端闪蒸/Fuel Gas 稳态边界）`
- 目标产能：`50万 Nm3/d`
- 原料气类型：`以经上游初步分离的商品天然气/井口处理气为主`
- 路线重点：`N2 expander` 与 `SMR/PRICO`
- 模型深度：`稳态方案级，接近工艺包草稿级表达`

---

## 2. 已收集案例清单

| 编号 | 案例名称 | 来源 | 原料气类型 | 路线类型 | 适合学习内容 | 局限性 | 质量等级 |
|---|---|---|---|---|---|---|---|
| C01 | Performance Enhancement of Nitrogen Dual Expander and SMR LNG Processes Using Jaya Optimization Approach | MDPI Energies, 2020 | 轻烃型天然气，低 N2 | `N2 dual expander` + `SMR` | 两条路线并行对比、HYSYS 假设、MITA、末端闪蒸比例、关键变量 | 以优化研究为主，原料气过于理想化，预处理被省略 | A- |
| C02 | Modeling of Single Mixed Refrigerant Process for Offshore Natural Gas Liquefaction | UMP thesis | 海上天然气，简化组成 | `SMR/PRICO` | 单混合制冷流程结构、MR 分离后混合、冷箱组织 | 更偏研究/教学，边界与工程输出不足 | B+ |
| C03 | Development of an Energy-Efficient Single Mixed Refrigerant Cycle for Small-Scale LNG Production | Ind. Eng. Chem. Res., 2021 | 小型 LNG，简化气源 | `SMR` | HYSYS 中 MSHE 的自由度、MR 组成/压力作为优化变量、结构改造思路 | 更偏优化研究，预处理和全厂接口不完整 | B+ |
| C04 | On Small Scale LNG Concepts | ASME / ResearchGate公开稿 | 纯甲烷假设 | `N2 expander` 对比研究 | 小型 LNG 路线适用性、机械驱动和负荷变化、N2 expander 稳健性 | 以纯甲烷代替天然气，不可直接当工程模板 | C+ |
| C05 | Single Mixed Refrigerant Gas Liquefaction Process | Google Patents US6347531B1 | 预脱水天然气 | `SMR/PRICO` | 工程化的 MR 分段蒸发、冷箱功能分区、SMR 工艺边界 | 专利强调发明点，不提供 HYSYS 可执行细节 | B |
| C06 | Multi Nitrogen Expansion Process for LNG Production | Google Patents WO2013057314A2 | 预处理后天然气 | `多级 N2 expander` | 多膨胀级减熵增、压力等级组织、N2 回路结构 | 偏路线示意，设备与报表信息不足 | B |
| C07 | Honeywell UOP LNG Pretreatment / LNG Industry Pretreatment Articles | Honeywell UOP / LNG Industry / BASF | 实际天然气 | 预处理边界 | AGRU、脱水、脱汞、重烃控制顺序和出口规格接口 | 不是 HYSYS 模型，不含收敛细节 | A-（作为边界模板） |
| C08 | Cheresources LNG exchanger / recycle discussions | Cheresources 论坛 | 不特定 | HYSYS 表达经验 | 多股换热器温差穿越、分段换热器建模、Recycle 关闭技巧 | 工程可信度参差不齐，不可直接模板化 | C |

---

## 3. 重点案例分析

### 案例 A：C01 `N2 dual expander` 与 `SMR` 并行对比

- 流程目标：比较中小型 LNG 中两条典型路线的能耗与火用表现。
- 流程边界：从净化天然气进入液化主流程开始，到 LNG 生成和末端闪蒸结束；预处理被边界化。
- 核心结构：
  - `SMR`：MR 压缩、后冷、分离、节流、主冷箱换热、末端闪蒸。
  - `N2 dual expander`：N2 多级压缩、中间冷却、双膨胀机、主冷箱换热、天然气节流/分离。
- 优点：
  - 明确给出`PR 物性`、`75% 压缩机/膨胀机效率`、`MITA = 3°C`、`末端闪蒸 8%`等关键假设。
  - 两条路线放在同一评价口径下，便于模板首轮选型。
  - 对中小型 LNG 路线比较非常有价值。
- 缺点：
  - 原料气过于简单，几乎没有真实预处理约束。
  - 末端闪蒸和 Fuel gas 只以研究性边界处理，没有完整稳态接口说明。
  - 更像“优化基线模型”，不是工程模板。
- 值得吸收的点：
  - 统一的比功口径。
  - 明确的冷箱 MITA 假设。
  - 对 `N2 expander` 与 `SMR` 的适用性区分。
- 不宜照搬的点：
  - 不能直接采用其简化原料气与无压降假设作为 50万方/天工程模板默认值。

### 案例 B：C02 `SMR/PRICO` 学位论文案例

- 流程目标：用 HYSYS 建立单混合制冷液化流程，并测试 MR 分离/混合结构改动。
- 流程边界：主要聚焦液化主循环，对预处理与下游罐区边界描述不足。
- 核心结构：
  - MR 压缩
  - 后冷却
  - 高压 MR 分离
  - 两相 MR 进入冷箱前重组或分路
  - 冷端 JT 节流
  - 主冷箱完成冷却、液化、过冷
- 优点：
  - 非常适合学习`PRICO 类最小模板`的 HYSYS 表达。
  - 对`MR 相态组织`和“分离后再混合”的处理有启发。
  - 可迁移到 50万方/天的方案级主循环骨架。
- 缺点：
  - 工程边界不够完整，缺少设备表/物流表/审查说明。
  - 不能直接代表陆上中小型 LNG 预处理和公用工程接口。
- 值得吸收的点：
  - `SMR` 主循环可拆成“压缩与后冷”“分离与节流”“主冷箱”三个子系统。
  - MR 进入冷箱前的相态管理必须显式化。
- 不宜照搬的点：
  - 不能把其流程图直接视作 50万方/天的工程模板全貌。

### 案例 C：C03 小型 LNG `SMR` 优化研究

- 流程目标：降低小型 LNG 的单位液化能耗。
- 流程边界：从净化气到 LNG 成品，重点在液化主回路和主冷箱。
- 核心结构：
  - HYSYS `MSHE`
  - MR 总流量与组成优化
  - 蒸发压力、压缩机排压、分流比优化
- 优点：
  - 把 `MSHE` 中哪些变量能调、哪些温度应作为自由度说得较清楚。
  - 适合提炼`关键设计变量模板`。
- 缺点：
  - 优化目的很强，工程可维护性、命名规范、边界说明不足。
  - 对预处理、末端 fuel gas、BOG 接口覆盖不够。
- 值得吸收的点：
  - `MR 组成 + 高低压 + 流量 + MSHE 出口温度`是 SMR 的核心变量集。
  - HYSYS 中换热器自由度必须受控，否则容易过约束。
- 不宜照搬的点：
  - 不应把优化后数字直接作为默认模板值。

### 案例 D：C04 小型 LNG 概念综述中的 `N2 expander`

- 流程目标：比较小型 LNG 概念和机械/工况适应性。
- 流程边界：偏热力学循环与机械特性，不含真实预处理。
- 核心结构：
  - 两级压缩 + 中间冷却
  - 膨胀机降温
  - N2 闭式循环与天然气换热
- 优点：
  - 明确表明 `N2 expander` 在结构简单、设备紧凑方面的优势。
  - 对首轮最小模板十分友好。
- 缺点：
  - 使用纯甲烷假设，仅适合路线学习。
  - 不能反映真实天然气中 N2、C2+、CO2、重烃和冻结风险。
- 值得吸收的点：
  - 首轮教学/最小模板优先选 `N2 expander` 更稳健。
- 不宜照搬的点：
  - 不能把纯甲烷案例的液化率和比功直接当作工程预测值。

### 案例 E：C07 预处理工程资料

- 流程目标：明确 LNG 液化前必须去除的风险组分与典型单元顺序。
- 流程边界：进站分离、MRU、AGRU、脱水、重烃控制，到进入液化冷箱前。
- 核心结构：
  - inlet separation
  - mercury removal
  - acid gas removal
  - molecular sieve dehydration
  - heavy hydrocarbon removal
- 优点：
  - 明确了工程边界和出口规格接口，是概念模板不可缺少的底层约束。
  - 能帮助 HYSYS 模板区分“应详细建模”和“应边界化处理”的对象。
- 缺点：
  - 不含 HYSYS 操作细节。
- 值得吸收的点：
  - 首轮模板必须至少保留`预处理出口规格接口`，即使不详细建模，也不能省略。
- 不宜照搬的点：
  - 不能把专利/厂商宣传中的性能表述直接当成设计保证值。

---

## 4. LNG流程的标准建模规律

### 4.1 标准主流程

#### `N2 expander` 路线

1. `RAW_FEED_GAS` 进入预处理边界。
2. 输出 `DRY_SWEET_FEED_GAS` / `FEED_TO_COLD_BOX`。
3. 天然气在主冷箱内完成预冷、液化、必要过冷。
4. 氮循环完成`压缩 - 后冷却 - 分流/分压级 - 膨胀 - 回冷箱 - 回压缩机吸入口`。
5. 冷端天然气经 `JT` 或闪蒸分离形成 `LNG_PRODUCT` 与 `FLASH_GAS_TO_FUEL`。

#### `SMR / PRICO` 路线

1. `DRY_SWEET_FEED_GAS` 进入主冷箱。
2. MR 回路完成`压缩 - 后冷 - 高压分离 -（必要时气液重组或分路）- 冷端节流 - 回冷箱蒸发吸热 - 回压缩机`。
3. 天然气在冷箱中依次完成预冷、液化、过冷。
4. 冷端经阀降压进入 `LNG_FLASH_SEPARATOR`。
5. 液相出 `LNG_PRODUCT`，气相进入 `FLASH_GAS_TO_FUEL / BOG_RETURN / VENT_INTERFACE`。

#### `50万 Nm3/d` 扩展模板必须补上的边界

- 预处理出口规格
- 燃料气回收接口
- 稳态 BOG 接口
- 总电耗统计口径
- 主要设备与物流输出

### 4.2 关键单元操作及作用

- `Separator`：进站分离、MR 高压闪蒸、LNG 末端闪蒸。
- `Compressor`：原料气补压、MR/N2 制冷剂压缩、BOG/Fuel gas 压缩。
- `Cooler / Aftercooler`：压缩后冷却、降低循环功。
- `Heat Exchanger`：局部冷却器、回热器。
- `MultiStream Heat Exchanger`：主冷箱核心单元，表达多股冷热物流换热。
- `Valve / JT Valve`：冷量生成、末端降压、MR 节流。
- `Expander`：N2 路线的主制冷设备，也可用于部分回收功。
- `Mixer / Splitter`：MR 相态组织和 N2 分流级。
- `Recycle`：闭合 MR/N2 回路、Fuel gas 回路。
- `Design Spec`：设定 LNG 出口温度、末端闪蒸率、MR 组成闭合目标。
- `Adjust`：联动压力、流量、分流比。
- `Spreadsheet`：只做报表和透明中间变量，不做隐藏工艺逻辑。
- `Boundary / Interface`：AGRU、Dehydration、MRU、Heavy HC Removal 的首轮黑箱边界表达。

### 4.3 关键设计变量

- 原料气压力、温度、流量、组成
- `N2`、`CO2`、`H2S`、`C2+`、`C5+` 含量
- 预处理出口规格
- 冷箱入口压力
- LNG 产品压力与温度
- 末端闪蒸比例
- MR 组成、总循环量、高低压
- N2 高/中/低压等级及分流比
- 压缩机级数与效率
- 膨胀机效率
- 冷箱 `MITA`
- 冷端温差分布与 pinch 位置
- 压降假设
- 甲烷回收率
- 单位 LNG 比功 / 单位原料气电耗

### 4.4 物性方法建议与边界

- 冷箱/液化主循环：首轮优先采用`Peng-Robinson`或同类烃类 EOS，便于天然气与 MR/N2 统一表达。
- 预处理区：
  - 若仅做概念边界，允许统一物性近似，但必须标注`用于接口，不用于溶剂/吸附设备详细设计`。
  - `AGRU`、含酸气吸收再生、含水吸附再生，不建议首轮在同一主模型中详细展开。
- 含酸性组分区域：若要详细建模，往往需要与主液化模型分边界处理，不能默认用同一 EOS 粗暴贯穿所有精细机理。
- 含水区域：液化主流程前必须边界化到“已满足进冷箱规格”，否则 HYSYS 冷端结果没有工程意义。
- 首轮可黑箱化：
  - `酸气脱除`
  - `脱水`
  - `脱汞`
  - `重烃控制`
- 但必须保留的接口规格：
  - `CO2`
  - `H2S`
  - `H2O`
  - `Hg`
  - `C5+ / 重烃露点`
  - `N2`

### 4.5 常见收敛难点

- 多股换热器温差穿越或局部 pinch 未被发现。
- MR 初始组成或初始相态不合理，导致冷箱入口闪蒸异常。
- N2 高中低压级设定不合理，导致 expander 出口温度和换热目标矛盾。
- `Recycle` 与 `Design Spec` 同时控制同一自由度，互相“打架”。
- 一开始就把预处理、液化、BOG、燃料气全部强耦合。
- LNG 出口温度、出口压力、液化率、闪蒸率同时被过约束。
- 冷箱压降、连接线压降不说明，导致能耗失真。
- 把复杂 MR 自动优化提前塞进首轮模板，使基线结构都不稳定。

### 4.6 常见坏习惯

- 把简单 `N2 expander` 教学模型直接当成 50万方/天工程模板。
- 把纯甲烷液化案例当成真实天然气液化方案。
- 省略预处理边界，只保留“天然气进冷箱”。
- 不说明路线为什么选 `N2` 还是 `SMR`。
- 不解释物性方法和适用边界。
- 不说明 `CO2/H2O/Hg/重烃冻结风险`。
- 只给流程图，不给假设表、物流表、设备表。
- 把 Spreadsheet 变成隐藏逻辑黑箱。
- 把稳态 BOG / fuel gas 接口伪装成储罐瞬态模型。

---

## 5. 建议的 HYSYS LNG模板结构

### 5.1 模板A：最小可行 LNG液化模型

#### A1 `N2 expander` 最小模板

- 适用目标：快速建立稳健、可收敛、可解释的 LNG 液化核心逻辑。
- 边界：
  - 输入 `DRY_SWEET_FEED_GAS`
  - 输出 `LNG_PRODUCT`
  - 输出 `FLASH_GAS_TO_FUEL`
- 必含单元：
  - `MCHE-101`
  - `K-301A/B/C Nitrogen Compressor`
  - `E-301A/B Intercooler`
  - `EXP-301/302`
  - `VLV-201 LNG JT Valve`
  - `V-201 LNG Flash Separator`
  - `REC-301 Nitrogen Recycle`
- 价值：
  - 最适合首轮学习收敛、命名、冷箱温差组织。
- 局限：
  - 能耗通常高于优质 `SMR`，不宜默认作为最优工程路线。

#### A2 `SMR/PRICO` 最小模板

- 适用目标：表达中小型 LNG 更工程化的主循环。
- 边界：
  - 输入 `DRY_SWEET_FEED_GAS`
  - 输入 `MR_MAKEUP`
  - 输出 `LNG_PRODUCT`
  - 输出 `FLASH_GAS_TO_FUEL`
- 必含单元：
  - `K-301 MR Compressor`
  - `E-301 MR Aftercooler`
  - `V-301 MR HP Separator`
  - `MCHE-101`
  - `VLV-301 MR JT Valve`
  - `VLV-201 LNG JT Valve`
  - `V-201 LNG Flash Separator`
  - `REC-301 MR Recycle`
- 价值：
  - 更接近 50万方/天中小型液化厂的方案表达。
- 局限：
  - 对 MR 组成、相态、换热器自由度更敏感。

#### 模板A 路线结论

- `A1` 更适合学习稳健结构和简洁收敛。
- `A2` 更适合作为中小型 LNG 的首选工程化模板骨架。
- 首轮模板不应无条件泛化到所有原料气场景，特别是高 N2、高重烃、高 CO2 原料气。

### 5.2 模板B：扩展版 `50万 Nm3/d` 工程模板

- 在模板A基础上增加：
  - `ABS-101 Acid Gas Removal Boundary`
  - `ADS-101 Dehydration Boundary`
  - `MBD-101 Mercury Removal Boundary`
  - `HHC-101 Heavy HC Control Boundary`
  - `K-101 Feed Gas Compressor`（如需补压）
  - `MCHE-101` 主冷箱
  - `V-201` 末端闪蒸
  - `BOG_RETURN` 稳态接口
  - `FLASH_GAS_TO_FUEL` / `VENT_INTERFACE`
  - `SPRD-101 Power & LNG KPI Sheet`
- 输出能力必须支持：
  - 设计基础表
  - 工艺边界说明
  - 关键假设表
  - 主要物流表
  - 主要设备表
  - 压缩机功耗与冷量统计
  - 甲烷回收率 / 液化率统计
  - 路线选择说明
  - 收敛说明
  - 局限性说明

### 5.3 模板C：系统级 LNG概念模型

- 目标：评估`原料气 - 预处理 - 液化 - LNG 产品 - Fuel gas / BOG`的一体化概念边界。
- 特征：
  - 允许预处理黑箱化，但必须显式保留接口规格。
  - 允许罐区只保留稳态 BOG 接口，不展开瞬态储罐模型。
  - 用于 TEA 前处理和路线筛选，不用于设备采购。

### 5.4 首轮不建议加入的复杂内容

- 动态开停工
- 冷箱真实几何结构与板翅/绕管详细模型
- 分子筛切换逻辑
- 脱汞床寿命模型
- 储罐瞬态 BOG
- 装车/船装瞬态
- 防喘振控制细化
- 全厂公用工程耦合
- 大规模 MR 自动优化
- 设备级机械设计计算

---

## 6. 人类可读性规范建议

### 6.1 命名规范

#### 物流命名示例

- `RAW_FEED_GAS`
- `FEED_GAS_TO_TREAT`
- `DRY_SWEET_FEED_GAS`
- `FEED_TO_COLD_BOX`
- `MR_COMP_SUCTION`
- `MR_COMP_DISCH`
- `MR_HP_STREAM`
- `MR_JT_OUT`
- `N2_EXP_IN`
- `N2_EXP_OUT`
- `LNG_SEPARATOR_VAP`
- `LNG_PRODUCT`
- `FLASH_GAS_TO_FUEL`
- `BOG_RETURN`
- `FUEL_GAS`
- `VENT_GAS`

#### 设备命名示例

- `K-101 Feed Gas Compressor`
- `E-101 Feed Gas Cooler`
- `ABS-101 Acid Gas Removal Boundary`
- `ADS-101 Dehydration Boundary`
- `MBD-101 Mercury Removal Boundary`
- `MCHE-101 Main Cryogenic Heat Exchanger`
- `VLV-201 LNG JT Valve`
- `EXP-201 Nitrogen Expander`
- `V-201 LNG Flash Separator`
- `K-301 MR Compressor`
- `REC-101 MR Recycle`
- `DS-101 LNG Outlet Specification`

#### 禁止命名

- `stream1`
- `cool2`
- `finalgas`
- `newhex`
- `case_final_real`
- `mixxx`
- `recycle_test`

### 6.2 分区规范

- 原料气区
- 预处理区
- 主压缩区
- 液化主循环区
- 制冷剂压缩与分离区
- 冷箱区
- 末端闪蒸与产品区
- flash gas / fuel gas / vent 区
- 公辅与能耗统计区

### 6.3 假设说明规范

每个模板必须显式列出：

- 原料气来源与组成边界
- 设计流量、压力、温度
- 预处理出口规格
- 物性方法
- 压降假设
- 压缩机效率
- 膨胀机效率
- 冷端 `MITA`
- 主冷箱建模方式
- 制冷剂组成与初值来源
- 末端闪蒸策略
- LNG 产品边界条件
- BOG/fuel gas 处理边界
- 模型不覆盖内容

### 6.4 HYSYS 表达规范

- 优先使用 `Sub-Flowsheet` 区分：
  - 预处理
  - 主液化循环
  - 制冷剂子系统
  - 产品与尾气边界
- `Design Spec` 必须命名并注明目的。
- `Recycle` 必须命名并注明闭合对象。
- `Spreadsheet` 只用于透明报表和简单中间变量。
- `MSHE` 必须明确冷热侧、主要 pinch 检查点和温差约束。
- 黑箱单元必须明确命名为 `Boundary` 或 `Interface`。
- 禁止用一整页未分区流程图堆积全部设备。

### 6.5 结果输出规范

模板输出必须支持：

- 模型摘要
- 工艺说明
- 设计基础表
- 主要设备表
- 主要物流表
- 关键假设表
- 电耗与负荷统计表
- 甲烷回收率/液化率统计表
- 收敛说明
- 局限性说明
- 需后续复核项清单

---

## 7. 学习结论

### 7.1 哪些案例值得进入模板库

- `C01`：适合进入`路线比较模板库`和`关键变量/假设模板库`。
- `C02`：适合进入`SMR 最小模板候选库`。
- `C03`：适合进入`SMR 关键变量与 MSHE 约束模板库`。
- `C07`：适合进入`预处理边界模板库`。
- `C05/C06`：适合进入`路线结构参考库`。

### 7.2 哪些只能做参考

- `C04`：适合学习 `N2 expander` 结构，但只能作路线教学参考。
- `C08`：适合学 HYSYS 实现细节与收敛问题，不可作为工程模板来源。

### 7.3 哪些不建议学习为工程模板

- 纯甲烷 JT 演示液化流程
- 不说明物性方法的“能跑通”分享文件
- 仅给流程图、不给假设和报表的案例
- 直接把大型 `C3MR/DMR` 方案缩放后冒充中小型 LNG 模板的资料

### 7.4 后续建模代理应优先使用什么模板路线

- 若目标是`先形成稳健、可读、可复核的基础模板`：优先 `模板A1 N2 expander`。
- 若目标是`尽快逼近 50万方/天的工程化方案模板`：优先 `模板A2/模板B 的 SMR/PRICO 骨架`。
- `C3MR` 只建议作为对照学习，不建议作为首轮默认模板。

---

## 8. 下一步建议

- 继续补充案例：
  - 补齐公开 `PRICO/SMR` HYSYS 个案
  - 补齐高氮天然气、小型 LNG、末端 BOG/fuel gas 资料
- 开始搭建最小模板：
  - 先做 `模板A1 N2 expander`
  - 再做 `模板A2 SMR`
- 开始建立扩展版工程模板：
  - 在最小模板稳定后增加预处理边界和报表接口
- 开始编写 LNG 工艺包输出模板：
  - 形成固定的`设计基础表 + 物流表 + 设备表 + KPI 表 + 局限性说明`
- 开始建立路线选择比较模板：
  - 对 `N2 expander`、`SMR/PRICO`、参考性 `C3MR` 建立统一决策表

---

## 9. 专项学习问题回答

### 9.1 对 `50万 Nm3/d` 中小型液化厂，首轮模板优先学习哪类路线

- `N2 expander`
  - 优点：结构简单、设备少、可读性强、HYSYS 收敛稳健。
  - 缺点：能耗通常偏高。
  - 结论：更适合`最小可行模板`与教学模板。
- `SMR / PRICO`
  - 优点：更接近中小型 LNG 的工程化主流路线，能效通常优于单纯 N2。
  - 缺点：MR 相态、组成、MSHE 约束更敏感。
  - 结论：更适合`50万方/天首轮工程模板`。
- `C3MR`
  - 优点：大中型 LNG 工程代表性强。
  - 缺点：复杂度与规模假设通常超出 50万方/天首轮模板需要。
  - 结论：只作参考上限，不作默认首选。

### 9.2 原料气预处理在概念模型中，应详细建模还是边界化黑箱更合理

- `酸气脱除`：首轮建议黑箱化，但必须保留 `CO2/H2S` 出口规格。
- `脱水`：首轮建议黑箱化，但必须保留进冷箱前 `H2O` 规格。
- `脱汞`：首轮建议黑箱化，但必须保留 `Hg` 风险说明和接口。
- `重烃控制`：首轮可边界化，但必须保留`重烃露点/冻结风险`说明。
- 结论：首轮`以边界化更合理`，但绝不能省略接口规格。

### 9.3 HYSYS 中物性方法应如何按区域处理

- 冷箱/液化主循环：优先统一 `PR` 类 EOS。
- 原料气预处理：若仅做边界，可与主模型统一近似；若做 AGRU/含水详细模型，应分边界处理。
- 含酸性组分区域：不建议与主液化模型强行共用单一粗略 EOS 做详细机理。
- 含水区域：只保留到“达标接口”，不在首轮冷箱主模型中延伸。
- 结论：首轮允许统一近似，但必须显式注明适用边界。

### 9.4 多股换热器应做到什么深度

- 教学表达深度：
  - 1 台 `MSHE` 表达主冷箱热量交换即可。
- 方案表达深度：
  - 至少标出主要热/冷侧、MITA、压降假设、pinch 检查点。
- 接近工艺包草稿的表达深度：
  - 可按功能区拆成预冷段、液化段、过冷段或 2~3 台串联换热器；
  - 但仍不应假装已经完成真实板翅几何设计。
- 首轮不能假装做完的内容：
  - 板翅详细通道
  - 翅片结构
  - 真实分配器
  - 详细机械校核

### 9.5 末端闪蒸、fuel gas、vent、BOG 边界应做到什么深度

- 稳态模型至少应做到：
  - `LNG_PRODUCT`
  - `FLASH_GAS_TO_FUEL`
  - `VENT_INTERFACE`
  - `BOG_RETURN` 稳态占位接口
- 不应混入首轮模板的内容：
  - 储罐瞬态
  - 装车/装船瞬态
  - 罐压波动控制
  - 动态 BOG 预测

### 9.6 哪些结果可直接用于技术经济分析输入，哪些不能

- 可用于 TEA 输入：
  - 稳态压缩机功耗
  - 主冷箱和后冷却器热负荷
  - LNG 产率
  - 甲烷回收率
  - 燃料气比例
  - 主要设备数量级
- 仅概念级有效：
  - 单位液化能耗
  - 冷量分配
  - MR 组成初值
  - 冷端温差分布
- 不可直接用于采购/施工设计：
  - 压缩机保证功率
  - 冷箱面积和几何
  - 分子筛床层尺寸
  - 脱汞床寿命
  - 控制阀最终选型

### 9.7 哪些风险必须在模板中显式提醒

- `CO2/H2O/重烃/Hg` 冻结或材料风险
- 冷端温差穿越与局部 pinch 风险
- 原料气中 `N2` 导致液化率下降和闪蒸损失增加
- 路线选择与能耗/复杂度权衡
- 稳态模型对实际操作波动、启停工和季节变化的代表性边界

---

## 10. 参考来源

1. MDPI Energies 2020: Performance Enhancement of Nitrogen Dual Expander and Single Mixed Refrigerant LNG Processes Using Jaya Optimization Approach  
   https://www.mdpi.com/1996-1073/13/12/3278
2. UMP Thesis: Modeling of Single Mixed Refrigerant Process for Offshore Natural Gas Liquefaction  
   https://umpir.ump.edu.my/id/eprint/5295/
3. Ind. Eng. Chem. Res. 2021: Development of an Energy-Efficient Single Mixed Refrigerant Cycle for Small-Scale LNG Production  
   https://pubs.acs.org/doi/abs/10.1021/acs.iecr.1c00432
4. Google Patents: US6347531B1 Single Mixed Refrigerant Gas Liquefaction Process  
   https://patents.google.com/patent/US6347531B1/en
5. Google Patents: WO2013057314A2 Multi Nitrogen Expansion Process for LNG Production  
   https://patents.google.com/patent/WO2013057314A2/en
6. Honeywell UOP LNG Pretreatment  
   https://uop.honeywell.com/en/industry-solutions/gas-processing/lng/lng-pretreatment
7. LNG Industry: The Fundamentals of Feed Gas Pretreatment  
   https://www.lngindustry.com/special-reports/27122019/the-fundamentals-of-feed-gas-pretreatment/
8. LNG Industry / BASF: Coming Out of the Ice Age  
   https://www.lngindustry.com/special-reports/06052021/coming-out-of-the-ice-age/
9. AspenTech webinar PDF: Improve Design and Operation of Gas / Better Process LNG Integration  
   https://www.aspentech.com/-/media/aspentech/home/resources/live-events-and-webinars/pdfs/fy24/q2/gas-processing-webinar.pdf
10. Cheresources: Temperature Cross in LNG Exchanger  
    https://www.cheresources.com/invision/topic/23016-temperature-cross-in-lng-exchanger/
11. Cheresources: Hysys Heat Exchanger (LNG)  
    https://www.cheresources.com/invision/topic/26361-hysys-heat-exchanger-lng/
12. On Small Scale LNG Concepts  
    https://www.researchgate.net/publication/354647904_On_Small_Scale_LNG_Concepts

---

## 11. 本轮自评

| 评价项 | 分数（1~5） | 说明 |
|---|---:|---|
| 案例覆盖度 | 4 | 已覆盖 `SMR`、`N2 expander`、预处理、专利、社区经验，但还缺更多公开 HYSYS 原生文件。 |
| 案例质量判断准确性 | 4 | 已能区分教学案例、优化案例、工程边界资料，但仍需更多一手培训案例交叉验证。 |
| LNG建模规律提炼深度 | 4 | 已提炼主流程、变量、物性、收敛和坏习惯，下一轮可补更细的 KPI 口径。 |
| 模板化程度 | 4 | 已形成 A/B/C 三层模板框架，但尚未落成具体 HYSYS 对象清单和子流程图。 |
| 对后续自动建模的可用性 | 4 | 已可指导自动建模代理的首轮路线与边界设置，下一步应补充具体模板字段和输出 schema。 |

结论：本轮成果可作为`第一轮学习基础`，但尚未达到“学习完成”。主要缺口是：`公开 HYSYS 原生案例样本不足`、`BOG/fuel gas 稳态边界案例仍偏少`、`扩展模板尚未转成可直接实例化的对象清单`。

---

# 第二轮专题补充：高氮天然气与 BOG / fuel gas 稳态边界

## 1）本轮学习对象

- 学习层级：`高氮天然气进入 LNG 冷端前的脱氮/NRU边界` + `LNG末端闪蒸、BOG、fuel gas、vent 的稳态边界`
- 原料气类型：`高 N2 天然气` 与 `常规 LNG 罐区/装船返回 BOG`
- 本轮路线对象：
  - 高氮气：`NRU + LNG 集成`
  - BOG：`recondensation / compression-to-fuel / partial reliquefaction`
- 本轮目标模型深度：`概念级到方案级稳态接口模板`

## 2）案例收集范围

- 高氮天然气液化、NRU、低温脱氮与 LNG 集成的 HYSYS 论文、专利和工程资料。
- LNG 装船/储罐 BOG 回收、再冷凝、送 fuel gas、必要放空的 HYSYS 研究和专利。
- 重点识别：
  - `N2 对液化率、闪蒸损失、产品规格、fuel gas 可用性` 的影响
  - `BOG 温度窗口`、`压缩机允许入口温度`、`flare/fuel gas/reliquefaction` 的分界条件

## 3）案例筛选标准

- 必须能看清 `NRU` 或 `BOG` 的流程边界，而不是只有热力学结果。
- 优先保留能指导`首轮 HYSYS 稳态模板边界设置`的资料。
- 仅在`接口条件、去向逻辑、压力层级、物性口径`清楚时，才进入专题模板候选库。

## 4）质量评估方法

- `A级`：能支撑边界模板或决策模板。
- `B级`：能提供结构与规律，但工程输出不完整。
- `C级`：只适合学局部操作或学术优化。
- `D级`：不建议用于模板提炼。

## 5）预期模板输出内容

- `高氮天然气模板补丁`：何时必须加 `NRU Interface`
- `BOG / fuel gas 稳态边界模板`
- `高氮气与 BOG 风险提醒清单`
- `路线选择触发条件表`

## 6）开始收集与分析

本轮聚焦补齐第一轮的两个缺口，不扩展到动态储运或详细 NRU 设备设计。

---

## 1. 本轮学习对象

- 主题A：`高氮天然气与 LNG 液化的耦合边界`
- 主题B：`BOG / fuel gas / vent / end flash gas 的稳态边界`
- 目标：建立后续自动建模代理在遇到`高 N2`和`BOG 接口`时的默认处理规则

---

## 2. 已补充案例清单

| 编号 | 案例名称 | 来源 | 原料气类型 | 路线类型 | 适合学习内容 | 局限性 | 质量等级 |
|---|---|---|---|---|---|---|---|
| S01 | Upfront Nitrogen Removal as Process Enhancing Concept | Qatar University thesis, 2023 | 含氮天然气 | `NRU + LNG 冷端集成` | 高氮气进入冷端前脱氮的价值、能耗与产量影响、HYSYS+EDR 集成思路 | 偏大厂冷端优化，不是中小型标准模板 | A- |
| S02 | Process analysis and optimization of high-N2 natural gas liquefaction | Journal of Natural Gas Science and Engineering, 2023 | 高 N2 天然气 | `单塔 NRU + LNG 集成` | 何时必须加 NRU、单塔脱氮的关键变量、N2 对比功与 LNG 产品规格的影响 | 偏研究优化，详细工程边界不足 | A- |
| S03 | Configurations and Methods for Nitrogen Rejection, LNG and NGL Production from High Nitrogen Feed Gases | US9920986B2 / US20150246859A1 | 高 N2、高 C3+ 天然气 | `NRU + NGL + LNG` | 工程边界、重烃与脱氮的耦合顺序、不同 N2 含量下路线分层 | 专利不提供完整 HYSYS 可执行细节 | B+ |
| S04 | Two-stage nitrogen removal from LNG streams | EP1715267A1 | LNG 中高 N2 | `两段脱氮 + fuel gas/vent 约束` | 高 N2 时 fuel gas 容忍度与 vent 纯度边界、N2 去向管理 | 更偏大型 LNG 场景，不直接适配中小型模板 | B |
| S05 | Computer Aided Design for the Recovery of Boil-Off Gas from LNG Plant | SCIRP, 2019 | LNG 罐区/装船 BOG | `quench + flash + compression-to-fuel` | BOG 温度场景、何时进压缩机、何时先淬冷/闪蒸、送 fuel gas 的稳态逻辑 | 数据质量一般，部分工况假设较粗 | B |
| S06 | Performance Improvement of a BOG Re-condensation Process with Pre-cooling at LNG Terminals | IJOT, 2015 | 接收站 BOG | `压缩 + 预冷 + 再冷凝` | BOG 再冷凝与预冷路径、功耗影响、BOG 稳态处理方法 | 偏接收站，不等同液化厂储罐边界 | B+ |
| S07 | Equipment and process for liquefaction of LNG boiloff gas | US7581411B2 | 储罐/船舶 BOG | `N2 循环 BOG 再液化` | BOG 可靠再液化、N2 expander 在 BOG 场景的适用性 | 偏船舶/独立再液化，不是 LNG 主厂流程 | B |
| S08 | LNG BOG compression / recondensation optimization articles | 中文期刊与终端研究 | 储罐/接收站 BOG | `直接压缩/再冷凝/高压 LNG 冷量回收` | BOG 处理的典型口径、功耗贡献、外输波动适应性 | 更偏接收站和罐区，不含主液化冷箱 | C+ |

---

## 3. 重点案例分析

### 案例 S01：上游脱氮前移到 LNG 冷端之前

- 流程目标：验证`高 N2 气源`在进入主液化冷端前，先做部分脱氮是否能够同时降低功耗并提升 LNG 产量。
- 流程边界：预处理后到冷端、NRU、液化和冷端换热优化，不展开上游 AGRU/脱水细节。
- 核心结构：
  - feed pretreatment interface
  - nitrogen removal unit
  - refrigeration cold section
  - LNG product and nitrogen-rich stream
- 优点：
  - 明确指出冷端由制冷循环、分馏、NRU、氦提取等组成，适合提醒后续模板不要把“高氮气直接液化”当默认路径。
  - 给出了`脱除约 87.5% N2`时功耗和产量改善的定量研究结论。
- 缺点：
  - 偏大型 LNG 冷端增强概念，规模与复杂度高于首轮模板。
- 值得吸收的点：
  - `N2` 不是单纯的产品质量问题，而是会改变`总功耗、液化率、冷端负荷分布`。
  - 当原料气氮含量偏高时，`NRU Interface`必须成为独立边界，而不是在主冷箱里“顺便处理”。
- 不宜照搬的点：
  - 不应把大型综合冷端配置直接搬到 50万方/天模板。

### 案例 S02：高氮天然气单塔 NRU + LNG 集成

- 流程目标：在 HYSYS 中用单塔脱氮与膨胀制冷耦合，研究高 N2 天然气液化的能耗与规格。
- 流程边界：预处理后天然气进入 NRU，再与 LNG 主流程耦合。
- 核心结构：
  - single-column NRU
  - methane-nitrogen expansion refrigeration
  - sensitivity on feed temperature, pressure, column pressure and refrigerant pressure
- 优点：
  - 非常适合提炼`高氮气触发条件`。
  - 给出了行业背景：天然气中 N2 常见范围可到 14.26%，甚至更高；管输甲烷质量常要求 N2 不高于约 3%。
  - 明确说明高 N2 会提升 LNG 运输能耗并降低热值。
- 缺点：
  - 偏单元优化，设备与输出结构不足。
- 值得吸收的点：
  - 对首轮模板，若`N2 > 常规商品气范围`并明显影响 LNG 成品或闪蒸损失，则必须单列 `NRU Interface`。
  - 高氮天然气不适合简单套用标准 `SMR/PRICO` 模板后只调 MR。
- 不宜照搬的点：
  - 不应把单塔 NRU 默认化为所有高氮气的唯一方案。

### 案例 S05：BOG 经淬冷 / 闪蒸 / 压缩送 fuel gas

- 流程目标：减少 LNG 厂装船或储运环节的 BOG 放空。
- 流程边界：从 BOG 返回总管开始，到送入 fuel gas 或回液相产品，不含储罐动态热漏建模。
- 核心结构：
  - BOG 按不同温度场景进入系统
  - 温度过高时先 flare 或先冷却
  - 允许时进入闪蒸/淬冷鼓
  - 气相进 BOG 压缩机
  - 液相泵回 LNG header
  - 压缩后气体送 fuel gas header
- 优点：
  - 明确区分了不同 BOG 场景的工程处理逻辑。
  - 点出了压缩机允许入口温度是稳态边界建模的重要切分条件。
- 缺点：
  - 案例质量一般，参数和工况更适合“规律学习”而不是模板数值来源。
- 值得吸收的点：
  - 首轮模板中，`BOG_RETURN`不能被简单画成“一股总是可压缩的冷气”。
  - 需要显式区分：
    - `warm BOG`
    - `cold BOG`
    - `normal tank BOG`
- 不宜照搬的点：
  - 不应直接照搬其流量和设备数据。

### 案例 S06：BOG 再冷凝 + 预冷

- 流程目标：减少 BOG 再冷凝系统的功耗。
- 流程边界：BOG 压缩后与 LNG 冷量耦合再冷凝，典型于接收站或大罐区。
- 核心结构：
  - double-stage BOG compression
  - precooling before recondenser
  - LNG cold energy used as heat sink
- 优点：
  - 说明`BOG` 不是只有“压缩送燃料”一条路，`再冷凝`在特定站场边界下更合理。
  - 很适合后续做`BOG 处理路线比较模板`。
- 缺点：
  - 场景更像接收站或大罐区，不是中小型液化厂默认配置。
- 值得吸收的点：
  - 当存在稳定可用的高压 LNG 冷量时，可以把`BOG recondensation`作为可选子模板，而非默认主模板。

### 案例 S07：N2 循环 BOG 再液化专利

- 流程目标：用相对紧凑的 N2 闭路循环再液化 BOG。
- 流程边界：BOG 独立再液化系统，不等同 LNG 主液化冷箱。
- 核心结构：
  - BOG 两级压缩
  - N2 多级压缩 / 膨胀
  - 低温换热器再液化
- 优点：
  - 证明 `N2 expander` 不只适合主液化，也适合 BOG 独立再液化场景。
- 缺点：
  - 不适合作为主厂模板默认方案。
- 值得吸收的点：
  - 若后续需要做“零放空”专题，N2 BOG reliquefaction 可作为扩展支线。

---

## 4. 专题建模规律提炼

### 4.1 高氮天然气进入 LNG 模板时的规则

- `N2` 含量不能只作为普通组分处理，因为它会同时影响：
  - LNG 成品热值
  - 末端闪蒸损失
  - 储运 BOG 倾向
  - 单位液化功耗
- 对首轮模板的建议分层：
  - `低 N2 / 商品气级`：可沿用标准 `SMR/PRICO` 或 `N2 expander` 主模板。
  - `中等 N2、但仍可接受概念近似`：可先在模板中保留`高 N2 风险提醒`，并增加 `FLASH_GAS_LOSS_CHECK`。
  - `高 N2，明显影响 LNG 质量或闪蒸损失`：必须增加 `NRU Interface`，不能直接沿用常规模板。
- `NRU Interface` 至少应输出：
  - `N2-depleted feed to liquefaction`
  - `nitrogen-rich vent or offgas`
  - 甲烷损失估计
  - NRU 功耗或冷量需求接口

### 4.2 高氮气的预处理与液化边界顺序

- 建议顺序：
  1. inlet separation
  2. AGRU interface
  3. dehydration interface
  4. mercury interface
  5. heavy hydrocarbon control interface
  6. `NRU Interface`（如需要）
  7. liquefaction cold box
- 原因：
  - CO2/H2O/重烃问题必须先被压住，否则 NRU 和冷端都没有工程意义。
  - `NRU` 不是替代预处理，而是高氮场景下的额外冷端前处理边界。

### 4.3 BOG / fuel gas / vent 的稳态边界规则

- 首轮稳态模型必须把以下几股流显式分开：
  - `END_FLASH_GAS`
  - `TANK_BOG_RETURN`
  - `BOG_TO_COMP`
  - `FUEL_GAS_TO_HEADER`
  - `VENT_GAS`
  - `BOG_TO_RECONDENSER`（如有）
- 不能把 `end flash gas` 和 `tank BOG` 默认合并成同一股，因为：
  - 温度来源不同
  - 压力层级不同
  - 可压缩性和是否需预冷不同
  - 对 flare 的触发条件不同

### 4.4 BOG 子系统的三种首轮表达深度

#### 教学表达

- `V-201 LNG Flash Separator`
- 气相直接送 `FUEL_GAS`
- 不展开储罐和装船系统

#### 方案表达

- 区分 `END_FLASH_GAS` 与 `TANK_BOG_RETURN`
- 增加 `K-401 BOG Compressor`
- 增加 `E-401 BOG Aftercooler`
- 增加 `VENT_INTERFACE`
- 允许 `BOG_TO_FUEL` 为默认去向

#### 接近工艺包草稿表达

- 增加可选 `D-401 BOG Quench Drum / Recondensation Drum`
- 明确 BOG 压缩机入口温度限制
- 明确何时 flare、何时送 fuel gas、何时再冷凝
- 给出 BOG 设计工况表：
  - normal holding
  - loading return
  - upset / warm gas not accepted

### 4.5 何时送 fuel gas，何时 vent，何时 flare

- `送 fuel gas`：
  - 气体温度、压力、组成满足燃料系统入口边界
  - 厂内 fuel gas 有消纳能力
- `送 recondensation / reliquefaction`：
  - 现场存在稳定冷量和相应设备
  - 有减少甲烷损失或减少 flare 的明确价值
- `vent / flare`：
  - 温度过高或压力/组分不满足压缩机及 fuel gas 边界
  - BOG 突增超出压缩机与再冷凝能力
  - 富氮 offgas 不适合作燃料

### 4.6 对技术经济分析的专题补充

- 高氮气场景中，可进入 TEA 的结果：
  - NRU 是否需要设置
  - NRU 后 LNG 产率变化
  - 甲烷损失范围
  - 单位能耗变化趋势
- 仅概念级有效：
  - 单塔还是双塔 NRU 的绝对最优性
  - 氮气 vent 纯度作为排放许可依据
- BOG 场景中，可进入 TEA 的结果：
  - BOG 压缩功
  - 再冷凝功耗趋势
  - flare 减量估计
  - fuel gas 回收潜力
- 不可直接用于采购：
  - BOG 压缩机最终容量
  - recondenser 换热面积
  - flare system 最终校核

### 4.7 首轮必须显式提醒的专题风险

- 高 `N2` 导致的 LNG 成品不达标风险
- 高 `N2` 导致末端闪蒸增加、甲烷回收率下降
- 富氮 offgas 不一定适合作 fuel gas
- BOG 温度过高时不可直接压缩
- 将接收站 BOG 案例直接套到液化厂罐区会导致边界失真
- 将稳态 BOG 模型误当作储罐瞬态模型是严重误用

---

## 5. 对现有 LNG 模板的修订建议

### 5.1 模板A 的修订

- `模板A1/A2` 默认增加两个可选占位接口：
  - `NRU-101 Nitrogen Rejection Interface`
  - `BOG-401 BOG Return Interface`
- 默认不展开详细设备，但在假设表中必须写明：
  - 当前案例是否考虑高 N2
  - 当前案例是否考虑 tank BOG

### 5.2 模板B 的修订

- 在扩展版 `50万 Nm3/d` 工程模板中新增：
  - `NRU-101`（可选）
  - `K-401 BOG Compressor`
  - `E-401 BOG Aftercooler`
  - `D-401 BOG Quench / Recondensation Drum`（可选）
  - `FG-401 Fuel Gas Interface`
  - `FLR-401 Vent / Flare Interface`

### 5.3 模板C 的修订

- 系统级概念模板必须把以下边界写清：
  - `high-N2 feed branch`
  - `nitrogen-rich offgas branch`
  - `end flash gas branch`
  - `tank BOG branch`
  - `fuel gas sink`
  - `vent / flare sink`

### 5.4 新增路线选择触发条件

- 优先保持标准 `SMR/PRICO` 模板：
  - 原料气 N2 处于常规范围
  - tank BOG 仅作稳态占位接口
- 触发 `NRU Interface`：
  - N2 明显拉低 LNG 质量或甲烷回收率
  - 末端闪蒸和 fuel gas 负荷异常增大
- 触发 `BOG 子模板`：
  - 方案边界包含储罐/装船返回蒸气
  - 用户需要估算 fuel gas 回收或 flare 负荷

---

## 6. 学习结论

### 6.1 哪些专题案例值得进入模板库

- `S01`、`S02`：进入`高氮天然气决策模板库`
- `S03`、`S04`：进入`NRU 工程边界参考库`
- `S05`、`S06`：进入`BOG / fuel gas 稳态边界模板库`
- `S07`：进入`BOG 零放空扩展路线参考库`

### 6.2 哪些只能做参考

- 偏接收站的 BOG 再冷凝研究，只能作为`BOG 子模板`参考，不能直接当液化厂默认配置。
- 偏大型 LNG 的高氮脱除专利，只能作为边界上限参考，不能直接缩放成中小型模板。

### 6.3 后续建模代理的新默认规则

- 见到`高 N2`，先判断是否需要 `NRU Interface`，而不是直接调 MR 组成。
- 见到 `BOG`，先判断是`end flash gas`、`tank BOG`还是`warm loading return`，再决定去向。
- 稳态模板中必须把 `fuel gas`、`vent/flare` 作为明确的去向边界，不得省略。

---

## 7. 下一步建议

- 开始建立路线选择比较模板：
  - 把 `N2 expander`、`SMR/PRICO`、`高N2 + NRU`、`BOG 子模板` 纳入统一决策表
- 开始搭建最小模板：
  - 在 `模板A1/A2` 中加入 `NRU` 与 `BOG` 可选接口
- 开始编写 LNG 工艺包输出模板：
  - 把 `高氮风险` 和 `BOG/fuel gas 边界` 固化进假设表与局限性说明

---

## 8. 本轮补充参考来源

1. Qatar University thesis: Upfront Nitrogen Removal as Process Enhancing Concept  
   https://qspace.qu.edu.qa/handle/10576/40564
2. Journal of Natural Gas Science and Engineering: Process analysis and optimization of high-N2 natural gas liquefaction  
   https://www.sciencedirect.com/science/article/pii/S0957582023007231
3. US9920986B2 Configurations and Methods for Nitrogen Rejection, LNG and NGL Production from High Nitrogen Feed Gases  
   https://patents.google.com/patent/US9920986B2/en
4. EP1715267A1 Two-stage nitrogen removal from LNG streams  
   https://patents.google.com/patent/EP1715267A1
5. Computer Aided Design for the Recovery of Boil-Off Gas from LNG Plant  
   https://file.scirp.org/Html/3-3700942_91583.htm
6. Performance Improvement of a BOG Re-condensation Process with Pre-cooling at LNG Terminals  
   https://dergipark.org.tr/en/pub/ijot/issue/5796/77092
7. US7581411B2 Equipment and process for liquefaction of LNG boiloff gas  
   https://patents.google.com/patent/US7581411B2/en
8. AspenTech gas processing webinar  
   https://www.aspentech.com/-/media/aspentech/home/resources/live-events-and-webinars/pdfs/fy24/q2/gas-processing-webinar.pdf

---

## 9. 本轮自评

| 评价项 | 分数（1~5） | 说明 |
|---|---:|---|
| 案例覆盖度 | 4 | 已补到高氮气、NRU、BOG/fuel gas/recondensation，但仍缺更多陆上中小型 LNG 一手案例。 |
| 案例质量判断准确性 | 4 | 已能区分接收站 BOG、船舶 BOG、液化厂稳态边界，但仍需更多厂级公开资料验证。 |
| LNG建模规律提炼深度 | 4 | 已形成高氮触发规则和 BOG 去向规则，下一轮可继续细化决策阈值。 |
| 模板化程度 | 4 | 已把 NRU 与 BOG 作为模板补丁写入，但尚未变成字段化模板清单。 |
| 对后续自动建模的可用性 | 5 | 已足以指导后续代理在遇到高 N2 或 BOG 边界时不再误套常规模板。 |

结论：第二轮补充有效填补了第一轮缺口，但仍未达到最终“学习完成”。下一步最有价值的动作是把这些规则转成`路线选择比较模板`或直接嵌入`最小模板/扩展模板骨架`。
