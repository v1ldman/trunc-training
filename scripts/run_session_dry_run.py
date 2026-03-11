#!/usr/bin/env python3
"""Run a lightweight terminal dry-run for a training scenario.

This is not the full AI product. It gives facilitators a structured way to run
scenario exercises today using existing JSON scenario files.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCENARIOS = ROOT / "docs" / "scenarios"


def load_scenario(path: Path) -> dict:
    return json.loads(path.read_text())


def print_list(items: list[str], indent: str = "  - ") -> None:
    for item in items:
        print(f"{indent}{item}")


def run_dry_run(scenario: dict, mode: str) -> None:
    print("=" * 72)
    print(f"Scenario: {scenario['id']} — {scenario['title']}")
    print("=" * 72)
    print(f"Mode: {mode}")
    print(f"Role: {scenario['userRole']} | Counterparty: {scenario['counterpartyStyle']}")
    print(
        f"Sector: {scenario['sector']} | Size: {scenario['dealSizeBand']} | "
        f"Risk: {scenario['riskProfile']} | Timeline: {scenario['timelinePressure']}"
    )
    print("\nClient Objectives:")
    print_list(scenario["mandate"]["clientObjectives"])
    print("\nRed Lines:")
    print_list(scenario["mandate"]["redLines"])
    print("\nTarget Modules:")
    print_list(scenario["targetModules"])

    print("\nFacilitator Round Plan")
    print("  1) Opening position from learner (2-3 min)")
    print("  2) Counter position from AI/facilitator (2-3 min)")
    print("  3) Concession or resistance with rationale (3-4 min)")
    print("  4) Draft language proposal (3-5 min)")
    print("  5) Final recommendation to client (2 min)")

    print("\nInject these dynamic events during the exercise:")
    for idx, event in enumerate(scenario["dynamicEvents"], start=1):
        print(f"  {idx}. trigger={event['trigger']}")
        print(f"     event: {event['event']}")
        print(f"     impact hint: {event['impactHint']}")

    print("\nScore with these anchors:")
    print("  Strong signals:")
    print_list(scenario["scoringAnchors"]["strongSignals"], indent="    + ")
    print("  Common errors:")
    print_list(scenario["scoringAnchors"]["commonErrors"], indent="    - ")

    if mode == "rapid-fire":
        print("\nRapid-fire prompts (facilitator can ask these):")
        print("  - What is your fallback if the other side rejects your cap proposal?")
        print("  - Which point is economically most material and why?")
        print("  - Which clause dependency could invalidate your current position?")

    print("\nSession output checklist")
    print("  - Final learner position per target module")
    print("  - Top 3 strengths")
    print("  - Top 3 improvement priorities")
    print("  - Recommended next scenario")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a terminal scenario dry-run")
    parser.add_argument(
        "--scenario",
        default="scenario-001-buyer-locked-box.json",
        help="Scenario filename in docs/scenarios or full path",
    )
    parser.add_argument(
        "--mode",
        choices=["live-negotiation", "redline", "rapid-fire"],
        default="live-negotiation",
        help="Exercise mode",
    )
    args = parser.parse_args()

    path = Path(args.scenario)
    if not path.exists():
        candidate = DEFAULT_SCENARIOS / args.scenario
        if candidate.exists():
            path = candidate

    if not path.exists():
        raise SystemExit(f"Scenario not found: {args.scenario}")

    scenario = load_scenario(path)
    run_dry_run(scenario, args.mode)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
