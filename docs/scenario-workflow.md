# Scenario Workflow: From Draft to Pilot Session

Use this workflow to turn the existing scenario files into repeatable training sessions.

## 1) Pick the training objective for this week
Choose one narrow objective per session batch:
- Locked-box negotiation discipline
- Limitation of liability trade-offs
- Completion accounts drafting precision
- CP / termination strategy under time pressure

Then pick 2-3 scenarios that focus on that objective.

## 2) Clone and adapt a scenario template
Start from:
- `docs/scenarios/templates/scenario-template.json`

Or copy an existing pack:
- `docs/scenarios/scenario-001-buyer-locked-box.json`
- `docs/scenarios/scenario-002-seller-completion-accounts.json`

Recommended naming:
- `scenario-003-buyer-tax-indemnity.json`
- `scenario-004-seller-liability-cap.json`

## 3) Fill the four high-value sections first
Prioritize quality in these fields:
1. `mandate.clientObjectives`
2. `mandate.redLines`
3. `dynamicEvents`
4. `scoringAnchors`

If these are weak, coaching quality and scoring quality will drop.

## 4) Validate the JSON and structure
Run the validation script:

```bash
python scripts/validate_scenarios.py
```

This checks:
- JSON syntax
- required keys
- enum validity
- minimum quality guards (dynamic events + anchors not empty)

## 5) Run an internal facilitation pass (human-in-the-loop)
Before exposing to associates, run a 15-20 minute dry run with one reviewer:
- Does the mandate feel realistic?
- Are dynamic events plausible?
- Are strong signals and common errors distinguishable?
- Can a supervisor explain expected concessions?

## 6) Attach to a weekly training cadence
For each associate:
- 2 scenario sessions/week
- 1 rapid-fire drill
- 1 feedback reflection log

Track per scenario:
- domain scores
- top 3 mistakes
- time spent per clause

## 7) Scale from 2 to 10 scenarios
Suggested sequence:
- Wave 1: 2 scenarios (already present)
- Wave 2: +3 scenarios across sectors
- Wave 3: +5 scenarios with red-flag-heavy DD and compressed timelines

Stop and recalibrate rubric after each wave.

## Definition of "ready" scenario
A scenario is ready for pilot if:
- it validates with `scripts/validate_scenarios.py`
- it has at least 2 dynamic events
- it has at least 2 strong signals and 2 common errors
- reviewer confirms mandate + fallback logic are coherent
