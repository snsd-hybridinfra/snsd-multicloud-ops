# Execution Plan

## Preparation

1. Review S001 toolchain readiness and confirm local evidence editing is available.
2. Confirm the S002 evidence directory exists.
3. Identify sanitized placeholders for each on-prem zone gateway.
4. Confirm firewall implementation is outside this scenario.

## Execution Steps

1. Verify the planned EVE-NG topology summary exists.
2. Verify the planned router configuration snapshot exists.
3. Plan the Management Zone gateway reachability check.
4. Plan the Bastion Zone gateway reachability check.
5. Plan the Internal Server Zone gateway reachability check.
6. Plan the Monitoring Zone gateway reachability check.
7. Plan the Transit Zone route existence check.
8. Plan inter-zone ping tests for approved routed paths.
9. Plan route table capture for relevant routers.
10. Define the failure condition for missing routes or unreachable gateways.

## Evidence Capture

1. Record planned commands and placeholders in `commands.md`.
2. Record validation checks and TODO results in `validation.md`.
3. Map future topology evidence to `configs/topology-summary.md` and `screenshots/eve-ng-topology.png`.
4. Map future router evidence to `configs/router-config-snapshot.md` and `logs/routing-validation.log`.
5. Do not capture real network identifiers unless they are intentionally sanitized.
