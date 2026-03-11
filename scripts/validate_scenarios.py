#!/usr/bin/env python3
"""Lightweight validator for scenario JSON files.

- Loads all docs/scenarios/*.json except templates.
- Validates schema-required fields and enum constraints.
- Applies extra quality checks for coaching usefulness.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIO_DIR = ROOT / "docs" / "scenarios"

REQUIRED_TOP_LEVEL = {
    "id",
    "title",
    "dealType",
    "sector",
    "dealSizeBand",
    "userRole",
    "counterpartyStyle",
    "riskProfile",
    "timelinePressure",
    "mandate",
    "targetModules",
    "dynamicEvents",
    "scoringAnchors",
}

ENUMS = {
    "dealType": {"private_swedish_share_acquisition"},
    "dealSizeBand": {"small_cap", "mid_cap", "large_cap"},
    "userRole": {"buyer_counsel", "seller_counsel"},
    "counterpartyStyle": {"cooperative", "aggressive", "inconsistent"},
    "riskProfile": {"clean", "moderate_flags", "red_flag_heavy"},
    "timelinePressure": {"normal", "compressed"},
}

MODULE_ENUM = {
    "definitions",
    "purchase_price_mechanism",
    "warranties_indemnities",
    "limitations_of_liability",
    "covenants",
    "conditions_precedent",
    "termination_remedies",
    "dispute_mechanics",
}


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        return [f"{path}: invalid JSON ({exc})"]

    missing = sorted(REQUIRED_TOP_LEVEL - set(data.keys()))
    if missing:
        errors.append(f"{path}: missing keys: {', '.join(missing)}")

    for key, allowed in ENUMS.items():
        if key in data and data[key] not in allowed:
            errors.append(f"{path}: {key}={data[key]!r} not in {sorted(allowed)}")

    mandate = data.get("mandate", {})
    if not mandate.get("clientObjectives"):
        errors.append(f"{path}: mandate.clientObjectives must contain at least 1 item")
    if not mandate.get("redLines"):
        errors.append(f"{path}: mandate.redLines must contain at least 1 item")

    modules = data.get("targetModules", [])
    if not modules:
        errors.append(f"{path}: targetModules must contain at least 1 item")
    invalid_modules = [m for m in modules if m not in MODULE_ENUM]
    if invalid_modules:
        errors.append(f"{path}: invalid targetModules {invalid_modules}")

    dynamic_events = data.get("dynamicEvents", [])
    if len(dynamic_events) < 1:
        errors.append(f"{path}: dynamicEvents should contain at least 1 event")

    anchors = data.get("scoringAnchors", {})
    strong = anchors.get("strongSignals", [])
    common = anchors.get("commonErrors", [])
    if len(strong) < 2:
        errors.append(f"{path}: scoringAnchors.strongSignals should have at least 2 items")
    if len(common) < 2:
        errors.append(f"{path}: scoringAnchors.commonErrors should have at least 2 items")

    return errors


def main() -> int:
    files = sorted(
        p for p in SCENARIO_DIR.glob("*.json") if "template" not in p.name.lower()
    )
    if not files:
        print("No scenario files found.")
        return 1

    all_errors: list[str] = []
    for file_path in files:
        all_errors.extend(validate_file(file_path))

    if all_errors:
        print("Scenario validation failed:\n")
        for err in all_errors:
            print(f"- {err}")
        return 1

    print(f"Validated {len(files)} scenario file(s) successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
