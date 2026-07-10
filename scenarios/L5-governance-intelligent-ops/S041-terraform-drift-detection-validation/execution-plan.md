# Execution Plan

1. Confirm that only placeholder Terraform environments, providers, resource names, and states are used.
2. Validate the Terraform working directory placeholder for `<terraform-env>`.
3. Review Terraform backend placeholder expectations without real backend values.
4. Review Terraform provider placeholder expectations without credentials.
5. Plan `terraform init` placeholder validation.
6. Plan `terraform validate` placeholder validation.
7. Plan `terraform plan` output review for drift detection.
8. Map AWS, Azure, and OpenStack drift placeholders.
9. Map security rule drift and tag or label drift placeholders.
10. Classify drift using `NO_DRIFT`, `DRIFT_DETECTED`, `INCONCLUSIVE`, or `OUT_OF_SCOPE`.
11. Capture future command, log, screenshot, and config summary evidence.
12. Record future validation results in `validation.md`.
