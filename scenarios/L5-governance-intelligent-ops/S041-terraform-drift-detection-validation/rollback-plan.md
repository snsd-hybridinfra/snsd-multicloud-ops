# Rollback Plan

1. Stop drift detection validation if real credentials, secrets, cloud account values, tfstate, private keys, kubeconfig, or account-specific values appear in commands or evidence.
2. Remove or sanitize unsafe Terraform evidence from `commands.md`, `validation.md`, `configs/`, `logs/`, and `screenshots/`.
3. Recheck that only placeholders such as `<terraform-env>`, `<provider>`, `<resource-name>`, `<drifted-resource>`, `<expected-state>`, and `<actual-state>` remain.
4. Mark S041 as `BLOCKED` if Terraform baseline, plan output, or drift judgment cannot be safely documented.
5. Preserve a short note in `docs/implementation-log.md` if rollback or sanitization is required.

No Terraform modules, real Terraform runs, tfstate, provider credentials, remediation workflow, or external IaC governance integration is created by this documentation skeleton.
