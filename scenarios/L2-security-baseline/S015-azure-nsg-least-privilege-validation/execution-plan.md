# Execution Plan

1. Confirm the scenario evidence directory exists for S015.
2. Identify the placeholder Azure NSG target as `<azure-nsg-name>`.
3. Record the planned NSG rule capture method using Terraform plan output or Azure CLI read-only output.
4. Review the planned SSH inbound rule and confirm it is restricted to `<bastion-cidr>`.
5. Review HTTP and HTTPS inbound placeholders and confirm each exposed service port has an operational purpose.
6. Review DB port `3306` rules and confirm Internet or unrestricted exposure is denied.
7. Review the Azure App-to-On-Prem DB placeholder rule and confirm it uses `<onprem-db-cidr>`.
8. Review the monitoring scrape placeholder rule and confirm it uses `<monitoring-cidr>`.
9. Review all inbound rules for unrestricted SSH, unrestricted DB access, or all-ports inbound access.
10. Review outbound rules and document whether they are role-specific or require later tightening.
11. Record TODO placeholders in evidence files until approved execution produces sanitized output.

## Execution Boundaries

This plan does not create, modify, or delete Azure resources. It only defines the review flow and evidence requirements for later approved validation.
