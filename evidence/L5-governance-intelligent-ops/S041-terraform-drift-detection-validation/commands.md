# Commands

## Static Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-terraform-drift-detection.ps1
```

Inspect `logs/terraform-drift-detection-validation.log` and `configs/terraform-drift-detection-validation-summary.md`.

Disposable-lab evidence must be manually sanitized into the documented sample schema. The validator does not run Terraform. Do not commit tfstate, tfvars, plan binaries, backend values, credentials, real identifiers, or network values. S042 owns remediation.

Live execution status: `NOT_RUN` and OUT OF SCOPE.
