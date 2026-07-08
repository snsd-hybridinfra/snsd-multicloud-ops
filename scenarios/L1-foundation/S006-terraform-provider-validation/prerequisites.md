# Prerequisites

## Required Previous Scenarios

- `S001-control-plane-toolchain-validation` is planned and identifies Terraform CLI readiness.
- `S003-aws-network-provisioning-validation` is planned as the AWS provider consumer.
- `S004-azure-network-provisioning-validation` is planned as the AzureRM provider consumer.
- `S005-openstack-network-provisioning-validation` is planned as the OpenStack provider consumer.

## Required Tools

- Terraform CLI availability, as planned in S001.
- Repository access for reviewing Terraform directory structure and `.gitignore`.
- Text editor for evidence documentation.

## Required Access Assumptions

- No cloud login is required for this skeleton.
- No Terraform backend, tfvars, credentials, private keys, or tfstate files are required.
- Future provider validation requires explicit approval before running commands that download providers or touch local `.terraform/` directories.
