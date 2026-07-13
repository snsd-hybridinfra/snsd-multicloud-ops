# Execution Plan

## Preparation

1. Open PowerShell at the repository root.
2. Confirm the module, environment, and S003 evidence directories exist.
3. Confirm no real variable or state files have been added.

## Execution Steps

1. Run `powershell -ExecutionPolicy Bypass -File tools\validate-aws-network-provisioning.ps1`.
2. Review all `PASS`, `WARN`, and `FAIL` lines.
3. Confirm Terraform absence produces only a formatting warning.
4. Confirm provider-dependent validation is skipped rather than initialized.
5. Review generated evidence.

## Evidence Capture

The script writes:

- `logs/aws-network-provisioning-validation.log`
- `configs/aws-network-provisioning-summary.md`

No screenshot, AWS output, plan, or state evidence is required.
