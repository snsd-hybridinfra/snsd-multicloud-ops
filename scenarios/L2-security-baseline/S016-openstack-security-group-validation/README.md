# S016-openstack-security-group-validation

| Field | Value |
|---|---|
| Scenario ID | S016 |
| Scenario Name | OpenStack Security Group Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Related Components | OpenStack Security Group policy, rule matrix, Terraform placeholders, local validator |
| Validation Type | Safe local repository validation |
| Evidence Directory | `evidence/L2-security-baseline/S016-openstack-security-group-validation/` |
| Status | NOT_STARTED |

## Objective Summary

Validate the OpenStack Security Group least-privilege baseline, rule matrix, Terraform placeholders, and repository safety without authenticating to OpenStack or modifying resources.

## Scope Summary

S016 reads local files only. It does not query live Security Groups, run OpenStack CLI, run Terraform init/plan/apply, provision resources, validate provider credentials, or authenticate to any external service.

## Validation Summary

Fourteen checks validate required policy artifacts, logical groups, Terraform resources, dangerous public ingress, public-web exceptions, egress justification, forbidden configuration files, sensitive content, backend absence, and execution safety.

## Evidence Output Summary

The validator writes an ignored execution log and a tracked sanitized Markdown summary under the S016 evidence directory.
