# HYSYS V14 / V15 Compatibility / 双版本兼容

## Version Contract / 版本约定

The supported control targets are Aspen HYSYS V14 and V15 on Windows with working product licenses and pywin32. Explicit selection is preferred for reproducible work. This is a control-layer contract, not a guarantee for all case files, plugins, unit operations, or operating systems.

支持目标为 Windows 上具备有效许可和 pywin32 的 HYSYS V14、V15。项目计算优先明确选版；“双版本控制兼容”不等于所有案例文件、插件、单元操作和操作系统均已验证。

| Selection | Resolved COM target | Rule |
| --- | --- | --- |
| `14` | `HYSYS.Application.V14.0` | Fail if V14 is not registered; never switch to V15. |
| `15` | `HYSYS.Application.V15.0` | Fail if V15 is not registered; never switch to V14. |
| `auto` | One of the above | Match the generic registration's CLSID to a supported target, or use the only installed supported target. Reject ambiguity. |

The wrapper checks `Application.Version` before touching a case. Preserve the full returned string, including the build: product V14 may report `Aspen HYSYS Version 14 (40.0)` and V15 may report `Aspen HYSYS Version 15 (41.0)`. The internal build number is not the product major. A mismatch or unrecognized version is an error, not an invitation to retry another version.

启动前查询指定版本的注册信息；启动后核对实际版本。默认 COM 入口可能随安装或修复改变，不能据此猜测当前是 V15。备用启动必须使用同一版本的注册程序和活动对象入口，不修改系统注册、不自动关闭借用的人类会话。

## Usage / 使用方法

```python
from hysys_automation import HysysCaseSession, HysysLaunchOptions

with HysysCaseSession(HysysLaunchOptions(hysys_version="14")) as session:
    print(session.target.prog_id, session.version)
    # Open only the approved version-specific workcopy here.
```

Use `hysys_version="15"` for V15. Existing `prog_id` and `registered_prog_id` arguments remain accepted for the supported targets; conflicting selectors fail before activation.

The following scripts accept `--hysys-version auto|14|15`:

- `scripts/hysys_readiness_check.py`: registry, activation, optional minimal create/save/reopen. Its legacy `--prog-id` also controls the actual launch, not just the registry check.
- `scripts/hysys_h2_density_table.py`: native hydrogen property-table smoke calculation.
- `scripts/hysys_pfd_layout.py`: selects the runtime; PFD capability and fingerprints still require case-specific verification.

```powershell
py -3.12 scripts/hysys_readiness_check.py --hysys-version 14 --create-smoke-case --output ./readiness-v14.json
py -3.12 scripts/hysys_h2_density_table.py --hysys-version 14 --start-mpa 1 --end-mpa 2 --step-mpa 1 --output-dir ./density-v14
```

Repeat with `15` and separate output paths. Never launch a dual-version comparison against the same writable case or assume independent processes/licenses simply because the ProgIDs differ.

## Acceptance Boundaries / 验收边界

1. Create separate V14 and V15 workcopies from an approved compatible source; retain each source hash and actual product/build string. Do not overwrite the V14 baseline after saving in V15. Downsave or round-trip compatibility requires separate evidence.
2. Reuse the same approved inputs, units, property method, required object map, and tolerances where supported. Check required COM members in the selected runtime, not from another version's remembered API.
3. Apply the [iterative convergence contract](convergence-control-loop.md) independently in each version: consecutive passing readbacks and save-close-reopen verification. Idle, readable results, or matching filenames are not acceptance.
4. Compare physical readbacks within approved tolerances, not binary equality of `.hsc` files. A version difference is a finding to review, never something to hide by copying results.
5. Treat Aspen EDR, Simulation Workbook/Excel, dynamics, PFD layout, special unit operations, and custom extensions as separate capability checks. A minimal material-stream smoke does not prove these capabilities.
6. Any future controlled greenfield mode must carry a V14/V15 test matrix. A stronger language model does not remove unit, topology, convergence, persistence, or human-review gates.

中文要点：两版独立工作副本、独立回读验收；禁止跨版本默默替换软件、猜测接口或复用另一版“已通过”的结论。尚未实测的复杂流程、插件及从零建模应明确标记待验证。

## Evidence / 验证记录

The automated unit tests cover version selection, ambiguous or missing installations, conflicting overrides, actual-version mismatch, same-version fallback, and preservation of an already-running borrowed application. These mock tests do not require HYSYS and are not native runtime evidence.

Local native checks on 2026-09-12 used Windows and Python 3.12.10 with pywin32, separate cases, and explicit version selection:

| Check | V14: `14 (40.0)` | V15: `15 (41.0)` |
| --- | --- | --- |
| Selected COM activation and actual-version readback | PASS | PASS |
| New minimal case, save, close, reopen | PASS | PASS |
| New Peng-Robinson basis, pure H2 stream, explicit-unit writes | PASS | PASS |
| Native density table at 20 C, 1 and 2 MPa(a) | PASS | PASS |
| Saved density case reopened; two consistent P/T/density/phase readbacks | PASS | PASS |
| Read-only reopen preserved the case SHA-256 | PASS | PASS |
| Complex flowsheet/recycle acceptance under this change | NOT TESTED | NOT TESTED |
| PFD layout, EDR, Workbook, dynamics under this change | NOT TESTED | NOT TESTED |

The reopened final point was checked against the corresponding saved table with relative and absolute tolerance `1e-8`. This tolerance is for this persistence smoke only, not a general engineering acceptance standard. Evidence files remain local; no private paths, licensed case files, or host logs are published.

中文：本轮已在两版真实软件上完成上述基础计算及保存重开验证，不是仅靠模拟测试。完整工艺流程、循环收敛、EDR 等扩展尚未在本轮逐版测试，仍须按项目单独验收。不能据此宣称全部从零建模能力已经完成。

For OS/Office/product prerequisites, consult the official [AspenTech platform support matrix](https://www.aspentech.com/en/platform-support). Platform documentation supports environment selection, not this repository's runtime acceptance claims.
