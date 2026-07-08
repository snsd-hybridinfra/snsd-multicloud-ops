# Objective

Validate the planned Terraform provider structure required for AWS, Azure, and OpenStack provisioning.

The scenario defines validation for:

- AWS provider validation plan
- AzureRM provider validation plan
- OpenStack provider validation plan
- Provider version pinning strategy
- Provider separation by environment
- Terraform init validation plan
- Terraform validate validation plan
- Terraform fmt validation plan
- No credential hardcoding
- No tfstate commit policy

Success means the repository has a clear, evidence-mapped plan for validating Terraform provider structure without storing AWS credentials, Azure credentials, OpenStack credentials, tfstate, private keys, or account-specific files.
