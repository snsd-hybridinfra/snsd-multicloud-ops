# 프로젝트 방법론

플랫폼 제품 흐름은 `사용자 요구 -> 카탈로그 -> 정책/승인 -> 자동화 -> OpenStack/k3s/네트워크 -> 관측/수명주기`를 따른다. 아래 Zero Trust 통제 검증 흐름은 이 제품 흐름을 가로지르는 독립 보안 품질 게이트이며 플랫폼 구현 상태를 대신하지 않는다.

## 필수 작업 흐름

```text
Zero Trust capability selected
-> target asset identified
-> KISA applicability assessed
-> version and environment checked
-> current state inspected
-> service impact assessed
-> backup and rollback prepared
-> minimum safe enforcement applied
-> positive behavior tested
-> negative behavior tested
-> bypass tested
-> persistence tested
-> rollback tested
-> sanitized evidence produced
-> package status evaluated
-> maturity impact assessed separately
```

## 원칙

- 점검 결과만 보고 맹목적으로 조치하지 않는다.
- 구성 파일의 존재만으로 성공을 추론하지 않는다.
- 문서나 로컬 테스트를 런타임 검증으로 바꾸지 않는다.
- 도구 개수나 평균 점수로 성숙도를 정하지 않는다.
- 서비스 가용성과 제3자 소유 구성을 보호한다.
- 잠금 위험이 있으면 독립 복구 경로를 유지한다.
- 최소 안전 변경, 사전 상태, 백업, 롤백과 증적을 한 세트로 관리한다.
- 제한사항, 예외와 잔여 위험을 그대로 기록한다.

## 상태 결정

플랫폼 제품 상태, 계획, 아키텍처, 매핑, 구현, 로컬 검증, 런타임 검증, 런타임 수용, 증적, 성숙도와 컴플라이언스 상태는 서로 독립적이다. 단일 `PASS`로 축약하지 않는다.
