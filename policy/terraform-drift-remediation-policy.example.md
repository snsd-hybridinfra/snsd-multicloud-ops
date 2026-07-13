# Terraform Drift Remediation Policy — Non-Production Example

- Remediation must reference S041 detection evidence.
- Critical drift requires approval before any remediation.
- Security drift requires rollback evidence; public exposure must not be silently accepted.
- Remediation execution and remediation validation are separate.
- Terraform state files and plan binaries must not be committed.
- Evidence must not contain credentials, backend values, account identifiers, or real resource identifiers.
- S043 owns Policy as Code validation.
- S045 owns cost guardrails when a proposal affects cost-bearing resources.
- This policy does not authorize Terraform, cloud API, or automatic remediation execution.
