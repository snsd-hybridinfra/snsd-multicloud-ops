# Commands

Scenario: S015-azure-nsg-least-privilege-validation
Level: L2-security-baseline
Capability: Azure NSG Least Privilege Validation
Target: `<azure-nsg-name>`
Execution timestamp: TODO

Record sanitized output only. Do not include Azure credentials, subscription IDs, tenant IDs, real public IPs, private keys, tfstate, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Azure NSG existence validation plan | Review Terraform plan output or approved read-only Azure CLI lookup for `<azure-nsg-name>`. | Confirm the NSG target is identifiable. | TODO: record sanitized output after approved execution. |
| V002 | SSH inbound restricted to Bastion CIDR validation plan | Review port `22` inbound source for `<bastion-cidr>`. | Confirm SSH access is limited to Bastion. | TODO: record sanitized output after approved execution. |
| V003 | HTTP/HTTPS inbound exposure validation plan | Review ports `80` and `443` inbound rule placeholders. | Confirm service exposure is intentional. | TODO: record sanitized output after approved execution. |
| V004 | DB port 3306 not exposed to public internet validation plan | Search rule output for port `3306` from `Internet`, `Any`, or `0.0.0.0/0`. | Confirm DB access is not publicly exposed. | TODO: record sanitized output after approved execution. |
| V005 | Azure App-to-On-Prem DB access rule validation plan | Review rule allowing `<azure-app-node>` to reach `<onprem-db-cidr>`. | Confirm app-to-DB access is explicitly scoped. | TODO: record sanitized output after approved execution. |
| V006 | Monitoring scrape access rule validation plan | Review monitoring source rule from `<monitoring-cidr>`. | Confirm monitoring access is explicitly scoped. | TODO: record sanitized output after approved execution. |
| V007 | No Any/Internet SSH rule validation plan | Search NSG rules for SSH from `Any`, `Internet`, or public internet. | Confirm unrestricted SSH is absent. | TODO: record sanitized output after approved execution. |
| V008 | No unrestricted all-ports inbound rule validation plan | Search NSG rules for all-protocol or all-port inbound access. | Confirm wide-open inbound access is absent. | TODO: record sanitized output after approved execution. |
| V009 | Outbound rule review plan | Review outbound rules for role-specific intent. | Confirm outbound access is documented and broad outbound access is flagged. | TODO: record sanitized output after approved execution. |
| V010 | Terraform plan or Azure CLI NSG rule capture plan | Capture sanitized Terraform plan or Azure CLI NSG rule output. | Produce reviewable rule evidence. | TODO: record sanitized output after approved execution. |
| V011 | Failure condition for unrestricted SSH, unrestricted DB, missing Bastion rule, missing service rule, or unexpected wide-open inbound rule | Review validation findings against failure criteria. | Confirm unsafe rule patterns result in `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/azure-nsg-rule-summary.md`
- `configs/azure-nsg-least-privilege-policy.md`
- `logs/azure-nsg-validation.log`
- `screenshots/azure-nsg-rules.png`
