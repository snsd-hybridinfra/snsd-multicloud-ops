# S014-aws-security-group-least-privilege-validation

| Field | Value |
|---|---|
| Scenario ID | S014 |
| Scenario Name | AWS Security Group Least Privilege Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Primary Domain | Repository-side AWS Security Group least-privilege baseline |
| Related Components | Rule policy, rule matrix, AWS Terraform Security Group placeholder |
| Validation Type | Security Validation |
| Evidence Directory | evidence/L2-security-baseline/S014-aws-security-group-least-privilege-validation/ |
| Status | VALIDATED |

## Objective Summary

Validate least-privilege AWS Security Group expectations and Terraform placeholders without authenticating to AWS or querying and modifying real resources.

## Scope Summary

S014 checks baseline files, five placeholder groups, policy statements, Terraform placeholder and artifact safety, credentials and addresses, dangerous public inbound rows, public-web exceptions, egress justification, backend absence, and execution safety.

## Related Components

- `security-baseline/aws-security-group-least-privilege-baseline.md`
- `security-baseline/aws-security-group-rule-matrix.example.md`
- `terraform/modules/aws-network/main.tf`
- `tools/validate-aws-security-group-least-privilege.ps1`

## Validation Summary

Only public web ports 80 and 443 may use public inbound exposure in the matrix. SSH, RDP, database, administration, and monitoring ports must use placeholders restricted from `0.0.0.0/0`.

## Evidence Output Summary

- `logs/aws-security-group-least-privilege-validation.log`
- `configs/aws-security-group-least-privilege-summary.md`
- `commands.md`
- `validation.md`
