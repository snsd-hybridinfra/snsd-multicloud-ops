# Commands

Scenario: S002-eve-ng-on-prem-routing-validation

Level: L1-foundation

Target: repository-side EVE-NG routing baseline

## Run Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-eve-ng-routing-baseline.ps1
```

## Inspect Generated Log

```powershell
Get-Content evidence\L1-foundation\S002-eve-ng-on-prem-routing-validation\logs\eve-ng-routing-baseline-validation.log
```

## Inspect Generated Summary

```powershell
Get-Content evidence\L1-foundation\S002-eve-ng-on-prem-routing-validation\configs\eve-ng-routing-baseline-summary.md
```

## Safety Notes

No planned command authenticates to EVE-NG, uses its API, connects to routers, reads credentials, accesses cloud accounts, reads kubeconfig, or accesses tfstate.
