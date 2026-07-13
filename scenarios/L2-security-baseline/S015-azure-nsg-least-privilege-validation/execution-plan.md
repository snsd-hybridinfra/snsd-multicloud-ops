# Execution Plan

1. Run `tools/validate-azure-nsg-least-privilege.ps1` from the repository root.
2. Confirm policy, matrix, logical NSGs, required statements, and Terraform placeholders.
3. Scan repository-side Azure inputs for unsafe state, variables, credentials, identity values, secrets, and public addresses.
4. Parse the matrix and reject public administrative, database, or monitoring ports.
5. Confirm that only ports 80 and 443 on `azure-public-web-nsg` use public inbound exposure.
6. Confirm egress justification, absence of a backend, and execution safety.
7. Review the generated log and summary.

## Execution Boundary

The script does not authenticate to Azure, invoke Azure CLI, query NSGs, or run Terraform init, plan, apply, or destroy.
