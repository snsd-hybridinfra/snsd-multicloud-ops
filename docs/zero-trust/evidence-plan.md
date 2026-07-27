# 증거 계획

모든 action은 `evidence-plan.yaml`에 등록되어 있다. 원시는 `.runtime/zero-trust/<package-or-action>/`에만 두며 Git이 추적하지 않는다. Git에는 검토·정제된 텍스트 기반 증적만 들어간다.

## 증거 분류

source metadata, pre-change, backup, applied change, positive, negative, bypass, persistence, rollback, log, validator와 final decision을 구분한다. 모든 분류가 기술적으로 적용되는 것은 아니며 실행 계획의 action별 요구사항이 최종 기준이다.

## 금지 정보

비밀번호, 개인키, MFA seed, 복구 코드, access token, session cookie, 전체 개인 식별자, raw cloud credential과 사설 절대 경로를 추적하거나 보고서에 넣지 않는다.

## 무결성

증거는 action/package ID, source, timestamp, validator version, 실제 decision, sanitization과 status record를 연결해야 한다. 자료가 있더라도 현재 구성·시각·주체와 일치하지 않으면 수용 증거가 아니다.
