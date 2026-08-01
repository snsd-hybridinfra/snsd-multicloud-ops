# Integrated Capability Assessment after P1-CV-001

## Current decision

The 2026-07-28 normalized-flow cycle assessed the bounded FND, NET, VIS, and
ID chain with the fixed ZT-CV-001 workflow. It completed 8 PASS / 2 WARN /
0 FAIL, found no current regression, and returned 10 package gates with zero
blocked or review-required decisions. ZT-CV-001 is `PARTIALLY_ACCEPTED` at
`EC3_ONE_TIME_RUNTIME`.

The first governed RV execution, `ZTRV-20260728T082825Z-f22b1052`, completed
8 PASS / 2 WARN / 0 FAIL. The second, `ZTRV-20260730T002834Z-ac20f30a`,
completed 6 PASS / 4 WARN / 0 FAIL. Both retained sanitization PASS and nine
of nine negative boundary requests blocked. The third,
`ZTRV-20260801T230020Z-daebf8ef`, completed 5 PASS / 5 WARN / 0 FAIL with the
same fixed fingerprints, sanitization PASS, and nine of nine negative boundary
requests blocked. ZT-RV-001 is `REPEATABILITY_ACCEPTED` at bounded
`EC4_REPEATABLE_RUNTIME` with three eligible successes. All maturity fields
remain `UNASSESSED`.

The bounded ZT-ID-001 endpoint was subsequently revalidated with 20/20
positive and 42/42 denied checks. The original stale execution remains
preserved, the new fresh record supersedes it for current regression analysis,
and no identity scope or maturity was promoted. As of 2026-08-01T23:05:00Z,
seven other current evidence streams are stale review findings; these do not
alter the independently accepted RV campaign but remain open for later gates.

## Historical assessment boundary

The 2026-07-22 assessment recommended `ZT-4.1.1` through `ZTCV-VAL-SYS`; the
2026-07-28 accepted CV decision activated that exact candidate without changing
the validator, workflow, target scope, or plan hash. All three counted runs are
unique, consecutive, current within the campaign window, and separated by at
least 24 hours. No immediate retry, failed run, copied evidence, or changed
fingerprint counts. The current result assigns only bounded EC4; it does not
assign scheduled operation, EC5, maturity, certification, or Phase 1
completion.
