# ZT-CV-001 Continuous Verification Foundation

## Accepted boundary

`ZT-CV-001` implements a default-deny, fixed-handler framework for evidence
freshness, repeatability, package and capability acceptance, regression
detection, exception governance, and proposal-only maturity reassessment. One
manual `EXECUTE_READ_ONLY` cycle completed as `PARTIAL` with 8 PASS, 2 WARN,
and 0 FAIL.

The cycle is `EC3_ONE_TIME_RUNTIME`. It is not continuous verification in the
operational `EC6` sense. It did not install a schedule, execute a mutation,
remediate a finding, update an authority file automatically, or assign
maturity.

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

## Runtime result

The accepted execution is `ZTA-20260722T045752Z-eb639d92` with plan hash
`72c0aa52f20b12fb67d7b149e7c1ed980c2cfcbcdafea9cfc344cac2f4912624`.
The two warnings retain the governance reference-frequency boundary and the
accepted OpenStack `CURRENT_DEGRADED 46/0/4` state. All nine predecessor
history records were fresh at assessment time, no evidence-hash regression
was detected, and all 12 reassessed capabilities retained `UNASSESSED`.

## Successor gate

`ZT-RV-001` may use this exact workflow, plan hash, validator version, and
scope as its candidate campaign baseline. It must still collect three
independent consecutive successful executions at least 24 hours apart. A
copied record, immediate retry, failed run, changed plan, or unsanitized result
does not count. `ZT-SCH-001` remains blocked until EC4 and separate installation
approval.
