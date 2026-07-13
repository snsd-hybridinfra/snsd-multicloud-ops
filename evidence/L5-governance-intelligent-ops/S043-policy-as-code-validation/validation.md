# Validation Results

| Check ID | Check Description | Expected Condition | Evidence File | Actual Result | Status |
|---|---|---|---|---|---|
| V001 | Artifacts | Complete | Generated log | Present | PASS |
| V002 | Commands | Optional/manual/out-of-scope | Command reference | Matched | PASS |
| V003 | Schema | Judgments/exceptions complete | Schema | Matched | PASS |
| V004 | Rules | Domains/mappings complete | Rule set | Matched | PASS |
| V005 | Inputs | Valid consistent JSON | Input examples | Matched | PASS |
| V006 | Load | No external engine | Load sample | Matched | PASS |
| V007 | Pass | POLICY_PASS | Pass sample | Matched | PASS |
| V008 | Fail | POLICY_FAIL | Fail sample | Matched | PASS |
| V009 | Exception | Complete/approved | Exception sample | Matched | PASS |
| V010 | Classification | Required fields | Classification | Matched | PASS |
| V011 | Summary | POLICY_PASS/no cloud | Final sample | Matched | PASS |
| V012 | Manifest | Fields/mappings | Manifest | Matched | PASS |
| V013 | Terraform safety | Forbidden artifacts absent | Generated log | Checked | PASS |
| V014 | Sensitive safety | Sensitive values absent | Generated log | Checked | PASS |
| V015 | Execution safety | No external execution | Validator | Checked | PASS |
| V016 | Maturity | Placeholder/native syntax | Summary | Expected | WARN |
