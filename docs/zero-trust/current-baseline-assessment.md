# Current Zero Trust Baseline Assessment

## Assessment Scope

- Assessment date: 2026-07-17
- Environment: non-production SNSD portfolio lab and repository governance artifacts
- Source: 제로트러스트 가이드라인 2.0, December 2024
- Scenario boundary: locked S001-S050 only
- Evaluator: Codex second-pass documentation QA

This is an evidence-based, capability-level baseline. It is not a compliance assessment, certification, enterprise-wide assessment, or overall maturity score.

## Target Architecture Boundary

[ZT-ARC-001](target-architecture/README.md) defines Advanced targets and a
repository-local `OPTIMAL_READY` extension design. It is `DESIGN_ONLY` /
`LOCAL_VALIDATED` and does not change this current assessment. Target
selection, implementation, validation, evidence, and current maturity remain
independent.

## Evidence Sources

- User-executed sanitized EVE-NG runtime evidence under S002
- User-executed sanitized OpenStack AIO runtime evidence under S005
- Codex-executed restricted live read-only S005 validation evidence
- Codex-executed bounded ZT-NET-001 persistent ACL and ZT-VIS-001 persistent
  telemetry evidence
- Scenario definitions and repository tracking matrices
- Local repository structure and quality validators

## Current Implementation Boundary

Runtime evidence supports bounded macro-segmentation, one persistent directional
inter-zone policy in EVE-NG, a limited OpenStack AIO provider/tenant data path,
restricted read-only control-plane validation, sanitized evidence capture, and
single-node persistent storage for approved sanitized telemetry. It does not
establish complete micro-segmentation, continuous identity verification,
endpoint compliance, PAM, EDR/XDR, DLP, enterprise security event management,
dynamic policy, automated response, complete data governance, or
organization-wide operation.

## Capability Coverage Summary

<!-- BEGIN GENERATED ZERO TRUST SUMMARY -->
Generated from `capability-catalog.yaml` and `current-baseline-assessment.yaml`. Do not edit this block manually.

These dimensions overlap; validation, maturity, and evidence are reported separately.

| Validation status | Count |
|---|---:|
| VALIDATED | 0 |
| PARTIALLY_VALIDATED | 12 |
| IMPLEMENTED | 0 |
| REFERENCE_ONLY | 5 |
| PLANNED | 0 |
| GAP_IDENTIFIED | 35 |
| NOT_APPLICABLE | 0 |

| Maturity | Count |
|---|---:|
| UNASSESSED | 52 |
| TRADITIONAL | 0 |
| INITIAL | 0 |
| ADVANCED | 0 |
| OPTIMAL | 0 |
| NOT_APPLICABLE | 0 |

| Evidence level | Count |
|---|---:|
| NONE | 35 |
| DESIGN | 5 |
| CONFIGURATION | 0 |
| RUNTIME | 12 |
| CONTINUOUS | 0 |

| Domain | Capabilities |
|---|---:|
| identity | 8 |
| device-endpoint | 6 |
| network | 7 |
| system | 5 |
| application-workload | 7 |
| data | 7 |
| visibility-analytics | 6 |
| automation-integration | 6 |
<!-- END GENERATED ZERO TRUST SUMMARY -->

## Validated Capabilities

None. Scenario-level validation does not establish full capability validation.

## Partially Validated Capabilities

| Capability | Korean name | Evidence scenarios | Evidence level | Confidence |
|---|---|---|---|---|
| ZT-3.1.1 | 매크로 세그멘테이션 | S002, S003, S004, S005, S014, S015, S016 | RUNTIME | MEDIUM |
| ZT-3.4.1 | 데이터 흐름 매핑 | S002, S003, S004, S005, S023, S024 | RUNTIME | MEDIUM |
| ZT-4.1.1 | 접근통제 | S005, S011, S012, S013, S014, S015, S016, S017, S018, S020 | RUNTIME | MEDIUM |
| ZT-4.3.1 | 네트워크 세분화 및 그룹 간 이동 | S002, S003, S004, S014, S015, S016 | RUNTIME | MEDIUM |
| ZT-7.1 | 모든 관련 활동 기록 | S005, S036 | RUNTIME | MEDIUM |
| ZT-8.2 | 중요 프로세스 자동화 | S005 | RUNTIME | MEDIUM |

## Mapped-Only Capabilities

| Capability | Korean name | Scenario references | Authority |
|---|---|---|---|
| ZT-3.2.1 | 위협 대응 | S037 | DESIGN_ONLY |
| ZT-3.5.1 | 네트워크 회복성 | S035 | DESIGN_ONLY |
| ZT-4.4.1 | 시스템 환경에 따른 정책 관리 | S037, S041, S042, S043, S044 | DESIGN_ONLY |
| ZT-5.1.1 | 리소스 권한 부여 및 통합 | S018, S020 | DESIGN_ONLY |
| ZT-5.4.1 | 안전한 애플리케이션 배포 | S044 | DESIGN_ONLY |
| ZT-6.2.1 | 데이터 접근제어 | S017 | DESIGN_ONLY |
| ZT-8.1 | 정책 통합 | S043, S044 | DESIGN_ONLY |

## Unassessed Capabilities and Gaps

All 52 capabilities have `current_maturity: UNASSESSED`. 39 capabilities have no direct implementation or runtime evidence and are marked `GAP_IDENTIFIED`. The authoritative gap list is [gap-register.md](gap-register.md); detailed per-capability state is in [current-baseline-assessment.yaml](current-baseline-assessment.yaml).

## Confidence Limitations

- Evidence is limited to a single non-production lab and repository-local validation.
- Most scenarios are `NOT_STARTED` under the tracking authority.
- Runtime checks cover selected paths and points in time, not continuous operation.
- User-executed and Codex-executed evidence are identified separately.
- No capability-specific source maturity table has been fully assessed.

## Next Recommended Priorities

1. Implement and validate bounded identity access controls without claiming continuous authentication.
2. Add endpoint inventory/posture evidence before mapping device capabilities.
3. Preserve the bounded directional ACL and expand policy coverage only through separately approved designs without relabeling VLANs as micro-segmentation.
4. Implement application/workload authorization and secure-deployment evidence under existing scenarios.
5. Establish data ownership, classification, access-control, and encryption scope before data-pillar assessment.
6. Add any new security-relevant telemetry source only with least-privilege collection, minimization, retention, and availability evidence.
7. Assess one bounded capability against its detailed Chapter 3 maturity table; do not calculate a repository-wide score.

## ZT-NET-001 bounded evidence update

The 2026-07-22 ZT-NET-001 execution adds one persistent directional ACL with
39 PASS, 0 WARN, 0 FAIL, 5/5 gateway allow, 0/5 Kubernetes deny, 5/5 public
allow, counter evidence, and startup persistence. The 2026-07-22 ZT-VIS-001
increment adds pinned single-node Grafana/Loki/Alloy storage with 336-hour
retention and post-restart query evidence for approved sanitized JSONL. These
bounded package validations do not promote any capability-wide status or
maturity; broader network and visibility gaps remain explicit.
