# Architecture

## Relevant Components

- Terraform module: `terraform/modules/aws-network/`
- Validation environment: `terraform/envs/aws-network-validation/`
- Placeholder resources: VPC, two subnets, two route tables, internet gateway, security group
- Repository validator and generated S003 evidence

## Logical Flow

1. The module defines AWS resource structure through variables and outputs.
2. The environment references the local module and supplies only example values.
3. The PowerShell validator reads the repository files and safety constraints.
4. Terraform formatting is checked only when the CLI is locally available.
5. Results are written to the matching S003 evidence directory.

## Out-of-Scope Components

AWS accounts, provider credentials, remote backends, state, plans, live resources, AWS CLI, Ansible, and Kubernetes are not accessed.
