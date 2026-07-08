# Commands

Scenario: S008-bastion-reachability-validation
Level: L1-foundation
Capability: Bastion Reachability Validation
Target: `<target-node>`
Execution timestamp: TODO

Record sanitized output only. Do not include real public IPs, private IPs, credentials, SSH private keys, tokens, tfstate, kubeconfig content, cloud account IDs, subscription IDs, tenant IDs, or provider-specific secrets.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Bastion inventory entry validation plan | Review inventory for `<bastion-host>` and `<bastion-ip>` placeholders. | Confirm bastion entry is present and sanitized. | TODO: record sanitized output after approved execution. |
| V002 | Management to Bastion ping or TCP reachability plan | `Test-NetConnection <bastion-ip> -Port 22` or `ping <bastion-ip>` | Confirm planned Management-to-Bastion reachability method. | TODO: record sanitized output after approved execution. |
| V003 | Bastion SSH reachability plan using placeholder command | `ssh <bastion-user>@<bastion-host>` | Confirm placeholder-only SSH reachability command pattern. | TODO: record sanitized output after approved execution. |
| V004 | Bastion to On-Prem DB node reachability plan | `ssh <bastion-user>@<bastion-host> "ping <db-primary-ip>"` | Confirm planned Bastion-to-DB reachability method. | TODO: record sanitized output after approved execution. |
| V005 | Bastion to Monitoring node reachability plan | `ssh <bastion-user>@<bastion-host> "ping <monitoring-node-ip>"` | Confirm planned Bastion-to-monitoring reachability method. | TODO: record sanitized output after approved execution. |
| V006 | Bastion to AWS service node reachability plan | `ssh <bastion-user>@<bastion-host> "ping <aws-app-node-ip>"` | Confirm planned Bastion-to-AWS reachability method. | TODO: record sanitized output after approved execution. |
| V007 | Bastion to Azure service node reachability plan | `ssh <bastion-user>@<bastion-host> "ping <azure-app-node-ip>"` | Confirm planned Bastion-to-Azure reachability method. | TODO: record sanitized output after approved execution. |
| V008 | Bastion to OpenStack service node reachability plan | `ssh <bastion-user>@<bastion-host> "ping <openstack-app-node-ip>"` | Confirm planned Bastion-to-OpenStack reachability method. | TODO: record sanitized output after approved execution. |
| V009 | SSH ProxyJump command pattern validation plan | `ssh -J <bastion-user>@<bastion-host> <target-user>@<target-host>` | Confirm ProxyJump syntax pattern without real users, hosts, or keys. | TODO: record sanitized result after review. |
| V010 | Evidence collection through Bastion path validation plan | Review planned evidence path through `<bastion-host>` to `<target-host>`. | Confirm evidence collection path is defined. | TODO: record sanitized result after review. |
| V011 | Unreachable Bastion, missing route, blocked SSH, or invalid inventory entry failure condition | Review failed reachability findings. | Confirm failure criteria produce `FAIL` or `BLOCKED` status. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/bastion-reachability-path-summary.md`
- `configs/ssh-jump-pattern-summary.md`
- `logs/bastion-reachability-validation.log`
- `screenshots/bastion-path-diagram.png`
