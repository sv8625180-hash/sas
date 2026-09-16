"""Reproduce synthetic retention and monthly economics; never forecast earnings."""

from collections import defaultdict
from decimal import Decimal, ROUND_CEILING
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def retention_by_period(rows):
    seen = set()
    output = []
    totals = defaultdict(lambda: {"eligible_observed": 0, "retained": 0})
    for row in rows:
        cohort, period, eligible, retained = (row[key] for key in ["cohort", "period", "eligible", "retained"])
        if not isinstance(cohort, str) or not cohort.strip() or type(period) is not int or period < 0:
            raise ValueError("Define a cohort and nonnegative integer period")
        if (cohort, period) in seen:
            raise ValueError("Duplicate cohort and period")
        seen.add((cohort, period))
        if type(eligible) is not int or eligible < 0:
            raise ValueError("Eligible users must be a nonnegative integer")
        if retained is not None and (type(retained) is not int or not 0 <= retained <= eligible):
            raise ValueError("Retained users must be between zero and eligible users")
        total = totals[period]
        observed = retained is not None and eligible > 0
        if observed:
            total["eligible_observed"] += eligible
            total["retained"] += retained
        output.append({**row, "retention": retained / eligible if observed else None})
    periods = []
    for period, total in sorted(totals.items()):
        denominator = total["eligible_observed"]
        periods.append({"period": period, **total,
                        "retention": total["retained"] / denominator if denominator else None})
    return {"rows": output, "periods": periods}


def monthly_economics(scenario):
    integer_fields = ["clients", "new_clients"]
    for key in integer_fields:
        if type(scenario[key]) is not int or scenario[key] < 0:
            raise ValueError(f"{key} must be a nonnegative integer")
    if scenario["clients"] == 0 or scenario["new_clients"] > scenario["clients"]:
        raise ValueError("Use active clients and no more new clients than active clients")
    keys = ["price", "refund_rate", "payment_fee_rate", "technology_per_client", "delivery_hours_per_client",
            "hourly_labor_cost", "onboarding_hours_per_new_client", "sales_hours", "admin_hours", "fixed_costs"]
    numbers = {}
    for key in keys:
        value = scenario[key]
        if isinstance(value, bool):
            raise ValueError(f"Invalid amount: {key}")
        amount = Decimal(str(value))
        if not amount.is_finite() or amount < 0:
            raise ValueError(f"Use a finite nonnegative amount: {key}")
        numbers[key] = amount
    n = scenario["clients"]
    new = scenario["new_clients"]
    d = numbers
    if d["refund_rate"] + d["payment_fee_rate"] > 1:
        raise ValueError("Refund and payment fee rates cannot exceed gross revenue")
    revenue = n * d["price"]
    refunds = revenue * d["refund_rate"]
    fees = revenue * d["payment_fee_rate"]
    technology = n * d["technology_per_client"]
    delivery = n * d["delivery_hours_per_client"] * d["hourly_labor_cost"]
    contribution = revenue - refunds - fees - technology - delivery
    onboarding = new * d["onboarding_hours_per_new_client"] * d["hourly_labor_cost"]
    sales = d["sales_hours"] * d["hourly_labor_cost"]
    admin = d["admin_hours"] * d["hourly_labor_cost"]
    overhead = onboarding + sales + admin + d["fixed_costs"]
    operating = contribution - overhead
    hours = n * d["delivery_hours_per_client"] + new * d["onboarding_hours_per_new_client"] + d["sales_hours"] + d["admin_hours"]
    unit = contribution / n
    result = {
        "gross_revenue": revenue, "refunds": refunds, "payment_fees": fees,
        "technology": technology, "delivery_labor": delivery,
        "contribution_after_delivery": contribution, "onboarding_labor": onboarding,
        "sales_labor": sales, "admin_labor": admin, "fixed_costs": d["fixed_costs"],
        "operating_result_before_tax": operating, "human_hours": hours,
        "cash_before_founder_pay": operating + delivery + onboarding + sales + admin,
    }
    return {
        "scenario": scenario["name"], **{key: float(value) for key, value in result.items()},
        "conditional_break_even_clients": int((overhead / unit).to_integral_value(rounding=ROUND_CEILING)) if unit > 0 else None,
    }


def demo():
    data = json.loads((ROOT / "examples/business-scenarios.json").read_text())
    rows = json.loads((ROOT / "examples/cohorts.json").read_text())
    return {"scope": data["scope"], "currency": data["currency"],
            "economics": [monthly_economics(scenario) for scenario in data["scenarios"]],
            "cohorts": retention_by_period(rows)}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2))
