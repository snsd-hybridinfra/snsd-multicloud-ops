# Commands

Scenario: S019-nginx-security-header-validation

Level: L2-security-baseline

## Run Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-nginx-security-header-baseline.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L2-security-baseline\S019-nginx-security-header-validation\logs\nginx-security-header-validation.log
Get-Content evidence\L2-security-baseline\S019-nginx-security-header-validation\configs\nginx-security-header-summary.md
```

## Safety Notes

These commands do not run or reload Nginx, modify configuration, curl services, connect to hosts, access TLS material, or require network access. No planned or `NOT_RUN` live-response output is required.
