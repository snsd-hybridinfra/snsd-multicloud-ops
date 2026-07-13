# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Required artifacts | Complete | files/summary |
| V002 | Runbook placeholders and exclusions | Complete | runbook |
| V003 | Misconfiguration criteria matrix | Ten types | criteria |
| V004 | Rollback decision matrix | Nine cases | decision matrix |
| V005 | Policy requirements | Complete metadata/prohibitions | policy |
| V006 | Command reference scope boundary | Modifications out of scope | commands |
| V007 | Pre-change least privilege evidence | Restricted sources | pre sample |
| V008 | Manual misconfiguration evidence | Explicit/not executed | event sample |
| V009 | Misconfiguration detection evidence | Rule/source/port/severity | detection |
| V010 | Exposure impact assessment | Classified/rollback | impact |
| V011 | Manual rollback evidence | Explicit/not executed | rollback |
| V012 | Post-rollback safe state | Restricted/no broad exposure | post sample |
| V013 | Final validation summary evidence | Detected/rollback/safe/no change | validation sample |
| V014 | Temporary exception expiry maturity | Concrete later or WARN | event sample |
| V015 | Identifier network and secret safety | No concrete value | log/summary |
| V016 | Execution safety boundary | No cloud/firewall execution | validator |
