# Commands

Planned/not-run output note: live inventory and cleanup commands remain `NOT_RUN`; only the implemented static validator is executed.

Run the safe repository-local validator:

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-resource-cleanup.ps1
```

Inspect generated evidence:

```powershell
Get-Content evidence/L5-governance-intelligent-ops/S046-resource-cleanup-validation/logs/resource-cleanup-validation.log
Get-Content evidence/L5-governance-intelligent-ops/S046-resource-cleanup-validation/configs/resource-cleanup-validation-summary.md
```

The script performs static parsing only. Terraform, cloud CLI/API, Kubernetes, inventory discovery, deletion, and cleanup execution are out of scope.
