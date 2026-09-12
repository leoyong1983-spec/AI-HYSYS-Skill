"""Check a human-reviewed drawing coverage manifest, without controlling HYSYS."""
from __future__ import annotations

import argparse
import json
import re
from itertools import islice
from pathlib import Path


DISPOSITIONS = {"modeled", "equivalent", "interface", "excluded", "pending"}


def nonempty(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_coverage(data) -> dict:
    errors = []
    total_pages = 0
    documents = data.get("documents") if isinstance(data, dict) else None
    if not isinstance(documents, list) or not documents:
        return {"status": "BLOCKED", "errors": ["documents must be a nonempty list"],
                "engineering_validated": False, "runtime_validated": False}
    seen_ids = set()
    for index, document in enumerate(documents):
        prefix = f"documents[{index}]"
        if not isinstance(document, dict):
            errors.append(f"{prefix}: expected an object")
            continue
        document_id = document.get("document_id")
        if not nonempty(document_id) or document_id in seen_ids:
            errors.append(f"{prefix}: missing or duplicate document_id")
        if nonempty(document_id):
            seen_ids.add(document_id)
        digest = document.get("source_sha256")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
            errors.append(f"{prefix}: source_sha256 must contain 64 hex characters")
        count = document.get("page_count")
        if type(count) is not int or count < 1:
            errors.append(f"{prefix}: page_count must be a positive integer")
            continue
        total_pages += count
        pages = document.get("pages")
        if not isinstance(pages, list):
            errors.append(f"{prefix}: pages must be a list")
            continue
        seen_pages = set()
        for record in pages:
            if not isinstance(record, dict):
                errors.append(f"{prefix}: page record must be an object")
                continue
            number = record.get("page")
            location = f"{prefix}.page[{number!r}]"
            if type(number) is not int or not 1 <= number <= count:
                errors.append(f"{location}: page outside declared range")
                continue
            if number in seen_pages:
                errors.append(f"{location}: duplicate page")
            seen_pages.add(number)
            disposition = record.get("disposition")
            if not isinstance(disposition, str) or disposition not in DISPOSITIONS:
                errors.append(f"{location}: unknown disposition")
            if disposition == "pending":
                errors.append(f"{location}: unresolved page cannot pass coverage")
            for key in ("evidence_ref", "scope_note"):
                if not nonempty(record.get(key)):
                    errors.append(f"{location}: missing {key}")
            if disposition in ("modeled", "equivalent", "interface"):
                objects = record.get("model_objects")
                if not isinstance(objects, list) or not objects or not all(nonempty(x) for x in objects):
                    errors.append(f"{location}: disposition requires model_objects")
        missing_count = count - len(seen_pages)
        if missing_count:
            preview = list(islice((n for n in range(1, count + 1) if n not in seen_pages), 20))
            errors.append(f"{prefix}: {missing_count} missing pages; first missing: {preview}")
    return {
        "status": "COVERAGE_COMPLETE" if not errors else "BLOCKED",
        "errors": errors,
        "document_count": len(documents),
        "declared_page_count": total_pages,
        "runtime_validated": False,
        "engineering_validated": False,
        "scope": "Manifest completeness only; does not read drawings, verify hashes, or inspect HYSYS.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = validate_coverage(json.loads(args.manifest.read_text(encoding="utf-8-sig")))
    except (OSError, ValueError) as exc:
        result = {"status": "BLOCKED", "errors": [str(exc)],
                  "runtime_validated": False, "engineering_validated": False}
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if result["status"] == "COVERAGE_COMPLETE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
