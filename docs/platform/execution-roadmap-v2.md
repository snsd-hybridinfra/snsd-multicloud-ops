# IDP 실행 로드맵 2.0

기준일: 2026-09-28
전체 상태: `IN_PROGRESS`
통합 런타임: `NOT_VALIDATED`

이 문서는 가상 증권사 Financial Hybrid-Ready Internal Developer Platform의 실행 순서와 진행 상태를 관리한다. 파일 존재, 설계 완료, 로컬 테스트 통과와 실제 런타임 검증을 구분하며, 증거 없이 상태나 성숙도를 승격하지 않는다.

## 최종 목표

```text
Developer Portal
  -> approved composite blueprint
  -> identity / policy / approval
  -> immutable manifest
  -> Terraform / Ansible / GitOps
  -> OpenStack / k3s / financial network
  -> observability / audit / cost / lifecycle / recovery
```

증권 업무는 합성 주문 API, 합성 사후처리, 포트폴리오·리스크 분석, 합성 시세 피드까지만 포함한다. 실주문, 거래소·브로커 실연동, 실제 고객·계좌 정보, 실시간 시세 재배포 및 운영 결제는 범위 밖이다. 퍼블릭 클라우드는 프라이빗 골든패스가 안정화된 뒤 공급자 어댑터로 추가한다.

## 상태 판정

| 상태 | 의미 |
| --- | --- |
| `DESIGN_ONLY` | 계약·문서만 존재 |
| `IMPLEMENTED_LOCAL` | 코드와 로컬 테스트가 있으나 외부 런타임 증거는 없음 |
| `PARTIAL` | 일부 경로만 구현 또는 검증됨 |
| `RUNTIME_VALIDATED` | 승인 대상에서 성공·실패·우회·정리 증거 확보 |
| `ACCEPTED` | 완료 조건과 증거가 검토되어 기준선으로 채택됨 |
| `DEFERRED` | 선행 조건 충족까지 의도적으로 유예됨 |

단순 진행률은 사용하지 않는다. 각 단계는 완료 조건이 충족됐을 때만 승격한다.

## 우선순위 실행 단계

### R0 저장소와 권위 기준선 통합

현재 상태: `COMPLETE`

- `F:/2차프로젝트/repos/snsd-multicloud-ops`를 최신 권위 저장소로 사용한다.
- `F:/github/snsd-multicloud-ops`의 유일한 추가 권위 후보였던 본 로드맵을 흡수한다.
- 아키텍처, 서비스 카탈로그, 증권 프로파일, 진행도와 배포 도메인을 한 권위 저장소에 둔다.
- 검증된 변경을 의미 단위로 커밋하고 `origin/main`과 동기화한다.
- 중복 저장소는 검증 완료 전 자동 삭제하지 않는다.

완료 조건: 작업 트리가 깨끗하고 로컬 `main`과 `origin/main`이 동일하며 아키텍처·카탈로그 검증기와 관련 회귀 테스트가 통과한다.

### R1 Private IaaS 골든패스

현재 상태: `LOCAL_RECOVERY_VALIDATED / LIVE_BLOCKED`

- 포털 신청 → 정책 → 승인 → 불변 매니페스트 → Terraform → 자원 등록 → 만료·회수 흐름을 고정한다.
- OpenStack 자격증명과 state는 저장소 밖에서만 주입한다.
- 합성 VM의 정상, 거부, 변조, 부분 실패, 롤백, 재시도, 만료·삭제를 검증한다.

완료 조건: 승인된 비운영 OpenStack 대상에서 전체 흐름을 완주하고 정제 증거와 복구 결과를 남긴다.

### R2 k3s PaaS와 컨테이너 공급망

현재 상태: `PARTIAL`

- CI에서 승인 베이스 이미지, SBOM, 스캔, 서명과 불변 digest를 생성한다.
- GHCR/GitHub Release, GitOps 승격 PR, Argo CD 설치 경계를 연결한다.
- namespace, quota, Pod Security, default-deny NetworkPolicy, ingress, registry, secrets reference와 관측 계약을 적용한다.
- Mini-Ona는 일반 금융 SaaS와 분리하고 강격리, brokered egress, 예산, 승인 재개 경계를 유지한다.

완료 조건: 승인된 PaaS 상품 하나가 요청부터 설치, 관측, 롤백, 만료·회수까지 통과한다.

### R3 증권 업무 상품화

현재 상태: `IMPLEMENTED_LOCAL / RUNTIME_NOT_VALIDATED`

| 업무 | 조합형 상품 | 다음 구현·검증 |
| --- | --- | --- |
| 합성 주문 API | `API_DEVELOPMENT_STACK` | 합성 계좌·주문·체결 API, 거부 정책, TTL 회수 |
| 합성 사후처리 | `API_DEVELOPMENT_STACK` | 합성 이벤트, 대사, 재처리, 실패 롤백 |
| 포트폴리오·리스크 | `DATA_PROCESSING_LAB` | 합성 포지션·가격 배치, quota, 결과 정제 |
| 합성 시세 피드 | `SYNTHETIC_MARKET_DATA_LAB` | 소스·그룹 제한, 멀티캐스트 분리, 장애 복구 |

NAS 자료교환은 새 상품이 아니라 `API_DEVELOPMENT_STACK`과 `DATA_PROCESSING_LAB`의 숨은 내부 컴포넌트다. 외부 반입함, 격리 검사, digest 승인, 내부 읽기 전용 배포함을 거치며 실제 금융 자료는 사용하지 않는다.

완료 조건: 네 업무가 승인된 기존 상품을 통해 요청되고 실제 데이터나 외부 시장 연결 없이 정상·거부·회수 증거를 남긴다. 새 사용자 선택형 상품이나 자유 조합은 추가하지 않는다.

### R4 금융 네트워크 패브릭

현재 상태: `DESIGN_ONLY`

- 단일 사이트 주소·VRF·VLAN·라우팅·관리망 소유권을 고정한다.
- NX-OS/IOS-XE 템플릿과 EVE-NG 테스트를 정제된 형태로 관리한다.
- BGP/OSPF 수렴, 경로 필터, 세그먼트 우회 차단, 합성 멀티캐스트와 롤백을 검증한다.
- NAS 외부 반입, 격리 검사와 내부 배포 영역 사이에 동일 writable share를 허용하지 않는다.

완료 조건: 사용자가 별도 제공한 라이선스 이미지로 비운영 에뮬레이터 검증을 통과한다. 이미지는 Git에 저장하지 않는다.

### R5 통합 운영과 복구

현재 상태: `PARTIAL`

- 요청 ID와 trace ID로 인프라, PaaS와 증권 워크로드의 metrics·logs·traces·audit·cost를 연결한다.
- 결정형 이상 탐지 뒤에 정제 수치만 받는 LLM 모니터링 보조 계층을 둔다. 결과는 비권위이며 차단·복구를 실행하지 않는다.
- NAS 교환의 수신·검사·승인·배포·거부·만료 상태를 파일명이나 본문 없이 집계 지표로 관측한다.
- 백업/복구와 선언적 재구축을 검증하되 다중 사이트 DR을 주장하지 않는다.
- 자원 상태, 알림, 비용, 만료와 회수 결과를 포털에 표시한다.

완료 조건: 합성 증권 서비스 하나의 장애 탐지, 보조 분석, 복구, 비용·감사 추적과 최종 회수를 정제 증거로 연결한다.

### R6 퍼블릭 클라우드 어댑터

현재 상태: `DEFERRED`

- R1~R5의 프라이빗 경로가 수용된 뒤 공급자를 선택한다.
- 공통 신원·정책·사설 연결·비용·상태·백업·회수 계약을 구현한다.

완료 조건: 선택 공급자에서 전체 계약과 teardown을 검증한 뒤에만 실제 하이브리드 운영 상태로 승격한다.

## 배포 기준

- 사용자 포털 canonical origin: `https://gg-snsdinfra.cloud`
- 관리자 포털: `https://admin.gg-snsdinfra.cloud`
- 조직 IDP: `https://id.gg-snsdinfra.cloud`
- DNS, 인증서 SAN, OIDC redirect와 실제 배포 증거가 모두 없으면 `NOT_VALIDATED`를 유지한다.

## 매일 두 번 실행

### 03:00

1. 저장소·원격·최근 실패와 차단 요인을 재확인한다.
2. 가장 높은 우선순위의 미완료 조건 하나를 선택한다.
3. 문서, 코드, 테스트와 안전한 로컬 구현을 진행한다.
4. 관련 검증을 실행하고 실패 원인을 수정한다.
5. 외부 승인이 필요하면 필요한 입력을 기록하고 다음 안전 작업으로 이동한다.

### 22:00

1. 03:00 결과와 새 변경을 검토한다.
2. 같은 우선순위 단계의 완료 조건을 최대한 닫는다.
3. 아키텍처·카탈로그·보안·회귀 검증을 실행한다.
4. 검증된 변경만 의미 단위로 커밋하고 권위 브랜치를 `origin`에 푸시한다.
5. 상태, 차단 요인과 다음 작업을 실제 결과에 맞게 갱신한다.

각 실행은 검증 가능한 작업 한 묶음에서 종료한다. 강제 푸시, 브랜치 삭제, 프로덕션 접근, 실제 금융 데이터 사용과 비인가 live apply는 수행하지 않는다.

## 다음 작업 큐

1. `R2`: 공급망 외부 차단 요인을 재확인하고 GitOps·정책 검증을 마무리한다.
2. `R3`: NAS 어댑터의 상태기계와 스캐너 계약을 안전한 로컬 시뮬레이션으로 구현한다.
3. `R1`: 승인된 OpenStack 입력과 실행 창이 준비되면 골든패스 live 검증을 수행한다.
4. `R5`: OpenAI Platform 서비스 주체와 OIDC 스코프가 준비되면 외부 모니터링 보조 호출을 검증한다.

## 진행 기록

각 실행은 실행 시각과 소스 커밋, 선택한 항목, 변경 파일, 검증 결과, 런타임 증거 또는 `NOT_VALIDATED`, 차단 요인, 커밋 SHA·푸시 결과와 다음 작업을 기록한다. 상태 변경은 구현 로드맵, 아키텍처 기준선과 관련 서비스 권위 파일에 함께 반영한다.
