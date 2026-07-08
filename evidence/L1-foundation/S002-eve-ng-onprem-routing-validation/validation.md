# Validation

Scenario: S002-eve-ng-onprem-routing-validation
Level: L1-foundation
Capability: EVE-NG On-Prem Routing Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real routing output has been collected yet. This file defines the validation record that must be completed during execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | EVE-NG topology file existence check | Topology summary exists or is marked TODO for capture. | TODO | NOT_RUN | `configs/topology-summary.md`; `screenshots/eve-ng-topology.png` |
| V002 | Router config snapshot existence check | Sanitized router config snapshot exists or is marked TODO for capture. | TODO | NOT_RUN | `configs/router-config-snapshot.md` |
| V003 | Management Zone gateway reachability | `<management-gateway>` is reachable from the approved source. | TODO | NOT_RUN | `commands.md`; `logs/routing-validation.log` |
| V004 | Bastion Zone gateway reachability | `<bastion-gateway>` is reachable from the approved source. | TODO | NOT_RUN | `commands.md`; `logs/routing-validation.log` |
| V005 | Internal Server Zone gateway reachability | `<internal-server-gateway>` is reachable from the approved source. | TODO | NOT_RUN | `commands.md`; `logs/routing-validation.log` |
| V006 | Monitoring Zone gateway reachability | `<monitoring-gateway>` is reachable from the approved source. | TODO | NOT_RUN | `commands.md`; `logs/routing-validation.log` |
| V007 | Transit Zone route check | Transit Zone route exists on the relevant router. | TODO | NOT_RUN | `commands.md`; `configs/router-config-snapshot.md` |
| V008 | Inter-zone ping test plan | Management-to-Bastion, Bastion-to-Internal, and Monitoring-to-Internal tests are defined. | TODO | NOT_RUN | `commands.md`; `logs/routing-validation.log` |
| V009 | Route table capture plan | Route table capture method is defined and sanitized. | TODO | NOT_RUN | `commands.md`; `configs/router-config-snapshot.md` |
| V010 | Missing route or unreachable gateway failure condition | Missing route or unreachable gateway produces `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Router config snapshot is captured: NOT_READY
- Topology summary is captured: NOT_READY
- Routing log is captured: NOT_READY
- EVE-NG topology screenshot is captured: NOT_READY

## Notes

Firewall boundaries may be noted as observations, but firewall rule implementation is excluded from S002.
