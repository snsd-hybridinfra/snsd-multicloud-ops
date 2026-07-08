# S014-aws-security-group-least-privilege-validation

| Field | Value |
|---|---|
| Scenario ID | S014 |
| Scenario Name | AWS Security Group Least Privilege Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Primary Domain | AWS network security |
| Related Components | AWS Service Zone, AWS service node, Security Group, Bastion, On-Prem DB, monitoring targets |
| Validation Type | Security Validation |
| Evidence Directory | evidence/L2-security-baseline/S014-aws-security-group-least-privilege-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate the AWS Security Group least privilege model for the SNSD Multi-Cloud Ops AWS Service Zone.

## Scope Summary

This scenario validates AWS Security Group rule design only. It covers ingress, egress, bastion SSH access, service exposure placeholders, app-to-database access placeholders, monitoring scrape placeholders, and denial of unrestricted SSH or DB access.

## Validation Summary

Validation checks confirm that AWS Security Group rules are intentionally scoped, that SSH and DB access are not exposed broadly, and that rule evidence can be captured through Terraform plan output or AWS CLI review without adding credentials or account-specific values.

## Evidence Output Summary

Evidence must be recorded under `evidence/L2-security-baseline/S014-aws-security-group-least-privilege-validation/`, with command plans in `commands.md`, validation results in `validation.md`, and future sanitized supporting artifacts under `configs/`, `logs/`, and `screenshots/`.
