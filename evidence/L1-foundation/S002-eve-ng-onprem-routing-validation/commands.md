# Commands

Scenario: S002-eve-ng-onprem-routing-validation
Level: L1-foundation
Capability: EVE-NG On-Prem Routing Validation
Target: `<target-node>`
Execution timestamp: TODO

Record sanitized output only. Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, real public IPs, private IPs, or real hostnames.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | EVE-NG topology file existence check | `Test-Path eve-ng/topology/<topology-summary-file>` | Confirm the topology summary can be located for review. | TODO: record sanitized result after execution. |
| V002 | Router config snapshot existence check | `Test-Path eve-ng/router-configs/<router-config-snapshot>` | Confirm sanitized router configuration snapshot can be located. | TODO: record sanitized result after execution. |
| V003 | Management Zone gateway reachability | `ping <management-gateway>` | Confirm Management Zone gateway reachability. | TODO: record sanitized result after execution. |
| V004 | Bastion Zone gateway reachability | `ping <bastion-gateway>` | Confirm Bastion Zone gateway reachability. | TODO: record sanitized result after execution. |
| V005 | Internal Server Zone gateway reachability | `ping <internal-server-gateway>` | Confirm Internal Server Zone gateway reachability. | TODO: record sanitized result after execution. |
| V006 | Monitoring Zone gateway reachability | `ping <monitoring-gateway>` | Confirm Monitoring Zone gateway reachability. | TODO: record sanitized result after execution. |
| V007 | Transit Zone route check | `show route <transit-zone-placeholder>` | Confirm Transit Zone route existence on the relevant router. | TODO: record sanitized result after execution. |
| V008 | Inter-zone ping test plan | `ping <destination-zone-gateway>` from approved source zones | Confirm planned Management-to-Bastion, Bastion-to-Internal, and Monitoring-to-Internal routing tests. | TODO: record sanitized result after execution. |
| V009 | Route table capture plan | `show route` or equivalent on `<transit-router>` | Capture sanitized route table evidence. | TODO: record sanitized result after execution. |
| V010 | Missing route or unreachable gateway failure condition | Review failed reachability and route checks. | Confirm missing route or unreachable gateway is marked `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/router-config-snapshot.md`
- `configs/topology-summary.md`
- `logs/routing-validation.log`
- `screenshots/eve-ng-topology.png`
