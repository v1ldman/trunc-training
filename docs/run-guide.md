# Run Guide

This repository currently provides **planning/content assets + CLI helpers**, not a full web app.

## Prerequisites
- Python 3.10+

## 1) Validate scenarios

```bash
python scripts/validate_scenarios.py
```

Expected output:
- `Validated X scenario file(s) successfully.`

## 2) Run a dry-run session in terminal

Use an existing scenario:

```bash
python scripts/run_session_dry_run.py --scenario scenario-001-buyer-locked-box.json --mode live-negotiation
```

Other modes:

```bash
python scripts/run_session_dry_run.py --scenario scenario-002-seller-completion-accounts.json --mode redline
python scripts/run_session_dry_run.py --scenario scenario-002-seller-completion-accounts.json --mode rapid-fire
```

This prints:
- mandate and red lines
- facilitator round plan
- dynamic event injection points
- scoring anchors
- session output checklist

## 3) Author a new scenario and re-run

1. Copy template:

```bash
cp docs/scenarios/templates/scenario-template.json docs/scenarios/scenario-003-your-topic.json
```

2. Edit content.
3. Validate again:

```bash
python scripts/validate_scenarios.py
```

4. Dry-run the new scenario:

```bash
python scripts/run_session_dry_run.py --scenario scenario-003-your-topic.json --mode live-negotiation
```

## What this means practically

You can start running coached sessions immediately with a human facilitator while engineering builds the full AI orchestration layer from the roadmap/MVP spec.
