# Validation

Scenario: S015-azure-nsg-least-privilege-validation
Level: L2-security-baseline
Capability: Azure NSG Least Privilege Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real Azure NSG output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Azure NSG existence validation plan | Azure NSG target is identifiable by placeholder name or ID. | TODO | NOT_RUN | `commands.md`; `configs/azure-nsg-rule-summary.md` |
| V002 | SSH inbound restricted to Bastion CIDR validation plan | SSH inbound allows only `<bastion-cidr>`. | TODO | NOT_RUN | `commands.md`; `configs/azure-nsg-least-privilege-policy.md` |
| V003 | HTTP/HTTPS inbound exposure validation plan | HTTP/HTTPS exposure is documented and intentionally scoped. | TODO | NOT_RUN | `commands.md`; `configs/azure-nsg-rule-summary.md` |
| V004 | DB port 3306 not exposed to public internet validation plan | DB access is not allowed from `Internet`, `Any`, `0.0.0.0/0`, or unrestricted sources. | TODO | NOT_RUN | `commands.md`; `configs/azure-nsg-least-privilege-policy.md` |
| V005 | Azure App-to-On-Prem DB access rule validation plan | DB access uses `<onprem-db-cidr>` or another approved placeholder source. | TODO | NOT_RUN | `commands.md`; `configs/azure-nsg-rule-summary.md` |
| V006 | Monitoring scrape access rule validation plan | Monitoring access uses `<monitoring-cidr>` and only required scrape ports. | TODO | NOT_RUN | `commands.md`; `configs/azure-nsg-rule-summary.md` |
| V007 | No Any/Internet SSH rule validation plan | No SSH rule allows unrestricted inbound access. | TODO | NOT_RUN | `commands.md`; `logs/azure-nsg-validation.log` |
| V008 | No unrestricted all-ports inbound rule validation plan | No unrestricted all-ports inbound rule exists. | TODO | NOT_RUN | `commands.md`; `logs/azure-nsg-validation.log` |
| V009 | Outbound rule review plan | Outbound access is documented and any broad outbound rule is flagged for review. | TODO | NOT_RUN | `commands.md`; `configs/azure-nsg-least-privilege-policy.md` |
| V010 | Terraform plan or Azure CLI NSG rule capture plan | NSG rules can be reviewed from sanitized evidence. | TODO | NOT_RUN | `commands.md`; `logs/azure-nsg-validation.log`; `screenshots/azure-nsg-rules.png` |
| V011 | Failure condition for unrestricted SSH, unrestricted DB, missing Bastion rule, missing service rule, or unexpected wide-open inbound rule | Unsafe or missing required rules produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Azure NSG rule summary is captured: NOT_READY
- Azure NSG least privilege policy summary is captured: NOT_READY
- Azure NSG validation log is captured: NOT_READY
- Azure NSG screenshot is captured: NOT_READY

## Notes

This scenario validates Azure NSG least privilege design only. AWS Security Group validation is handled in S014, and OpenStack Security Group validation is handled in S016.
