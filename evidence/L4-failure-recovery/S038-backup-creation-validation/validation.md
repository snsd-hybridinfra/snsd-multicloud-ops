# Validation Result

- Actual Result: StaticEvidence validation completed; generated summary is authoritative.
- Status: PASS when critical failures equal zero.

| Check ID | Check Description | Expected Condition | Evidence File | Result |
|---|---|---|---|---|
| V001 | Artifacts | Complete | summary | PASS |
| V002 | Workflow | Complete | runbook | PASS |
| V003 | Criteria | Complete | criteria | PASS |
| V004 | Retention policy | Complete | policy | PASS |
| V005 | Ansible | Debug only | playbook | PASS |
| V006 | Command evidence | Sanitized | command sample | PASS |
| V007 | Metadata | Positive/complete | metadata | PASS |
| V008 | Checksum | SHA256 | checksum | PASS |
| V009 | Listing | Symbolic | listing | PASS |
| V010 | Manifest | Complete | manifest | PASS |
| V011 | Summary | Complete/no artifact | creation summary | PASS |
| V012 | Artifact safety | None | evidence tree | PASS |
| V013 | Path/secret safety | Safe | summary | PASS |
| V014 | Execution safety | No action | validator | PASS |
| V015 | Command boundary | Out of scope | commands | PASS |
