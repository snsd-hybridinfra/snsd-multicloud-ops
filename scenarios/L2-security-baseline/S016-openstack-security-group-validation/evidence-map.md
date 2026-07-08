# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| OpenStack Security Group existence validation plan | `commands.md`; `configs/openstack-security-group-rule-summary.md`; `validation.md` | command plan, rule summary, validation record | yes |
| SSH ingress restricted to Bastion CIDR validation plan | `commands.md`; `configs/openstack-sg-least-privilege-policy.md`; `validation.md` | command plan, policy summary, validation record | yes |
| HTTP/HTTPS ingress exposure validation plan | `commands.md`; `configs/openstack-security-group-rule-summary.md`; `validation.md` | command plan, rule summary, validation record | yes |
| DB port 3306 not exposed to public or provider network validation plan | `commands.md`; `configs/openstack-sg-least-privilege-policy.md`; `validation.md` | command plan, policy summary, validation record | yes |
| OpenStack App-to-On-Prem DB access rule validation plan | `commands.md`; `configs/openstack-security-group-rule-summary.md`; `validation.md` | command plan, rule summary, validation record | yes |
| Monitoring scrape access rule validation plan | `commands.md`; `configs/openstack-security-group-rule-summary.md`; `validation.md` | command plan, rule summary, validation record | yes |
| No 0.0.0.0/0 SSH rule validation plan | `commands.md`; `logs/openstack-security-group-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| No unrestricted all-ports ingress validation plan | `commands.md`; `logs/openstack-security-group-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Egress rule review plan | `commands.md`; `configs/openstack-sg-least-privilege-policy.md`; `validation.md` | command plan, policy summary, validation record | yes |
| Terraform plan or OpenStack CLI security group rule capture plan | `commands.md`; `logs/openstack-security-group-validation.log`; `screenshots/openstack-security-group-rules.png`; `validation.md` | command plan, log, screenshot reference, validation record | yes |
| Failure condition for unrestricted SSH, unrestricted DB, missing Bastion rule, missing service rule, or unexpected wide-open ingress | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real OpenStack Security Group output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
