# Commands

Scenario: S009-dns-hostname-resolution-validation

Level: L1-foundation

## Run Validation

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-dns-hostname-resolution-model.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L1-foundation\S009-dns-hostname-resolution-validation\logs\dns-hostname-resolution-validation.log
Get-Content evidence\L1-foundation\S009-dns-hostname-resolution-validation\configs\dns-hostname-resolution-summary.md
```

## Safety Notes

No planned command queries DNS, connects to hosts, changes a resolver, authenticates to a cloud provider, or requires live network access. The validator reads repository text only.
