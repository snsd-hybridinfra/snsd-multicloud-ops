# Commands

Scenario: S007-multi-cloud-inventory-validation
Level: L1-foundation
Capability: Multi-Cloud Inventory Validation
Target: `<target-node>`
Execution timestamp: TODO

Record sanitized output only. Do not include real public IPs, private IPs, credentials, SSH private keys, tokens, tfstate, kubeconfig content, account IDs, subscription IDs, tenant IDs, project IDs, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Inventory file existence validation plan | `Test-Path ansible/inventories/<inventory-file>` | Confirm planned inventory file path exists when implementation is approved. | TODO: record sanitized output after approved execution. |
| V002 | Required inventory group validation plan | Review inventory for `aws_nodes`, `azure_nodes`, `openstack_nodes`, `eve_ng_network`, `onprem_bastion`, `onprem_db_primary`, `onprem_db_replicas`, `onprem_monitoring`, `kubernetes_nodes`, `observability_targets`, and `evidence_targets`. | Confirm all required inventory groups are present. | TODO: record sanitized output after approved execution. |
| V003 | Placeholder-only value validation plan | Review host values for placeholders such as `<aws-app-node-ip>` and `<db-primary-ip>`. | Confirm no real network values are present. | TODO: record sanitized result after review. |
| V004 | No secret or private key validation plan | Review inventory for credentials, keys, tokens, and secret-like values. | Confirm inventory contains no sensitive values. | TODO: record sanitized result after review. |
| V005 | Provider grouping validation plan | Review provider groups. | Confirm AWS, Azure, OpenStack, EVE-NG, and on-prem groups are separated. | TODO: record sanitized result after review. |
| V006 | Role grouping validation plan | Review role groups and host metadata. | Confirm role boundaries are clear. | TODO: record sanitized result after review. |
| V007 | On-Prem DB grouping validation plan | Review `onprem_db_primary` and `onprem_db_replicas`. | Confirm DB primary and replica roles are separated. | TODO: record sanitized result after review. |
| V008 | Observability target grouping validation plan | Review `observability_targets`. | Confirm exporter and monitoring targets are grouped. | TODO: record sanitized result after review. |
| V009 | Evidence collection target grouping validation plan | Review `evidence_targets`. | Confirm evidence collection targets are grouped. | TODO: record sanitized result after review. |
| V010 | Missing group, real credential, or inconsistent hostname failure condition | Review failed inventory findings. | Confirm failure criteria produce `FAIL` or `BLOCKED` status. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/inventory-structure-summary.md`
- `configs/inventory-sanitization-check.md`
- `logs/inventory-validation.log`
