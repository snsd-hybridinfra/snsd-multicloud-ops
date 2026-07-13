# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Required artifacts | Complete | files/summary |
| V002 | Runbook workflow and placeholders | Complete | runbook |
| V003 | Criteria matrix | Ten phases | criteria |
| V004 | Restore policy requirements | Complete | policy |
| V005 | Ansible placeholder safety | Debug only | playbook |
| V006 | Restore precheck evidence | Manifest/disposable target | precheck |
| V007 | Checksum verification evidence | SHA256/match | checksum |
| V008 | Manual restore command evidence | Explicit/not executed | command sample |
| V009 | Restore artifact metadata | Positive size/all fields | metadata |
| V010 | Restore consistency evidence | Passed/no data | consistency |
| V011 | Restore manifest fields | Complete | manifest |
| V012 | Restore completion summary | Complete/S040/no artifact | completion |
| V013 | Restore artifact path and secret safety | Safe | evidence/log |
| V014 | Execution safety boundary | No restore action | validator |
| V015 | Command reference boundary | Out of scope | commands |
