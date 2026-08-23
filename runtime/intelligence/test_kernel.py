import json
import tempfile
import unittest
from pathlib import Path

from kernel import ValidationError, aggregate_paired_results, append_record, example_coverage, load_json, paired_decision, validate_record


ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "runtime" / "intelligence"


class IntelligenceKernelTests(unittest.TestCase):
    def test_all_fixture_records_validate_against_their_schema(self):
        schema_by_type = {
            "research_memory": "research-memory.schema.json",
            "lesson_memory": "lesson-memory.schema.json",
            "example_record": "example-record.schema.json",
            "intent_prediction": "intent-prediction.schema.json",
            "communication_trial": "communication-trial.schema.json",
            "evaluation_record": "evaluation-record.schema.json",
            "improvement_record": "improvement-record.schema.json",
            "benchmark_run": "benchmark-run.schema.json",
            "behavior_observation": "behavior-observation.schema.json",
        }
        records = [json.loads(line) for line in (ROOT / "examples" / "intelligence" / "records.jsonl").read_text().splitlines()]
        self.assertGreaterEqual(len(records), 9)
        for record in records:
            validate_record(record, load_json(SCHEMA_DIR / schema_by_type[record["record_type"]]))

    def test_validation_rejects_unsafe_or_incomplete_records(self):
        schema = load_json(SCHEMA_DIR / "intent-prediction.schema.json")
        record = {"schema_version": "1.0", "record_type": "intent_prediction"}
        with self.assertRaises(ValidationError):
            validate_record(record, schema)

    def test_example_coverage_requires_counterexamples_and_exceptions(self):
        kinds = [{"kind": kind} for kind in ["positive", "negative", "borderline", "exception", "transformation"]]
        result = example_coverage(kinds)
        self.assertTrue(result["complete"])
        self.assertEqual(result["missing"], [])
        self.assertFalse(example_coverage(kinds[:2])["complete"])

    def test_memory_append_is_append_only(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "memory.jsonl"
            append_record(path, {"record_id": "one", "value": 1})
            append_record(path, {"record_id": "two", "value": 2})
            records = [json.loads(line) for line in path.read_text().splitlines()]
            self.assertEqual([item["record_id"] for item in records], ["one", "two"])

    def test_paired_decision_rejects_gate_failure(self):
        result = paired_decision({"quality": 0.5}, {"quality": 0.9}, {"safety": False})
        self.assertEqual(result["decision"], "reject")
        self.assertEqual(result["reason"], "hard_gate_failure")

    def test_paired_decision_rejects_regression(self):
        result = paired_decision({"quality": 0.8, "cost": 1.0}, {"quality": 0.9, "cost": 1.2}, {"safety": True}, lower_is_better=["cost"])
        self.assertEqual(result["decision"], "reject")
        self.assertIn("cost", result["regressions"])

    def test_paired_decision_promotes_only_measured_improvement(self):
        result = paired_decision({"quality": 0.5, "cost": 1.0}, {"quality": 0.6, "cost": 1.0}, {"safety": True, "privacy": True})
        self.assertEqual(result["decision"], "promote")
        self.assertIn("quality", result["improvements"])

    def test_paired_decision_holds_when_metrics_do_not_change(self):
        result = paired_decision({"quality": 0.5}, {"quality": 0.5}, {"safety": True})
        self.assertEqual(result["decision"], "hold")
        self.assertEqual(result["reason"], "no_measurable_improvement")


    def test_aggregate_paired_results_preserves_regressions_and_residual_failures(self):
        result = aggregate_paired_results([
            {"case_id": "gain", "baseline_success": False, "candidate_success": True, "hard_gates": {"safety": True}},
            {"case_id": "regression", "baseline_success": True, "candidate_success": False, "hard_gates": {"safety": True}},
            {"case_id": "residual", "baseline_success": False, "candidate_success": False, "hard_gates": {"safety": False}},
            {"case_id": "same", "baseline_success": True, "candidate_success": True, "hard_gates": {"safety": True}},
        ])
        self.assertEqual(result["gains"], ["gain"])
        self.assertEqual(result["regressions"], ["regression"])
        self.assertEqual(result["residual_failures"], ["residual"])
        self.assertEqual(result["hard_gate_failures"], {"safety": ["residual"]})
        self.assertEqual(result["net_success_delta"], 0.0)

    def test_aggregate_paired_results_rejects_duplicate_or_incomplete_cases(self):
        with self.assertRaises(ValidationError):
            aggregate_paired_results([{"case_id": "one", "baseline_success": True, "candidate_success": True}, {"case_id": "one", "baseline_success": True, "candidate_success": True}])
        with self.assertRaises(ValidationError):
            aggregate_paired_results([{"case_id": "one", "baseline_success": True}])


if __name__ == "__main__":
    unittest.main()
