# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Bastion inventory entry validation plan | `commands.md`; `configs/bastion-reachability-path-summary.md`; `validation.md` | command plan, path summary, validation record | yes |
| Management to Bastion ping or TCP reachability plan | `commands.md`; `logs/bastion-reachability-validation.log`; `validation.md` | command plan, reachability log, validation record | yes |
| Bastion SSH reachability plan using placeholder command | `commands.md`; `configs/ssh-jump-pattern-summary.md`; `validation.md` | command plan, jump pattern summary, validation record | yes |
| Bastion to On-Prem DB node reachability plan | `commands.md`; `logs/bastion-reachability-validation.log`; `validation.md` | command plan, reachability log, validation record | yes |
| Bastion to Monitoring node reachability plan | `commands.md`; `logs/bastion-reachability-validation.log`; `validation.md` | command plan, reachability log, validation record | yes |
| Bastion to AWS service node reachability plan | `commands.md`; `logs/bastion-reachability-validation.log`; `validation.md` | command plan, reachability log, validation record | yes |
| Bastion to Azure service node reachability plan | `commands.md`; `logs/bastion-reachability-validation.log`; `validation.md` | command plan, reachability log, validation record | yes |
| Bastion to OpenStack service node reachability plan | `commands.md`; `logs/bastion-reachability-validation.log`; `validation.md` | command plan, reachability log, validation record | yes |
| SSH ProxyJump command pattern validation plan | `commands.md`; `configs/ssh-jump-pattern-summary.md`; `validation.md` | command plan, jump pattern summary, validation record | yes |
| Evidence collection through Bastion path validation plan | `configs/bastion-reachability-path-summary.md`; `screenshots/bastion-path-diagram.png`; `validation.md` | path summary, diagram reference, validation record | yes |
| Unreachable Bastion, missing route, blocked SSH, or invalid inventory entry failure condition | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real reachability output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
