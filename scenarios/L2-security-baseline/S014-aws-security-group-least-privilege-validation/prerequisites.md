# Prerequisites

## Required Previous Scenarios

- S001-control-plane-toolchain-validation: confirms local toolchain planning.
- S003-aws-network-provisioning-validation: defines the AWS baseline network model.
- S007-multi-cloud-inventory-validation: defines placeholder node and target inventory.
- S008-bastion-reachability-validation: defines the bastion reachability model.

## Required Tools or References

- Terraform CLI plan review capability, when future implementation exists.
- AWS CLI rule review capability, when future credentials are approved outside this repository.
- AWS Security Group naming and placeholder conventions from repository naming rules.
- Evidence model from `docs/evidence-model.md`.

## Safety Preconditions

- Do not add AWS credentials, account IDs, access keys, tfstate, private keys, or account-specific values.
- Do not record real public IPs.
- Do not execute live AWS changes as part of this scenario skeleton.
