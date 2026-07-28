# Repeatable and Scheduled Validation

```json runbook-metadata
{"runbook_id":"RB-P1-007","phase":"PHASE_1","related_packages":["ZT-CV-001","ZT-RV-001","ZT-SCH-001"],"procedure_status":"PARTIALLY_IMPLEMENTED","validation_status":"PARTIALLY_RUNTIME_VALIDATED","live_execution_permitted":true}
```

## Purpose

Define and operate the bounded read-only cross-capability gate, then preserve
the separate predecessor gates for repeatable and scheduled validation.

## Current boundary

ZT-CV-001 tooling is `IMPLEMENTED / PARTIALLY_RUNTIME_VALIDATED`, but its
2026-07-27 normalized-flow execution is `BLOCKED`. The final cycle completed
8 PASS / 2 WARN / 0 FAIL with no regression, but the current FND record has
one warning against an allowed-warning budget of zero. ZT-RV-001 and
ZT-SCH-001 remain `NOT_IMPLEMENTED / NOT_VALIDATED`. No scheduler, job, CI
workflow, automatic retry, notification integration, or accepted
repeatability evidence exists.

## Required sequence

1. CV validates FND, NET, VIS, and ID together and records conflicts or missing controls.
2. RV repeats an accepted deterministic CV plan and proves evidence consistency.
3. SCH may be designed and installed only after RV acceptance and separate scheduler approval.
4. Scheduled validation must detect missed or failed runs, verify freshness and retention, and support disable and rollback.

## Pass criteria

CV passes only when every mandatory predecessor gate is accepted in the same
assessment. A `REVIEW_REQUIRED`, `BLOCKED`, stale, failed, or inconsistent
predecessor decision blocks CV and therefore RV. The current decision is
blocked by `ZTCV-GATE-FND / WARNING_BUDGET_EXCEEDED`; no schedule exists and
Phase 1 remains NOT_COMPLETE.
