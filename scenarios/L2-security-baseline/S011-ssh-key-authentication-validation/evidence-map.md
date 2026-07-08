# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| SSH private key permission validation plan | `commands.md`; `configs/ssh-key-authentication-plan.md`; `validation.md` | command plan, key auth plan, validation record | yes |
| SSH public key placement validation plan | `configs/ssh-key-authentication-plan.md`; `validation.md` | key auth plan, validation record | yes |
| Control Plane to Bastion key authentication plan | `commands.md`; `logs/ssh-key-authentication-validation.log`; `validation.md` | command plan, SSH log, validation record | yes |
| Bastion to On-Prem DB node key authentication plan | `commands.md`; `logs/ssh-key-authentication-validation.log`; `validation.md` | command plan, SSH log, validation record | yes |
| Bastion to Monitoring node key authentication plan | `commands.md`; `logs/ssh-key-authentication-validation.log`; `validation.md` | command plan, SSH log, validation record | yes |
| Bastion to AWS service node key authentication plan | `commands.md`; `logs/ssh-key-authentication-validation.log`; `validation.md` | command plan, SSH log, validation record | yes |
| Bastion to Azure service node key authentication plan | `commands.md`; `logs/ssh-key-authentication-validation.log`; `validation.md` | command plan, SSH log, validation record | yes |
| Bastion to OpenStack service node key authentication plan | `commands.md`; `logs/ssh-key-authentication-validation.log`; `validation.md` | command plan, SSH log, validation record | yes |
| SSH ProxyJump command pattern validation plan | `commands.md`; `configs/ssh-proxyjump-pattern-summary.md`; `validation.md` | command plan, ProxyJump summary, validation record | yes |
| Missing key, wrong key permission, missing authorized_keys entry, or unreachable target failure condition | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real SSH authentication output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
