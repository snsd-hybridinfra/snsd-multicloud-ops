# Validation

Scenario: S008-bastion-reachability-validation
Level: L1-foundation
Capability: Bastion Reachability Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real reachability command output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Bastion inventory entry validation plan | Bastion entry is documented with placeholder hostname and IP only. | TODO | NOT_RUN | `commands.md`; `configs/bastion-reachability-path-summary.md` |
| V002 | Management to Bastion ping or TCP reachability plan | Management-to-Bastion reachability method is defined. | TODO | NOT_RUN | `commands.md`; `logs/bastion-reachability-validation.log` |
| V003 | Bastion SSH reachability plan using placeholder command | Bastion SSH reachability command pattern is defined without credentials or keys. | TODO | NOT_RUN | `commands.md`; `configs/ssh-jump-pattern-summary.md` |
| V004 | Bastion to On-Prem DB node reachability plan | Bastion-to-DB reachability method is defined. | TODO | NOT_RUN | `commands.md`; `logs/bastion-reachability-validation.log` |
| V005 | Bastion to Monitoring node reachability plan | Bastion-to-monitoring reachability method is defined. | TODO | NOT_RUN | `commands.md`; `logs/bastion-reachability-validation.log` |
| V006 | Bastion to AWS service node reachability plan | Bastion-to-AWS reachability method is defined. | TODO | NOT_RUN | `commands.md`; `logs/bastion-reachability-validation.log` |
| V007 | Bastion to Azure service node reachability plan | Bastion-to-Azure reachability method is defined. | TODO | NOT_RUN | `commands.md`; `logs/bastion-reachability-validation.log` |
| V008 | Bastion to OpenStack service node reachability plan | Bastion-to-OpenStack reachability method is defined. | TODO | NOT_RUN | `commands.md`; `logs/bastion-reachability-validation.log` |
| V009 | SSH ProxyJump command pattern validation plan | ProxyJump pattern is documented without real users, hosts, or keys. | TODO | NOT_RUN | `commands.md`; `configs/ssh-jump-pattern-summary.md` |
| V010 | Evidence collection through Bastion path validation plan | Evidence path is defined without real host access. | TODO | NOT_RUN | `configs/bastion-reachability-path-summary.md`; `screenshots/bastion-path-diagram.png` |
| V011 | Unreachable Bastion, missing route, blocked SSH, or invalid inventory entry failure condition | Reachability failures produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Bastion reachability path summary is captured: NOT_READY
- SSH jump pattern summary is captured: NOT_READY
- Bastion reachability log is captured: NOT_READY
- Bastion path diagram is captured: NOT_READY

## Notes

This scenario validates reachability design only. SSH hardening is excluded and handled in L2 scenarios.
