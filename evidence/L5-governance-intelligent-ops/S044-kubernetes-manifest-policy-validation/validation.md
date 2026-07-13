# Validation Results

| Check ID | Check Description | Expected Condition | Evidence File | Actual Result | Status |
|---|---|---|---|---|---|
| V001 | Artifacts | Complete | Generated log | Present | PASS |
| V002 | Commands | Optional/no live cluster | Command reference | Matched | PASS |
| V003 | Rules | Areas/judgments/exceptions | Rules | Matched | PASS |
| V004 | Compliant | Secure baseline | Compliant example | Matched | PASS |
| V005 | Violation | Labeled violations | Violation example | Matched | PASS |
| V006 | Exception | Complete | Exception example | Matched | PASS |
| V007 | Exposure | Violation-only/ClusterIP | Service example | Matched | PASS |
| V008 | Evidence | Consistent | Evidence samples | Matched | PASS |
| V009 | Summary | PASS/no live operation | Final sample | Matched | PASS |
| V010 | Manifest | Fields/mappings | Manifest | Matched | PASS |
| V011 | Kubeconfig | Absent | Generated log | Checked | PASS |
| V012 | Sensitive safety | Clean | Generated log | Checked | PASS |
| V013 | Execution | None | Validator | Checked | PASS |
| V014 | Boundaries | S018/S043/out-of-scope | Runbook | Matched | PASS |
| V015 | Maturity | Placeholder warning | Summary | Expected | WARN |
