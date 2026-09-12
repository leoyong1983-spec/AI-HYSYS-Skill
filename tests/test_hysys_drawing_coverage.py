import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from hysys_drawing_coverage import validate_coverage


def example():
    return {"documents": [{"document_id": "synthetic-drawing", "source_sha256": "a" * 64,
                           "page_count": 2, "pages": [
        {"page": 1, "disposition": "modeled", "evidence_ref": "review/page-1",
         "scope_note": "Synthetic stream", "model_objects": ["Feed @Main"]},
        {"page": 2, "disposition": "excluded", "evidence_ref": "review/page-2",
         "scope_note": "Legend only"}]}]}


class CoverageTests(unittest.TestCase):
    def test_complete_inventory_does_not_claim_engineering_acceptance(self):
        result = validate_coverage(example())
        self.assertEqual(result["status"], "COVERAGE_COMPLETE")
        self.assertFalse(result["engineering_validated"])
        self.assertFalse(result["runtime_validated"])

    def test_missing_and_duplicate_pages_fail_even_if_count_matches(self):
        data = example()
        data["documents"][0]["pages"][1]["page"] = 1
        self.assertEqual(validate_coverage(data)["status"], "BLOCKED")

    def test_unresolved_page_blocks(self):
        data = example()
        data["documents"][0]["pages"][1]["disposition"] = "pending"
        self.assertEqual(validate_coverage(data)["status"], "BLOCKED")

    def test_page_requires_evidence_and_scope(self):
        for field in ("evidence_ref", "scope_note", "model_objects"):
            data = example()
            del data["documents"][0]["pages"][0][field]
            with self.subTest(field=field):
                self.assertEqual(validate_coverage(data)["status"], "BLOCKED")

    def test_bad_document_identity_rejected(self):
        for value in ("", "not-a-hash", None):
            data = example()
            data["documents"][0]["source_sha256"] = value
            self.assertEqual(validate_coverage(data)["status"], "BLOCKED")
        data = example()
        data["documents"].append(copy.deepcopy(data["documents"][0]))
        self.assertEqual(validate_coverage(data)["status"], "BLOCKED")

    def test_invalid_shapes_and_page_numbers_fail(self):
        for data in (None, [], {}, {"documents": [None]}):
            self.assertEqual(validate_coverage(data)["status"], "BLOCKED")

        for number in (True, 0, 3, "1", None):
            data = example()
            data["documents"][0]["pages"][0]["page"] = number
            self.assertEqual(validate_coverage(data)["status"], "BLOCKED")

    def test_large_declared_page_count_does_not_allocate_a_page_set(self):
        data = example()
        data["documents"][0]["page_count"] = 10**12
        self.assertEqual(validate_coverage(data)["status"], "BLOCKED")


if __name__ == "__main__":
    unittest.main()
