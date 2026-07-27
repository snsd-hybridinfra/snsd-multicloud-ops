# P1-VIS-CLOSE Completion Report

## Outcome

ZT-VIS-001 is accepted for the bounded Phase 1 local-visibility scope. Four
fixed validator-summary transports produced attributed sanitized events, and
the existing single-node Grafana/Loki/Alloy stack passed service health,
loopback exposure, retention, ingestion, query, secret-boundary, and restart
persistence checks. No logging or permission configuration was changed.

## Negative and freshness behavior

The initial collection while dependencies were stopped failed visibly. After
only the reviewed dependencies were started, all four transports produced
events. The OpenStack source retained four current diagnostic failures at
46 PASS / 0 WARN / 4 FAIL, and those failures generated two live findings.
They were not bypassed or converted to successful checks. The controlled
fixture remained separately labeled. All sources were attributable and the
newest event was inside the 900-second freshness window.

## Time and permission boundary

The guest used UTC, active systemd-timesyncd, and an identified public NTP
source. External UDP/123 replies timed out at the physical-network boundary.
The KVM RTC remained aligned to the OpenStack control host within the
three-second sequential-measurement bound. One no-configuration timesyncd
restart returned the service to its original active state but did not recover
external replies. Persistent NTP synchronization and
KISA U-65 acceptance are therefore not claimed. Configuration, sanitized
input, service data, and the VM-local secret retained their reviewed 0700,
0750, role-owned, and root-only 0600 boundaries without modification.

## Rollback and status

The exact telemetry Compose project passed restart persistence. The two
OpenStack instances then returned to `SHUTOFF` with no pending task, and all
three EVE lab process types returned to zero. ZT-VIS-001 is now
`RUNTIME_VALIDATED` / `VALIDATED` / `ACCEPTED` only for
`BOUNDED_SINGLE_NODE_SANITIZED_LOCAL_TELEMETRY`. Evidence continuity remains
EC3; central visibility, ZT-VIS-002, continuous operation, scheduling, SIEM/SOC,
automated response, and maturity remain open. Phase 1 remains
`PARTIAL / PARTIALLY_VALIDATED / NOT_COMPLETE` at `ZT-SCH-001`.

Exactly one next action is `P1-CV-001`.
