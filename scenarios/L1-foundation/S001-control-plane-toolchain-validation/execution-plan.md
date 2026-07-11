# Execution Plan

## Preparation

1. Open PowerShell at the repository root.
2. Confirm `tools/validate-control-plane-toolchain.ps1` exists.
3. Confirm the S001 evidence directory is writable.

## Execution Steps

1. Run `powershell -ExecutionPolicy Bypass -File tools\validate-control-plane-toolchain.ps1`.
2. Review the console `PASS`, `WARN`, and `FAIL` lines.
3. Confirm the process exit code is zero when all core tools pass.
4. Treat later-stage warnings as readiness follow-ups, not S001 core failures.

## Evidence Capture

The script writes:

- `logs/control-plane-toolchain-validation.log`
- `configs/control-plane-toolchain-summary.md`

The operator then records the generated results in `validation.md`. No screenshot is required for this command-line scenario.
