# 매핑 방법론

1. 제로트러스트 역량과 패키지 통제 목적을 선택한다.
2. 인증된 2026 KISA 원문에서 자산 도메인, 정확한 item code, item name과 중요도를 확인한다.
3. 대상 자산·제품·버전·환경과 서비스 영향을 확인한다.
4. `DIRECT`, `SUPPORTING`, `PARTIAL`, `GOVERNANCE_ONLY`, `FUTURE_SCOPE`, `NOT_APPLICABLE` 중 하나를 선택한다.
5. 적용성을 `APPLICABLE`, `CONDITIONALLY_APPLICABLE`, `NOT_APPLICABLE`, `NOT_YET_ASSESSED`로 별도 기록한다.
6. 구현·런타임·증거 상태는 package/control evidence에서만 가져온다.
7. 예외, 보상통제, rollback, version constraint와 limitation을 기록한다.
8. 수용 사례와 증거가 생기기 전에는 구현 또는 준수 상태를 올리지 않는다.

`DIRECT`는 목적의 직접 연관성을 뜻하며 구현 증거가 아니다. 원문 코드가 확인되지 않으면 record를 만들지 않는다.
