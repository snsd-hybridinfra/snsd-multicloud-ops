# Commands

Scenario: S004-azure-network-provisioning-validation

Level: L1-foundation

## Run Validation

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-azure-network-provisioning.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L1-foundation\S004-azure-network-provisioning-validation\logs\azure-network-provisioning-validation.log
Get-Content evidence\L1-foundation\S004-azure-network-provisioning-validation\configs\azure-network-provisioning-summary.md
```

## Safety Notes

No planned command authenticates to Azure, reads credentials or kubeconfig, contacts Azure APIs, or runs Terraform init, validate, plan, apply, or destroy. The validator reads repository files and optionally runs `terraform fmt -check` only.
