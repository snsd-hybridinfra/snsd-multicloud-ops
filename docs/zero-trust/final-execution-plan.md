# 권위 있는 L3 실행 계획

기계 권위는 `final-execution-plan.yaml`이다. 모든 action은 목표, 선행조건, 의존성, 입력, 허용·보호 범위, 구현 작업, 수용 사례, 증거, validator, 롤백, 위험, 중단 조건, 완료 기준, effort와 후속 action을 가진다. 이 계획 자체는 인프라 구현을 실행하거나 상태를 승격하지 않는다.

| Phase | Mandatory order |
|---|---|
| 0 | ZT-SCN-RETIRE-001 -> ZT-GOV-MAP-001 -> P0-ACC-001 |
| 1 | P1-ID-ENF-001-RETRY -> P1-NET-CLOSE -> P1-VIS-CLOSE -> P1-CV-001 -> P1-RV-001 -> P1-SCH-001 -> P1-ACC-001 |
| 2 | central VIS and ID -> OIDC/MFA/RBAC -> P2-CV-001 -> P2-ACC-001 |
| 3 | P3-ASSET-001 -> parallel control expansion -> P3-CV-001 -> P3-ACC-001 |
| 4 | P4-PAC-001 -> P4-DRIFT-001 -> CI/approved response/dashboard -> P4-ACC-001 |
| 5 | P5-METRIC-001 -> P5-MAT-001 -> P5-PORT-001 -> P5-DEMO-001 -> P5-ACC-001 |

## Dependency invariants

- CV requires FND, NET, VIS and ID.
- RV requires stable validators and CV.
- SCH requires RV; Phase 1 acceptance requires SCH.
- OIDC requires central identity; RBAC requires OIDC or equivalent integration.
- Phase 2 CV requires central identity and visibility.
- Multi-environment validation requires two genuinely different deployed environments.
- Drift requires authoritative desired-state policy.
- L3 assessment requires a complete evidence index and open-gap register.

## Current planning truth

`ZT-SCN-RETIRE-001`, `ZT-GOV-MAP-001`, `P0-ACC-001`, `P1-ID-ENF-001-RETRY`, `P1-NET-CLOSE`, and `P1-VIS-CLOSE` are recorded as completed from reviewed Git and action evidence. ZT-ID-001 is accepted only for one bounded non-production validator endpoint, ZT-NET-001 only for one bounded directional inter-zone ACL, and ZT-VIS-001 only for four sanitized summary sources plus one single-node local telemetry stack. Persistent NTP synchronization and central visibility remain open and are not claimed. Exactly one next action is `P1-CV-001`; it remains `NOT_STARTED`. Phase 1 remains `PARTIAL / PARTIALLY_VALIDATED / NOT_COMPLETE`, L3 remains a target, and L4 remains roadmap-only.
