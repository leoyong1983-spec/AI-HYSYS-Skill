import importlib.util
import sys
import types
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


class PfdChecksTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        client = types.ModuleType("win32com.client")
        client.Dispatch = Mock(side_effect=lambda value: value)
        package = types.ModuleType("win32com")
        package.client = client
        automation = types.ModuleType("hysys_automation")
        automation.HysysCaseSession = Mock()
        automation.HysysLaunchOptions = Mock()
        spec = importlib.util.spec_from_file_location(
            "isolated_pfd_checks", Path(__file__).resolve().parents[1] / "scripts/hysys_pfd_layout.py"
        )
        cls.mod = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {"pythoncom": Mock(), "win32com": package,
                                     "win32com.client": client, "hysys_automation": automation}):
            spec.loader.exec_module(cls.mod)

    def fingerprint(self, mass=10.0, heat=2.0, recycle=0):
        return {"material_stream_count": 1, "energy_stream_count": 1, "operation_count": 1,
                "operations": [{"name": "REC", "type": "recycle"}],
                "recycle_convergence": {"REC": recycle},
                "material_mass_flow_kg_h": {"feed": mass}, "energy_heat_flow_kw": {"Q": heat}}

    def test_finite_equal_fingerprints_pass(self):
        result = self.mod.compare_fingerprints(self.fingerprint(), self.fingerprint(), 0.01, 0.01)
        self.assertTrue(self.mod.comparison_passed(result))

    def test_unknown_on_both_sides_is_not_a_pass(self):
        for value in (None, float("nan"), float("inf"), -32767.0, True):
            for key in ("mass", "heat", "recycle"):
                with self.subTest(value=value, key=key):
                    before = self.fingerprint(**{key: value})
                    after = self.fingerprint(**{key: value})
                    result = self.mod.compare_fingerprints(before, after, 0.01, 0.01)
                    self.assertFalse(self.mod.comparison_passed(result))

    def test_missing_or_changed_flow_fails(self):
        before = self.fingerprint()
        after = self.fingerprint(mass=100.0)
        result = self.mod.compare_fingerprints(before, after, 0.01, 0.01)
        self.assertFalse(self.mod.comparison_passed(result))
        after["material_mass_flow_kg_h"] = {}
        result = self.mod.compare_fingerprints(before, after, 0.01, 0.01)
        self.assertFalse(self.mod.comparison_passed(result))

    def test_invalid_tolerance_rejected(self):
        for tolerance in (-1, float("nan"), float("inf"), True):
            with self.assertRaises(ValueError):
                self.mod.compare_scalar_maps({"a": 1}, {"a": 1}, tolerance)

    def test_items_member_is_resolved_from_runtime(self):
        pfd = Mock()
        pfd._oleobj_.GetIDsOfNames.return_value = 123
        self.mod.pfd_items(pfd, -2)
        pfd._oleobj_.GetIDsOfNames.assert_called_once_with("Items")
        self.assertEqual(pfd._oleobj_.InvokeTypes.call_args.args[0], 123)

    def test_duplicate_item_name_is_rejected(self):
        items = Mock(Count=2)
        items.Item.side_effect = [types.SimpleNamespace(name="same"), types.SimpleNamespace(name="same")]
        with self.assertRaises(ValueError):
            self.mod.item_map(items)

    def collection(self, items):
        return types.SimpleNamespace(Count=len(items), Item=lambda index: items[index])

    def test_shuffled_labels_bind_by_full_object_identity(self):
        a = types.SimpleNamespace(name="A", Object=types.SimpleNamespace(TaggedName="A @Main"))
        b = types.SimpleNamespace(name="B", Object=types.SimpleNamespace(TaggedName="B @Main"))
        la = types.SimpleNamespace(Object=a.Object)
        lb = types.SimpleNamespace(Object=b.Object)
        result = self.mod.label_map_by_object(self.collection([a, b]), self.collection([lb, la]))
        self.assertIs(result["A"], la)
        self.assertIs(result["B"], lb)

    def test_missing_native_label_owner_blocks_instead_of_guessing(self):
        item = types.SimpleNamespace(name="A", Object=types.SimpleNamespace(TaggedName="A @Main"))
        with self.assertRaises(RuntimeError):
            self.mod.label_map_by_object(self.collection([item]), self.collection([object()]))

    def test_duplicate_and_incomplete_label_associations_block(self):
        item = types.SimpleNamespace(name="A", Object=types.SimpleNamespace(TaggedName="A @Main"))
        label = types.SimpleNamespace(Object=item.Object)
        for labels in ([], [label, label]):
            with self.assertRaises(ValueError):
                self.mod.label_map_by_object(self.collection([item]), self.collection(labels))

    def test_missing_and_nontext_identities_are_not_stringified(self):
        for identity in (None, "", " ", 12, []):
            item = types.SimpleNamespace(name="A", Object=types.SimpleNamespace(TaggedName=identity))
            label = types.SimpleNamespace(Object=item.Object)
            with self.subTest(identity=identity), self.assertRaises(ValueError):
                self.mod.label_map_by_object(self.collection([item]), self.collection([label]))


if __name__ == "__main__":
    unittest.main()
