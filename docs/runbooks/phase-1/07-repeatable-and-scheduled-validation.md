# Repeatable and Scheduled Validation

```json runbook-metadata
{"runbook_id":"RB-P1-007","phase":"PHASE_1","related_packages":["ZT-CV-001","ZT-RV-001","ZT-SCH-001"],"procedure_status":"PARTIALLY_IMPLEMENTED","validation_status":"PARTIALLY_RUNTIME_VALIDATED","live_execution_permitted":true}
```

## Purpose

Define and operate the bounded read-only cross-capability gate, then preserve
the separate predecessor gates for repeatable and scheduled validation.

## Current boundary

ZT-CV-001 is `IMPLEMENTED / PARTIALLY_RUNTIME_VALIDATED /
PARTIALLY_ACCEPTED` at EC3. Its 2026-07-28 cycle completed 8 PASS / 2 WARN /
0 FAIL with zero blocked gates. ZT-RV-001 is `IMPLEMENTED / VALIDATED /
ACCEPTED` at bounded EC4 after three eligible independent successes with
stable fingerprints and enforced separation. ZT-SCH-001 is `IMPLEMENTED /
LOCAL_VALIDATED / RUNTIME_NOT_VALIDATED`: its bounded Windows Task Scheduler
job is installed and enabled. Six sanitized scheduled candidates from
2026-08-03 through 2026-08-08 failed on the unavailable fixed OpenStack SSH
target. A bounded 09:00-11:00 `StartWhenAvailable` path was installed on
2026-08-11 without changing the limited interactive-token principal. No
successful scheduled runtime, CI workflow, automatic retry, or notification
integration exists.

## Required sequence

1. CV validates FND, NET, VIS, and ID together and records conflicts or missing controls.
2. RV repeats an accepted deterministic CV plan and proves evidence consistency.
3. SCH was installed only after RV acceptance and the explicit 2026-08-02 scheduler approval.
4. Scheduled validation may catch up only within two hours, must detect missed or failed runs, verify freshness and retention, and support disable and rollback.

## Pass criteria

CV passes only when every mandatory predecessor gate is accepted in the same
assessment. RV accepts only unique, sanitized, fingerprint-consistent runs
with zero blocking failures and at least 24 hours of separation. The current
RV state is accepted at 3/3 and bounded EC4. The installed schedule has zero
successful correlated dates and therefore no runtime or EC5 credit; seven non-RV evidence streams
currently require freshness review, and Phase 1 remains NOT_COMPLETE.
