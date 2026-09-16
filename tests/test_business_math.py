import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from business_math import monthly_economics, retention_by_period


class CohortTests(unittest.TestCase):
    def test_weighted_retention_is_not_unweighted_average(self):
        result = retention_by_period([
            {"cohort": "A", "period": 1, "eligible": 10, "retained": 8},
            {"cohort": "B", "period": 1, "eligible": 5, "retained": 1},
        ])
        self.assertEqual(result["periods"][0]["retention"], 0.6)

    def test_unobserved_and_empty_denominators_are_not_zero_retention(self):
        result = retention_by_period([
            {"cohort": "future", "period": 2, "eligible": 5, "retained": None},
            {"cohort": "empty", "period": 2, "eligible": 0, "retained": 0},
        ])
        self.assertTrue(all(row["retention"] is None for row in result["rows"]))
        self.assertIsNone(result["periods"][0]["retention"])

    def test_invalid_counts_and_duplicates_are_rejected(self):
        row = {"cohort": "A", "period": 1, "eligible": 10, "retained": 8}
        with self.assertRaises(ValueError):
            retention_by_period([row, row])
        for retained in [11, -1, True, 1.5]:
            with self.subTest(retained=retained), self.assertRaises(ValueError):
                retention_by_period([{**row, "retained": retained}])


class EconomicsTests(unittest.TestCase):
    def setUp(self):
        self.scenarios = json.loads((ROOT / "examples/business-scenarios.json").read_text())["scenarios"]

    def test_report_results_reproduce(self):
        for scenario, expected in zip(self.scenarios, [-1281, 1062.5, 5550]):
            self.assertEqual(monthly_economics(scenario)["operating_result_before_tax"], expected)

    def test_negative_contribution_has_no_volume_break_even(self):
        self.assertIsNone(monthly_economics(self.scenarios[0])["conditional_break_even_clients"])
        self.assertEqual(monthly_economics(self.scenarios[1])["conditional_break_even_clients"], 3)

    def test_price_and_labor_sensitivity(self):
        base = self.scenarios[1]
        self.assertEqual(monthly_economics({**base, "delivery_hours_per_client": 12})["operating_result_before_tax"], 562.5)
        self.assertEqual(monthly_economics({**base, "price": 600})["operating_result_before_tax"], 350)
        self.assertEqual(monthly_economics(base)["human_hours"], 80)

    def test_invalid_assumptions_are_rejected(self):
        for change in [{"new_clients": 99}, {"refund_rate": 1.2}, {"price": "NaN"},
                       {"clients": True}, {"price": -1}, {"technology_per_client": "Infinity"}]:
            with self.subTest(change=change), self.assertRaises(ValueError):
                monthly_economics({**self.scenarios[1], **change})


if __name__ == "__main__":
    unittest.main()
