# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | AWS Security Group existence validation plan | Document read-only lookup or Terraform plan review for `<aws-security-group-id>`. | AWS Security Group target is identifiable by placeholder name or ID. | `commands.md`, `configs/aws-security-group-rule-summary.md`, `validation.md` |
| V002 | SSH ingress restricted to Bastion CIDR validation plan | Review SSH ingress source for port `22`. | SSH ingress allows only `<bastion-cidr>`. | `commands.md`, `configs/aws-sg-least-privilege-policy.md`, `validation.md` |
| V003 | HTTP/HTTPS ingress exposure validation plan | Review planned ports `80` and `443`. | HTTP/HTTPS exposure is documented and intentionally scoped. | `commands.md`, `configs/aws-security-group-rule-summary.md`, `validation.md` |
| V004 | DB port 3306 not exposed to public internet validation plan | Review ingress rules for port `3306`. | DB access is not allowed from `0.0.0.0/0` or unrestricted sources. | `commands.md`, `configs/aws-sg-least-privilege-policy.md`, `validation.md` |
| V005 | App-to-On-Prem DB access rule validation plan | Review placeholder app-to-database rule. | DB access uses `<onprem-db-cidr>` or another approved placeholder source. | `commands.md`, `configs/aws-security-group-rule-summary.md`, `validation.md` |
| V006 | Monitoring scrape access rule validation plan | Review monitoring scrape placeholder rule. | Monitoring access uses `<monitoring-cidr>` and only required scrape ports. | `commands.md`, `configs/aws-security-group-rule-summary.md`, `validation.md` |
| V007 | No 0.0.0.0/0 SSH rule validation plan | Search planned rules for SSH from public internet. | No SSH rule allows `0.0.0.0/0`. | `commands.md`, `logs/aws-security-group-validation.log`, `validation.md` |
| V008 | No unrestricted all-ports ingress validation plan | Search planned rules for all-protocol or all-port ingress. | No unrestricted all-ports ingress rule exists. | `commands.md`, `logs/aws-security-group-validation.log`, `validation.md` |
| V009 | Egress policy review plan | Review outbound rules for role alignment. | Egress is documented and any broad egress is flagged for review. | `commands.md`, `configs/aws-sg-least-privilege-policy.md`, `validation.md` |
| V010 | Terraform plan or AWS CLI rule capture plan | Capture planned rule output from approved read-only source. | Security Group rules can be reviewed from sanitized evidence. | `commands.md`, `logs/aws-security-group-validation.log`, `screenshots/aws-security-group-rules.png`, `validation.md` |
| V011 | Failure condition for unrestricted SSH, unrestricted DB, missing Bastion rule, missing service rule, or unexpected wide-open ingress | Evaluate findings against explicit failure conditions. | Unsafe or missing required rules produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario is AWS-specific; Azure NSG validation is S015 and OpenStack Security Group validation is S016.
