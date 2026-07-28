# Zero Trust Implementation Roadmap

The authoritative post-Phase-1 roadmap is
[ZT-ARC-001](target-architecture/phase-roadmap.md). The machine dependency
authority is
[implementation-dependency-map.yaml](target-architecture/implementation-dependency-map.yaml).
The 52-capability backlog and Waves W0-W5 remain planning inputs; neither a
phase nor a queue position promotes current state or maturity.

## Phase 1 - Foundation and Verification Operations

Boundary: `ZT-SCH-001` (`DESIGN_ONLY`).

Phase state: `PARTIAL` implementation / `PARTIALLY_VALIDATED` validation /
`NOT_COMPLETE` completion. `ZT-ID-001` is `PRESENT`, `IMPLEMENTED`, and
`RUNTIME_VALIDATED`; runtime validation is `VALIDATED` and acceptance is
`ACCEPTED` for one `BOUNDED_NON_PRODUCTION_TARGET`. Maturity is `UNASSESSED`,
and the Phase 2 centralized-identity dependency remains open. `ZT-DEV-001` is
`IMPLEMENTED` / `PARTIALLY_RUNTIME_VALIDATED` for six classified aliases and
one mandatory live VM; reboot review, dedicated scanning, broad endpoint
coverage, EDR/XDR, patch automation, and device-based enforcement remain open.
`ZT-APP-001` is `IMPLEMENTED` / `PARTIALLY_RUNTIME_VALIDATED` for two
applications, four workloads, a partial three-image direct-component SBOM, and
one unchanged Alloy pilot. Immutable digests, signing, transitive component
coverage, dedicated vulnerability scanning, application authorization,
Kubernetes runtime, automated deployment, and maturity remain open.
`ZT-DATA-001` is `IMPLEMENTED` / `PARTIALLY_RUNTIME_VALIDATED` for seven
metadata-only assets, manual classification, six default-deny policies, five
flows, redacted detection-only DLP, and one isolated synthetic restore.
Automatic discovery/classification, enterprise governance, dynamic access,
platform encryption, key management, live backup/restore, blocking DLP,
continuous analysis, and maturity remain open.

The boundary covers restricted validation, evidence governance, automation
safety, repeatable validation, and a scheduled-validation foundation. Actual
completion evidence is separate: `ZT-FND-001`, `ZT-NET-001`, and
`ZT-VIS-001` are validated for their bounded package scopes; `ZT-DEV-001` and
`ZT-APP-001`, and `ZT-DATA-001` are partially runtime validated. The boundary identifier
is not itself an implementation package result.

`ZT-AUTO-001` and `ZT-CV-001` are implemented and partially runtime validated
at one-time EC3 boundaries. ZT-CV-001 is bounded `PARTIALLY_ACCEPTED` after the
clean FND remediation and the 8/2/0 integrated cycle. `ZT-RV-001` is
implemented and in progress with one accepted independent execution; EC4
still requires two additional consecutive successes separated by at least 24
hours. `ZT-SCH-001` remains unimplemented and blocked by RV acceptance, so
Phase 1 remains not complete.

## Phase 2 - Centralized Identity and Visibility

Phase state: `DESIGN_ONLY`. No Phase 2 package is promoted by this roadmap.

Primary use case: protect Grafana through centralized identity, OIDC, MFA,
role mapping, explicit allow/deny behavior, and access-decision telemetry.
Monitoring is an enabling platform.

Candidates: `ZT-USE-001`, `ZT-ID-002`, `ZT-APP-002`, `ZT-ACC-001`,
`ZT-PEP-001`, `ZT-VIS-002`, and `ZT-EFF-001`. The existing queue's
`ZT-ID-001` remains the approved bounded Phase 1 identity predecessor; `ZT-ID-002` is a later
candidate, not a rename. Active `ZT-VIS-002` work under `.runtime` remains an
unaccepted dependency until sanitized package evidence passes review.

Exit requires runtime-validated monitoring and identity stacks, OIDC, MFA,
role mapping, allow and deny behavior, access-decision telemetry, and sanitized
evidence.

## Phase 3 - Cross-Domain Policy Enforcement

Candidates: `ZT-PIP-001`, `ZT-POL-002`, `ZT-NET-002`, `ZT-SYS-002`,
`ZT-DEV-002`, `ZT-COR-001`, `ZT-INC-001`, `ZT-AUTO-002`, `ZT-RESP-001`, and
`ZT-REC-001`.

Exit requires connected selected trust signals, a validated policy-decision
model and PEP, deterministic correlation, an approval boundary for response,
and recovery validation.

## Phase 4 - IaC, Configuration as Code, and Policy as Code Convergence

Candidates: `ZT-ONB-001`, `ZT-IAC-001`, `ZT-IAC-002`, `ZT-CFG-001`,
`ZT-PAC-001` through `ZT-PAC-004`, `ZT-DRIFT-001`, `ZT-PLN-001`, and
`ZT-DEP-001`.

Exit requires a validated target profile, at least one IaC path, existing-VM
or physical-server onboarding, Configuration as Code idempotency, a Policy as
Code deny test, deployment gate, drift detection, and approved reconciliation.

## Phase 5 - Portability, Runbooks, Handoff, and Advanced Acceptance

Candidates: `ZT-RUN-001`, `ZT-HOF-001`, `ZT-MAT-001`, and `ZT-PLT-001`.

Exit requires clean deployment, rollback, backup and restore, clean-operator
handoff, validated runbooks, capability-specific maturity reassessment, and no
unsupported maturity statement.

## Future Phase 6 - Optimal-Maturity Expansion

`ZT-RISK-001`, `ZT-BA-001`, `ZT-PDP-002`, `ZT-PEP-002`, `ZT-AUTO-003`,
`ZT-OPT-001`, and `ZT-OPT-002` are all `NOT_STARTED` / `UNASSESSED` /
`ROADMAP_ONLY`. They require separate scope approval and do not establish
current `OPTIMAL` maturity.

## Common Gates

- Canonical source and capability ownership
- Approved dependency and architecture boundary
- Explicit mutation and service-impact authority
- Secret-free profile and external secret source
- Policy result and approval bound to an unchanged plan hash
- Rollback and validator availability
- Sanitized evidence plan and evidence authority
- Capability-specific source-table assessment
- No overall maturity inference from a lab result
