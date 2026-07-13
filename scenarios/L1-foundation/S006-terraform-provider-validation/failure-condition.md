# Failure Condition

## Critical Failure Conditions

- The provider directory or a required file is missing.
- `required_version`, `required_providers`, an expected provider source, version constraint, or provider block is missing.
- A real tfvars, auto tfvars, tfstate, or `.terraform` artifact is present.
- A backend block is configured.
- A credential, private key, access key, UUID-like identifier, account-specific assignment, or secret is detected.
- Required safety-boundary documentation is missing.
- The validator attempts provider initialization, download, authentication, runtime validation, planning, or apply.

## Non-Critical Warnings

- Terraform is unavailable for formatting checks.
- Runtime provider validation is skipped because initialization, download, and authentication are prohibited.

Critical failures produce a non-zero exit. Warnings remain documented without weakening the safety boundary.
