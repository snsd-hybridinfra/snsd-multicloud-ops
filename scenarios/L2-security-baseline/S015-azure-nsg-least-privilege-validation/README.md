# S015-azure-nsg-least-privilege-validation

| Field | Value |
|---|---|
| Scenario ID | S015 |
| Scenario Name | Azure NSG Least Privilege Validation |
| Level | L2 Security Baseline Validation |
| Category | Security Baseline |
| Primary Domain | Azure network security |
| Related Components | Azure Service Zone, Azure App Node, Network Security Group, Bastion, On-Prem DB, monitoring targets |
| Validation Type | Security Validation |
| Evidence Directory | evidence/L2-security-baseline/S015-azure-nsg-least-privilege-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate the Azure Network Security Group least privilege model for the SNSD Multi-Cloud Ops Azure Service Zone.

## Scope Summary

This scenario validates Azure NSG rule design only. It covers inbound rules, outbound rules, bastion SSH access, HTTP/HTTPS service exposure placeholders, App Node to On-Prem DB placeholders, monitoring scrape placeholders, and denial of unrestricted SSH or DB access.

## Validation Summary

Validation checks confirm that Azure NSG rules are intentionally scoped, that SSH and DB access are not exposed broadly, and that rule evidence can be captured through Terraform plan output or Azure CLI review without adding credentials or account-specific values.

## Evidence Output Summary

Evidence must be recorded under `evidence/L2-security-baseline/S015-azure-nsg-least-privilege-validation/`, with command plans in `commands.md`, validation results in `validation.md`, and future sanitized supporting artifacts under `configs/`, `logs/`, and `screenshots/`.
