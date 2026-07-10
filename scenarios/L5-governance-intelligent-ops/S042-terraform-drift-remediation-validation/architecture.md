# Architecture

S042 models a controlled Terraform remediation review flow.

## Components

- Terraform environment placeholder: `<terraform-env>`.
- Provider placeholder: `<provider>`.
- Drifted resource placeholder: `<drifted-resource>`.
- Expected state placeholder: `<expected-state>`.
- Actual state placeholder: `<actual-state>`.
- Remediation plan placeholder: `<remediation-plan>`.
- Evidence directory: `evidence/L5-governance-intelligent-ops/S042-terraform-drift-remediation-validation/`.

## Flow

1. Review prior S041 drift detection evidence.
2. Identify the Terraform-managed resource affected by drift.
3. Compare expected state, actual state, and remediation plan placeholders.
4. Review Terraform plan output placeholder before remediation.
5. Record a manual approval placeholder.
6. Document Terraform apply placeholder behavior.
7. Review post-remediation plan placeholder.
8. Classify remediation judgment state.
9. Store sanitized evidence.

This architecture is evidence and governance documentation only. It does not create infrastructure or execute Terraform.
