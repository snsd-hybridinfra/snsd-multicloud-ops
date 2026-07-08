# Prerequisites

## Required Previous Scenarios

- `S001-control-plane-toolchain-validation` is planned and identifies Terraform CLI and Azure CLI readiness checks.
- `S002-eve-ng-onprem-routing-validation` is planned and documents the on-prem routing baseline that may later connect to cloud networks.
- `S003-aws-network-provisioning-validation` is planned as the AWS baseline network counterpart.

## Required Tools

- Terraform CLI availability, as planned in S001.
- Azure CLI availability, as planned in S001.
- Access to repository documentation and evidence directories.

## Required Access Assumptions

- No Azure login is required for this skeleton.
- No Terraform backend, tfvars, credentials, subscription IDs, tenant IDs, private keys, or tfstate files are required.
- Future execution requires explicit approval before any real Azure resource interaction.
