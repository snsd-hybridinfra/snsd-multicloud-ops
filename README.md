# 증적 기반 제로트러스트 멀티클라우드 보안 운영 플랫폼

**공식 프로젝트명:** 제로트러스트 가이드라인 2.0 기반 멀티클라우드 보안통제 구현 및 기술적 취약점 자동 검증 체계 구축
**English:** Implementation of Multi-Cloud Security Controls and Automated Technical Vulnerability Validation Based on Zero Trust Guideline 2.0

이 저장소는 제로트러스트 가이드라인 2.0의 역량을 KISA 기술적 취약점 통제와 연결하고, 여러 인프라 환경에서 패키지 단위 보안통제를 구현·검증하며, 허용·거부·우회·지속성·롤백 행동과 정제된 증적을 반복 가능하게 관리하는 보안 엔지니어링 프로젝트다.

다음 주장을 하지 않는다.

- 제품 설치 포트폴리오
- 체크리스트만 수행하는 취약점 진단
- 단순 클라우드 인프라 구축
- 문서만 작성하는 제로트러스트 연구
- KISA 또는 규정 준수 공식 인증
- L3 달성 또는 L4 구현 완료

## 목표와 권위

- 실제 완료 목표: `L3_ADVANCED` - 구현·런타임 검증·수용 증거가 모두 충족된 뒤에만 평가한다.
- 장기 로드맵: `L4_OPTIMAL` - `ROADMAP_ONLY`; 구현·검증·달성을 주장하지 않는다.
- 1차 권위: 제로트러스트 가이드라인 2.0
- 기술 참조: 2026 주요정보통신기반시설 기술적 취약점 분석·평가 방법 상세가이드
- 구현 권위: ZT 패키지와 패키지 소유 구성
- 행동 검증 권위: 패키지 수용 사례
- 결과 권위: 정제된 런타임 증적과 동기화된 상태 기록

매핑이나 문서의 주장은 실제 구현과 증적을 초과할 수 없다.

## 패키지 아키텍처

```text
ZT-ARC-001 surrounds
ZT-FND-001 -> ZT-NET-001 -> ZT-VIS-001 -> ZT-ID-001
           -> ZT-CV-001 -> ZT-RV-001 -> ZT-SCH-001
           -> P1-ACC-001
```

`ZT-ARC-001`은 순차 패키지가 아니라 전체 프로젝트를 둘러싼 아키텍처 권위다. 번호형 시나리오 프레임워크는 은퇴했고 후속 번호 체계는 없다.

## 현재 진실

- 실행 범위: 비운영 EVE-NG 및 OpenStack 실험실과 저장소
- Phase 1: `PARTIAL / PARTIALLY_VALIDATED / NOT_COMPLETE`
- 현재 경계: `ZT-SCH-001`
- 추적 `.runtime/**`: 금지
- 문서 작업에 의한 구현·런타임·수용·성숙도·컴플라이언스 승격: 금지

## 권위 문서

- [프로젝트 정의](docs/project-definition.md)
- [프로젝트 방법론](docs/project-methodology.md)
- [통제 검증 생명주기](docs/control-validation-lifecycle.md)
- [최종 로드맵](docs/zero-trust/final-roadmap.md)
- [실행 계획](docs/zero-trust/final-execution-plan.md)
- [마일스톤과 게이트](docs/zero-trust/milestones-and-gates.md)
- [임계경로](docs/zero-trust/critical-path.md)
- [증거 계획](docs/zero-trust/evidence-plan.md)
- [성숙도 목표](docs/zero-trust/maturity-target.md)
- [KISA 매핑](docs/zero-trust/mappings/README.md)
- [번호형 시나리오 은퇴](docs/zero-trust/governance/scenario-framework-retirement.md)

## 읽기 전용 검증

```powershell
python tools/validate_zt_project_definition.py --strict
python tools/validate_zt_roadmap.py --strict
python tools/validate_zt_execution_plan.py --strict
python tools/validate_zt_dependency_graph.py --strict
python tools/validate_zt_milestones.py --strict
python tools/validate_zt_risk_register.py --strict
python tools/validate_zt_evidence_plan.py --strict
python tools/validate_zt_maturity_target.py --strict
python tools/validate_zt_kisa_mapping.py --strict
python tools/validate_zt_package_acceptance_cases.py --strict
python tools/validate_zt_status_truth.py --strict
python tools/validate_scenario_retirement.py --strict
python tools/validate_zero_trust.py --strict
python tools/check_zero_trust_sync.py
python -m unittest discover -s tests
```
