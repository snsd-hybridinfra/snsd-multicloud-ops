# Milestones and Gates

| Milestone | Outcome | Current decision |
|---|---|---|
| M0 | Package governance normalized | APPROVED |
| M1 | Core identity, network and local visibility validated | APPROVED |
| M2 | CV and historical repeatability accepted with a scoped RV freshness exception | APPROVED |
| M3 | Central identity and visibility operational | PENDING |
| M4 | Multi-environment controls validated | PENDING |
| M5 | Policy as Code and drift operational | PENDING |
| M6 | L3 evidence assessment and deferred final scheduling completed | PENDING |

Each milestone retains explicit entry criteria, required actions, exit criteria,
blocking gaps, evidence requirements, and a decision in
`milestones-and-gates.yaml`. M0, the bounded core-control M1, and M2 are
approved from action evidence. M2 uses the reviewed `P1-RV-FRESHNESS-001`
exception: the historical three-run decision is preserved, the records remain
explicitly stale, and Phase 1 is `COMPLETED_WITH_GAPS`. A fresh manual RV window
is still mandatory before the final scheduling and acceptance gate. M3 through
M6 remain `PENDING`. The disabled ZT-SCH-001 task is deferred to M6 immediately
before the final L3 decision.
Neither approval assigns maturity nor proves compliance.
