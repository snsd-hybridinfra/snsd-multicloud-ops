# Zero Trust 패키지 권위

## 권위 순서

1. 제로트러스트 가이드라인 2.0: 역량·아키텍처·성숙도 의미
2. 2026 주요정보통신기반시설 기술적 취약점 분석·평가 방법 상세가이드: 자산별 점검·하드닝 참조
3. `capability-catalog.yaml`: 역량 분류 권위
4. `package-flow.yaml`, 패키지 메타데이터와 `package-status.yaml`: 흐름·현재 상태 권위
5. `package-acceptance-cases.yaml`: 행동 검증 계약
6. 패키지 validator와 정제 증적: 실제 결과 권위
7. Markdown: 검토용 표현 계층

KISA 매핑은 구현·검증·컴플라이언스의 증거가 아니다.

## Phase 1

`ZT-ARC-001`이 다음 흐름 전체를 둘러싼다.

```text
ZT-ARC-001 surrounds:
ZT-FND-001 -> ZT-NET-001 -> ZT-VIS-001 -> ZT-ID-001
           -> ZT-CV-001 -> ZT-RV-001 -> ZT-SCH-001
           -> P1-ACC-001
```

Phase 1은 `PARTIAL / PARTIALLY_VALIDATED / NOT_COMPLETE`이며 경계는 `ZT-SCH-001`이다.

```mermaid
flowchart LR
  subgraph ARC["ZT-ARC-001 - architecture authority"]
    FND["ZT-FND-001"] --> NET["ZT-NET-001"] --> VIS["ZT-VIS-001"] --> ID["ZT-ID-001"]
    ID --> CV["ZT-CV-001"] --> RV["ZT-RV-001"] --> SCH["ZT-SCH-001"] --> ACC["P1-ACC-001"]
  end
```

## 경계

- 번호형 시나리오 권위와 후속 번호 체계는 없다.
- 문서·매핑·계획은 구현이나 런타임 상태를 승격하지 않는다.
- L3는 목표이지 현재 성숙도 주장이 아니다.
- L4는 `ROADMAP_ONLY`다.
- KISA 준수, 인증, 생산 준비 또는 전사 검증을 주장하지 않는다.
