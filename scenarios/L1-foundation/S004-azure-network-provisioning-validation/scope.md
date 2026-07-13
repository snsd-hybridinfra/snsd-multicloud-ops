# Scope

## Included

- Azure resource group Terraform definition.
- Virtual network and two subnet definitions.
- Baseline network security group and subnet associations.
- Route table and subnet associations.
- Safe non-production example CIDRs and `koreacentral` location.
- Local checks for required files, resource blocks, unsafe files, backend blocks, identity assignments, and credential-like content.
- Optional `terraform fmt -check` when Terraform is locally available.
- Generated local log and Markdown summary evidence.

## Excluded

- Azure authentication and Azure CLI execution.
- Provider initialization or download.
- `terraform init`, `validate`, `plan`, `apply`, or `destroy` execution.
- Real variable files, backend configuration, state, identity IDs, credentials, or account-specific values.
- Real Azure resource creation, modification, lookup, or deletion.
- Public IP, bastion, compute, production routing, or production NSG rules.
- Terraform provider validation, which belongs to S006.
- Azure NSG least-privilege validation, which belongs to S015.

## Assumptions

- Definitions are non-production repository artifacts only.
- Later provider or cloud execution requires a separately approved scenario.
