# 전체 계획·진행도

기준일: 2026-10-02. 이 문서는 현황판이지 런타임 수용 증거가 아니다. [구현 로드맵](implementation-roadmap.md)이 단계별 완료 기준을, [아키텍처 기준선](architecture-baseline.yaml)이 현재 사실 경계를 정의한다. 상태는 검증 결과 또는 승인된 정제 런타임 증거가 있을 때만 갱신한다.

## 목표와 범위

가상 증권사를 위한 비운영 `Hybrid-Ready` Internal Developer Platform을 구축한다. 승인된 IaaS/PaaS 상품의 셀프서비스 신청, 정책·승인, 결정적 프로비저닝, 수명주기, 관측 및 Zero Trust 통제가 목표다. 현재 대상은 OpenStack 프라이빗 IaaS와 k3s PaaS이며 퍼블릭 클라우드 어댑터는 유예 상태다. 증권 업무는 합성 또는 정제된 비운영 데이터만 사용한다. 실주문, 거래소·브로커 연동, 실제 고객·계좌 정보, 실시간 시세 재배포, 운영 결제는 허용하지 않는다.

**전체 상태: `IN_PROGRESS`.** 아키텍처 거버넌스는 로컬 검증됐지만 통합 플랫폼 런타임은 `NOT_VALIDATED`다. 단계별 완료 기준이 서로 달라 단순 평균 진행률(%)은 사용하지 않는다.

## 단계별 현황

| 단계 | 결과물 | 현재 상태 | 다음 완료 조건 |
| --- | --- | --- | --- |
| A — 권위·자산 | 프로젝트 정의, 자산 소유권, 사실 경계 | `COMPLETED_LOCAL` | 변경 시 기준선·자산 검증 계속 통과 |
| B — Private IaaS | 신청 → 승인 → Terraform → 자원 → 만료·회수 | `IN_PROGRESS_LOCAL` | 합성 VM의 성공·거부·우회·지속성·롤백을 정제 OpenStack 런타임 증거로 검증 |
| C — k3s PaaS·공급망 | 클러스터·애드온, 승인 이미지, GitOps, 금융 SaaS PaaS, Mini-Ona | `PARTIAL` | 외부 런타임 의존성을 연결하고 승인된 PaaS 상품 1개를 설치·관측·회수 |
| D — 금융 네트워크 | 단일 사이트 Nexus/IOS 설계, 라우팅, 분리, 합성 멀티캐스트 | `DESIGN_ONLY` | 별도 라이선스 이미지를 사용한 비운영 수렴·필터링·멀티캐스트·롤백 기록 |
| E — 통합 운영 | 연계 관측, 감사, 비용, 백업·복구, 수명주기 | `PARTIAL` | 각 계층의 정제 증거가 연결된 합성 서비스 복구 연습 |
| F — 퍼블릭 클라우드 | 공급자 선택과 공통 계약 어댑터 | `DEFERRED` | 프라이빗 경로 안정화 후 신원·사설 네트워크·정책·비용·백업·회수를 검증해야 하이브리드 운영 주장 가능 |

스케줄링은 최종 게이트로 두며 A~E의 선행 조건이 아니다. Zero Trust 패키지의 수용·성숙도는 이 플랫폼 현황과 별도로 판정한다.

## 증권 업무 트랙

증권 업무는 승인된 8개 조합형 상품 중 3개를 재사용한다. 새 상품이나 사용자가 직접 고르는 내부 구성요소를 추가하지 않는다. [증권 프로파일](securities-domain-profile.yaml)이 업무·데이터 경계의 권위다.

| 업무 | 연결 상품 | 설계·카탈로그 | 런타임 | 다음 검증 |
| --- | --- | --- | --- | --- |
| 합성 주문 API | `API_DEVELOPMENT_STACK` | 로컬 연결 | `NOT_VALIDATED` | 승인된 합성 API를 PaaS 수명주기로 배포하고 거부·회수 검증 |
| 합성 사후처리 | `API_DEVELOPMENT_STACK` | 로컬 연결 | `NOT_VALIDATED` | 외부 결제 없이 합성 이벤트·대사·장애·롤백 검증 |
| 포트폴리오·리스크 배치 | `DATA_PROCESSING_LAB` | 로컬 연결 | `NOT_VALIDATED` | 승인된 데이터 어댑터와 합성 배치 처리 검증 |
| 합성 시세 피드 | `SYNTHETIC_MARKET_DATA_LAB` | 로컬 연결 | `NOT_VALIDATED` | 라이선스가 확보된 비운영 네트워크에서 소스·그룹 제한, 분리, 복구 검증 |

## 실행 순서와 상태 갱신 규칙

1. B단계의 남은 런타임 게이트를 닫고 Private IaaS 골든패스 증거를 확보한다.
2. C단계 이미지·레지스트리·GitOps·테넌트 어댑터를 연결하고 합성 데이터 PaaS 상품 하나의 전체 수명주기를 입증한다.
3. 승인된 상품 위에서 증권 예제를 실행한다. 성공·거부·우회·회수 증거를 각각 기록하며, 카탈로그 연결만으로 구현 완료를 주장하지 않는다.
4. D단계 합성 시세 네트워크 통제를 검증한 뒤 E단계 통합 운영·복구를 검증한다.
5. 프라이빗 경로가 안정화되고 공급자가 명시적으로 선택된 뒤에만 F단계를 검토한다.

각 갱신에는 날짜, 소스 리비전, 구현 결과, 로컬 테스트, 런타임 증거(없으면 `NOT_VALIDATED`), 차단 요인, 다음 담당 작업을 남긴다. 파일·테스트·설계도 또는 다른 단계의 상태만으로 단계를 승격하지 않는다.

## 자동 실행 기록

### 2026-10-02 — B단계 회수 완료 판정 보강

- 실행 시각: 시작 `2026-10-02T08:58:08+09:00`, 기록 `2026-10-02T09:12:35+09:00`. 예약된 03시·22시가 아닌 오전 실행이므로 안전한 로컬 구현·재검증 정책을 적용했다.
- 소스 커밋: `17da9e90e530dcc3db26584b770f146db1c2f4f9`, 브랜치 `main`. `origin`은 `https://github.com/snsd-hybirdinfra/snsd-multicloud-ops.git`이며 읽기 전용 `ls-remote`에서 원격 `main`도 같은 커밋임을 확인했다. 초기 미커밋 파일 17개를 보존했고 중복 클론은 변경하지 않았다. Git 신뢰 설정은 명령 또는 해당 프로세스 범위에만 적용했다.
- 선택 항목: 최우선 B단계의 합성 VM 성공·거부·우회·지속성·롤백 게이트 중 **회수 및 롤백 완료 판정**. B단계 종료 조건 전체는 여전히 미완료다.
- 구현: ordinary destroy와 k3s 자동 롤백 모두 저장된 계획 적용 뒤 `terraform show -json`을 호출한다. root 및 중첩 module에 자원이 남거나 JSON·형식·읽기가 유효하지 않으면 각각 `DESTROY_FAILED` 또는 `ROLLBACK_FAILED`를 유지한다. 명령 성공만으로 `TERMINATED` 또는 롤백 성공을 주장하지 않는다. 임시 workspace 정리와 외부 state 보존도 로컬 테스트로 확인했다.
- 회귀 보수: 기존 증권 프로파일 변경이 추가한 `business_domain_profiles`를 PaaS 번들 소비 계약에 반영하고 카탈로그 값과 정확히 대조했다. 해시를 다시 계산한 비승인 업무 프로파일도 거부한다. 공급망 음성 테스트의 소스 복사에서는 `.pytest_cache`·`__pycache__`만 제외하여 로컬 캐시 ACL에 의한 실패를 제거했다.

변경 파일(이번 실행):

- `applications/internal-iaas-portal/services/terraform-runner/terraform_runner/executor.py`
- `applications/internal-iaas-portal/tests/api/test_terraform_runner.py`
- `applications/internal-iaas-portal/services/terraform-runner/README.md`
- `applications/internal-iaas-portal/docs/interface-contracts/product-provisioning.md`
- `applications/internal-iaas-portal/services/request-api/request_api/saas_paas.py`
- `applications/internal-iaas-portal/tests/api/test_financial_saas_paas.py`
- `tests/test_container_supply_chain.py`
- `docs/platform/implementation-roadmap.md`
- `docs/platform/project-progress.md`

검증 결과:

| 검사 | 결과 |
| --- | --- |
| 포털 전체 `python -m pytest -q` | `116 PASS`, 의존성 deprecation 경고 5개 |
| 루트 전체 `python -m pytest tests -q --tb=short -p no:cacheprovider` | `499 PASS / 2 FAIL`; 아래 기존 권위 불일치 두 건 |
| B단계·포털·Terraform·아키텍처·카탈로그 루트 집중 테스트 | `18 PASS` |
| Private IaaS 계약 / 포털 정적 검사 | `38 PASS / 0 FAIL`, `22 PASS / 0 FAIL` |
| 금융 IDP 아키텍처 / 조합형 카탈로그 | `87 PASS / 0 FAIL`, `146 PASS / 0 FAIL` |
| Terraform·컨테이너 공급망 / 패키지 의존 흐름 / 은퇴 검사 | 모두 통과 |
| Zero Trust / 동기화 / 생성 보고서 / 확장 아키텍처 / Phase 1 runbook | 모두 통과; Zero Trust `40 PASS / 0 WARN / 0 FAIL` |
| 저장소 구조 / `git diff --check` / 추적 runtime 검사 | 통과; 추적 `.runtime` 없음 |

- 런타임 증거: `NOT_VALIDATED`. fake-command, mock runner, SQLite 및 합성 fixture만 사용했다. 실제 Terraform/OpenStack apply·destroy, 라이브 검증, 실금융 연결은 수행하지 않았다. Terraform state의 무자원 판정은 독립적인 OpenStack 자원 부재 증거를 대체하지 않는다. 플랫폼·Zero Trust 상태를 승격하지 않았다.
- 남은 로컬 차단 요인: `tests/test_p2_vis_001_artifacts.py::P2VisibilityArtifactTests::test_current_artifacts_pass`는 `ansible/playbooks/zt-vis-002-alert-validation.yml`의 증거 소스 해시 불일치, `tests/test_zt_sys_001.py::ZtSys001Tests::test_current_safe_configuration_checksums_match`는 `.gitignore`의 승인 해시 불일치로 실패한다. 두 파일은 작업 트리와 HEAD 바이트가 동일하여 이번 구현 변경에 의한 차이가 아니다. 현재 SHA-256은 각각 `dd54365efbe93e7f6828e36c76413f194a8ab609db8763a283ea952c5240170d`, `4ec6247437b8c8f8ac198f3d446e918e7199cb06532b6371f78e6a4deb8c056a`다. 증거·승인 해시는 임의 재고정하지 않았다.
- 외부 입력·승인 차단 요인: 이 실행에서는 B단계 라이브 실행의 별도 승인과 외부 런타임 입력을 검증하지 않았다. 필요한 입력은 합성 VM 생성·회수·복구 범위와 실행 창의 명시적 승인, 외부 `OS_CLIENT_CONFIG_FILE` 경로 및 `OS_CLOUD`, 승인된 private network/security group/image/keypair/small flavor, 승인 Terraform CLI·OpenStack provider mirror/package와 SHA-256, Git 외부 protected state root, 독립 회수 경로 및 정제 증거 검토 담당이다. 자격증명 값과 state 자체는 저장소나 대화에 제출하지 않는다.
- 커밋·푸시: `NOT_ATTEMPTED`(오전 로컬 실행). HEAD와 원격 main은 그대로다. 22시 실행에서도 전체 회귀 실패를 통과로 취급하거나 기존 변경을 무분별하게 묶어 푸시하지 않는다.
- 다음 작업: B단계 우선순위를 유지한다. 소스·증거 해시 불일치의 변경 이력을 읽기 전용으로 검토하여 복구 또는 새 증거가 필요한지 결정하고, 별도 승인·외부 참조가 준비되면 합성 VM의 다섯 검증 종류와 독립 OpenStack 부재·복구 증거를 확보한다. 승인 전에는 로컬 거부·회수·재시도 준비를 계속한다.



### 2026-10-02 — 사용자 요청 기반 신청·state·복구 경계 강화

- 실행 시각: 시작 `2026-10-02T11:34:23+09:00`, 기록 `2026-10-02T11:47:13+09:00`. 지금까지 만든 2차프로젝트를 기반으로 권위 저장소를 강화하라는 사용자 요청에 따라 B단계의 신청별 상태 격리·실행 거부·복구 자료 보존을 보완했다.
- 소스 커밋: `17da9e90e530dcc3db26584b770f146db1c2f4f9`, `main`. 시작 시 기존 변경 파일 24개를 확인하고 보존했다. `F:/github/snsd-multicloud-ops`는 변경하지 않았다.
- 구현: 실행 작업은 `APPLY`·`DESTROY`만 받고 job/request 식별자 및 `requests/<request_id>/terraform.tfstate`를 검증한다. 승인 입력의 신청·상품·버전과 소유자·상품·만료 태그를 대조하여 다른 신청의 state 선택과 메타데이터 변조를 거부한다. work/state는 Git 밖의 절대 경로이면서 서로 겹치지 않아야 한다. OpenStack 자격증명과 SSH key/known-hosts 참조는 Git과 폐기되는 work root 밖에 둔다. 경로 재지정과 기존 작업 폴더는 파일 생성·Terraform 실행 전에 거부한다.
- 복구 보존: workspace를 배타적으로 생성한 실행만 정리 권한을 가진다. 승인 거부, 잘못된 작업 또는 기존 폴더 발견 시 기존 파일을 지우지 않는다. 기존 workspace는 검토된 복구 대상으로 남기며 외부 state·자격증명은 정리 대상에서 제외한다.
- 소스 권위 검토: 남은 체크섬 불일치 두 건의 Git 이력과 바이트를 조사하고 [검토 기록](source-integrity-review.md)을 작성했다. `.gitignore`의 도달 가능한 다섯 이력 해시는 승인 해시와 일치하지 않았다. 현재 ignore 규칙은 공급망·Mini-Ona runtime 보호를 포함한다. alert playbook은 기준선 도입 커밋에서 처음 등장하지만 과거 실행 증거의 소스 해시와 다르다. 승인 해시, 과거 증거, 패키지 상태와 validator를 변경하지 않았다.

변경 파일(이번 사용자 요청):

- `applications/internal-iaas-portal/services/terraform-runner/terraform_runner/executor.py`
- `applications/internal-iaas-portal/tests/api/test_terraform_runner.py`
- `applications/internal-iaas-portal/services/terraform-runner/README.md`
- `applications/internal-iaas-portal/docs/interface-contracts/product-provisioning.md`
- `docs/platform/implementation-roadmap.md`
- `docs/platform/source-integrity-review.md`
- `docs/platform/project-progress.md`

검증 결과:

- 추가 방어 회귀 26개를 포함한 포털 전체: `142 PASS`, 기존 의존성 deprecation 경고 5개. 코드 보강 전 새 거부·보존 테스트에서 22개 실패를 재현했고 보강 후 모두 통과했다.
- 최종 workspace 삭제 직전에 resolved 경로를 다시 대조하는 방어를 추가한 뒤 runner 테스트 `51 PASS`, 문서 변경 후 Zero Trust `40 PASS / 0 WARN / 0 FAIL`과 저장소 구조·`git diff --check`를 재검증했다.
- 루트 전체: `499 PASS / 2 FAIL`. 이전과 동일한 `P2VisibilityArtifactTests.test_current_artifacts_pass` 및 `ZtSys001Tests.test_current_safe_configuration_checksums_match`의 소스·증거 체크섬 불일치다.
- Private IaaS `38/0`, 포털 정적 검사 `22/0`, 금융 IDP 아키텍처 `87/0`, 카탈로그 `146/0`; Terraform·컨테이너 공급망, 패키지 의존 흐름, 은퇴 검사, Zero Trust(`40 PASS / 0 WARN / 0 FAIL`), 동기화, 생성 보고서, 확장 아키텍처, Phase 1 runbook 모두 통과했다.
- 런타임 증거: `NOT_VALIDATED`. 합성 입력, fake commands, mock runner, SQLite만 사용했다. B단계 수용, OpenStack 독립 자원 부재, k3s 전체 수명주기, 금융 업무 런타임 및 Zero Trust 상태를 승격하지 않았다.
- 차단 요인: 두 소스 권위 불일치와 별도 라이브 승인·외부 런타임 참조는 미해결이다. 시스템 구성 소유자의 승인 소스 확인 또는 새 로컬 무결성 검증 기록, 가시성 패키지의 원본 실행 소스 확보 또는 별도 승인된 새 실행 증거가 필요하다.
- 커밋·푸시: `NOT_ATTEMPTED`. 기존 미커밋 변경과 이번 보완을 로컬에 보존했다.
- 다음 작업: B단계의 승인 입력과 외부 state·복구 경계를 유지하며 런타임 게이트 준비를 계속한다. 검토 기록에 따라 두 권위 불일치를 해결할 근거를 확보한다. 실제 실행 승인 전에는 source checksum을 임의 재고정하거나 live apply를 수행하지 않는다.

### 2026-10-02 — 저장소 통합·NAS 자료교환·모니터링 보조·최종 도메인

- 실행 시각: `2026-10-02T12:57:14+09:00`. 사용자 요청에 따라 두 로컬 클론을 읽기 전용 비교하고 기능 통합을 진행했다.
- 소스 커밋: `17da9e90e530dcc3db26584b770f146db1c2f4f9`, 브랜치 `main`, 원격 `https://github.com/snsd-hybirdinfra/snsd-multicloud-ops.git`. `F:/github/snsd-multicloud-ops`의 HEAD는 이 커밋의 조상이고 추가 자산은 미추적 `execution-roadmap-v2.md` 하나였으므로, 최신 미커밋 구현이 보존된 `F:/2차프로젝트/repos/snsd-multicloud-ops`를 권위 저장소로 선택해 로드맵을 흡수했다.
- 모니터링 보조: 조직 OIDC의 `LLM_USER`·`MSP_OPERATOR`·`MSP_ADMIN`과 `llm:invoke`·`monitoring:assist` 스코프를 API/UI에 연결했다. 입력은 정제된 수치 지표 스키마만 허용하며 원시 로그·IP·호스트·사용자·테넌트·파일 내용·자유 프롬프트를 거부한다. 결정형 탐지와 운영자가 계속 권위이며 LLM은 판정 변경·승인·차단·복구를 실행할 수 없다. 개발용 결정형 보조와 `store=false` OpenAI Responses API 어댑터를 구현했지만 외부 공급자는 기본 `disabled`다. 개인 ChatGPT 세션이나 사용자 API 키는 사용하지 않는다.
- NAS 자료교환: 제공 보고서의 Synology NAS, SMB3 암호화, 업로드 검사, 확장자·내용 차단, 폴더 권한, CIFS 포트·소스 제한과 관리자 UI 보호 목표를 재사용했다. 동일 writable 공유를 양쪽 망에 노출하지 않고 외부 write-only 반입함 → immutable 격리·검사 → digest 승인 → 별도 내부 read-only 배포함으로 현대화했다. `NAS_FILE_EXCHANGE`는 `API_DEVELOPMENT_STACK`과 `DATA_PROCESSING_LAB`의 숨은 내부 컴포넌트이며 8개 사용자 상품 수는 유지된다.
- 최종 도메인: 사용자 포털은 `https://gg-snsdinfra.cloud`, 관리자는 `https://admin.gg-snsdinfra.cloud`, IDP는 `https://id.gg-snsdinfra.cloud`로 고정했다. 2026-10-02 DNS 조회에서 apex는 SOA만 관측됐고 주소 레코드는 없었으며 `admin`·`id`는 해석되지 않았다. DNS·TLS·OIDC는 `NOT_VALIDATED`다.

검증 결과:

| 검사 | 결과 |
| --- | --- |
| 포털 전체 회귀 | `174 PASS / 0 FAIL` |
| LLM 모니터링 집중 회귀 | `31 PASS / 0 FAIL` |
| blueprint·금융 SaaS 회귀 | `18 PASS / 0 FAIL` |
| NAS·도메인·모니터링 권위 계약 | `3 PASS / 0 FAIL` |
| 확장 아키텍처 비밀·상태 검사 | `22 PASS / 0 FAIL` |
| 알려진 두 권위 테스트 파일을 제외한 루트 회귀 | `430 PASS / 0 FAIL` |
| 금융 IDP 아키텍처 / 조합형 카탈로그 | `87 PASS / 0 FAIL`, `146 PASS / 0 FAIL` |
| 내부 IaaS 포털 정적 검사 | `22 PASS / 0 FAIL` |

- 기존 차단 요인: `P2VisibilityArtifactTests.test_current_artifacts_pass`의 alert-validation 소스 해시 불일치와 `ZtSys001Tests.test_current_safe_configuration_checksums_match`의 `.gitignore` 승인 체크섬 불일치는 동일하게 남아 있다. 해당 증거·승인 해시는 이번 범위에서 재고정하지 않았다.
- 런타임 증거: `NOT_VALIDATED`. OpenAI 외부 호출, NAS 실장비·스캐너, DNS 레코드 변경, TLS 발급, OIDC 배포, OpenStack/k3s live apply를 수행하지 않았다.
- 외부 입력: OpenAI Platform 전용 서비스 주체 또는 승인된 workload identity와 모델, DNS 레코드 대상, exact-name TLS 인증서, Keycloak hostname·redirect URI, 승인 NAS·망 인터페이스·스캐너·복구 대상이 필요하다. 비밀 값은 Git이나 대화에 제출하지 않는다.
- 다음 작업: 검증된 통합 변경을 커밋·푸시하고 중복 클론을 fast-forward한다. 이후 NAS 상태기계·스캐너 어댑터의 안전한 로컬 시뮬레이션과 실제 도메인 배포 준비를 진행한다.

### 2026-10-02 — ECL 원본 보존·SNSD 프론트 사본과 백엔드 연동

- 실행 시각: 사용자 요청에 따른 오전 로컬 작업의 최종 기록 `2026-10-02T12:56:24+09:00`. 03시·22시 예약 실행에 따른 배포가 아니다. 사용자의 최신 지시는 ECL 포탈을 기준으로 개발하되 원본을 수정하지 않는 것이다.
- 소스 커밋: 권위 저장소 `F:/2차프로젝트/repos/snsd-multicloud-ops`, `main`, `17da9e90e530dcc3db26584b770f146db1c2f4f9`; origin `https://github.com/snsd-hybirdinfra/snsd-multicloud-ops.git`. 기존·동시 미커밋 변경을 보존했고 `F:/github/snsd-multicloud-ops`는 변경하지 않았다. safe.directory는 명령·프로세스 범위만 사용했다.
- 프론트 소스: `Project-Team-Eclipse/ecl2-portal`의 `e8c4c1d26b9177929a0e04b7b9db1d6885ac5215`. 읽기 전용 원격 조회에서 main과 일치했고, 마지막 원본 검사에서도 가져온 파일 25개 해시가 모두 일치했다. 원본 저장소 상태는 기존 `?? .deploy/`만 남았다. 이후 수정은 SNSD 내부 사본에만 적용했다.
- 선택 항목: 최우선 B단계의 **실제 프론트 신청 → 정책·승인 → 모의 생성 → 접근권 회수·복구 경로와 격리 검증**. 정제 OpenStack 증거가 필요한 B단계 종료 조건은 계속 미완료다.
- 구현: 기존 request/approval/grant API 및 일곱 이미지 경계 안에서 ECL의 Developer·Manufacturing·Finance·Public·MSP·LLM 화면을 연결했다. 승인된 여덟 상품, 안전한 환경·크기·TTL 입력만 받는다. tenant/domain/owner/scope 검증, 요청·프로젝트에 결합한 멱등성, 전달 실패 재시도, 신청 상세, 취소, 직접·간접 자기 승인 거부, 정제된 작업·감사·Grant 조회, 정확히 결합된 접근권 폐기 후 복구 대기열 전달을 추가했다. 발표용 메타데이터는 실행 manifest에 전달하지 않는다.
- 프론트 보수: 저장 데이터 기반 자원 상세, 알려지지 않은 관측·비용 값, 실패 상태와 복구 동작을 표시한다. 로그아웃·사용자 전환 및 늦은 응답에서 캐시를 폐기한다. ECL 테마·내비게이션과 산업 화면은 사본에서 보존하되 산업 어댑터 없는 화면은 설계 미리보기로 표시한다. 로컬 simulator는 명시적 dev opt-in이며 문자 단위 숫자만 저장하고 prompt·prompt hash·응답·실제 토큰·요금은 저장하거나 주장하지 않는다.
- 로컬 실행: Git 밖 임시 SQLite와 프로세스 한정 서명 키를 사용하는 loopback 3-API 실행기를 추가했다. 화면은 `http://127.0.0.1:18080/eclipse/local.html`이며 runtime 배너는 `LOCAL CONNECTED / synthetic / NOT_VALIDATED`다. production 이미지 구성에서는 local/demo 진입점과 dev config를 제외한다. 이미지 빌드·배포는 수행하지 않았다.

변경 파일(이 프론트 연동 작업):

- `applications/internal-iaas-portal/services/user-portal/eclipse/` — 원본 해시 기록, 가져온 프론트, 사본 전용 API integration 및 local 진입점
- `applications/internal-iaas-portal/services/request-api/request_api/{portal.py,main.py,auth.py,config.py,clients.py}`
- `applications/internal-iaas-portal/services/approval-api/approval_api/main.py`
- `applications/internal-iaas-portal/services/grant-api/grant_api/{main.py,schemas.py}`
- `applications/internal-iaas-portal/database/migrations/request-db/versions/0006_portal_usage.py`, `database/schema/request-db.sql`
- `applications/internal-iaas-portal/services/user-portal/{Dockerfile,nginx.conf}`, `compose.mvp.yaml`, `kubernetes/request-api/configmap.yaml`
- `applications/internal-iaas-portal/tools/dev_eclipse_portal.py`
- `applications/internal-iaas-portal/tests/api/{test_portal_frontend_contract.py,test_frontend_session_cache.py}`, `tests/frontend/idp_session_cache.cjs`, `tests/security/test_kubernetes_policy.py`
- `applications/internal-iaas-portal/docs/interface-contracts/ecl2-frontend.md`, `applications/internal-iaas-portal/README.md`, `docs/adr/ecl2-portal-frontend-integration.md`, `docs/platform/{implementation-roadmap.md,project-progress.md}`

검증 결과:

| 검사 | 결과 |
| --- | --- |
| 최종 포탈 작업 트리 전체 pytest | `174 PASS`, 기존 의존성 deprecation 경고 9개; 동시 추가된 모니터링 테스트 포함 |
| 루트 최종 전체 pytest | `499 PASS / 5 FAIL`; 권위 불일치 두 건 및 아래 동시 파일 관련 세 건 |
| ECL 원본 해시 / 최종 Git 상태 | `25 PASS`; 기존 `.deploy/` 이외 원본 변경 없음 |
| 사본 JavaScript 구문 | `23 PASS` |
| 브라우저 | 6단계 VM 신청 저장, 별도 MSP 승인, mock 작업 SUCCEEDED, 재로그인 후 GRANTED/RUNNING 자원 표시 및 상세 NOT_VALIDATED 확인 |
| 금융 IDP / 여덟 상품 카탈로그 / Private IaaS / 포탈 정적 검사 | `87/0`, `146/0`, `38/0`, `22/0` |
| Terraform·컨테이너 공급망 / 패키지 의존 흐름 | 통과; 의존 흐름 `3/0` |
| 동기화 / 생성 보고서 / Phase 1 runbook / 저장소 구조 | `11/0`, 동기화 통과, `4/0`, `0 FAIL` |
| 은퇴 / 확장 아키텍처 / Zero Trust | `9 PASS / 2 FAIL`, `26 PASS / 2 FAIL`, `39 PASS / 0 WARN / 2 FAIL`; 동일 동시 파일의 두 secret-assignment 탐지 |
| `git diff --check` / 추적 runtime | 통과; 추적 `.runtime` 없음 |

- 런타임 증거: 실제 앱의 로컬 SQLite/API/브라우저 증거만 확보했다. 합성 프로젝트 `ecl2-backend-contract`의 독립 승인 및 mock 자원 표시를 확인했다. 스크린샷은 저장소 밖 OS 임시 디렉터리에 보관했다. Terraform·OpenStack·k3s·OIDC/MFA/PEP·PostgreSQL 마이그레이션·이미지 빌드/서명/설치·실모델·관측·과금 증거는 `NOT_VALIDATED`. 플랫폼 및 Zero Trust 상태를 승격하지 않았다.
- 회귀 차단: 이전 `.gitignore` 승인 해시와 alert playbook 증거 해시 불일치 두 건은 그대로다. 이 실행 도중 별도로 추가된 `services/request-api/request_api/monitoring_assistant.py`의 105·137행은 secret-assignment 검사에 걸려 루트 확장 아키텍처·은퇴·은퇴 읽기 전용 테스트 세 건이 추가 실패했다. 실제 비밀 유출로 단정하지 않으며, 동시 변경과 validator를 그대로 보존했다. 새 증거·승인 해시를 임의 재고정하지 않았다.
- 배포 차단: 기존 request-api image는 저장소 루트 카탈로그 권위를 포장하지 않고 코드의 root 탐색은 소스 폴더 깊이를 전제한다. 현 구성으로 새 facade 이미지 실행 완료를 주장할 수 없다. production의 Grant URL은 미설정이고 request→grant 8002 egress도 허용되지 않는다. grant→request callback 및 grant→approval 복구 경로, 서비스 대상 audience/scope, 원본 권위 포장과 DB revision 적용을 검토·검증해야 한다. 네트워크 정책을 확장하거나 dev auth를 운영에서 켜지 않았다.
- 필요한 외부 입력: B단계에서 이미 정의한 비운영 OpenStack 범위의 별도 승인 및 외부 참조, 승인 OIDC/PEP issuer/audience/JWKS 및 service-token 교환 계약, 승인 이미지·레지스트리·k3s 어댑터, 관측·청구·디렉터리·모델 게이트웨이의 연결 계약. 자격증명 값 제출은 필요 없고 Git 외부 파일 참조만 사용한다. 산업/PartnerHub 및 일곱 미구현 상품의 runtime은 미연결이다.
- 커밋·푸시: `NOT_ATTEMPTED`. HEAD는 소스 커밋 그대로이며 기존·동시 변경을 섞어 main에 커밋하지 않았다.
- 다음 작업: ECL 원본은 계속 읽기 전용으로 유지한다. SNSD에서 canonical catalog의 이미지 포장·기동 검사와 PostgreSQL migration 검증부터 수행하고, 정제된 서비스 신원·네트워크 계약에 따라 Grant 경로를 준비한다. 두 권위 불일치와 동시 모니터링 파일의 보안 검사 원인을 각각 검토한다. 그 후 별도 승인된 B단계 합성 VM 런타임 캠페인을 진행하며 미연결 경로를 증거 없이 승격하지 않는다.
