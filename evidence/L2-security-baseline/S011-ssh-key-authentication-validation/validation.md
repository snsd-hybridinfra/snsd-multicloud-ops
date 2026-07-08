# Validation

Scenario: S011-ssh-key-authentication-validation
Level: L2-security-baseline
Capability: SSH Key Authentication Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real SSH authentication output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | SSH private key permission validation plan | Private key permission expectations are defined without storing the key. | TODO | NOT_RUN | `commands.md`; `configs/ssh-key-authentication-plan.md` |
| V002 | SSH public key placement validation plan | Public key placement validation method is defined without real key content. | TODO | NOT_RUN | `configs/ssh-key-authentication-plan.md` |
| V003 | Control Plane to Bastion key authentication plan | Control Plane-to-Bastion key authentication method is defined. | TODO | NOT_RUN | `commands.md`; `logs/ssh-key-authentication-validation.log` |
| V004 | Bastion to On-Prem DB node key authentication plan | Bastion-to-DB key authentication method is defined. | TODO | NOT_RUN | `commands.md`; `logs/ssh-key-authentication-validation.log` |
| V005 | Bastion to Monitoring node key authentication plan | Bastion-to-monitoring key authentication method is defined. | TODO | NOT_RUN | `commands.md`; `logs/ssh-key-authentication-validation.log` |
| V006 | Bastion to AWS service node key authentication plan | Bastion-to-AWS key authentication method is defined. | TODO | NOT_RUN | `commands.md`; `logs/ssh-key-authentication-validation.log` |
| V007 | Bastion to Azure service node key authentication plan | Bastion-to-Azure key authentication method is defined. | TODO | NOT_RUN | `commands.md`; `logs/ssh-key-authentication-validation.log` |
| V008 | Bastion to OpenStack service node key authentication plan | Bastion-to-OpenStack key authentication method is defined. | TODO | NOT_RUN | `commands.md`; `logs/ssh-key-authentication-validation.log` |
| V009 | SSH ProxyJump command pattern validation plan | ProxyJump pattern is documented without real users, hosts, or keys. | TODO | NOT_RUN | `commands.md`; `configs/ssh-proxyjump-pattern-summary.md` |
| V010 | Missing key, wrong key permission, missing authorized_keys entry, or unreachable target failure condition | Key-authentication failures produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- SSH key authentication plan is captured: NOT_READY
- SSH ProxyJump pattern summary is captured: NOT_READY
- SSH key authentication validation log is captured: NOT_READY
- SSH key authentication screenshot is captured: NOT_READY

## Notes

This scenario validates SSH key authentication only. Password login denial is handled in S012, and root login denial is handled in S013.
