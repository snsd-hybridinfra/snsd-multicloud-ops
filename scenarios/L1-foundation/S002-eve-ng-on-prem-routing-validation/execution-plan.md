# Execution Plan

## Preparation

1. Open PowerShell at the repository root.
2. Confirm the topology and router example directories are present.
3. Confirm the S002 evidence directory is writable.

## Execution Steps

1. Run `powershell -ExecutionPolicy Bypass -File tools\validate-eve-ng-routing-baseline.ps1`.
2. Review each `PASS`, `WARN`, or `FAIL` console line.
3. Confirm the script does not initiate any remote connection.
4. Review the generated log and summary.

## Evidence Capture

The script generates:

- `logs/eve-ng-routing-baseline-validation.log`
- `configs/eve-ng-routing-baseline-summary.md`

No screenshot or live routing output is required.
