# Architecture

This scenario models Terraform drift detection as a plan-output and evidence-review workflow. It does not create Terraform providers, backends, state, or cloud resources.

## Relevant Components

- Terraform environment placeholder: `<terraform-env>`.
- Provider placeholder: `<provider>`.
- Resource name placeholder: `<resource-name>`.
- Drifted resource placeholder: `<drifted-resource>`.
- Expected state placeholder: `<expected-state>`.
- Actual state placeholder: `<actual-state>`.
- Evidence store: `evidence/L5-governance-intelligent-ops/S041-terraform-drift-detection-validation/`.

## Drift Detection Flow

1. Validate the Terraform working directory placeholder.
2. Review backend and provider placeholders without real credentials.
3. Plan `terraform init`, `terraform validate`, and `terraform plan` as placeholder command flow.
4. Compare expected and actual resource state through planned Terraform output.
5. Classify drift using the judgment model.
6. Capture sanitized command, log, screenshot, and summary evidence.

This scenario stops at detection. Remediation is handled in S042.
