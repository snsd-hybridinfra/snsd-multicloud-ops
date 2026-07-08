# Prerequisites

## Required Previous Scenarios

- S001-control-plane-toolchain-validation: confirms local toolchain planning.
- S004-azure-network-provisioning-validation: defines the Azure baseline network model.
- S007-multi-cloud-inventory-validation: defines placeholder node and target inventory.
- S008-bastion-reachability-validation: defines the bastion reachability model.

## Required Tools or References

- Terraform CLI plan review capability, when future implementation exists.
- Azure CLI NSG rule review capability, when future credentials are approved outside this repository.
- Azure NSG naming and placeholder conventions from repository naming rules.
- Evidence model from `docs/evidence-model.md`.

## Safety Preconditions

- Do not add Azure credentials, subscription IDs, tenant IDs, tfstate, private keys, or account-specific values.
- Do not record real public IPs.
- Do not execute live Azure changes as part of this scenario skeleton.
