# Execution Plan

## Preparation

1. Review S001 Terraform CLI readiness.
2. Confirm this scenario is documentation and evidence planning only.
3. Confirm no AWS, Azure, or OpenStack credentials are present or required.
4. Confirm no tfstate, private keys, backend files, or account-specific files are created.
5. Confirm the S006 evidence directory exists.

## Execution Steps

1. Define the Terraform CLI availability validation plan.
2. Define the Terraform fmt validation plan.
3. Define the Terraform init plan for AWS provider.
4. Define the Terraform init plan for AzureRM provider.
5. Define the Terraform init plan for OpenStack provider.
6. Define Terraform validate checks for each provider environment.
7. Define provider version pinning checks.
8. Define provider credential hardcoding checks.
9. Define tfstate exclusion checks.
10. Define failure conditions for missing provider, invalid provider version, or credential exposure.

## Evidence Capture

1. Record planned commands and placeholders in `commands.md`.
2. Record validation checks and TODO results in `validation.md`.
3. Map provider structure evidence to `configs/terraform-provider-structure-summary.md`.
4. Map Terraform command evidence to `logs/terraform-provider-validation.log`.
5. Map tfstate ignore evidence to `configs/gitignore-tfstate-check.md`.
