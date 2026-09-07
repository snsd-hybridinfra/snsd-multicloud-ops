# SNSD Financial Hybrid-Ready Internal Developer Platform

**공식 프로젝트명:** 가상 증권사 Hybrid-Ready Private Cloud 기반 Internal Developer Platform 구축
**English:** Financial Hybrid-Ready Private Cloud Internal Developer Platform

이 저장소는 금융권 운영·개발 조직이 승인된 IaaS와 PaaS를 셀프서비스로 신청하고, 정책에 따라 자동 프로비저닝·운영·회수할 수 있는 비운영 플랫폼 랩이다. OpenStack을 프라이빗 IaaS, k3s를 PaaS 실행면, Terraform·Ansible·GitOps를 자동화 계층으로 사용한다. Nexus NX-OS/IOS-XE 기반 금융 네트워크를 목표 언더레이로 두고, Zero Trust는 플랫폼 전체를 보호하고 검증하는 횡단 보안 통제면이다.

현재 외부 퍼블릭 클라우드는 연결하지 않았으므로 프로젝트를 `Hybrid-Ready`로 표현한다. AWS·Azure·KT Cloud 등 특정 공급자 연동은 공통 계약을 통과하는 어댑터로만 추가하며, 실제 연결과 검증 전에는 하이브리드 운영 완료를 주장하지 않는다.

## 목표 구조

```text
금융 업무·개발 조직
        |
        v
Developer Portal / Approved Composite Blueprints / Request & Approval / Lifecycle
        |
        v
Policy Gate / Terraform / Ansible / GitOps / Agent Job Orchestration
        |
        +---------------------+
        |                     |
        v                     v
OpenStack Private IaaS     k3s PaaS
        |                     |
        +----------+----------+
                   v
 Nexus/IOS Underlay · Segmentation · Routing · Multicast

횡단 통제: Zero Trust · Observability · Audit · Backup/Restore · FinOps
미래 확장: Provider Adapter -> approved public cloud
```

## 프로젝트 권위

- 플랫폼 목표와 경계: [`docs/platform/README.md`](docs/platform/README.md)
- 목표 아키텍처: [`docs/platform/target-architecture.md`](docs/platform/target-architecture.md)
- 구현 로드맵: [`docs/platform/implementation-roadmap.md`](docs/platform/implementation-roadmap.md)
- 기계 판독 기준선: [`docs/platform/architecture-baseline.yaml`](docs/platform/architecture-baseline.yaml)
- 승인된 조합형 상품 카탈로그: [`docs/platform/composite-service-catalog.yaml`](docs/platform/composite-service-catalog.yaml)
- Project Mini-Ona 샌드박스 계약: [`docs/platform/ai-agent-sandbox.yaml`](docs/platform/ai-agent-sandbox.yaml)
- 아키텍처 결정: [`docs/adr/0018-financial-hybrid-ready-idp.md`](docs/adr/0018-financial-hybrid-ready-idp.md)
- 현재 Zero Trust 상태: [`docs/zero-trust/package-status.yaml`](docs/zero-trust/package-status.yaml)

## 현재 진실

- 프로젝트 전환: `ACCEPTED / LOCAL_GOVERNANCE_VALIDATED`
- OpenStack IaaS: 기존 비운영 랩 자산 보유; IDP 통합은 `PARTIAL`
- k3s PaaS: 후보 자동화와 별도 `platform/` 자산 보유; 루트 권위 통합은 `PARTIAL`
- Project Mini-Ona: 8개 상품 중 `AI_AGENT_SANDBOX`; 상태 머신, 비배포 Kubernetes 번들, Redis-ready DB outbox, credential lease, brokered-egress, 원자적 예산 예약과 정제 Trace 저장소는 `PARTIALLY_IMPLEMENTED_LOCAL`, 외부 서비스와 라이브 런타임은 `NOT_VALIDATED`
- IDP 포털: 로컬 후보 구현; 배포는 `NOT_AUTHORIZED`
- Nexus/IOS 금융 네트워크 언더레이: `DESIGN_ONLY`; 라이선스 이미지와 런타임 증적 없음
- 퍼블릭 클라우드 어댑터: `DEFERRED / NOT_IMPLEMENTED`
- Zero Trust: 기존 패키지 상태와 증적을 그대로 유지하며 자동 승격하지 않음
- 추적 `.runtime/**`, 자격증명, Terraform state, kubeconfig, 장비 이미지는 금지

## 보안 프로그램

기존 **제로트러스트 가이드라인 2.0 기반 멀티클라우드 보안통제 구현 및 기술적 취약점 자동 검증 체계 구축**
(**Implementation of Multi-Cloud Security Controls and Automated Technical Vulnerability Validation Based on Zero Trust Guideline 2.0**)과 포트폴리오명 **증적 기반 제로트러스트 멀티클라우드 보안 운영 플랫폼**은 삭제하지 않고 이 플랫폼의 보안·검증 프로그램으로 편입한다.

`ZT-ARC-001`은 플랫폼을 둘러싼 Zero Trust 아키텍처 권위이며, 패키지·검증기·정제 증적·상태 결정의 독립성은 계속 유지한다. 번호형 시나리오 프레임워크는 은퇴 상태다.

## 읽기 전용 검증

```powershell
python tools/validate_financial_idp_architecture.py --strict
python tools/validate_composite_service_catalog.py --strict
python tools/validate_ai_agent_sandbox.py --strict
python tools/validate_private_iaas_golden_path.py --strict
python tools/validate_zt_project_definition.py --strict
python tools/validate_scenario_retirement.py --strict
python tools/validate_zero_trust.py --strict
python tools/check_zero_trust_sync.py
python -m unittest discover -s tests
```
