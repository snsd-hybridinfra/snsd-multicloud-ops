# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | EVE-NG topology file existence check | Confirm planned topology summary exists. | Topology summary is available or marked TODO for capture. | `configs/topology-summary.md`, `screenshots/eve-ng-topology.png`, `validation.md` |
| V002 | Router config snapshot existence check | Confirm sanitized router snapshot exists. | Router config snapshot is available or marked TODO for capture. | `configs/router-config-snapshot.md`, `validation.md` |
| V003 | Management Zone gateway reachability | Plan ping or equivalent reachability check to `<management-gateway>`. | Gateway reachability can be tested without exposing real addressing. | `commands.md`, `logs/routing-validation.log`, `validation.md` |
| V004 | Bastion Zone gateway reachability | Plan ping or equivalent reachability check to `<bastion-gateway>`. | Gateway reachability can be tested without exposing real addressing. | `commands.md`, `logs/routing-validation.log`, `validation.md` |
| V005 | Internal Server Zone gateway reachability | Plan ping or equivalent reachability check to `<internal-server-gateway>`. | Gateway reachability can be tested without exposing real addressing. | `commands.md`, `logs/routing-validation.log`, `validation.md` |
| V006 | Monitoring Zone gateway reachability | Plan ping or equivalent reachability check to `<monitoring-gateway>`. | Gateway reachability can be tested without exposing real addressing. | `commands.md`, `logs/routing-validation.log`, `validation.md` |
| V007 | Transit Zone route check | Plan route lookup for `<transit-router>`. | Required Transit Zone route exists or missing route is clearly recorded. | `commands.md`, `configs/router-config-snapshot.md`, `validation.md` |
| V008 | Inter-zone ping test plan | Document approved Management-to-Bastion, Bastion-to-Internal, and Monitoring-to-Internal checks. | Inter-zone routing tests are defined and mapped to evidence. | `commands.md`, `logs/routing-validation.log`, `validation.md` |
| V009 | Route table capture plan | Document route table capture for relevant routers. | Route table evidence can be captured and sanitized. | `commands.md`, `configs/router-config-snapshot.md`, `validation.md` |
| V010 | Missing route or unreachable gateway failure condition | Confirm failure criteria are explicit. | Missing route or unreachable gateway produces `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. Firewall boundary observations are allowed, but firewall implementation is explicitly excluded.
