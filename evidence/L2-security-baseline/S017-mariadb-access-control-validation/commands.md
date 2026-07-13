# Commands

Scenario: S017-mariadb-access-control-validation

Level: L2-security-baseline

## Run Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-mariadb-access-control-baseline.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L2-security-baseline\S017-mariadb-access-control-validation\logs\mariadb-access-control-validation.log
Get-Content evidence\L2-security-baseline\S017-mariadb-access-control-validation\configs\mariadb-access-control-summary.md
```

## Safety Notes

These commands do not connect to MariaDB, execute SQL, invoke a database client, read credentials, modify users or grants, create dumps, or contact external systems. No planned or `NOT_RUN` live-database output is required.
