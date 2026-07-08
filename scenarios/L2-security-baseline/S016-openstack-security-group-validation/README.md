# S016-openstack-security-group-validation

| Field | Value |
|---|---|
| Scenario ID | S016 |
| Scenario Name | OpenStack Security Group Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Primary Domain | OpenStack network security |
| Related Components | OpenStack Private Cloud Service Zone, OpenStack App VM, Security Group, Bastion, On-Prem DB, monitoring targets |
| Validation Type | Security Validation |
| Evidence Directory | evidence/L2-security-baseline/S016-openstack-security-group-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate the OpenStack Security Group least privilege model for the SNSD Multi-Cloud Ops OpenStack Private Cloud Service Zone.

## Scope Summary

This scenario validates OpenStack Security Group rule design only. It covers service VM ingress, service VM egress, bastion SSH access, HTTP/HTTPS service exposure placeholders, App VM to On-Prem DB placeholders, monitoring scrape placeholders, and denial of unrestricted SSH or DB access.

## Validation Summary

Validation checks confirm that OpenStack Security Group rules are intentionally scoped, that SSH and DB access are not exposed broadly, and that rule evidence can be captured through Terraform plan output or OpenStack CLI review without adding credentials or account-specific values.

## Evidence Output Summary

Evidence must be recorded under `evidence/L2-security-baseline/S016-openstack-security-group-validation/`, with command plans in `commands.md`, validation results in `validation.md`, and future sanitized supporting artifacts under `configs/`, `logs/`, and `screenshots/`.
