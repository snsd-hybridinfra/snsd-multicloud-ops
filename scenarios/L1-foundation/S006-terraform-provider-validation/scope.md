# Scope

## Included

- Terraform CLI availability validation plan.
- Terraform fmt validation plan.
- Terraform init plan for AWS provider.
- Terraform init plan for AzureRM provider.
- Terraform init plan for OpenStack provider.
- Terraform validate plan for each provider environment.
- Provider version pinning check.
- Provider separation by environment.
- Provider credential hardcoding check.
- tfstate exclusion check.
- Failure condition for missing provider, invalid provider version, or credential exposure.

## Excluded

- Real Terraform provider credentials.
- AWS credentials, Azure credentials, OpenStack credentials, private keys, tfstate files, or account-specific files.
- Real cloud provider authentication.
- Terraform plan, apply, destroy, or state operations against a real environment.
- New technologies outside the locked repository scope.

## Assumptions

- Provider configuration is represented with placeholders such as `<aws-region>`, `<azure-subscription-id-redacted>`, and `<openstack-cloud-name>`.
- Future provider initialization may be tested in isolated validation directories only after explicit approval.
- Any future command output must be sanitized before commit.
