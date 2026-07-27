# Terraform Drift Remediation Policy — Non-Production Example

- Remediation must reference retired-numbered-case detection evidence.
- Critical drift requires approval before any remediation.
- Security drift requires rollback evidence; public exposure must not be silently accepted.
- Remediation execution and remediation validation are separate.
- Terraform state files and plan binaries must not be committed.
- Evidence must not contain credentials, backend values, account identifiers, or real resource identifiers.
- retired-numbered-case owns Policy as Code validation.
- retired-numbered-case owns cost guardrails when a proposal affects cost-bearing resources.
- This policy does not authorize Terraform, cloud API, or automatic remediation execution.
