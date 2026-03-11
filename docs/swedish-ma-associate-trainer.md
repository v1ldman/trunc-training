# Product Blueprint: AI Training Tool for Swedish M&A Associates

## 1) Target Users and Goals

### Audience
- Junior associates (0-2 PQE equivalent)
- Mid-level associates (2-5 PQE equivalent)
- Optional: supervising partner/PSL view for oversight

### Primary Learning Goals
The user should be able to:
1. Negotiate key SPA clauses in Swedish private M&A deals.
2. Explain legal/commercial rationale behind fallback positions.
3. Manage process workstreams (timelines, issue lists, sign/close sequencing).
4. Spot and assess due diligence findings and their SPA impact.
5. Communicate advice clearly to clients under time pressure.

---

## 2) Training Philosophy (3-6 Month Program)

The system should combine **deliberate practice**, **scenario repetition with variation**, and **AI coaching**.

### Program Cadence
- 2-3 structured sessions/week (45-75 min)
- 1 assessment checkpoint every 2 weeks
- 1 monthly capstone simulation

### Program Structure

#### Month 1: Foundations of Swedish SPA Practice
- SPA anatomy (definitions, purchase price, closing mechanics)
- Intro to key Swedish market norms and negotiation posture
- Guided clause-by-clause exercises (high scaffolding)

#### Month 2: Core Risk Allocation
- Warranties, disclosure mechanics, limitation regime
- Liability cap/basket/de minimis/time limits
- Materiality qualifiers and knowledge qualifiers
- Mid-month benchmark simulation

#### Month 3: Deal Economics + Completion Mechanics
- Locked-box vs completion accounts dynamics
- Leakage concepts and permitted leakage drafting
- Conditions precedent and long-stop date strategy
- Bring-down logic and termination rights

#### Month 4: Advanced Negotiation Dynamics
- Multi-party pressure simulation (client + opposing counsel + management)
- Time pressure, hostile redlines, strategic concessions
- Trade-off frameworks (e.g., warranty scope vs limitation package)

#### Month 5: Due Diligence-to-Drafting Integration
- Translate DD findings into specific SPA asks
- Prioritize issues by value-at-risk
- Build negotiation playbook from DD report

#### Month 6: Capstone + Performance Consolidation
- Full-cycle SPA negotiation simulation (term sheet to signing)
- Oral defense of negotiated position
- Final competency scoring and individualized development plan

---

## 3) Scenario Engine Design

Each simulation should be generated from structured inputs so difficulty and focus can be controlled.

### Core Scenario Inputs
- Deal type: private Swedish share acquisition
- Sector: e.g., SaaS, manufacturing, healthcare
- Deal size band: small/mid/large cap
- User role: buyer counsel or seller counsel
- Counterparty style: cooperative, aggressive, inconsistent
- Risk profile: clean business vs red-flag heavy DD
- Time constraints: normal vs compressed signing timeline

### Negotiation Objects (SPA Modules)
Train against modules, then full integrated drafts:
1. Definitions and interpretation
2. Purchase price mechanism (locked-box/completion accounts)
3. Warranties and specific indemnities
4. Limitations of liability
5. Covenants pre-closing/post-closing
6. Conditions precedent and closing deliverables
7. Termination and remedies
8. Governing law/dispute mechanics (as configured for Swedish context)

### Interaction Formats
- **Live negotiation mode:** turn-based negotiation with AI counsel
- **Redline mode:** user edits clause text; AI counters and explains impact
- **Oral defense mode:** user explains rationale to simulated partner/client
- **Rapid-fire mode:** short doctrinal/commercial questions

---

## 4) AI Tutoring and Remediation Loop

After each session, the platform should produce:
1. **Clause-level score breakdown**
2. **Mistake taxonomy** (legal issue, tactical issue, drafting issue, process issue)
3. **Why it matters** (risk, economics, enforceability, client outcome)
4. **Targeted drills** (10-20 min) for weak areas

### Example Remediation Paths
- If weak on limitation regimes -> assign 3 drills on cap/basket interplay.
- If weak on completion mechanics -> assign 2 drafting labs + 1 oral defense drill.
- If weak on negotiation process -> assign project-management simulations with timelines/checklists.

---

## 5) Competency Model and Scoring

Use a transparent multi-axis score (0-100 each axis):

1. **Legal Accuracy**
   - Correctness of clause interpretation
   - Correct issue spotting
2. **Commercial Judgment**
   - Prioritization of material points
   - Realistic trade-off handling
3. **Negotiation Execution**
   - Concession strategy
   - Outcome quality vs mandate
4. **Drafting Precision**
   - Clarity, consistency, internal SPA coherence
5. **Process/Project Management**
   - Timelines, dependency management, escalation discipline
6. **Client Communication**
   - Clarity, brevity, action-oriented advice

### Scoring Outputs
- Session scorecard
- Rolling 30-day trendline
- Benchmark against expected level (junior/mid)
- “Readiness indicator” per module (Foundational / Developing / Deal-Ready)

---

## 6) Personalization Logic

The AI coach should adapt based on:
- Historical weak points
- Recurring error patterns
- User confidence self-assessment
- Time available per week

### Adaptive Rules (Example)
- If score <60 in a domain for 3 sessions -> mandatory micro-curriculum.
- If score >80 for 5 sessions -> increase complexity (multi-issue negotiations, noisy facts).
- If drafting strong but oral defense weak -> rebalance toward spoken simulations.

---

## 7) Suggested Technical Architecture

### Components
1. **Scenario Orchestrator**
   - Builds each training scenario from templates + variables.
2. **Negotiation Agent(s)**
   - AI counterparty personas with configurable strategy.
3. **Assessment Engine**
   - Rubric-based evaluator + explanation generator.
4. **Learning Planner**
   - Assigns next sessions and remediation.
5. **Content Store**
   - SPA clause libraries, model answers, DD datasets, rubric configs.
6. **Analytics Dashboard**
   - User progress, competency heatmaps, cohort reporting.

### Data Model (High-Level)
- `User`
- `Session`
- `Scenario`
- `ClauseAttempt`
- `ScoreBreakdown`
- `FeedbackItem`
- `TrainingPlan`
- `CheckpointAssessment`

---

## 8) MVP Scope (First 8-12 Weeks)

### MVP Should Include
- 8-12 core Swedish SPA scenarios
- 3 interaction formats (live negotiation, redline, rapid-fire)
- Competency scoring on 4 axes (legal, commercial, negotiation, drafting)
- Personalized next-session recommendations
- Basic manager dashboard

### Deferred to Phase 2
- Voice-mode simulations
- Team-based negotiation rooms
- Cross-border transaction variants
- Integration with law firm LMS/HR systems

---

## 9) Example Session Flow

1. User receives scenario brief (deal facts + role + client mandate).
2. User negotiates two SPA sections with AI counterpart.
3. AI injects dynamic events (new DD finding, client priority shift, timing pressure).
4. User submits final clause wording and rationale.
5. Assessment engine scores and provides actionable feedback.
6. Planner schedules next exercises (targeting weak domains).

---

## 10) Quality, Safety, and Professional Guardrails

- Mark tool as **training support**, not legal advice.
- Keep jurisdiction/context labels explicit in all scenarios.
- Maintain auditable scoring rationales.
- Allow supervisor review/override for high-stakes evaluations.
- Use anonymized synthetic datasets for practice fact patterns.

---

## 11) Success Metrics

### Learning Metrics
- Improvement in domain scores over 30/60/90 days
- Capstone pass rates
- Time-to-competency reduction (junior -> mid-level tasks)

### Product Metrics
- Weekly active learners
- Session completion rate
- Recommendation acceptance rate
- Manager-reported quality uplift

---

## 12) Immediate Next Steps

1. Confirm competency rubric with 2-3 Swedish M&A partners.
2. Draft first 10 scenario packs (balanced buyer/seller perspectives).
3. Implement scoring engine prototype with human calibration.
4. Pilot with a small associate cohort for 4-6 weeks.
5. Use pilot data to tune difficulty curves and feedback style.

This gives you a realistic path to a robust, adaptive training system that mirrors the real pressure and complexity of Swedish SPA negotiations while still being structured enough for measurable skill progression.
