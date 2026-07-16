# Progress Tracker

This file tracks scenario-based progress across the five validation levels.

## Status Values

Scenario status values: `NOT_STARTED`, `PLANNED`, `IN_PROGRESS`, `IMPLEMENTED`, `VALIDATED`, `PARTIAL`, `BLOCKED`, `DEPRECATED`

Evidence status values: `NOT_READY`, `PARTIAL`, `READY`, `REVIEWED`

## Level Summary

| Level | Category | Scenarios | Implemented | Validated | Notes |
|---|---|---:|---:|---:|---|
| L1 | Foundation | 10/10 | 1/10 | 1/10 | S002 network foundation is VALIDATED with READY E001-E014 evidence; other L1 scenarios remain unchanged |
| L2 | Security Baseline | 10/10 | 0/10 | 0/10 | Definitions exist; all S011-S020 scenarios are NOT_STARTED |
| L3 | Service Operations | 10/10 | 0/10 | 0/10 | Definitions exist; all S021-S030 scenarios are NOT_STARTED |
| L4 | Failure Recovery | 10/10 | 0/10 | 0/10 | Definitions exist; all S031-S040 scenarios are NOT_STARTED |
| L5 | Governance Intelligent Ops | 10/10 | 0/10 | 0/10 | Definitions exist; all S041-S050 scenarios are NOT_STARTED |
| Total | All Levels | 50/50 | 1/50 | 1/50 | S002 is the first validated runtime scenario; all unrelated statuses remain unchanged |

Repository/document structure checks may be run locally, but their results do
not count as S001-S050 implementation, evidence readiness, or runtime validation.

## Environment Note

The EVE-NG host, `SNSD-R1`, `SNSD-SW1`, six VLAN gateways, Router-on-a-Stick,
NAT/PAT, and temporary directional ACL test are operator-confirmed implemented.
The repository contains only the earlier sanitized host bridge/address/route
output plus sanitized KVM, live router/switch state, VLAN/trunk/subinterface,
routing, NAT/counter, persistence, pre-ACL allow, post-ACL deny, reverse permit,
gateway, public-connectivity, post-ACL-removal cleanup, host-only ping, SSH/22,
and HTTP/80 results. E001-E014 are represented, so S002 is
`VALIDATED`/`READY`. HTTPS/443 remains accurately recorded unavailable.

Lab Phase 0 host-capacity, VM allocation, staged execution, and storage policy
documents remain planning artifacts only. They do not add to the scenario
totals; S002 alone accounts for the current 1/50 implementation and validation
totals.

## Update Rule

Update this file whenever a scenario moves to `PLANNED`, `IN_PROGRESS`, `IMPLEMENTED`, `VALIDATED`, `PARTIAL`, `BLOCKED`, or `DEPRECATED`.
