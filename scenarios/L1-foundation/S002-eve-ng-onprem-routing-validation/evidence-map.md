# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| EVE-NG topology file existence check | `configs/topology-summary.md`; `screenshots/eve-ng-topology.png`; `validation.md` | topology summary, screenshot reference, validation record | yes |
| Router config snapshot existence check | `configs/router-config-snapshot.md`; `validation.md` | sanitized config snapshot, validation record | yes |
| Management Zone gateway reachability | `commands.md`; `logs/routing-validation.log`; `validation.md` | command plan, routing log, validation record | yes |
| Bastion Zone gateway reachability | `commands.md`; `logs/routing-validation.log`; `validation.md` | command plan, routing log, validation record | yes |
| Internal Server Zone gateway reachability | `commands.md`; `logs/routing-validation.log`; `validation.md` | command plan, routing log, validation record | yes |
| Monitoring Zone gateway reachability | `commands.md`; `logs/routing-validation.log`; `validation.md` | command plan, routing log, validation record | yes |
| Transit Zone route check | `commands.md`; `configs/router-config-snapshot.md`; `validation.md` | command plan, sanitized route evidence, validation record | yes |
| Inter-zone ping test plan | `commands.md`; `logs/routing-validation.log`; `validation.md` | command plan, routing log, validation record | yes |
| Route table capture plan | `commands.md`; `configs/router-config-snapshot.md`; `validation.md` | command plan, sanitized route table evidence, validation record | yes |
| Missing route or unreachable gateway failure condition | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real routing output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
