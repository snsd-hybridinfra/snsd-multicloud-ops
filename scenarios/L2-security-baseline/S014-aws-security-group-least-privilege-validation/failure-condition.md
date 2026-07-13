# Failure Condition

## Critical Failure Conditions

- A required baseline, matrix, placeholder group, policy statement, or Terraform Security Group placeholder is missing.
- Inbound `0.0.0.0/0` is paired with SSH, RDP, database, admin, or monitoring ports.
- A public inbound row is not HTTP/HTTPS on the public web placeholder.
- Egress lacks documentation or justification.
- A real tfvars, state, backend, credential, key, account ID, secret, or real public IP is detected.
- The validator contains or executes AWS CLI, Terraform mutation, or network access.
- Documentation implies that the matrix proves deployed cloud state.

Any critical failure produces a non-zero exit and must be documented without exposing unsafe content.
