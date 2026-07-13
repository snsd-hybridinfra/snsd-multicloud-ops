# Commands

Scenario: S020-grafana-anonymous-access-denial-validation

Level: L2-security-baseline

## Run Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-grafana-anonymous-access-denial.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L2-security-baseline\S020-grafana-anonymous-access-denial-validation\logs\grafana-anonymous-access-denial-validation.log
Get-Content evidence\L2-security-baseline\S020-grafana-anonymous-access-denial-validation\configs\grafana-anonymous-access-denial-summary.md
```

## Safety Notes

These commands do not run Grafana, start containers, curl endpoints, connect to hosts, read environment secrets or credentials, or validate live login. No planned or `NOT_RUN` live-instance output is required.
