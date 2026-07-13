# Validation Results

| Check ID | Check Description | Expected Condition | Evidence File | Actual Result | Status |
|---|---|---|---|---|---|
| V001 | Required artifacts | Complete | Generated log | Present | PASS |
| V002 | Command safety | Manual/out-of-scope boundaries | Command reference | Confirmed | PASS |
| V003 | S041 reference | Complete | Detection sample | Matched | PASS |
| V004 | Decision | Valid option/risk/no execution | Decision sample | Matched | PASS |
| V005 | Approval | Present | Approval sample | Matched | PASS |
| V006 | Plan | Complete/not executed | Plan sample | Matched | PASS |
| V007 | Rollback | Complete/manual-only | Rollback sample | Matched | PASS |
| V008 | No drift | Exit 0/NO_DRIFT | Post sample | Matched | PASS |
| V009 | Final summary | Full chain/validated | Final sample | Matched | PASS |
| V010 | Manifest | Required fields/mappings | Manifest | Matched | PASS |
| V011 | JSON | Parseable examples | Terraform examples | Matched | PASS |
| V012 | Policy | Required controls | Policy | Matched | PASS |
| V013 | Artifact safety | Forbidden files absent | Generated log | Checked | PASS |
| V014 | Sensitive safety | Sensitive values absent | Generated log | Checked | PASS |
| V015 | Execution safety | No execution | Validator/final sample | Confirmed | PASS |
| V016 | Evidence maturity | Placeholder warning | Generated summary | Placeholder-only | WARN |

Generated result section: the validator output is authoritative. No real remediation was performed.
