# Drawing-to-Model Basis / 图纸与模型对应依据

Use this reference when drawings are used to explain, audit, extend, or plan a HYSYS model. It is a preparation and acceptance workflow, not a general drawing-to-HSC builder. A new topology still needs explicit scope and a version-tested adapter.

## Coverage / 不漏页，不夸大范围

给每份受控图纸记录文件哈希、实际页数和版次。对每页保留可追溯的审阅定位，并选择处理方式：参与计算、等效处理、模型边界、排除或待确认。图例、仪控及辅助系统也要登记；“页码已覆盖”不等于“所有设备已模拟”。跨页关系须由接续标识与端口证据核实，不凭线条外观补全。

Keep the source fact, a proposed assumption, and a model result separate. Critical ambiguities block the affected calculation claim; do not change source values merely to obtain a solvable model. Tie each modeled object to the reviewed page and each accepted result to its case hash and runtime version.

Use `scripts/hysys_drawing_coverage.py` to reject missing/duplicate pages, unresolved dispositions, and incomplete mapping records. The script checks **manifest completeness only**: it cannot prove that a page was read, a hash is genuine, a COM binding exists, or the model converged. The agent must verify those independently.

The following is a synthetic schema example; replace its illustrative digest and evidence reference with actual reviewed evidence:

```json
{
  "documents": [{
    "document_id": "source-01",
    "source_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "page_count": 1,
    "pages": [{
      "page": 1,
      "disposition": "modeled",
      "evidence_ref": "review/page-001.md",
      "model_objects": ["Feed @Main"],
      "scope_note": "Synthetic example of a reviewed material boundary."
    }]
  }]
}
```

Allowed dispositions: `modeled`, `equivalent`, `interface`, `excluded`, `pending`. Every page needs `evidence_ref` and `scope_note`; the first three also require nonempty `model_objects`. `pending` blocks completion. Record missing data and exclusions honestly rather than selecting another label to pass.

```powershell
py -3.12 scripts/hysys_drawing_coverage.py --manifest ./drawing-coverage.json --output ./coverage-check.json
```

Keep real manifests in the project's controlled working area, not the public skill repository. Exit code 0 and `COVERAGE_COMPLETE` refer only to this structural check. The output explicitly leaves runtime and engineering validation false.

## Model Binding / 真正连上再说建成

- Record the intended device, flowsheet, material/energy port and direction; compare with an independent native readback. A diagram junction is not a simulator connection certificate.
- Bind composition arrays to the component names and order of that stream's actual fluid package. A main-flowsheet component list must not be presumed valid for every subflowsheet.
- Separate material recirculation from energy exchange between independent material networks. Explanatory graphics must not add a material path solely to make the drawing appear connected.
- Record what each approximation omits and which claims it can support. A simplified energy exchange or equilibrium model is not equipment-performance acceptance.

V14 与 V15 分别验证对象绑定和求解行为。有限调参、原生排版和报告任务仍遵守各自写入边界；这份清单不授权重建既有模型，也不放宽[循环收敛验收](convergence-control-loop.md)。
