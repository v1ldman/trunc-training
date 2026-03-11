# MVP Specification (8-12 Weeks)

## Scope

Build a training MVP for junior/mid-level associates focused on Swedish private M&A share purchase agreement negotiation.

In-scope:
- Scenario-driven practice
- 3 interaction modes
- 4 primary score domains in MVP
- Personalized follow-up recommendations
- Basic manager dashboard

Out-of-scope for MVP:
- Voice-mode simulations
- Team negotiation rooms
- Cross-border variants
- LMS/HRIS integration

## Personas

1. **Associate learner**
   - Wants realistic practice and clear feedback.
2. **Supervising partner / PSL**
   - Wants confidence that scoring reflects practical standards.
3. **Program manager**
   - Wants insight into progress and training ROI.

## User Stories

### Learner stories
- As an associate, I can enter a role-based scenario and receive a mandate brief.
- As an associate, I can negotiate with an AI counterparty over SPA clauses.
- As an associate, I can submit redlined text and get impact-aware feedback.
- As an associate, I can receive a score breakdown and next steps.

### Supervisor stories
- As a supervisor, I can review score rationales and override when required.
- As a supervisor, I can view trends by associate and competency domain.

## Functional Requirements

### Scenario Orchestrator
- Input dimensions:
  - deal type (private Swedish share acquisition)
  - sector
  - deal size band
  - user role
  - counterparty style
  - risk profile
  - timeline pressure
- Output:
  - complete session brief
  - module targets
  - dynamic events queue

### Interaction Modes

1. Live negotiation mode
- turn-based proposals and counters
- stateful memory within scenario

2. Redline mode
- user edits specific clause text
- AI returns counterproposal + consequences

3. Rapid-fire mode
- short doctrinal/commercial prompts
- immediate correctness and rationale

### Assessment Engine
- Domain scores (MVP):
  - legal accuracy
  - commercial judgment
  - negotiation execution
  - drafting precision
- Required outputs:
  - clause-level commentary
  - taxonomy tags
  - why-it-matters explanation

### Learning Planner
- Deterministic adaptation rules in MVP
- Generate 1-3 recommended sessions after each completed session

### Dashboard
- Per-associate trendline
- Domain heatmap
- Completion rates

## Non-Functional Requirements

- Explainability: every score must have traceable rationale.
- Auditability: supervisor overrides must be logged.
- Jurisdiction clarity: every scenario explicitly labeled Swedish private M&A training.
- Safety: UI and output clearly indicate “training support, not legal advice.”

## Data Objects

- `User`
- `Scenario`
- `Session`
- `ClauseAttempt`
- `ScoreBreakdown`
- `FeedbackItem`
- `TrainingPlan`
- `CheckpointAssessment`

## Success Criteria

Learning:
- median score uplift after 30 days
- capstone progression rate

Product:
- weekly active learners
- session completion rate
- recommendation acceptance rate

## Delivery Plan

- Week 1-2: rubric + content
- Week 3-4: core interactions + scoring
- Week 5: personalization + dashboard
- Week 6: pilot launch prep
- Week 7-12: run pilot and iterate
