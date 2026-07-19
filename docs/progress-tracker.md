# Progress Tracker

This file tracks scenario-based progress across the five validation levels.

## Status Values

Scenario status values: `NOT_STARTED`, `PLANNED`, `IN_PROGRESS`, `IMPLEMENTED`, `VALIDATED`, `PARTIAL`, `BLOCKED`, `DEPRECATED`

Evidence status values: `NOT_READY`, `PARTIAL`, `READY`, `REVIEWED`

## Level Summary

| Level | Category | Scenarios | Implemented | Validated | Notes |
|---|---|---:|---:|---:|---|
| L1 | Foundation | 10/10 | 2/10 | 2/10 | S002 EVE-NG foundation and S005 OpenStack AIO network path are VALIDATED with READY evidence |
| L2 | Security Baseline | 10/10 | 0/10 | 0/10 | Definitions exist; all S011-S020 scenarios are NOT_STARTED |
| L3 | Service Operations | 10/10 | 0/10 | 0/10 | Definitions exist; all S021-S030 scenarios are NOT_STARTED |
| L4 | Failure Recovery | 10/10 | 0/10 | 0/10 | Definitions exist; all S031-S040 scenarios are NOT_STARTED |
| L5 | Governance Intelligent Ops | 10/10 | 0/10 | 0/10 | Definitions exist; all S041-S050 scenarios are NOT_STARTED |
| Total | All Levels | 50/50 | 2/50 | 2/50 | S002 and S005 are validated; all unrelated statuses remain unchanged |

## Zero Trust Documentation Progress

- Authoritative source processing: complete for the documentation framework.
- Top-level domains represented: 8/8.
- Detailed capability records: 52/52.
- Existing scenario mappings reviewed: 50/50.
- Conservative second-pass mappings: 22 mapped and 28 `REVIEW_REQUIRED`/`NOT_MAPPED`.
- Current capability baseline: 0 fully validated, 6 partially validated in the bounded lab scope, 7 mapped-only, and 39 gap-identified.
- Capability maturity assessments completed: 0/52; all remain `UNASSESSED`.
- Capability implementation backlog: 52/52 planning records schema-validated; 17 `LAB_IMPLEMENTABLE`, 27 `PARTIALLY_LAB_IMPLEMENTABLE`, and 8 `REFERENCE_ONLY`.
- Planning artifacts: dependency model, Waves W0-W5, control patterns, verification plan, phase gates, queue, and future-scenario governance documented.
- Scenario implementation and validation counts: unchanged at 2/50.
- ZT-FND-001 restricted-validation package: `IMPLEMENTED` / `VALIDATED`; OpenStack returned 50 PASS/0 WARN/0 FAIL and EVE-NG returned 42 PASS/0 WARN/0 FAIL through forced endpoints with required boundary denials.
- ZT-NET-001 restricted-router package: `IMPLEMENTED` / `PARTIALLY_VALIDATED`; the live endpoint returned 38 PASS/1 WARN/0 FAIL and blocked interactive, arbitrary, configuration, and arbitrary-ping requests. The remaining warning is the absence of a persistent interface ACL binding. No S001-S050 scenario count or capability maturity changed.
- ZT-VIS-001 telemetry package: `IMPLEMENTED` / `PARTIALLY_VALIDATED`; four live bounded sources produced 164 normalized events, seven deterministic non-blocking rules loaded, live correlation produced zero findings, and one controlled fixture produced the expected finding. Persistent central storage is not installed. No S001-S050 scenario count or capability maturity changed.
- ZT-ID-001 bounded identity policy package: `PRESENT` / `IMPLEMENTED` / `LOCAL_VALIDATED`; synthetic identity inventory, roles, authentication requirements, lifecycle, deterministic decisions, schemas, validator, 9 positive cases, and 34 negative cases are locally validated. Runtime identity validation is `NOT_VALIDATED`, MFA/OIDC/RBAC are not deployed, maturity remains `UNASSESSED`, and no scenario status changed.
- ZT-ARC-001 target architecture: `DESIGN_ONLY` / `LOCAL_VALIDATED`; all 52 capabilities are represented as 21 Advanced primary, 15 Advanced supporting, 4 Initial, 5 design-only, and 7 future Optimal-roadmap selections. Nine schemas, 29 runbooks, three profile templates, six ADRs, and the architecture validator exist. No scenario, capability current state, or maturity changed.
- ZT-VIS-002 monitoring dependency: active work exists only under the ignored runtime boundary. It is not tracked evidence, not accepted as a package result, and remains protected from architecture edits.

Documentation framework completion does not advance scenario status, evidence
readiness, capability implementation, capability validation, or maturity.
Backlog applicability and proposed target maturity are planning judgments only
and do not change the current capability baseline.

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
totals.

The operator also completed a non-production Kolla-Ansible single-node AIO
deployment. Supplied results cover control-plane health, Neutron provider and
tenant resources, Open vSwitch mapping, EVE-NG VLAN 70 integration, Floating IP
DNAT, instance gateway/Internet reachability, and cloud-init completion. Codex
normalized and sanitized those results, then independently corroborated the
current state through a forced-command read-only endpoint: 50 PASS, 0 FAIL,
exit 0. S005 therefore accounts for the second implemented/validated scenario.

## Update Rule

Update this file whenever a scenario moves to `PLANNED`, `IN_PROGRESS`, `IMPLEMENTED`, `VALIDATED`, `PARTIAL`, `BLOCKED`, or `DEPRECATED`.
