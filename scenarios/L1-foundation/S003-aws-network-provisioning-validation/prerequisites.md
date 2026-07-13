# Prerequisites

## Required Previous Scenarios

- S001 records Terraform as a later-stage warning, but Terraform absence does not block S003 repository checks.
- S002 defines the repository-side on-prem routing baseline; S003 does not test connectivity to it.

## Required Tools

- PowerShell
- Local repository read access
- Write access to the S003 evidence directory
- Terraform is optional and used only for `fmt -check`

## Required Access Assumptions

- No AWS login, provider credential, backend, tfstate, real tfvars, or cloud resource access is required.
