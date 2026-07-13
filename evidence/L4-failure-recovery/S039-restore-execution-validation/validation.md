# Validation Result

- Actual Result: StaticEvidence validation completed; generated summary is authoritative.
- Status: PASS when critical failures equal zero.

| Check ID | Check Description | Expected Condition | Evidence File | Result |
|---|---|---|---|---|
| V001 | Artifacts | Complete | summary | PASS |
| V002 | Workflow | Complete | runbook | PASS |
| V003 | Criteria | Complete | criteria | PASS |
| V004 | Policy | Complete | policy | PASS |
| V005 | Ansible | Debug only | playbook | PASS |
| V006 | Precheck | Disposable/ready | precheck | PASS |
| V007 | Checksum | SHA256/match | checksum | PASS |
| V008 | Restore command | Manual/not executed | command | PASS |
| V009 | Metadata | Positive/complete | metadata | PASS |
| V010 | Consistency | Passed/no data | consistency | PASS |
| V011 | Manifest | Complete | manifest | PASS |
| V012 | Completion | Complete/S040/no artifact | completion | PASS |
| V013 | Artifact/path safety | Safe | summary | PASS |
| V014 | Execution safety | No action | validator | PASS |
| V015 | Command boundary | Out of scope | commands | PASS |
