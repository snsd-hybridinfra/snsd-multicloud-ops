# Prerequisites

## Required Previous Scenarios

- `S001-control-plane-toolchain-validation` is planned and identifies Terraform CLI and OpenStack CLI readiness checks.
- `S002-eve-ng-onprem-routing-validation` is planned and documents the on-prem routing baseline.
- `S003-aws-network-provisioning-validation` and `S004-azure-network-provisioning-validation` are planned as cloud network validation counterparts.

## Required Tools

- Terraform CLI availability, as planned in S001.
- OpenStack CLI availability, as planned in S001.
- Access to repository documentation and evidence directories.

## Required Access Assumptions

- No OpenStack login is required for this skeleton.
- No `openrc` file, `clouds.yaml`, Terraform backend, tfvars, credentials, private keys, or tfstate files are required.
- Future execution requires explicit approval before any real OpenStack resource interaction.
