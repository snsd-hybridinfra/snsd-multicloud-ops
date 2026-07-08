# Commands

Scenario: S011-ssh-key-authentication-validation
Level: L2-security-baseline
Capability: SSH Key Authentication Validation
Target: `<target-node>`
Execution timestamp: TODO

Record sanitized output only. Do not include real SSH private keys, credentials, real public IPs, account-specific usernames, tfstate, kubeconfig content, cloud account IDs, subscription IDs, tenant IDs, or provider-specific secrets.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | SSH private key permission validation plan | `Get-Acl <ssh-private-key-path>` or approved equivalent after future approval. | Confirm planned private key permission check without storing key content. | TODO: record sanitized output after approved execution. |
| V002 | SSH public key placement validation plan | Review target `authorized_keys` placement using placeholder path. | Confirm public key placement validation method. | TODO: record sanitized result after review. |
| V003 | Control Plane to Bastion key authentication plan | `ssh -i <ssh-private-key-path> <bastion-user>@<bastion-host>` | Confirm Control Plane-to-Bastion key-auth command pattern. | TODO: record sanitized output after approved execution. |
| V004 | Bastion to On-Prem DB node key authentication plan | `ssh -i <ssh-private-key-path> <target-user>@<db-primary-node>` from `<bastion-host>`. | Confirm Bastion-to-DB key-auth command pattern. | TODO: record sanitized output after approved execution. |
| V005 | Bastion to Monitoring node key authentication plan | `ssh -i <ssh-private-key-path> <target-user>@<monitoring-node>` from `<bastion-host>`. | Confirm Bastion-to-monitoring key-auth command pattern. | TODO: record sanitized output after approved execution. |
| V006 | Bastion to AWS service node key authentication plan | `ssh -i <ssh-private-key-path> <target-user>@<aws-service-node>` from `<bastion-host>`. | Confirm Bastion-to-AWS key-auth command pattern. | TODO: record sanitized output after approved execution. |
| V007 | Bastion to Azure service node key authentication plan | `ssh -i <ssh-private-key-path> <target-user>@<azure-service-node>` from `<bastion-host>`. | Confirm Bastion-to-Azure key-auth command pattern. | TODO: record sanitized output after approved execution. |
| V008 | Bastion to OpenStack service node key authentication plan | `ssh -i <ssh-private-key-path> <target-user>@<openstack-service-node>` from `<bastion-host>`. | Confirm Bastion-to-OpenStack key-auth command pattern. | TODO: record sanitized output after approved execution. |
| V009 | SSH ProxyJump command pattern validation plan | `ssh -i <ssh-private-key-path> -J <bastion-user>@<bastion-host> <target-user>@<target-node>` | Confirm ProxyJump command pattern with placeholders only. | TODO: record sanitized result after review. |
| V010 | Missing key, wrong key permission, missing authorized_keys entry, or unreachable target failure condition | Review failed SSH key-auth findings. | Confirm failure criteria produce `FAIL` or `BLOCKED` status. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/ssh-key-authentication-plan.md`
- `configs/ssh-proxyjump-pattern-summary.md`
- `logs/ssh-key-authentication-validation.log`
- `screenshots/ssh-key-authentication-test.png`
