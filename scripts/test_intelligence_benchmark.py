import json
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_intelligence_benchmark import compare_metrics, validate_suite


ROOT = Path(__file__).resolve().parents[1]


class IntelligenceBenchmarkTests(unittest.TestCase):
    def test_real_suite_manifest_validates_and_has_held_out_cases(self):
        summary = validate_suite(ROOT / "evals" / "intelligence-benchmark.json", ROOT / "evals" / "cases.jsonl")
        self.assertEqual(summary["status"], "manifest_validated")
        self.assertGreater(summary["families"]["held_out"], 0)

    def test_comparison_requires_measured_same_arm_controls(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory) / "baseline.json"
            candidate = Path(directory) / "candidate.json"
            payload = {"measurement_status": "measured", "model_ref": "m1", "budget_ref": "b1", "metrics": {"quality": 0.5}}
            base.write_text(json.dumps(payload))
            candidate.write_text(json.dumps({**payload, "model_ref": "m2", "metrics": {"quality": 0.7}}))
            with self.assertRaises(ValueError):
                compare_metrics(base, candidate, {"safety": True}, [])

    def test_comparison_refuses_unmeasured_fixtures(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory) / "baseline.json"
            candidate = Path(directory) / "candidate.json"
            payload = {"measurement_status": "fixture", "model_ref": "m1", "budget_ref": "b1", "metrics": {"quality": 0.5}}
            base.write_text(json.dumps(payload))
            candidate.write_text(json.dumps({**payload, "metrics": {"quality": 0.7}}))
            with self.assertRaises(ValueError):
                compare_metrics(base, candidate, {"safety": True}, [])

    def test_comparison_rejects_quality_gain_with_gate_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory) / "baseline.json"
            candidate = Path(directory) / "candidate.json"
            common = {"measurement_status": "measured", "model_ref": "m1", "budget_ref": "b1"}
            base.write_text(json.dumps({**common, "metrics": {"quality": 0.5}}))
            candidate.write_text(json.dumps({**common, "metrics": {"quality": 0.7}}))
            result = compare_metrics(base, candidate, {"safety": False}, [])
            self.assertEqual(result["decision"], "reject")


if __name__ == "__main__":
    unittest.main()
