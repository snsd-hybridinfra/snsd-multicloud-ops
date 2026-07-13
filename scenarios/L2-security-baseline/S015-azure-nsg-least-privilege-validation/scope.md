# Scope

## Included

- Azure NSG baseline and non-production rule matrix validation.
- Default-deny, explicit-allow, public-web exception, internal access, and egress policy checks.
- Local inspection of Azure Terraform NSG and association placeholders.
- Dangerous public inbound detection for ports 22, 3389, 3306, 5432, 6379, 9200, 5601, 9090, and 3000.
- Sensitive-content, public-address, state, tfvars, backend, and execution-boundary checks.

## Excluded

- Azure authentication, Azure CLI, cloud API calls, and live NSG queries.
- Terraform init, plan, apply, destroy, backend, state, or real variables.
- Azure resource creation or modification.
- Azure network provisioning (S004), provider validation (S006), SSH controls (S011-S013), AWS Security Groups (S014), and OpenStack Security Groups (S016).
