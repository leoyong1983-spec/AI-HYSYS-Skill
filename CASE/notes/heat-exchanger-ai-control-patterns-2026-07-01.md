# HYSYS 换热器 AI 控制/优化知识沉淀

日期：2026-07-01（Asia/Shanghai）

## 一句话结论

当前可采纳的强证据不是“AI 直接闭环控制换热器”，而是：

`已有 HYSYS 或 HYSYS/EDR case -> 变量 schema -> DOE/有限场景 -> ML/灰箱/优化器给候选方案 -> HYSYS 或 EDR 回算 -> KPI 导出 -> 人工验收`。

这条路线适合并入 AI-HYSYS-Skill，用于换热器、HEN、Aspen EDR、`Delta Tmin`、LNG 冷箱和低温换热器任务。

## 有价值资料

1. `Galigeigei-Z/HDA-Surrogate-Optimization`
   - 链接：https://github.com/Galigeigei-Z/HDA-Surrogate-Optimization
   - 价值：公开 HYSYS/Python 程序案例，面向 HEN supertargeting 和 `Delta Tmin` 预筛选。
   - 采用方式：学习 workflow，不作为默认依赖。

2. Artificial intelligence assisted prediction of optimum operating conditions of shell and tube heat exchangers
   - 链接：https://doi.org/10.1049/cit2.12393
   - 价值：换热器仿真 + 灰箱/AI/GA 优化的论文证据。
   - 采用方式：支持“候选优化 + 仿真回算 + 人工确认”的换热器任务模板。

3. Optimizing Pressure Swing Distillation Using Aspen HYSYS and Machine Learning Algorithms
   - 链接：https://doi.org/10.1007/s11814-026-00646-x
   - 价值：Aspen HYSYS + XGBoost + PSO 做热负荷预测和工况优化。
   - 采用方式：作为相邻证据，说明 HYSYS baseline、ML surrogate、optimizer、HYSYS/人工复核的模式可行。

4. Enhancing LNG supply chain robustness through digital twin-driven machine learning models: cryogenic heat exchanger case
   - 链接：https://doi.org/10.1016/j.jgsce.2025.205714
   - 价值：低温换热器数字孪生和 ML 监测/预警证据。
   - 采用方式：可用于 LNG 冷箱监测、早期预警、KPI 报告，不作为生产闭环写回证据。

5. Aspen Exchanger Design and Rating
   - 链接：https://www.aspentech.com/en/products/engineering/aspen-exchanger-design-and-rating
   - 价值：AspenTech 官方换热器设计与评级能力来源。
   - 采用方式：作为产品能力依据；项目级结论仍需本地 HYSYS/EDR runtime 验证。

## 已转化为技能规则

- 换热器 AI 任务必须从已有 HYSYS、HYSYS/EDR 或 workbook-backed case 开始。
- 写入前必须记录 exchanger object、stream map、hot/cold side、单位、调节变量、上下限和回滚值。
- ML、灰箱模型、GA、BO、PSO 输出只能作为候选建议。
- 接受候选方案前必须完成 HYSYS/EDR workcopy 回算、收敛状态记录、KPI 导出、失败样本保留和人工验收。
- 建议 KPI 包括 heat duty、outlet temperature、approach temperature/MITA、pressure drop、utility cost、constraint violation 和 solver status。

## 明确不采纳的说法

- 不宣称 AI 可以可靠地从零生成 HYSYS 换热器或 LNG 冷箱模型。
- 不宣称 AI 可以直接闭环控制生产换热器，除非项目已有明确写回审批和运行证据。
- 不把外部 ML 预测、Excel-only 计算或 Aspen EDR 结果自动说成 HYSYS-native 结果。
