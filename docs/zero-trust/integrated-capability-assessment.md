# Integrated Capability Assessment after P1-CV-001

## Current decision

The 2026-07-27 normalized-flow cycle assessed the bounded FND, NET, VIS, and
ID chain with the fixed ZT-CV-001 workflow. It completed 8 PASS / 2 WARN /
0 FAIL and found no current regression, but it is not an accepted CV cycle.

The refreshed FND execution retained one package-level warning while
`ZTCV-GATE-FND` permits zero. The package assessment is therefore
`REVIEW_REQUIRED / WARNING_BUDGET_EXCEEDED`, and P1-CV-001 is `BLOCKED`.
ZT-RV-001 is not authorized to start from this assessment.

The freshness view contained 9 fresh records, 1 aging record, and 1 preserved
superseded stale record. The stale historical FND record is retained for
integrity but is not treated as a current-stream regression because the same
validator and scope have a newer fresh record. All maturity fields remain
`UNASSESSED`.

## Historical assessment boundary

The 2026-07-22 assessment evaluated 12 capability records and recommended one
possible repeatability candidate, `ZT-4.1.1` through `ZTCV-VAL-SYS`. That
recommendation is historical and suspended while P1-CV-001 is blocked. It did
not assign EC4, schedule operation, maturity, certification, or Phase 1
completion.

Any future RV campaign still requires accepted CV, the exact stable validator,
workflow, scope, plan, sanitization, zero blocking failures, and three
independent consecutive successes separated by at least 24 hours. P1-CV-001
must first be rerun after separately authorized resolution of the FND blocker.
