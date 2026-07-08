# Commands

Scenario: S016-openstack-security-group-validation
Level: L2-security-baseline
Capability: OpenStack Security Group Least Privilege Validation
Target: `<openstack-security-group-id>`
Execution timestamp: TODO

Record sanitized output only. Do not include OpenStack credentials, openrc content, clouds.yaml content, real public IPs, private keys, tfstate, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | OpenStack Security Group existence validation plan | Review Terraform plan output or approved read-only OpenStack CLI lookup for `<openstack-security-group-id>`. | Confirm the Security Group target is identifiable. | TODO: record sanitized output after approved execution. |
| V002 | SSH ingress restricted to Bastion CIDR validation plan | Review port `22` ingress source for `<bastion-cidr>`. | Confirm SSH access is limited to Bastion. | TODO: record sanitized output after approved execution. |
| V003 | HTTP/HTTPS ingress exposure validation plan | Review ports `80` and `443` ingress rule placeholders. | Confirm service exposure is intentional. | TODO: record sanitized output after approved execution. |
| V004 | DB port 3306 not exposed to public or provider network validation plan | Search rule output for port `3306` from `0.0.0.0/0`, public network, or provider network sources. | Confirm DB access is not publicly or broadly exposed. | TODO: record sanitized output after approved execution. |
| V005 | OpenStack App-to-On-Prem DB access rule validation plan | Review rule allowing `<openstack-app-node>` to reach `<onprem-db-cidr>`. | Confirm app-to-DB access is explicitly scoped. | TODO: record sanitized output after approved execution. |
| V006 | Monitoring scrape access rule validation plan | Review monitoring source rule from `<monitoring-cidr>`. | Confirm monitoring access is explicitly scoped. | TODO: record sanitized output after approved execution. |
| V007 | No 0.0.0.0/0 SSH rule validation plan | Search Security Group rules for SSH from `0.0.0.0/0`. | Confirm unrestricted SSH is absent. | TODO: record sanitized output after approved execution. |
| V008 | No unrestricted all-ports ingress validation plan | Search Security Group rules for all-protocol or all-port ingress. | Confirm wide-open ingress is absent. | TODO: record sanitized output after approved execution. |
| V009 | Egress rule review plan | Review outbound rules for role-specific intent. | Confirm egress is documented and broad egress is flagged. | TODO: record sanitized output after approved execution. |
| V010 | Terraform plan or OpenStack CLI security group rule capture plan | Capture sanitized Terraform plan or OpenStack CLI Security Group rule output. | Produce reviewable rule evidence. | TODO: record sanitized output after approved execution. |
| V011 | Failure condition for unrestricted SSH, unrestricted DB, missing Bastion rule, missing service rule, or unexpected wide-open ingress | Review validation findings against failure criteria. | Confirm unsafe rule patterns result in `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/openstack-security-group-rule-summary.md`
- `configs/openstack-sg-least-privilege-policy.md`
- `logs/openstack-security-group-validation.log`
- `screenshots/openstack-security-group-rules.png`
