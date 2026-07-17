# Maturity Model

## Official Levels

| Level | English | Summary boundary |
|---|---|---|
| 기존 단계 | Traditional | Mainly manual, static, perimeter-oriented characteristics |
| 초기 단계 | Initial | Partial automation and capability-specific lifecycle management |
| 향상 단계 | Advanced | Broader automation, centralized visibility and integrated control |
| 최적화 단계 | Optimal | Dynamic, highly automated policy and interoperability characteristics |
| UNASSESSED | Repository extension | Evidence has not established a source maturity level |
| NOT_APPLICABLE | Repository extension | Capability is outside the assessed scope with justification |

Source: 제로트러스트 가이드라인 2.0, p. 43, Table 3-3; p. 44, Figure 3-2.

## Assessment Rules

1. Capability maturity is evidence-based.
2. Architecture alignment alone does not establish maturity.
3. Documentation alone does not establish implementation.
4. Implementation alone does not establish runtime validation.
5. A higher level requires evidence for the source-defined characteristics being claimed.
6. Lower-level characteristics are not assumed; exceptions are explicit.
7. Confidence is `LOW`, `MEDIUM`, or `HIGH`.
8. One lab does not establish enterprise maturity.
9. Repository-wide Optimal maturity is prohibited without independently supported capability assessments.
10. Aggregate scoring requires a documented formula, evidence threshold, exclusions, and sensitivity analysis.

## Evidence Levels

`NONE` -> `DESIGN` -> `CONFIGURATION` -> `RUNTIME` -> `CONTINUOUS`.

Progression is not automatic. Reassessment occurs after material configuration, evidence, environment, or source changes. Exceptions record scope, owner, rationale, expiry where applicable, and next action.

## Effectiveness and ISMS-P Boundary

The source treats maturity-based assessment and penetration-test-based
effectiveness analysis as related but distinct activities. This repository has
not performed a Zero Trust penetration-test effectiveness assessment. The
source appendix also discusses relationships with ISMS-P requirements;
capability mapping here is neither an ISMS-P assessment nor certification.

Source: 제로트러스트 가이드라인 2.0, Chapter 5 and Appendix Section 6.
