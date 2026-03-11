# Swedish M&A Associate Negotiation Trainer

This repository now contains a practical blueprint for building an AI-driven training platform for junior and mid-level associates working with Swedish private M&A transactions.

## What this tool does

The platform simulates realistic negotiations around a Swedish share purchase agreement (SPA), then evaluates each lawyer over time across legal, tactical, and execution skills.

Core outcomes:
- Place the user in role-based negotiation scenarios (buyer counsel, seller counsel, management team, etc.).
- Train over a 3-6 month program with adaptive progression.
- Mix live negotiation practice with free-form legal Q&A and micro-tutoring.
- Score the lawyer by topic and suggest tailored next sessions (drafting, negotiation, project management, due diligence).

## Where to start

Read the full product blueprint:

- [`docs/swedish-ma-associate-trainer.md`](docs/swedish-ma-associate-trainer.md)

It includes:
- Curriculum and progression model (months 1-6)
- Scenario architecture for Swedish SPA negotiations
- Scoring model and competency map
- Personalization and remediation loops
- Suggested technical architecture, implementation phases, and guardrails


## Implementation assets

- [`ROADMAP.md`](ROADMAP.md)
- [`docs/mvp-spec.md`](docs/mvp-spec.md)
- [`docs/rubric-v1.md`](docs/rubric-v1.md)
- [`docs/scenario-schema.json`](docs/scenario-schema.json)
- [`docs/scenarios/`](docs/scenarios/)
- [`docs/scenario-workflow.md`](docs/scenario-workflow.md)
- [`docs/run-guide.md`](docs/run-guide.md)
- `python scripts/validate_scenarios.py`


## Quick run

```bash
python scripts/validate_scenarios.py
python scripts/run_session_dry_run.py --scenario scenario-001-buyer-locked-box.json --mode live-negotiation
```
