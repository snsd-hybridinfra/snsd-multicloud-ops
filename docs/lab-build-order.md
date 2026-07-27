# Authoritative Lab Phase Plan

**Status: ACTIVE — the EVE-NG foundation (retired-numbered-case) and OpenStack AIO network path
(retired-numbered-case) are validated; later platform phases remain unvalidated.**

## Authority and Purpose

This is the single authoritative execution order for the non-production SNSD
Multi-Cloud Secure Operations Validation Platform lab. It normalizes earlier
phase labels without provisioning infrastructure or changing the locked retired numbered scenario framework scenario set. A phase entry describes planned work, not implementation or
validation evidence.

Supporting architecture, addressing, cost, lifecycle, and exposure rules are
defined in the documents linked from `docs/lab-reference-architecture.md`.

## Repository Preflight

Before Lab Phase 0:

- review `docs/scope-lock.md`, `docs/excluded-scope.md`, and this plan;
- run repository structure and scenario-quality validators;
- confirm the worktree contains no credential, state, kubeconfig, private key,
  account-specific value, or unsanitized evidence;
- identify the scenario that will own every later evidence artifact.

Preflight proves repository readiness only. It does not prove lab readiness.

## Canonical Phase Order

| Phase | Objective | Primary Work | Exit Condition |
|---|---|---|---|
| Lab Phase 0 | Architecture and host-capacity baseline | Platform roles, address plan, zones, host capacity, VM allocations, staged execution profiles, storage/snapshot policy, cost guardrails, lifecycle, NICs, gateways, external exposure, and ADR | Planning documents agree; profile arithmetic preserves the host reserve; unresolved provider networks remain discovery-required |
| Lab Phase 1 | EVE-NG and bastion network control | On-Prem routing, Bastion path, inter-zone ACLs, and network failure-path planning | Planned routes/ACLs are reviewed; no real device value is committed |
| Lab Phase 2 | OpenStack private cloud | Kolla-Ansible AIO, Neutron tenant/provider networks, router, one instance, Floating IP, and later Terraform reproduction | AIO and end-to-end network path validated; Terraform, Security Group policy, cleanup, storage, and hardening remain pending |
| Lab Phase 3 | Minimum AWS and Azure foundations | One bounded VPC/VNet foundation, subnets, SG/NSG, and optional temporary compute | Cost guardrails and tags pass before apply; temporary compute/public addresses have TTL and cleanup owner |
| Lab Phase 4 | Multi-cloud inventory and optional connectivity | Inventory normalization and optional WireGuard overlay decision | Provider roles and non-overlapping routes are documented; overlay remains optional |
| Lab Phase 5 | Kubernetes service platform | Local Kubernetes workloads, Ingress, reverse proxy, load balancing, and platform-local validation | Service path is healthy and sanitized evidence maps to retired-numbered-case-retired-numbered-case |
| Lab Phase 6 | Database platform | Local MariaDB primary/replica, access control, replication, and lag | Least privilege and replication evidence are complete without credentials or dumps |
| Lab Phase 7 | Observability | Prometheus, Grafana, exporters, Blackbox, and bounded metric collection | Approved targets are observable and committed outputs are sanitized |
| Lab Phase 8 | Failure, backup, and recovery | Controlled failures, backup, restore, rollback, and post-recovery health | Preconditions, manual actions, rollback, and post-checks are evidenced in owning L4 scenarios |
| Lab Phase 9 | Governance and intelligent operations | Drift, policy, cost, cleanup, metric dataset, anomaly analysis, and reporting | Governance judgments reference sanitized inputs and do not claim automated enforcement |
| Lab Phase 10 | Final evidence and reporting | Coverage aggregation, missing-evidence review, final report generation, and repository QA | retired-numbered-case report and repository validators reflect actual evidence maturity without certification claims |

## Phase Gates

Every infrastructure-bearing phase follows:

`Plan -> Apply -> Validate -> Collect sanitized evidence -> Destroy -> Verify cleanup`

- Apply requires an owner, TTL, purpose, cost review, and rollback/cleanup plan.
- Public addresses exist only during an approved validation window.
- AWS/Azure/OpenStack compute stays disabled by default where practical.
- A later phase cannot convert a planning artifact into a validation claim.

## Lab Phase 0 Planning Completion

Lab Phase 0 documentation is complete at the planning level only. It establishes
the host-capacity baseline, 294GB nominal VM disk plan, mutually exclusive
execution profiles, storage roles, snapshot limits, and one-small-Nova-instance
initial ceiling. It does not prove that a VM, router, firewall, network zone,
OpenStack service, Kubernetes service, database, monitoring service, backup
repository, AWS resource, or Azure resource exists.

## Current Evidence State

retired-numbered-case now has partial authoritative runtime evidence for the EVE-NG host bridge,
default route, KVM, live router/switch state, VLAN/trunk/subinterfaces/routes,
NAT/PAT, persistence, pre-ACL permitted traffic, post-ACL denied traffic,
reverse-direction permit, local gateway reachability, and public IPv4
reachability, post-ACL-removal state, host-only ping, SSH/22, and HTTP/80.
HTTPS/443 is accurately recorded unavailable; no required retired-numbered-case gap remains.
Static, sample, synthetic, and provenance-uncertain artifacts created before
the truth-state reset remain quarantined and support no scenario state.

retired-numbered-case additionally records user-executed Kolla-Ansible AIO deployment,
control-plane health, Neutron resource state, Open vSwitch provider mapping,
EVE-NG VLAN 70 reachability, Floating IP DNAT, tenant gateway/Internet
reachability, and cloud-init completion. Codex normalized and sanitized the
supplied results but did not connect to or re-execute checks against the lab.

## Non-Production Disclaimer

This phase plan governs a disposable portfolio lab. It does not authorize cloud
spend, provision resources, prove production readiness, or change any scenario
status by itself.
