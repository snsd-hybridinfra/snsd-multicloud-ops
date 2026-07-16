# S015-azure-nsg-least-privilege-validation

| Field | Value |
|---|---|
| Scenario ID | S015 |
| Scenario Name | Azure NSG Least Privilege Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Validation Type | Safe local repository validation |
| Evidence Directory | `evidence/L2-security-baseline/S015-azure-nsg-least-privilege-validation/` |
| Status | NOT_STARTED |

## Objective Summary

Validate the Azure NSG least-privilege baseline, rule matrix, Terraform structural placeholders, and repository safety without authenticating to Azure or modifying resources.

## Scope Summary

S015 reads local files only. It does not query live NSGs, run Azure CLI, run Terraform init/plan/apply, provision resources, validate provider credentials, or authenticate to Azure, Kubernetes, Docker registries, or any other external service.

## Related Components

- Azure NSG security baseline and example rule matrix.
- Azure network Terraform NSG and subnet-association placeholders.
- Local PowerShell validator and S015 evidence directory.

## Validation Summary

Thirteen checks validate required files and statements, logical NSGs, Terraform placeholders, dangerous public inbound rules, the public-web exception, egress justification, sensitive content, backend absence, and execution safety.

## Evidence Output Summary

The validator writes an ignored execution log and a tracked Markdown summary under the scenario evidence directory.
