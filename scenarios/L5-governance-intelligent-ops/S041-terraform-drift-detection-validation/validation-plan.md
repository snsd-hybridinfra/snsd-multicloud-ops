# Validation Plan

| Check ID | Validation Item | Expected Condition |
|---|---|---|
| V001 | Required artifacts | All baselines, JSON examples, samples, and manifest exist |
| V002 | Command safety | Plan is manual-lab-only; mutation/state commands are out of scope |
| V003 | No-drift evidence | Exit 0 and NO_DRIFT |
| V004 | Drift evidence | Exit 2 and DRIFT_DETECTED |
| V005 | Critical drift | Security exposure and CRITICAL_DRIFT |
| V006 | Classification | Expected/observed/severity and S042 mapping |
| V007 | Final summary | No remediation; S042/S043 links |
| V008 | Manifest | Required fields and links |
| V009 | Plan JSON | Three parseable sanitized examples |
| V010 | Terraform artifacts | No state, tfvars, plan binary, or .terraform directory |
| V011 | Sensitive safety | No real IDs, network values, credentials, keys, or secrets |
| V012 | Policy | Evidence/artifact/escalation requirements |
| V013 | Remediation boundary | No remediation execution claim |
| V014 | Execution safety | Validator does not run Terraform or cloud CLIs |
| V015 | Evidence maturity | Placeholder-only evidence is reported as WARN |

PASS requires zero critical failures. V015 may warn until disposable-lab evidence replaces placeholders.
