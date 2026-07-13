# Execution Plan

1. Run `tools/validate-openstack-security-group-baseline.ps1` from the repository root.
2. Confirm policy, matrix, logical groups, required statements, and Terraform placeholders.
3. Scan repository-side OpenStack inputs for unsafe state, variables, configuration files, credentials, identity values, secrets, and public addresses.
4. Parse the matrix and reject public administrative, database, or monitoring ports.
5. Confirm that only ports 80 and 443 on `openstack-public-web-sg` use public ingress.
6. Confirm egress justification, absence of a backend, and execution safety.
7. Review the generated log and summary.

## Execution Boundary

The script does not authenticate to OpenStack, invoke OpenStack CLI, query Security Groups, or run Terraform init, plan, apply, or destroy.
