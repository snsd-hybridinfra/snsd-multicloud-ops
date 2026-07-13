# Scope

## Included

- Review a reusable `aws-network` Terraform module placeholder.
- Review a local `aws-network-validation` environment placeholder.
- Validate required module and environment files.
- Validate VPC, subnet, route table, internet gateway, and security group resource block types.
- Validate the example variable file and approved non-production CIDRs.
- Detect real tfvars, tfstate, backend blocks, credentials, private keys, and account-ID patterns.
- Optionally run `terraform fmt -check` when Terraform is installed.

## Excluded

- AWS authentication, AWS CLI calls, or cloud API access.
- Terraform `init`, `validate`, `plan`, `apply`, or `destroy`.
- Provider configuration and validation, handled in S006.
- Security group least-privilege rules, handled in S014.
- Drift detection, handled in S041.
- Cost guardrails, handled in S045.
- Real AWS resources, account IDs, credentials, backend names, public addresses, tfstate, and real tfvars.

## Assumptions

- `terraform.tfvars.example` contains only documented non-production values.
- Provider initialization will occur only in a later explicitly authorized scenario.
