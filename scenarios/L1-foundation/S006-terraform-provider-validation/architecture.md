# Architecture

## Relevant Components

- AWS provider role: validates AWS provisioning capability for future AWS network scenarios without storing credentials.
- AzureRM provider role: validates Azure provisioning capability for future Azure network scenarios without storing subscription or tenant identifiers.
- OpenStack provider role: validates OpenStack provisioning capability for future OpenStack network scenarios without storing `openrc`, `clouds.yaml`, or credentials.
- Provider version pinning: keeps provider behavior reviewable and repeatable.
- Environment separation: keeps provider configuration isolated by environment or platform boundary.
- `.gitignore` tfstate policy: prevents generated Terraform state from entering the repository.

## Logical Flow

1. Terraform CLI availability is confirmed as a prerequisite.
2. Provider structure is reviewed for AWS, AzureRM, and OpenStack separation.
3. Provider version constraints are checked for each provider family.
4. Terraform fmt, init, and validate plans are documented for future safe execution.
5. Credential hardcoding and tfstate commit controls are reviewed.

## Out-of-Scope Components

No provider credentials, backend state, cloud authentication, Terraform state, private keys, live resources, or account-specific values are used by this scenario.
