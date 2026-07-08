# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Bastion inventory entry validation plan | Review bastion inventory placeholder entry. | Bastion entry is documented with placeholder hostname and IP only. | `commands.md`, `configs/bastion-reachability-path-summary.md`, `validation.md` |
| V002 | Management to Bastion ping or TCP reachability plan | Document planned ping or TCP check from Management Zone to `<bastion-ip>`. | Management-to-Bastion reachability method is defined. | `commands.md`, `logs/bastion-reachability-validation.log`, `validation.md` |
| V003 | Bastion SSH reachability plan using placeholder command | Document placeholder SSH check to `<bastion-host>`. | Bastion SSH reachability command pattern is defined without credentials or keys. | `commands.md`, `configs/ssh-jump-pattern-summary.md`, `validation.md` |
| V004 | Bastion to On-Prem DB node reachability plan | Document reachability from `<bastion-host>` to `<db-primary-ip>`. | Bastion-to-DB reachability method is defined. | `commands.md`, `logs/bastion-reachability-validation.log`, `validation.md` |
| V005 | Bastion to Monitoring node reachability plan | Document reachability from `<bastion-host>` to `<monitoring-node-ip>`. | Bastion-to-monitoring reachability method is defined. | `commands.md`, `logs/bastion-reachability-validation.log`, `validation.md` |
| V006 | Bastion to AWS service node reachability plan | Document reachability from `<bastion-host>` to `<aws-app-node-ip>`. | Bastion-to-AWS reachability method is defined. | `commands.md`, `logs/bastion-reachability-validation.log`, `validation.md` |
| V007 | Bastion to Azure service node reachability plan | Document reachability from `<bastion-host>` to `<azure-app-node-ip>`. | Bastion-to-Azure reachability method is defined. | `commands.md`, `logs/bastion-reachability-validation.log`, `validation.md` |
| V008 | Bastion to OpenStack service node reachability plan | Document reachability from `<bastion-host>` to `<openstack-app-node-ip>`. | Bastion-to-OpenStack reachability method is defined. | `commands.md`, `logs/bastion-reachability-validation.log`, `validation.md` |
| V009 | SSH ProxyJump command pattern validation plan | Review `ssh -J <bastion-user>@<bastion-host> <target-user>@<target-host>` pattern. | ProxyJump pattern is documented without real users, hosts, or keys. | `commands.md`, `configs/ssh-jump-pattern-summary.md`, `validation.md` |
| V010 | Evidence collection through Bastion path validation plan | Document how evidence would be collected through bastion path. | Evidence path is defined without real host access. | `configs/bastion-reachability-path-summary.md`, `screenshots/bastion-path-diagram.png`, `validation.md` |
| V011 | Unreachable Bastion, missing route, blocked SSH, or invalid inventory entry failure condition | Define explicit failure criteria. | Reachability failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. SSH hardening is explicitly excluded from S008 and belongs to L2 scenarios.
