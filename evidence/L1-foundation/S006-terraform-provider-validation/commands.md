# Commands

Scenario: S006-terraform-provider-validation

Level: L1-foundation

## Run Validation

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-terraform-provider-baseline.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L1-foundation\S006-terraform-provider-validation\logs\terraform-provider-validation.log
Get-Content evidence\L1-foundation\S006-terraform-provider-validation\configs\terraform-provider-baseline-summary.md
```

## Safety Notes

No planned command authenticates to a provider, reads credentials or kubeconfig, contacts cloud APIs, downloads providers, or runs Terraform init, validate, plan, apply, or destroy. The validator reads repository files and optionally runs `terraform fmt -check` only.
