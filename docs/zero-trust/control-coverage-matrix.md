# Control Coverage Matrix

Coverage is capability-level and conservative. Scenario validation does not automatically validate every mapped capability. Authority values follow the repository evidence-authority enum. Proposed applicability, targets, dependencies, and waves are planning-only fields in the [capability implementation backlog](capability-implementation-backlog.yaml); they do not alter this current-state matrix.

| Capability | Korean name | Pillar | Function | Implementation | Validation | Evidence | Authority | Mapped scenarios | Gap status | Target phase |
|---|---|---|---|---|---|---|---|---|---|---|
| ZT-1.1.1 | 사용자 인벤토리 | identity | identifier-management | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-1.1.2 | ID 연계 및 사용자 자격 증명 | identity | identifier-management | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-1.2.1 | 다중인증 (MFA) | identity | authentication | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-1.2.2 | 지속 인증 | identity | authentication | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-1.3.1 | 통합 ICAM 플랫폼 | identity | risk-assessment | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-1.3.2 | 행동, 컨텍스트 기반 ID 및 생체 인식 | identity | risk-assessment | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-1.4.1 | 조건부 사용자 접근 | identity | access-management | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-1.4.2 | 최소 권한 접근 | identity | access-management | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-2.1.1 | 기기 감지 및 규정 준수 | device-endpoint | policy-compliance-monitoring | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-2.2.1 | 실시간 검사를 통한 기기 권한 부여 | device-endpoint | data-access-control | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-2.3.1 | 기기 인벤토리 | device-endpoint | asset-management | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-2.3.2 | 통합 엔드포인트 관리 및 모바일 기기 관리 | device-endpoint | asset-management | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-2.4.1 | 엔드포인트 및 확장된 탐지·대응 (EDR 및 XDR) | device-endpoint | device-threat-protection | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-2.4.2 | 자산, 취약성 및 패치 관리 자동화 | device-endpoint | device-threat-protection | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-3.1.1 | 매크로 세그멘테이션 | network | network-segmentation | MAPPED | PARTIALLY_VALIDATED | RUNTIME | USER_EXECUTED_RUNTIME; CODEX_EXECUTED_LIVE_RUNTIME | S002, S003, S004, S005, S014, S015, S016 | PARTIAL | Phase 1 |
| ZT-3.1.2 | 마이크로 세그멘테이션 | network | network-segmentation | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 1 |
| ZT-3.1.3 | 소프트웨어 정의 네트워킹 | network | network-segmentation | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 1 |
| ZT-3.2.1 | 위협 대응 | network | threat-response | MAPPED | REFERENCE_ONLY | DESIGN | DESIGN_ONLY | S037 | MAPPED_NOT_VALIDATED | Phase 1 |
| ZT-3.3.1 | 트래픽 암호화 | network | traffic-encryption | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 1 |
| ZT-3.4.1 | 데이터 흐름 매핑 | network | traffic-management | MAPPED | PARTIALLY_VALIDATED | RUNTIME | USER_EXECUTED_RUNTIME; CODEX_EXECUTED_LIVE_RUNTIME | S002, S003, S004, S005, S023, S024 | PARTIAL | Phase 1 |
| ZT-3.5.1 | 네트워크 회복성 | network | network-resilience | MAPPED | REFERENCE_ONLY | DESIGN | DESIGN_ONLY | S035 | MAPPED_NOT_VALIDATED | Phase 1 |
| ZT-4.1.1 | 접근통제 | system | access-control | MAPPED | PARTIALLY_VALIDATED | RUNTIME | CODEX_EXECUTED_LIVE_RUNTIME | S005, S011, S012, S013, S014, S015, S016, S017, S018, S020 | PARTIAL | Phase 1 |
| ZT-4.2.1 | PAM | system | system-account-management | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 1 |
| ZT-4.2.2 | 자격 증명 관리 | system | system-account-management | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 1 |
| ZT-4.3.1 | 네트워크 세분화 및 그룹 간 이동 | system | network-separation-policy | MAPPED | PARTIALLY_VALIDATED | RUNTIME | USER_EXECUTED_RUNTIME | S002, S003, S004, S014, S015, S016 | PARTIAL | Phase 1 |
| ZT-4.4.1 | 시스템 환경에 따른 정책 관리 | system | system-security-policy-management | MAPPED | REFERENCE_ONLY | DESIGN | DESIGN_ONLY | S037, S041, S042, S043, S044 | MAPPED_NOT_VALIDATED | Phase 1 |
| ZT-5.1.1 | 리소스 권한 부여 및 통합 | application-workload | application-access | MAPPED | REFERENCE_ONLY | DESIGN | DESIGN_ONLY | S018, S020 | MAPPED_NOT_VALIDATED | Phase 2 |
| ZT-5.2.1 | 지속적인 모니터링 및 진행 중인 승인 | application-workload | application-threat-protection | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-5.3.1 | 원격 접속 | application-workload | accessible-application | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-5.4.1 | 안전한 애플리케이션 배포 | application-workload | secure-application-deployment | MAPPED | REFERENCE_ONLY | DESIGN | DESIGN_ONLY | S044 | MAPPED_NOT_VALIDATED | Phase 2 |
| ZT-5.4.2 | 애플리케이션 인벤토리 | application-workload | secure-application-deployment | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-5.5.1 | 안전한 소프트웨어·애플리케이션 개발 및 통합 | application-workload | software-application-security | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-5.5.2 | 소프트웨어 취약 관리 | application-workload | software-application-security | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-6.1.1 | 데이터 카탈로그 위험 정렬 | data | data-inventory-management | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-6.1.2 | 기업 데이터 거버넌스 | data | data-inventory-management | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-6.2.1 | 데이터 접근제어 | data | access-decision-method | MAPPED | REFERENCE_ONLY | DESIGN | DESIGN_ONLY | S017 | MAPPED_NOT_VALIDATED | Phase 2 |
| ZT-6.3.1 | 데이터 암호화 및 권한 관리 | data | data-encryption | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-6.4.1 | 데이터 라벨링 및 태그 지정 | data | data-classification | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-6.5.1 | 데이터 손실 방지 (DLP) | data | data-loss-prevention | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-6.5.2 | 데이터 모니터링 및 감지 | data | data-loss-prevention | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-7.1 | 모든 관련 활동 기록 | visibility-analytics | visibility-analytics | MAPPED | PARTIALLY_VALIDATED | RUNTIME | USER_EXECUTED_RUNTIME; CODEX_EXECUTED_LIVE_RUNTIME | S005, S036 | PARTIAL | Phase 2 |
| ZT-7.2 | 중앙집중적 보안 정보 및 이벤트 관리 | visibility-analytics | visibility-analytics | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-7.3 | 보안 위협 분석 | visibility-analytics | visibility-analytics | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-7.4 | 사용자 및 기기 동작 분석 | visibility-analytics | visibility-analytics | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-7.5 | 위협 인텔리전스 통합 | visibility-analytics | visibility-analytics | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-7.6 | 자동화된 동적 정책 | visibility-analytics | visibility-analytics | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 2 |
| ZT-8.1 | 정책 통합 | automation-integration | automation-integration | MAPPED | REFERENCE_ONLY | DESIGN | DESIGN_ONLY | S043, S044 | MAPPED_NOT_VALIDATED | Phase 3 |
| ZT-8.2 | 중요 프로세스 자동화 | automation-integration | automation-integration | MAPPED | PARTIALLY_VALIDATED | RUNTIME | CODEX_EXECUTED_LIVE_RUNTIME | S005 | PARTIAL | Phase 3 |
| ZT-8.3 | 인공지능 | automation-integration | automation-integration | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 3 |
| ZT-8.4 | 보안 통합, 자동화 및 대응 | automation-integration | automation-integration | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 3 |
| ZT-8.5 | 데이터 교환 표준화 | automation-integration | automation-integration | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 3 |
| ZT-8.6 | 보안 운영 조정 및 사고 대응 | automation-integration | automation-integration | GAP_IDENTIFIED | GAP_IDENTIFIED | NONE | MISSING | 0 | GAP_IDENTIFIED | Phase 3 |
