# Execution Plan

1. Confirm the scenario evidence directory exists for S014.
2. Identify the placeholder AWS Security Group target as `<aws-security-group-id>`.
3. Record the planned Security Group rule capture method using Terraform plan output or AWS CLI read-only output.
4. Review the planned SSH ingress rule and confirm it is restricted to `<bastion-cidr>`.
5. Review HTTP and HTTPS ingress placeholders and confirm each exposed service port has an operational purpose.
6. Review DB port `3306` rules and confirm public internet exposure is denied.
7. Review the App Node to On-Prem DB placeholder rule and confirm it uses `<onprem-db-cidr>`.
8. Review the monitoring scrape placeholder rule and confirm it uses `<monitoring-cidr>`.
9. Review all ingress rules for unrestricted SSH, unrestricted DB access, or all-ports ingress.
10. Review egress rules and document whether they are role-specific or require later tightening.
11. Record TODO placeholders in evidence files until approved execution produces sanitized output.

## Execution Boundaries

This plan does not create, modify, or destroy AWS resources. It only defines the review flow and evidence requirements for later approved validation.
