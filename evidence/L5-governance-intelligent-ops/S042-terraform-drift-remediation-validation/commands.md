# Commands

## Static Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-terraform-drift-remediation.ps1
```

Inspect `logs/terraform-drift-remediation-validation.log` and `configs/terraform-drift-remediation-validation-summary.md`.

Disposable-lab evidence must be manually sanitized. The validator does not run Terraform. Apply, destroy, import, and state commands are out of scope. Do not commit state, tfvars, plan binaries, backend values, credentials, or real identifiers. S041 owns detection, S043 policy, and S045 cost guardrails.

Live execution status: `NOT_RUN` and OUT OF SCOPE.
