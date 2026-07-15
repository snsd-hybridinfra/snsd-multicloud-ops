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

## Real Virtual-Lab Command Patterns

The following placeholders document the operator-provided lab workflow. These
commands were not executed by the repository validator.

```text
ssh <ssh-user-placeholder>@<db-primary-ip-placeholder>
systemctl is-active mariadb
mariadb --version
ss -lntp
SHOW GRANTS FOR '<application-user-placeholder>'@'<client-host-placeholder>';
SHOW GRANTS FOR '<readonly-user-placeholder>'@'<client-host-placeholder>';
mariadb -h <db-primary-ip-placeholder> -u <database-user-placeholder> -p <database-placeholder>
SELECT <approved-columns-placeholder> FROM <database-placeholder>.<table-placeholder>;
INSERT INTO <database-placeholder>.<table-placeholder> (...) VALUES (...); -- denial test for read-only account
CREATE TABLE <database-placeholder>.<table-placeholder> (...); -- denial test for read-only account
CREATE USER '<unauthorized-user-placeholder>'@'<client-host-placeholder>'; -- denial test; no credential clause
```

Passwords must be entered interactively and must never be recorded. Do not add
password command-line arguments, authentication strings, password hashes, or
credential-bearing CREATE USER statements.

Inspect the sanitized records:

```powershell
Get-Content evidence/L2-security-baseline/S017-mariadb-access-control-validation/logs/20260715-S017-mariadb-service-listener.sanitized.txt
Get-Content evidence/L2-security-baseline/S017-mariadb-access-control-validation/logs/20260715-S017-mariadb-grants.sanitized.txt
Get-Content evidence/L2-security-baseline/S017-mariadb-access-control-validation/logs/20260715-S017-readonly-allow-deny.sanitized.txt
Get-Content evidence/L2-security-baseline/S017-mariadb-access-control-validation/logs/20260715-S017-application-user-allow-deny.sanitized.txt
Get-Content evidence/L2-security-baseline/S017-mariadb-access-control-validation/configs/20260715-S017-mariadb-access-control-validation-summary.md
```
