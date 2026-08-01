# L3 Execution Plan

The machine-readable authority is `final-execution-plan.yaml`. Every action
defines objectives, prerequisites, dependencies, inputs, authorized and
protected scope, implementation tasks, acceptance cases, evidence, validators,
rollback, risks, stop conditions, completion criteria, effort, and successors.
The plan does not promote implementation or maturity by itself.

| Phase | Mandatory order |
|---|---|
| 0 | ZT-SCN-RETIRE-001 -> ZT-GOV-MAP-001 -> P0-ACC-001 |
| 1 | P1-ID-ENF-001-RETRY -> P1-NET-CLOSE -> P1-VIS-CLOSE -> P1-CV-001 -> P1-RV-001 -> P1-SCH-001 -> P1-ACC-001 |
| 2 | Central VIS and ID -> OIDC/MFA/RBAC -> P2-CV-001 -> P2-ACC-001 |
| 3 | P3-ASSET-001 -> parallel control expansion -> P3-CV-001 -> P3-ACC-001 |
| 4 | P4-PAC-001 -> P4-DRIFT-001 -> CI/approved response/dashboard -> P4-ACC-001 |
| 5 | P5-METRIC-001 -> P5-MAT-001 -> P5-PORT-001 -> P5-DEMO-001 -> P5-ACC-001 |

## Dependency invariants

- CV requires FND, NET, VIS, and ID.
- RV requires stable validators and accepted CV.
- SCH requires accepted RV; Phase 1 acceptance requires SCH.
- OIDC requires central identity; RBAC requires OIDC or equivalent integration.
- Phase 2 CV requires central identity and visibility.
- Multi-environment validation requires two genuinely different deployed environments.
- Drift requires authoritative desired-state policy.
- L3 assessment requires a complete evidence index and open-gap register.

## Current planning truth

`ZT-SCN-RETIRE-001`, `ZT-GOV-MAP-001`, `P0-ACC-001`,
`P1-ID-ENF-001-RETRY`, `P1-NET-CLOSE`, and `P1-VIS-CLOSE` are completed from
reviewed Git and action evidence. ZT-ID-001, ZT-NET-001, and ZT-VIS-001 remain
accepted only within their recorded bounded scopes.

P1-CV-001 is completed with a bounded `PASS_WITH_OPEN_GAPS` decision. Its
2026-07-28 read-only cycle completed 8 PASS / 2 WARN / 0 FAIL with no blocked
gate. P1-RV-001 is completed with three eligible consecutive successes and a
bounded `REPEATABILITY_ACCEPTED / EC4_REPEATABLE_RUNTIME` decision.
P1-SCH-001 has not begun and requires separate scheduler approval.

Phase 1 remains `PARTIAL / PARTIALLY_VALIDATED / NOT_COMPLETE`. Persistent NTP
synchronization, central visibility, broader central identity, scheduling,
maturity, and compliance remain unclaimed. L3 remains a target and L4 remains
roadmap-only.
