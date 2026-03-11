# Implementation Roadmap: Swedish M&A Associate Negotiation Trainer

This roadmap translates the product blueprint into an executable 6-week MVP plan with concrete deliverables, owners, and acceptance criteria.

## Milestones Overview

| Milestone | Timebox | Owner(s) | Output |
|---|---|---|---|
| M1. Rubric Freeze | Week 1 | Product + Supervising Partners | Locked scoring rubric and calibration set |
| M2. Scenario Content Pack | Week 2 | PSL/SME + Product | 10 scenario packs in schema format |
| M3. Core Simulation Loop | Week 3 | Engineering | Negotiation + redline + rapid-fire MVP flow |
| M4. Assessment & Feedback | Week 4 | Engineering + Product | Clause-level scoring and feedback generation |
| M5. Personalization & Dashboard | Week 5 | Engineering | Adaptive recommendations + manager dashboard |
| M6. Pilot Launch | Week 6 | Product + Training Leads | 4-6 week pilot with baseline metrics |

## Detailed Plan

### M1 — Rubric Freeze and Calibration
- Finalize scoring definitions for:
  - Legal accuracy
  - Commercial judgment
  - Negotiation execution
  - Drafting precision
  - Process/project management
  - Client communication
- Run calibration workshop with 2-3 Swedish M&A partners.
- Produce 15-20 “golden response” examples for benchmark scoring.

**Acceptance criteria**
- `docs/rubric-v1.md` approved by internal reviewers.
- Inter-rater agreement target documented (e.g., +/- 10 points on 0-100 scale).

### M2 — Scenario Authoring
- Create 10 scenario packs balanced by:
  - Buyer-side vs seller-side mandates
  - Sector distribution
  - Risk profile (clean vs red-flag heavy)
  - Time pressure levels
- For each scenario:
  - Facts and mandate
  - Target clauses/modules
  - Counterparty persona
  - Expected concession ranges

**Acceptance criteria**
- Scenario files validate against `docs/scenario-schema.json`.
- 100% of scenarios contain scoring anchors and fallback positions.

### M3 — Core Simulation Loop
- Implement 3 MVP formats:
  - Live negotiation (turn-based)
  - Redline mode
  - Rapid-fire questions
- Persist each user action as a `ClauseAttempt` event.

**Acceptance criteria**
- End-to-end run from scenario start to submission works for all 3 formats.
- Session state is saved and recoverable.

### M4 — Assessment and Feedback
- Implement rubric scorer with:
  - Domain score output (0-100)
  - Clause-level breakdown
  - Mistake taxonomy tags
  - “Why it matters” rationale
- Add reviewer override function for supervisor QA.

**Acceptance criteria**
- Every completed session returns structured score + narrative feedback.
- Supervisor override is recorded with audit metadata.

### M5 — Personalization and Reporting
- Implement deterministic adaptation rules:
  - `<60` in same domain across 3 sessions -> mandatory remediation path
  - `>80` across 5 sessions -> complexity increase
- Generate individual training plans and manager summary dashboard.

**Acceptance criteria**
- Next-session recommendations generated automatically after each session.
- Dashboard displays trendline and module readiness per user.

### M6 — Pilot Execution
- Launch with a small cohort (e.g., 8-15 associates) for 4-6 weeks.
- Capture metrics weekly and run midpoint review.
- Tune rubric weights, prompt instructions, and scenario difficulty.

**Acceptance criteria**
- Pilot report includes learning outcomes and product usage outcomes.
- Clear go/no-go decision for expanded rollout.

## Risks and Mitigations

- **Risk:** Hallucinated legal references in feedback.
  - **Mitigation:** Constrain evaluator prompts to rubric + scenario facts and require citation to scenario artifacts.
- **Risk:** Scoring inconsistency between sessions.
  - **Mitigation:** Weekly benchmark re-scoring against golden set.
- **Risk:** Overly generic coaching.
  - **Mitigation:** Force recommendation engine to map each suggestion to one identified weakness.

## Definition of MVP Done

1. 10 validated Swedish SPA scenario packs.
2. 3 interaction modes live.
3. Session scorecards with rationale and remediation suggestions.
4. Personalized next-session planning.
5. Pilot cohort completed with measurable trend data.
