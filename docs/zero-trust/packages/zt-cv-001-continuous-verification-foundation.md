# ZT-CV-001 Continuous Verification Foundation

## Implemented boundary

`ZT-CV-001` implements a default-deny, fixed-handler framework for evidence
freshness, repeatability, package and capability acceptance, regression
detection, exception governance, and proposal-only maturity reassessment. The
tooling and fixed plan are implemented, but package acceptance is currently
blocked.

The runtime evidence level is `EC3_ONE_TIME_RUNTIME`. It is not continuous
verification in the operational `EC6` sense. It does not install a schedule,
execute a mutation, remediate a finding, update an authority automatically, or
assign maturity.

## Decision flow

1. Validate the Zero Trust and CV authorities.
2. Evaluate existing evidence freshness without deletion.
3. Run the fixed bounded live-system validator.
4. Calculate continuity from unique execution records.
5. Evaluate package and capability gates.
6. Detect regressions without remediation.
7. Produce a check-only maturity reassessment result.
8. Write sanitized output under the ignored runtime boundary.

Every step is registered in the reviewed automation catalogs. YAML does not
contain an executable command, arbitrary SSH target, or caller-controlled
working directory.

## Historical runtime result

The preserved pre-normalization execution is
`ZTA-20260722T045752Z-eb639d92` with plan hash
`72c0aa52f20b12fb67d7b149e7c1ed980c2cfcbcdafea9cfc344cac2f4912624`.
It completed 8 PASS / 2 WARN / 0 FAIL and remains historical EC3 evidence. It
does not override the current normalized-flow gate.

## Current normalized-flow decision

Execution `ZTA-20260727T125822Z-519fe693` used the same fixed plan hash and
completed `PARTIAL` with 8 PASS, 2 WARN, and 0 FAIL. Freshness assessment found
9 fresh records, 1 aging record, 1 preserved superseded stale record, and no
current regression. Package acceptance nevertheless returned
`ZT-FND-001 = REVIEW_REQUIRED / WARNING_BUDGET_EXCEEDED`: the refreshed FND
validator retained one package-level warning while its configured budget is
zero. P1-CV-001 therefore stops as `BLOCKED`; the transient 503 attempt and
the earlier stale-FND attempt receive no acceptance or continuity credit.

Both OpenStack instances and all EVE node processes were returned to their
original stopped state. No target configuration, ACL, identity policy,
logging configuration, authority file, or schedule was changed by the live
workflow.

## Successor gate

`ZT-RV-001` cannot begin until P1-CV-001 is accepted. The exact FND blocker
must be remediated under separate authority and the same bounded CV plan must
be rerun without bypassing the zero-warning gate. A copied record, immediate
retry, failed run, changed plan, blocked run, or unsanitized result does not
count. `ZT-SCH-001` remains blocked until EC4 and separate installation
approval.
