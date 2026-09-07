# L3 Execution Plan

The machine-readable authority is `final-execution-plan.yaml`. Every action
defines objectives, prerequisites, dependencies, inputs, authorized and
protected scope, implementation tasks, acceptance cases, evidence, validators,
rollback, risks, stop conditions, completion criteria, effort, and successors.
The plan does not promote implementation or maturity by itself.

| Phase | Mandatory order |
|---|---|
| 0 | ZT-SCN-RETIRE-001 -> ZT-GOV-MAP-001 -> P0-ACC-001 |
| 1 | P1-ID-ENF-001-RETRY -> P1-NET-CLOSE -> P1-VIS-CLOSE -> P1-CV-001 -> P1-RV-001 -> P1-ACC-001 |
| 2 | Central VIS and ID -> OIDC/MFA/RBAC -> P2-CV-001 -> P2-ACC-001 |
| 3 | P3-ASSET-001 -> parallel control expansion -> P3-CV-001 -> P3-ACC-001 |
| 4 | P4-PAC-001 -> P4-DRIFT-001 -> CI/approved response/dashboard -> P4-ACC-001 |
| 5 | P5-METRIC-001 -> P5-MAT-001 -> P5-PORT-001 -> P5-DEMO-001 -> P1-SCH-001 -> P5-ACC-001 |

## Dependency invariants

- CV requires FND, NET, VIS, and ID.
- RV requires stable validators and accepted CV.
- Phase 1 acceptance requires accepted bounded RV, while SCH is deferred until after the Phase 5 demonstration and before the final L3 decision.
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
bounded historical `REPEATABILITY_ACCEPTED / EC4_REPEATABLE_RUNTIME` decision.
At the 2026-08-20 P1-ACC-001 preflight, all three RV records exceeded the P7D
freshness limit. The historical denial is preserved, and ADR 0014 applies the
reviewed `P1-RV-FRESHNESS-001` exception. P1-ACC-001 is completed as
`ACCEPTED_WITH_GAPS`; a fresh manual RV window remains mandatory before final
scheduling or P5-ACC-001.
The first separately approved manual refresh execution completed at
`2026-08-20T11:59:07.686986Z` with 4 PASS / 6 WARN / 0 FAIL. The current refresh
window is 1/3 at `STALE / EC3 / IN_PROGRESS`; the second run is not eligible
before `2026-08-21T11:59:07.686986Z`. Phase 2 partial runtime work continues in
parallel without scheduler use or Phase 2 completion.
P1-SCH-001 retains its historical identifier, but the installed task is disabled
and the action is deferred to the final Phase 5 gate. Re-enabling requires
separate scheduler approval.

Phase 1 is `PARTIAL / PARTIALLY_VALIDATED / COMPLETED_WITH_GAPS`. Phase 2 is
`IN_PROGRESS_PARTIAL_RUNTIME` for P2-VIS-001. The bounded OpenStack deployment
uses one private monitoring VM, one port, one Cinder volume and one attachment,
with no Floating IP. Five fixed components, private mTLS plus Grafana login,
sanitized ingestion, restart persistence, package-only rollback,
preserved-data/offline-image recovery, cleanup and evidence-integrity checks
passed in the accepted EC3 campaign. ZT-VIS-002 is therefore only
`PARTIALLY_IMPLEMENTED / PARTIALLY_VALIDATED / PARTIALLY_ACCEPTED`.
Alert-rule and notification delivery, elapsed-retention behavior, and full
Cinder snapshot rebuild/reattachment restore remain open. Persistent NTP
synchronization, P2-VIS-001 completion, broader central identity, final
scheduling, maturity, and compliance remain unclaimed. L3 remains a target and
L4 remains roadmap-only.
