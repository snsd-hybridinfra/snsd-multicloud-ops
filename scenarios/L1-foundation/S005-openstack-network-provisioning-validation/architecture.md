# Architecture

## Repository Components

- `terraform/modules/openstack-network/`: reusable OpenStack network definitions.
- `terraform/envs/openstack-network-validation/`: local composition and non-production example values.
- `tools/validate-openstack-network-provisioning.ps1`: repository-only safety and completeness checks.
- `evidence/L1-foundation/S005-openstack-network-provisioning-validation/`: generated evidence.

## Defined Network Model

1. A private network represents the validation tenant network.
2. A private subnet uses `10.30.11.0/24` within the documented `10.30.0.0/16` plan.
3. A router references `<external-network-name>` without resolving it.
4. A router interface connects the private subnet to the router definition.
5. A baseline security group contains a management-rule placeholder restricted to `10.30.1.0/24`; detailed validation remains in S016.

## Validation Flow

The PowerShell validator reads repository files, checks expected Terraform resource types and safety boundaries, optionally runs formatting checks, and writes a log and summary. It does not initialize providers, authenticate, read `clouds.yaml` or openrc, create state, or contact OpenStack.
