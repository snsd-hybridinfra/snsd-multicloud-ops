# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Azure NSG existence validation plan | Document read-only lookup or Terraform plan review for `<azure-nsg-name>`. | Azure NSG target is identifiable by placeholder name or ID. | `commands.md`, `configs/azure-nsg-rule-summary.md`, `validation.md` |
| V002 | SSH inbound restricted to Bastion CIDR validation plan | Review SSH inbound source for port `22`. | SSH inbound allows only `<bastion-cidr>`. | `commands.md`, `configs/azure-nsg-least-privilege-policy.md`, `validation.md` |
| V003 | HTTP/HTTPS inbound exposure validation plan | Review planned ports `80` and `443`. | HTTP/HTTPS exposure is documented and intentionally scoped. | `commands.md`, `configs/azure-nsg-rule-summary.md`, `validation.md` |
| V004 | DB port 3306 not exposed to public internet validation plan | Review inbound rules for port `3306`. | DB access is not allowed from `Internet`, `Any`, `0.0.0.0/0`, or unrestricted sources. | `commands.md`, `configs/azure-nsg-least-privilege-policy.md`, `validation.md` |
| V005 | Azure App-to-On-Prem DB access rule validation plan | Review placeholder app-to-database rule. | DB access uses `<onprem-db-cidr>` or another approved placeholder source. | `commands.md`, `configs/azure-nsg-rule-summary.md`, `validation.md` |
| V006 | Monitoring scrape access rule validation plan | Review monitoring scrape placeholder rule. | Monitoring access uses `<monitoring-cidr>` and only required scrape ports. | `commands.md`, `configs/azure-nsg-rule-summary.md`, `validation.md` |
| V007 | No Any/Internet SSH rule validation plan | Search planned rules for SSH from `Any`, `Internet`, or public internet. | No SSH rule allows unrestricted inbound access. | `commands.md`, `logs/azure-nsg-validation.log`, `validation.md` |
| V008 | No unrestricted all-ports inbound rule validation plan | Search planned rules for all-protocol or all-port inbound access. | No unrestricted all-ports inbound rule exists. | `commands.md`, `logs/azure-nsg-validation.log`, `validation.md` |
| V009 | Outbound rule review plan | Review outbound rules for role alignment. | Outbound access is documented and any broad outbound rule is flagged for review. | `commands.md`, `configs/azure-nsg-least-privilege-policy.md`, `validation.md` |
| V010 | Terraform plan or Azure CLI NSG rule capture plan | Capture planned rule output from approved read-only source. | NSG rules can be reviewed from sanitized evidence. | `commands.md`, `logs/azure-nsg-validation.log`, `screenshots/azure-nsg-rules.png`, `validation.md` |
| V011 | Failure condition for unrestricted SSH, unrestricted DB, missing Bastion rule, missing service rule, or unexpected wide-open inbound rule | Evaluate findings against explicit failure conditions. | Unsafe or missing required rules produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario is Azure-specific; AWS Security Group validation is S014 and OpenStack Security Group validation is S016.
