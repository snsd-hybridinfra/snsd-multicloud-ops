# P1-ACC-001 Blocked Acceptance Report

## Outcome

P1-ACC-001 is `BLOCKED_STALE_EVIDENCE`. FND, NET, VIS, ID, CV, and historical
RV decisions are present, but the current acceptance gate cannot use the three
RV records because each exceeds the `P7D` maximum evidence age.

At `2026-08-20T11:08:50.558164Z`, the read-only RV assessment returned zero
accepted current records, `STALE` freshness, `EC3_ONE_TIME_RUNTIME`, and
`NOT_STARTED`. The newest record was approximately 18.51 days old. Phase 1
therefore remains `PARTIAL / PARTIALLY_VALIDATED / NOT_COMPLETE`.

## Recovery path

Use the existing ZT-RV-001 manual campaign after separate live authorization.
Three new eligible read-only executions must succeed with stable fingerprints,
sanitized evidence, zero blocking failures, and at least `PT24H` separation.
Then rerun P1-ACC-001. ZT-SCH-001 remains disabled and is not required for this
recovery path.

## Non-claims

This decision does not execute a live validator, change a target, re-enable the
scheduler, grant Phase 1 acceptance, start Phase 2, assign EC5 or maturity, or
claim compliance, certification, production readiness, or full success.
