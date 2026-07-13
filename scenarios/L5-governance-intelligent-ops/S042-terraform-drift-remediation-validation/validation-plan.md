# Validation Plan

| Check ID | Validation Item | Expected Condition |
|---|---|---|
| V001 | Required artifacts | All baselines, JSON examples, samples, and manifest exist |
| V002 | Command safety | Plan/manual rollback restricted; mutation/state commands out of scope |
| V003 | S041 reference | Detection ID, status, severity, resource present |
| V004 | Decision | Approved option, reason, risk, no real operation |
| V005 | Approval | Required sanitized approval present |
| V006 | Remediation plan | Complete and explicitly not executed |
| V007 | Rollback plan | ID, condition, owner, command placeholder, manual-only |
| V008 | No-drift evidence | Exit 0, NO_DRIFT, REMEDIATION_VALIDATED |
| V009 | Final summary | Complete evidence chain and no execution |
| V010 | Manifest | Required fields and S041/S043/S045 links |
| V011 | JSON examples | Revert/codify/post examples parse and match |
| V012 | Policy | Detection, approval, rollback, artifact, policy/cost boundaries |
| V013 | Terraform artifacts | No state, tfvars, plan binary, .terraform directory |
| V014 | Sensitive safety | No real identifiers, network values, credentials, keys, secrets |
| V015 | Execution safety | No Terraform/cloud CLI or execution claim |
| V016 | Evidence maturity | Placeholder decision/approval/rollback reported as WARN |

PASS requires zero critical failures. V016 may warn until disposable-lab evidence exists.
