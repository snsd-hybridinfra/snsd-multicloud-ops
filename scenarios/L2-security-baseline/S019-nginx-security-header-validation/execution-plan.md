# Execution Plan

1. Run `tools/validate-nginx-security-header-baseline.ps1` from the repository root.
2. Confirm the baseline, rule matrix, and non-production config.
3. Validate `server_tokens off`, all six headers, exact values/placeholders, and `always`.
4. Confirm the legacy compatibility note, evidence model, and static-validation limitations.
5. Reject TLS key/certificate paths, private material, real domains, numeric addresses, credentials, and identifiers.
6. Confirm the validator contains no Nginx, curl, host, or network command.
7. Review generated log and summary.

## Execution Boundary

The script does not run or reload Nginx, change configuration, curl a service, connect to a host, or validate live HTTP/TLS behavior.
