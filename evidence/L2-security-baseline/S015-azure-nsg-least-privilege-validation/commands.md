# Commands

Scenario: S015-azure-nsg-least-privilege-validation

Level: L2-security-baseline

## Run Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-azure-nsg-least-privilege.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L2-security-baseline\S015-azure-nsg-least-privilege-validation\logs\azure-nsg-least-privilege-validation.log
Get-Content evidence\L2-security-baseline\S015-azure-nsg-least-privilege-validation\configs\azure-nsg-least-privilege-summary.md
```

## Safety Notes

These commands do not authenticate to Azure, invoke Azure CLI, query NSGs, initialize Terraform, create a plan, apply changes, read credentials, or contact external systems.

No planned or `NOT_RUN` live-cloud output is required; only generated local validation evidence is inspected.
