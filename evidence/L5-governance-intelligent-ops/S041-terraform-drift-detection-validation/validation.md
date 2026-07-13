# Validation Results

| Check ID | Check Description | Expected Condition | Evidence File | Actual Result | Status |
|---|---|---|---|---|---|
| V001 | Required artifacts | Complete | Generated log | Present | PASS |
| V002 | Command safety | Manual/out-of-scope boundaries | Command reference | Confirmed | PASS |
| V003 | No drift | Exit 0/NO_DRIFT | No-drift sample | Matched | PASS |
| V004 | Drift | Exit 2/DRIFT_DETECTED | Drift sample | Matched | PASS |
| V005 | Critical drift | Critical/CRITICAL_DRIFT | Critical sample | Matched | PASS |
| V006 | Classification | Fields and S042 | Classification sample | Matched | PASS |
| V007 | Final summary | No execution; S042/S043 | Final summary sample | Matched | PASS |
| V008 | Manifest | Required fields | Manifest sample | Matched | PASS |
| V009 | JSON | Parseable examples | Terraform examples | Matched | PASS |
| V010 | Artifact safety | Forbidden files absent | Generated log | Checked | PASS |
| V011 | Sensitive safety | Sensitive values absent | Generated log | Checked | PASS |
| V012 | Policy | Required controls | Policy example | Matched | PASS |
| V013 | No remediation | No execution claim | Final summary | Confirmed | PASS |
| V014 | Execution safety | No Terraform/cloud CLI | Validator source | Confirmed | PASS |
| V015 | Evidence maturity | Placeholder warning | Generated summary | Placeholder-only | WARN |

Generated result section: the validator output is authoritative. No real Terraform or cloud operation was run.
