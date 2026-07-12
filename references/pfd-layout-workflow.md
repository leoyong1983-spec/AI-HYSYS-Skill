# HYSYS 原生 PFD 视觉整理工作流

## 适用范围

用于已有、可运行 HYSYS case 的原生 PFD 整理，使人类工程师能够沿工艺主线继续审查和修改。该工作流只允许修改 PFD 图标、标签和视图布局，不允许借机改变拓扑、设备参数、物性方法、物流边界或计算结果。

## 默认视觉组织

1. 先按正式 PFD、P&ID 或工程师确认的工艺顺序识别大型设备和主线。
2. 主流程从左到右；并联机组使用独立水平泳道。
3. 回流、循环气和高压侧线置于主线以上；液相回流和排液置于主线以下。
4. 能量流、Spreadsheet、检查表和辅助对象放在主工艺带以外。
5. 先保证设备层次和连接关系可读，再调整流股标签；不要为了画面对称改变工艺含义。
6. 长设备名和流股名上下错层。以标签真实宽度做碰撞检查，不按图标宽度猜测。

## 写入边界

- 始终从已验证基线复制新的 layout workcopy，不覆盖 frozen baseline。
- 暂停 solver 后批量修改 PFD，完成后恢复原 solver 状态。
- PFD 整理前后分别导出对象坐标和计算指纹。
- 保存后必须关闭并重开 workcopy，再比较对象数、关键物流、能量流、循环收敛和坐标。
- 只要计算指纹发生变化，就把本次布局整理判为失败并回退。

## Aspen HYSYS V15 COM 实测行为

以下行为已在真实 Aspen HYSYS V15 case 上验证：

1. `Flowsheet.PFDs.ActivePFD` 可访问当前 PFD；`PFDItem` 暴露 `XPosition`、`YPosition`、`Width`、`Height`、`Hidden`、`Rotation`、`Mirror` 和 `AutoPosition()`。
2. 独立自动化会话中 `PFDs.Count`、`ActivePFD` 和按名称 `Item(...)` 的可用时序可能不同。PFD 选择器应依次尝试按名称绑定、集合枚举和活动对象回退，不能只依赖集合计数。
3. 原生 PFD 具有 GUI 生命周期依赖。若 headless COM 无法绑定 PFD，或绑定后 `PFDOperation` 数量为 0，应依次尝试 `case.Visible=True`、再尝试显示 application；验证报告必须记录是否使用了 GUI 初始化。
4. pywin32 生成包装层中的 `pfd.Items(...)` 可能返回 `None`。应通过 `Items` 属性的 DISPID 调用 `InvokeTypes`，或使用已验证的兼容 helper。
5. 不要依次给所有设备和流股直接写绝对坐标。后移动的流股端点、能量流或标签可能反向牵引已经定位的设备。
6. 设备绝对定位优先使用 `pfd.MoveBy((item,), dx, dy)`。直接写 `XPosition`/`YPosition` 在混合器、冷却器、阀门或喷嘴受约束对象上可能被忽略或吸附。
7. 推荐稳定顺序：设备正向定位 -> 流股 `AutoPosition()` -> 设备再次定位 -> 标签错层 -> 设备反向定位 -> 短连接对按 `final_priority` 收口。
8. `AutoPosition()` 适合流股，但能量流和单端流股可能轻微带动连接设备，所以设备必须在其后再次定位。
9. 移动标签也可能触发设备网格吸附。标签处理后必须再次回读设备坐标。
10. 单独隐藏某个 operation label 在部分 V15 视图中可能表现为共享可见性变化。未验证前保持所有标签可见，用错层和增大设备间距解决遮挡。
11. `PFD.Centre()` 不是 GUI 的“适合窗口”，不要把它当成 `ZoomToFit`。GUI 中 `Home` 对应 Fit to Window，但跨桌面会话的模拟按键并不可靠。
12. `PFD.Extent` 在无 GUI 的独立自动化实例中可能为 `None`；这不是 case 或 PFD 损坏，验证脚本必须允许空值。

## 配置文件

使用 `scripts/hysys_pfd_layout.py` 时提供 JSON：

```json
{
  "pfd": "PFD 1",
  "targets": {
    "TK-100": [0, 0],
    "K-101A": [900, -300],
    "K-101B": [900, 220],
    "E-101": [1800, -40]
  },
  "label_below": ["K-101B"],
  "label_x_shift": {},
  "label_y_shift": {},
  "final_priority": ["E-101", "MIX-101"],
  "label_height": 18
}
```

`targets` 必须覆盖该 PFD 的全部非流股对象，并且不能包含物料流或能量流。坐标来自项目 PFD 的人工分区，不应由脚本自行推断工艺含义。

## 执行示例

```powershell
py .\scripts\hysys_pfd_layout.py `
  --case .\model\baseline.hsc `
  --output-case .\model\baseline_visual_workcopy.hsc `
  --layout .\model\pfd_layout.json `
  --report .\model\pfd_layout_validation.json
```

脚本默认拒绝覆盖源 case 和已有输出文件。确认需要重建工作副本时增加 `--overwrite`。

## 最低验收条件

- workcopy 可独立重开。
- solver 状态正常，且整理前后对象清单一致。
- 所有 `targets` 坐标回读误差在容差内。
- 物料流量、能量流和 recycle 状态与整理前一致。
- 可见标签碰撞为零；如人工确认某些重叠可接受，必须显式使用允许参数并在报告中保留清单。
- 人工打开 case 后按 `Home` 执行 Fit to Window，完成最终视觉签认。
