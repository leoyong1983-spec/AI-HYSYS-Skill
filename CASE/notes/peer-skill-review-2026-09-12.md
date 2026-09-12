# gao-hysys Review / 同事技能择优吸收

## Source Identity

- Repository: [gaoruhai123-cmyk/gao-hysys](https://github.com/gaoruhai123-cmyk/gao-hysys).
- Reviewed commit: `f9ebc8553e740504837f9856f919bfdc8f7a0cc6`, published 2026-09-12.
- Read README, SKILL and all five reference documents; the tree contains documentation and agent metadata, not the described project-specific automation scripts or benchmark cases.
- Grade: **B-/C+**, direct HYSYS workflow candidate. Public retrospective descriptions cannot reproduce the author's runtime checks. The source itself distinguishes historical numerical checks from engineering validation.
- License/access: public readable repository; no LICENSE or reuse grant found in the inspected tree. No source code, document bodies, case files or screenshots are vendored. This note is original analysis and attribution; project improvements are independently implemented. Our MIT license is unchanged and does not relicense the source.

## Comparison and Decisions / 对比与取舍

| Topic | Existing project | Decision |
| --- | --- | --- |
| [Drawing evidence](https://github.com/gaoruhai123-cmyk/gao-hysys/blob/f9ebc8553e740504837f9856f919bfdc8f7a0cc6/references/drawing-modeling.md) | Case provenance present, but no deterministic page-inventory check | Add a small manifest checker and scoped drawing-to-model reference; no automatic PDF interpretation or model generation claim. |
| [COM readback](https://github.com/gaoruhai123-cmyk/gao-hysys/blob/f9ebc8553e740504837f9856f919bfdc8f7a0cc6/references/com-validation.md) | Strong convergence gate; layout comparison could accept unavailable values on both sides | Reject unavailable/invalid required fingerprint values. Retain existing loop, units and version safeguards rather than duplicating them. |
| [PFD integrity](https://github.com/gaoruhai123-cmyk/gao-hysys/blob/f9ebc8553e740504837f9856f919bfdc8f7a0cc6/references/pfd-layout.md) | Native layout runner paired labels by collection position and assumed generated COM metadata | Replace unsupported assumptions with runtime member lookup and verified association requirements; do not lower checks when an interface is unavailable. |
| [Report delivery](https://github.com/gaoruhai123-cmyk/gao-hysys/blob/f9ebc8553e740504837f9856f919bfdc8f7a0cc6/references/report-delivery.md) | Layered package outputs, limited Office visual-acceptance detail | Add a focused report-evidence guide: single snapshot, explicit KPI boundaries, application reopening and page review tracked separately. |
| [Historical case](https://github.com/gaoruhai123-cmyk/gao-hysys/blob/f9ebc8553e740504837f9856f919bfdc8f7a0cc6/references/case-evidence.md) | V14/V15 tests must be independently evidenced | Do not import case quantities, model settings, tolerance values or reported performance as local acceptance results. |

## Not Adopted / 不直接采纳

- A universal greenfield builder: the colleague's published package does not contain one. Controlled greenfield development remains a separate scope with a V14/V15 test matrix.
- Generic rotation constants, cached numeric DISPIDs, or label pairing based on equal collection counts: these require target-runtime proof, not similarity of API names.
- Automatic dummy-feed substitution or graphical "jitter" as routine repair: a case-specific workaround can alter meaning or hide the original failure. Keep such experiments isolated and reversible if separately approved.
- A universal ban on alternative Office renderers, a fixed report length, and exact historical layout targets: these are not portable requirements. Preserve the current user's format and tool choices.

The adopted documentation describes our acceptance policy, not a new runtime success claim. Unit tests validate the new deterministic checks. Any native probes performed for this change have a separately recorded narrow scope; no private project assets are published.

## Verification and Migration Limit / 验证与迁移限制

- Python 3.12: 40 unit tests passed; standalone manifest CLI accepted the complete synthetic inventory and rejected the unresolved one. Both outputs explicitly deny runtime/engineering acceptance. Syntax checks covered 12 script/test files; the repository PowerShell validator passed.
- Limited native V14/V15 probes resolved the `Items` member and read PFD collections after GUI initialization. One V14 reopening still returned an empty canvas. The sample labels did not expose a usable underlying-object identity; no complete native layout regression is claimed.
- The layout runner now fails before movement when label association is unproven, rather than guessing by collection order. This intentionally restricts previously permissive behavior, requires review and a separately verified adapter for affected views, and must not be silently deployed as a full V14/V15 layout upgrade.
- No Word report was generated or visually accepted by this change. Report guidance is a policy improvement, not completed document QA. No borrowed implementation, additional runtime dependency or private probe output is included.
