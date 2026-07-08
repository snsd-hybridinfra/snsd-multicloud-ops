# Validation

Scenario: S014-aws-security-group-least-privilege-validation
Level: L2-security-baseline
Capability: AWS Security Group Least Privilege Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real AWS Security Group output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | AWS Security Group existence validation plan | AWS Security Group target is identifiable by placeholder name or ID. | TODO | NOT_RUN | `commands.md`; `configs/aws-security-group-rule-summary.md` |
| V002 | SSH ingress restricted to Bastion CIDR validation plan | SSH ingress allows only `<bastion-cidr>`. | TODO | NOT_RUN | `commands.md`; `configs/aws-sg-least-privilege-policy.md` |
| V003 | HTTP/HTTPS ingress exposure validation plan | HTTP/HTTPS exposure is documented and intentionally scoped. | TODO | NOT_RUN | `commands.md`; `configs/aws-security-group-rule-summary.md` |
| V004 | DB port 3306 not exposed to public internet validation plan | DB access is not allowed from `0.0.0.0/0` or unrestricted sources. | TODO | NOT_RUN | `commands.md`; `configs/aws-sg-least-privilege-policy.md` |
| V005 | App-to-On-Prem DB access rule validation plan | DB access uses `<onprem-db-cidr>` or another approved placeholder source. | TODO | NOT_RUN | `commands.md`; `configs/aws-security-group-rule-summary.md` |
| V006 | Monitoring scrape access rule validation plan | Monitoring access uses `<monitoring-cidr>` and only required scrape ports. | TODO | NOT_RUN | `commands.md`; `configs/aws-security-group-rule-summary.md` |
| V007 | No 0.0.0.0/0 SSH rule validation plan | No SSH rule allows `0.0.0.0/0`. | TODO | NOT_RUN | `commands.md`; `logs/aws-security-group-validation.log` |
| V008 | No unrestricted all-ports ingress validation plan | No unrestricted all-ports ingress rule exists. | TODO | NOT_RUN | `commands.md`; `logs/aws-security-group-validation.log` |
| V009 | Egress policy review plan | Egress is documented and any broad egress is flagged for review. | TODO | NOT_RUN | `commands.md`; `configs/aws-sg-least-privilege-policy.md` |
| V010 | Terraform plan or AWS CLI rule capture plan | Security Group rules can be reviewed from sanitized evidence. | TODO | NOT_RUN | `commands.md`; `logs/aws-security-group-validation.log`; `screenshots/aws-security-group-rules.png` |
| V011 | Failure condition for unrestricted SSH, unrestricted DB, missing Bastion rule, missing service rule, or unexpected wide-open ingress | Unsafe or missing required rules produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- AWS Security Group rule summary is captured: NOT_READY
- AWS least privilege policy summary is captured: NOT_READY
- AWS Security Group validation log is captured: NOT_READY
- AWS Security Group screenshot is captured: NOT_READY

## Notes

This scenario validates AWS Security Group least privilege design only. Azure NSG validation is handled in S015, and OpenStack Security Group validation is handled in S016.
