# Terraform Drift Detection Policy — Non-Production Example

- Drift detection must be evidence-based and sanitized.
- Evidence must not contain credentials, tokens, backend values, account identifiers, or real resource identifiers.
- Terraform state files and Terraform plan binaries must not be committed.
- Drift detection and remediation are separate; remediation is handled in S042.
- Security-related drift must be escalated.
- Public exposure drift is Critical or High; tag-only drift may be lower severity.
- Policy as Code validation is handled in S043.
- This policy does not authorize Terraform or cloud API execution.
