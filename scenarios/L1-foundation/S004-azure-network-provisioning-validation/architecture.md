# Architecture

## Repository Components

- `terraform/modules/azure-network/`: reusable Azure resource definitions.
- `terraform/envs/azure-network-validation/`: local composition and non-production example values.
- `tools/validate-azure-network-provisioning.ps1`: repository-only safety and completeness checks.
- `evidence/L1-foundation/S004-azure-network-provisioning-validation/`: generated evidence.

## Defined Network Model

1. A resource group contains the validation resources.
2. One virtual network uses the example `10.20.0.0/16` address space.
3. Public-tier and private-tier subnets use `10.20.1.0/24` and `10.20.11.0/24`.
4. A baseline NSG is associated with both subnets; detailed rule validation remains in S015.
5. A route table is associated with both subnets; no production routes are declared.

## Validation Flow

The PowerShell validator reads repository files, checks expected Terraform resource types and safety boundaries, optionally runs formatting checks, and writes a log and summary. It does not initialize providers, authenticate, read credentials, create state, or contact Azure.
