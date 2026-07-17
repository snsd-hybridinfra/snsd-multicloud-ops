from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools/telemetry"))

import correlate_events  # noqa: E402
import normalize_events  # noqa: E402


class TelemetryToolTests(unittest.TestCase):
    def test_malformed_event_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.jsonl"
            path.write_text('{"not_event": true}\n', encoding="utf-8")
            with self.assertRaises(ValueError):
                correlate_events.load_events(path)

    def test_duplicate_rule_id_is_rejected(self) -> None:
        source = json.loads((ROOT / "docs/zero-trust/correlation-rule-catalog.yaml").read_text(encoding="utf-8"))
        source["rules"].append(copy.deepcopy(source["rules"][0]))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "rules.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaises(ValueError):
                correlate_events.load_rules(path)

    def test_blocking_action_is_rejected(self) -> None:
        source = json.loads((ROOT / "docs/zero-trust/correlation-rule-catalog.yaml").read_text(encoding="utf-8"))
        source["rules"][0]["response_actions"] = ["BLOCK"]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "rules.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaises(ValueError):
                correlate_events.load_rules(path)

    def test_unsanitized_input_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "summary.txt"
            path.write_text("[PASS] endpoint 203.0.113.10 validated\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                normalize_events.normalize(path, "validator-summary", "test-validator", "<runtime>")


if __name__ == "__main__":
    unittest.main()
