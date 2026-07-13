# Architecture

## Repository Components

- `terraform/envs/provider-validation/versions.tf`: Terraform and provider source/version constraints.
- `terraform/envs/provider-validation/providers.tf`: non-authenticating provider blocks.
- `terraform/envs/provider-validation/README.md`: provider safety boundary.
- `tools/validate-terraform-provider-baseline.ps1`: repository-only validation.
- `evidence/L1-foundation/S006-terraform-provider-validation/`: generated evidence.

## Provider Model

1. AWS uses the `hashicorp/aws` source with an explicit bounded version range.
2. AzureRM uses the `hashicorp/azurerm` source with an explicit bounded version range and an empty `features` block.
3. OpenStack uses the `terraform-provider-openstack/openstack` source with an explicit bounded version range.
4. Provider blocks contain no authentication or account values.

## Validation Flow

The PowerShell validator reads local files, checks declaration completeness and safety boundaries, optionally runs formatting checks, and writes a log and summary. It does not initialize or validate providers, download plugins, authenticate, create state, or contact external systems.
