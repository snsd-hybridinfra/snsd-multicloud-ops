#!/usr/bin/env python3
"""Shared read-only validation for ZT-PROJECT-PLAN-001 authorities."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Callable

import validate_zero_trust as core


ROOT = Path(__file__).resolve().parents[1]

PROJECT_TITLE_KO = "제로트러스트 가이드라인 2.0 기반 멀티클라우드 보안통제 구현 및 기술적 취약점 자동 검증 체계 구축"
PROJECT_TITLE_EN = "Implementation of Multi-Cloud Security Controls and Automated Technical Vulnerability Validation Based on Zero Trust Guideline 2.0"
PORTFOLIO_TITLE = "증적 기반 제로트러스트 멀티클라우드 보안 운영 플랫폼"
PHASE_ORDER = [f"PHASE_{number}" for number in range(6)]
PACKAGE_SEQUENCE = ["ZT-FND-001", "ZT-NET-001", "ZT-VIS-001", "ZT-ID-001", "ZT-CV-001", "ZT-RV-001", "ZT-SCH-001", "P1-ACC-001"]
TECHNICAL_PACKAGE_IDS = PACKAGE_SEQUENCE[:-1] + ["ZT-DEV-001", "ZT-APP-001", "ZT-DATA-001", "ZT-SYS-001", "ZT-AUTO-001"]
CASE_TYPES = ["positive", "negative", "bypass", "persistence", "rollback", "evidence_integrity"]
KISA_SHA256 = "44fe393981b244147be6af7423d99dc15633c089fad0bcb296cbe2371dde812d"

AUTHORITIES = {
    "roadmap": (Path("docs/zero-trust/final-roadmap.yaml"), Path("schemas/zt-roadmap.schema.json")),
    "execution_plan": (Path("docs/zero-trust/final-execution-plan.yaml"), Path("schemas/zt-execution-plan.schema.json")),
    "milestones": (Path("docs/zero-trust/milestones-and-gates.yaml"), Path("schemas/zt-milestones-and-gates.schema.json")),
    "risk_register": (Path("docs/zero-trust/risk-register.yaml"), Path("schemas/zt-risk-register.schema.json")),
    "evidence_plan": (Path("docs/zero-trust/evidence-plan.yaml"), Path("schemas/zt-evidence-plan.schema.json")),
    "maturity_target": (Path("docs/zero-trust/maturity-target.yaml"), Path("schemas/zt-maturity-target.schema.json")),
    "kisa_mapping": (Path("docs/zero-trust/mappings/zt-kisa-technical-control-map.yaml"), Path("schemas/zt-kisa-technical-control-mapping.schema.json")),
    "acceptance_cases": (Path("docs/zero-trust/package-acceptance-cases.yaml"), Path("schemas/zt-package-acceptance-cases.schema.json")),
    "package_status": (Path("docs/zero-trust/package-status.yaml"), Path("schemas/zt-package-status.schema.json")),
}

KISA_ITEMS = {
    "U-01": ("root 계정 원격 접속 제한", "HIGH", "UNIX_SERVER"),
    "U-05": ("root 이외의 UID가 ‘0’ 금지", "HIGH", "UNIX_SERVER"),
    "U-06": ("사용자 계정 su 기능 제한", "HIGH", "UNIX_SERVER"),
    "U-07": ("불필요한 계정 제거", "LOW", "UNIX_SERVER"),
    "U-08": ("관리자 그룹에 최소한의 계정 포함", "MEDIUM", "UNIX_SERVER"),
    "U-10": ("동일한 UID 금지", "MEDIUM", "UNIX_SERVER"),
    "U-11": ("사용자 Shell 점검", "LOW", "UNIX_SERVER"),
    "U-12": ("세션 종료 시간 설정", "LOW", "UNIX_SERVER"),
    "U-16": ("/etc/passwd 파일 소유자 및 권한 설정", "HIGH", "UNIX_SERVER"),
    "U-18": ("/etc/shadow 파일 소유자 및 권한 설정", "HIGH", "UNIX_SERVER"),
    "U-28": ("접속 IP 및 포트 제한", "HIGH", "UNIX_SERVER"),
    "U-63": ("sudo 명령어 접근 관리", "HIGH", "UNIX_SERVER"),
    "W-06": ("관리자 그룹에 최소한의 사용자 포함", "HIGH", "WINDOWS_SERVER"),
    "WEB-06": ("웹 서비스 상위 디렉터리 접근 제한 설정", "HIGH", "WEB_SERVICE"),
    "S-06": ("보안장비 원격 관리 접근 통제", "HIGH", "SECURITY_DEVICE"),
    "S-10": ("보안장비 로그 설정", "MEDIUM", "SECURITY_DEVICE"),
    "N-06": ("VTY 접근(ACL) 설정", "HIGH", "NETWORK_DEVICE"),
    "N-14": ("정책에 따른 로깅 설정", "MEDIUM", "NETWORK_DEVICE"),
    "D-04": ("데이터베이스 관리자 권한을 꼭 필요한 계정 및 그룹에 대해서만 허용", "HIGH", "DBMS"),
    "D-10": ("원격에서 DB 서버로의 접속 제한", "HIGH", "DBMS"),
    "CI": ("코드 인젝션 (Code Injection)", "HIGH", "WEB_APPLICATION"),
    "IA": ("불충분한 인증 절차", "HIGH", "WEB_APPLICATION"),
    "HV-04": ("가상화 장비 계정 권한 관리", "HIGH", "VIRTUALIZATION"),
    "HV-15": ("시스템 주요 이벤트 로그 설정", "HIGH", "VIRTUALIZATION"),
    "CA-03": ("MFA(Multi-Factor Authentication) 설정", "HIGH", "CLOUD"),
    "CA-06": ("네트워크 서비스 정책 관리", "HIGH", "CLOUD"),
    "CA-13": ("클라우드 서비스 사용자 계정 로깅 설정", "HIGH", "CLOUD"),
}


@dataclass
class Finding:
    level: str
    category: str
    message: str


@dataclass
class Result:
    findings: list[Finding] = field(default_factory=list)
    integrity_error: bool = False

    def passed(self, category: str, message: str) -> None:
        self.findings.append(Finding("PASS", category, message))

    def fail(self, category: str, message: str, *, integrity: bool = False) -> None:
        self.findings.append(Finding("FAIL", category, message))
        self.integrity_error = self.integrity_error or integrity

    @property
    def failed(self) -> int:
        return sum(item.level == "FAIL" for item in self.findings)


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"duplicate key: {key}")
        output[key] = value
    return output


def load(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicate_keys)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f"{path}: {exc}") from exc


def _schema(root: Path, key: str, result: Result) -> Any | None:
    authority_path, schema_path = AUTHORITIES[key]
    try:
        authority = load(root / authority_path)
        schema = load(root / schema_path)
    except ValueError as exc:
        result.fail(f"{key}.configuration", str(exc), integrity=True)
        return None
    errors = core.validate_schema_instance(authority, schema)
    for error in errors:
        result.fail(f"{key}.schema", error)
    if not errors:
        result.passed(f"{key}.schema", f"{authority_path} conforms to {schema_path}.")
    return authority


def validate_project_definition(root: Path, result: Result) -> None:
    paths = [root / "README.md", root / "docs/project-definition.md"]
    for path in paths:
        if not path.is_file():
            result.fail("project.files", f"missing {path.relative_to(root)}", integrity=True)
            continue
        text = path.read_text(encoding="utf-8")
        for value in (PROJECT_TITLE_KO, PROJECT_TITLE_EN, PORTFOLIO_TITLE):
            if value not in text:
                result.fail("project.title", f"{path.relative_to(root)} is missing synchronized title: {value}")
    definition = (root / "docs/project-definition.md").read_text(encoding="utf-8") if (root / "docs/project-definition.md").is_file() else ""
    required = ["L3_ADVANCED", "L4_OPTIMAL", "ROADMAP_ONLY", "KISA 인증", "규정 준수 인증"]
    for token in required:
        if token not in definition:
            result.fail("project.boundary", f"project definition is missing {token}")
    diagrams = {
        Path("docs/project-definition.md"): ("Zero Trust Guideline 2.0", "Maturity assessment"),
        Path("docs/zero-trust/README.md"): ("ZT-FND-001", "P1-ACC-001"),
        Path("docs/zero-trust/final-roadmap.md"): ("Phase 0", "Phase 5"),
        Path("docs/control-validation-lifecycle.md"): ("Case executed", "maturity assessment"),
        Path("docs/zero-trust/maturity-target.md"): ("L3_NOT_YET_ACHIEVED", "L4_OPTIMAL"),
    }
    for relative, tokens in diagrams.items():
        text = (root / relative).read_text(encoding="utf-8") if (root / relative).is_file() else ""
        if "```text" not in text or "```mermaid" not in text or any(token.lower() not in text.lower() for token in tokens):
            result.fail("project.diagram", f"{relative} must contain synchronized plain-text and Mermaid views")
    if not any(item.level == "FAIL" and item.category.startswith("project.") for item in result.findings):
        result.passed("project", "Official titles, project definition, exclusions, and L3/L4 boundary are synchronized.")


def validate_roadmap(root: Path, result: Result) -> None:
    data = _schema(root, "roadmap", result)
    if data is None:
        return
    phases = data["phases"]
    if [phase["id"] for phase in phases] != PHASE_ORDER:
        result.fail("roadmap.order", "Phase order must be PHASE_0 through PHASE_5.")
    if any(phase["id"] in {"PHASE_2", "PHASE_3", "PHASE_4", "PHASE_5"} and phase["current_status"] != "NOT_STARTED" for phase in phases):
        result.fail("roadmap.claim", "Future implementation phases must remain NOT_STARTED.")
    markdown = (root / "docs/zero-trust/final-roadmap.md").read_text(encoding="utf-8")
    for token in ("Phase 0", "Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5", "L4_OPTIMAL", "ROADMAP_ONLY"):
        if token not in markdown:
            result.fail("roadmap.sync", f"roadmap Markdown is missing {token}")
    if not any(item.level == "FAIL" and item.category.startswith("roadmap.") for item in result.findings):
        result.passed("roadmap", "Phase 0-5 and L4 roadmap-only boundary are valid and synchronized.")


def _action_map(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["action_id"]: item for item in data["actions"]}


def validate_dependency_data(data: dict[str, Any], result: Result) -> None:
    actions = _action_map(data)
    if len(actions) != len(data["actions"]):
        result.fail("dependency.ids", "Action IDs must be unique.")
    order = {action_id: index for index, action_id in enumerate(actions)}
    for action_id, action in actions.items():
        for dependency in action["dependencies"]:
            if dependency not in actions:
                result.fail("dependency.reference", f"{action_id}: unknown dependency {dependency}")
            elif order[dependency] >= order[action_id]:
                result.fail("dependency.order", f"{action_id}: dependency {dependency} is not earlier")
        for successor in action["next_actions"]:
            if successor not in actions:
                result.fail("dependency.next", f"{action_id}: unknown next action {successor}")

    required_dependencies = {
        "P1-RV-001": {"P1-CV-001"},
        "P1-SCH-001": {"P1-RV-001"},
        "P1-ACC-001": {"P1-SCH-001"},
        "P2-OIDC-001": {"P2-ID-001"},
        "P2-RBAC-001": {"P2-OIDC-001"},
        "P2-CV-001": {"P2-ID-001", "P2-VIS-001"},
        "P3-CV-001": {"P3-ASSET-001"},
        "P4-DRIFT-001": {"P4-PAC-001"},
        "P5-MAT-001": {"P5-METRIC-001"},
    }
    for action_id, required in required_dependencies.items():
        missing = required - set(actions.get(action_id, {}).get("dependencies", []))
        if missing:
            result.fail("dependency.rule", f"{action_id}: missing required dependencies {sorted(missing)}")
    cv = actions.get("P1-CV-001", {})
    prereq_text = " ".join(cv.get("prerequisites", []))
    for package_id in ("ZT-FND-001", "ZT-NET-001", "ZT-VIS-001", "ZT-ID-001"):
        if package_id not in prereq_text:
            result.fail("dependency.cv", f"P1-CV-001 must require {package_id}")
    multi = actions.get("P3-CV-001", {})
    if "two different environments" not in " ".join(multi.get("prerequisites", [])).lower():
        result.fail("dependency.multi-environment", "P3-CV-001 must require two different deployed environments.")
    maturity = actions.get("P5-MAT-001", {})
    maturity_prereqs = " ".join(maturity.get("prerequisites", [])).lower()
    for phrase in ("evidence index", "open-gap register"):
        if phrase not in maturity_prereqs:
            result.fail("dependency.maturity", f"P5-MAT-001 must require {phrase}.")


def validate_execution_plan(root: Path, result: Result, dependencies_only: bool = False) -> None:
    data = _schema(root, "execution_plan", result)
    if data is None:
        return
    validate_dependency_data(data, result)
    actions = _action_map(data)
    if set(data["critical_path"]) - set(actions):
        result.fail("execution.critical-path", "Critical path contains unknown action IDs.")
    completed = {item["action_id"] for item in data["actions"] if item["current_status"] == "COMPLETED"}
    if completed != {"ZT-SCN-RETIRE-001"}:
        result.fail("execution.current-state", f"Only verified retirement may be COMPLETED, got {sorted(completed)}")
    plan_ids = [item["action_id"] for item in data["actions"]]
    roadmap = load(root / AUTHORITIES["roadmap"][0])
    roadmap_ids = [action for phase in roadmap["phases"] for action in phase["actions"]]
    if plan_ids != roadmap_ids:
        result.fail("execution.sync", "Execution action order must match roadmap action order.")
    risk_ids = {item["risk_id"] for item in load(root / AUTHORITIES["risk_register"][0])["risks"]}
    for action in data["actions"]:
        unknown = set(action["risks"]) - risk_ids
        if unknown:
            result.fail("execution.risk", f"{action['action_id']}: unknown risks {sorted(unknown)}")
        if not action["rollback_requirements"] or not action["stop_conditions"] or not action["required_evidence"]:
            result.fail("execution.completeness", f"{action['action_id']}: evidence, rollback and stop conditions are mandatory")
    if not dependencies_only and not any(item.level == "FAIL" and item.category.startswith(("execution.", "dependency.")) for item in result.findings):
        result.passed("execution", "All actions, dependencies, critical path, evidence, rollback, risks and stop conditions are valid.")
    if dependencies_only and not any(item.level == "FAIL" and item.category.startswith("dependency.") for item in result.findings):
        result.passed("dependency", "Dependency graph and predecessor rules are valid.")


def validate_milestones(root: Path, result: Result) -> None:
    data = _schema(root, "milestones", result)
    if data is None:
        return
    if [item["milestone_id"] for item in data["milestones"]] != data["milestone_order"]:
        result.fail("milestones.order", "Milestone records must follow M0-M6 order.")
    plan_ids = set(_action_map(load(root / AUTHORITIES["execution_plan"][0])))
    for item in data["milestones"]:
        unknown = set(item["required_actions"]) - plan_ids
        if unknown:
            result.fail("milestones.actions", f"{item['milestone_id']}: unknown actions {sorted(unknown)}")
        if item["approval_decision"] != "PENDING":
            result.fail("milestones.claim", f"{item['milestone_id']} must remain PENDING during planning")
    markdown = (root / "docs/zero-trust/milestones-and-gates.md").read_text(encoding="utf-8")
    for milestone_id in data["milestone_order"]:
        if milestone_id not in markdown:
            result.fail("milestones.sync", f"Markdown is missing {milestone_id}")
    if not any(item.level == "FAIL" and item.category.startswith("milestones.") for item in result.findings):
        result.passed("milestones", "M0-M6 gates are complete, synchronized and pending evidence-based approval.")


def validate_risk_register(root: Path, result: Result) -> None:
    data = _schema(root, "risk_register", result)
    if data is None:
        return
    ids = [item["risk_id"] for item in data["risks"]]
    if len(ids) != len(set(ids)):
        result.fail("risk.ids", "Risk IDs must be unique.")
    required_phrases = ["lockout", "firewall", "evidence", "secret", "personal", "hardware", "cloud", "drift", "multi-environment", "L3"]
    corpus = " ".join(item["risk_id"] + " " + item["description"] for item in data["risks"])
    for phrase in required_phrases:
        if phrase.lower() not in corpus.lower():
            result.fail("risk.coverage", f"Risk register does not cover {phrase}")
    if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", corpus):
        result.fail("risk.privacy", "Risk register must not contain personal contact details.")
    if not any(item.level == "FAIL" and item.category.startswith("risk.") for item in result.findings):
        result.passed("risk", f"{len(ids)} risks include prevention, detection, response, rollback, role owner and residual risk.")


def validate_evidence_plan(root: Path, result: Result) -> None:
    data = _schema(root, "evidence_plan", result)
    if data is None:
        return
    plan_ids = set(_action_map(load(root / AUTHORITIES["execution_plan"][0])))
    evidence_ids = [item["action_id"] for item in data["action_evidence_plans"]]
    if len(evidence_ids) != len(set(evidence_ids)):
        result.fail("evidence.ids", "Evidence action IDs must be unique.")
    if set(evidence_ids) != plan_ids:
        result.fail("evidence.coverage", f"Evidence plan coverage mismatch: missing={sorted(plan_ids-set(evidence_ids))}, extra={sorted(set(evidence_ids)-plan_ids)}")
    prohibited = " ".join(data["prohibited_content"]).lower()
    for phrase in ("password", "private keys", "mfa seeds", "recovery codes", "access tokens", "private absolute paths"):
        if phrase not in prohibited:
            result.fail("evidence.prohibited", f"Missing prohibited content class: {phrase}")
    if not any(item.level == "FAIL" and item.category.startswith("evidence.") for item in result.findings):
        result.passed("evidence", "Every action has an evidence plan and raw/tracked/sensitive-data boundaries are explicit.")


def validate_maturity_target(root: Path, result: Result) -> None:
    data = _schema(root, "maturity_target", result)
    if data is None:
        return
    if data["l3_completion_decision"] != "NOT_YET_ASSESSED":
        result.fail("maturity.claim", "Planning action must not make an L3 completion decision.")
    if any(item != {"theme": item["theme"], "implementation_status": "ROADMAP_ONLY", "runtime_validation_status": "NOT_VALIDATED", "maturity_claim": "NOT_CLAIMED"} for item in data["l4_roadmap"]):
        result.fail("maturity.l4", "Every L4 record must remain roadmap-only, not validated, and not claimed.")
    dimension_ids = [item["id"] for item in data["dimensions"]]
    if dimension_ids != data["mandatory_dimensions"]:
        result.fail("maturity.dimensions", "Dimension records must match mandatory dimension order.")
    markdown = (root / "docs/zero-trust/maturity-target.md").read_text(encoding="utf-8")
    for token in ("L3_ADVANCED", "UNASSESSED", "L4", "ROADMAP_ONLY"):
        if token not in markdown:
            result.fail("maturity.sync", f"Maturity Markdown is missing {token}")
    if not any(item.level == "FAIL" and item.category.startswith("maturity.") for item in result.findings):
        result.passed("maturity", "L3 is an evidence-backed target and all L4 records remain roadmap-only non-claims.")


def validate_kisa_mapping(root: Path, result: Result) -> None:
    data = _schema(root, "kisa_mapping", result)
    if data is None:
        return
    source = load(root / "docs/references/kisa-2026-critical-infrastructure-guide.yaml")
    if source.get("sha256") != KISA_SHA256 or source.get("page_count") != 873 or source.get("publication_year") != 2026:
        result.fail("kisa.source", "KISA source metadata does not match the authenticated 2026, 873-page source.")
    if source.get("handling", {}).get("raw_pdf_tracked") is not False or source.get("handling", {}).get("private_absolute_path_recorded") is not False:
        result.fail("kisa.handling", "Raw PDF and private absolute path must not be tracked.")
    if data["metadata"]["guide_sha256"] != source["sha256"]:
        result.fail("kisa.source", "Mapping and source SHA-256 differ.")
    records = data["mappings"]
    if data["metadata"]["mapping_count"] != len(records):
        result.fail("kisa.count", "mapping_count does not equal mapping records.")
    ids = [item["mapping_id"] for item in records]
    if len(ids) != len(set(ids)):
        result.fail("kisa.ids", "Mapping IDs must be unique.")
    catalog = load(root / "docs/zero-trust/capability-catalog.yaml")
    capability_ids = {item["id"] for item in catalog["capabilities"]}
    domains: set[str] = set()
    for item in records:
        expected = KISA_ITEMS.get(item["kisa_item_code"])
        actual = (item["kisa_item_name"], item["kisa_severity"], item["kisa_asset_domain"])
        if expected is None:
            result.fail("kisa.guessed", f"{item['mapping_id']}: unverified or unknown KISA item {item['kisa_item_code']}")
        elif actual != expected:
            result.fail("kisa.item", f"{item['mapping_id']}: item metadata differs from authenticated source")
        unknown = set(item["zt_capability_ids"]) - capability_ids
        if unknown:
            result.fail("kisa.capability", f"{item['mapping_id']}: unknown capabilities {sorted(unknown)}")
        if item["implementation_status"] != "REFERENCED_ONLY" or item["runtime_validation_status"] != "NOT_VALIDATED" or item["evidence_status"] != "SOURCE_METADATA_ONLY":
            result.fail("kisa.overclaim", f"{item['mapping_id']}: planning mapping overclaims implementation or runtime evidence")
        domains.add(item["kisa_asset_domain"])
    required_domains = {"UNIX_SERVER","WINDOWS_SERVER","WEB_SERVICE","WEB_APPLICATION","SECURITY_DEVICE","NETWORK_DEVICE","DBMS","VIRTUALIZATION","CLOUD"}
    if not required_domains.issubset(domains):
        result.fail("kisa.coverage", f"Seed misses required evaluated domains: {sorted(required_domains-domains)}")
    markdown = (root / "docs/zero-trust/mappings/zt-kisa-technical-control-map.md").read_text(encoding="utf-8")
    for package in sorted({item["zt_package_id"] for item in records}):
        if package not in markdown:
            result.fail("kisa.sync", f"Mapping Markdown is missing {package}")
    if not any(item.level == "FAIL" and item.category.startswith("kisa.") for item in result.findings):
        result.passed("kisa", f"{len(records)} exact source-verified planning mappings cover the required asset domains without implementation or compliance claims.")


def validate_acceptance_cases(root: Path, result: Result) -> None:
    data = _schema(root, "acceptance_cases", result)
    if data is None:
        return
    packages = [item["package_id"] for item in data["packages"]]
    if packages != TECHNICAL_PACKAGE_IDS:
        result.fail("acceptance.packages", "Acceptance package order must cover all twelve technical packages.")
    case_ids: list[str] = []
    for package in data["packages"]:
        for case_type in CASE_TYPES:
            group = package["acceptance_cases"][case_type]
            if group["applicable"] and not group["cases"]:
                result.fail("acceptance.missing", f"{package['package_id']} {case_type}: applicable group requires a case")
            if not group["applicable"] and group["cases"]:
                result.fail("acceptance.inapplicable", f"{package['package_id']} {case_type}: inapplicable group must have no cases")
            case_ids.extend(item["case_id"] for item in group["cases"])
        for mandatory in ("positive", "negative", "evidence_integrity"):
            if not package["acceptance_cases"][mandatory]["applicable"]:
                result.fail("acceptance.mandatory", f"{package['package_id']}: {mandatory} must be applicable")
    if len(case_ids) != len(set(case_ids)):
        result.fail("acceptance.ids", "Acceptance case IDs must be unique.")
    if any(re.fullmatch(r"S0?[0-9]{2}", case_id) for case_id in case_ids):
        result.fail("acceptance.numbering", "Numbered scenario IDs are prohibited.")
    if not any(item.level == "FAIL" and item.category.startswith("acceptance.") for item in result.findings):
        result.passed("acceptance", f"{len(case_ids)} descriptive package-owned cases cover applicable behavior and evidence integrity.")


def validate_status_truth(root: Path, result: Result) -> None:
    data = _schema(root, "package_status", result)
    if data is None:
        return
    records = {item["package_id"]: item for item in data["packages"]}
    flow = load(root / "docs/zero-trust/package-flow.yaml")
    if flow["phase_1_sequence"] != PACKAGE_SEQUENCE:
        result.fail("status.flow", "Canonical Phase 1 package sequence is invalid.")
    architecture = records["ZT-ARC-001"]
    expected_arch = ("DESIGN_ONLY", "LOCAL_VALIDATED", "NOT_VALIDATED", "UNASSESSED")
    actual_arch = (architecture["implementation_status"], architecture["local_validation_status"], architecture["runtime_validation_status"], architecture["maturity_status"])
    if actual_arch != expected_arch:
        result.fail("status.architecture", f"ZT-ARC-001 status changed: {actual_arch}")
    flow_records = {item["package_id"]: item for item in flow["packages"]}
    for package_id, flow_record in flow_records.items():
        status = records[package_id]
        for field in ("implementation_status", "local_validation_status", "runtime_validation_status", "runtime_acceptance_status", "maturity_status"):
            if status[field] != flow_record[field]:
                result.fail("status.preservation", f"{package_id}: {field} differs from package flow")
    expected_extended = {
        "ZT-DEV-001": ("IMPLEMENTED", "PARTIALLY_RUNTIME_VALIDATED"),
        "ZT-APP-001": ("IMPLEMENTED", "PARTIALLY_RUNTIME_VALIDATED"),
        "ZT-DATA-001": ("IMPLEMENTED", "PARTIALLY_RUNTIME_VALIDATED"),
        "ZT-SYS-001": ("IMPLEMENTED", "PARTIALLY_RUNTIME_VALIDATED"),
        "ZT-AUTO-001": ("IMPLEMENTED", "PARTIALLY_RUNTIME_VALIDATED"),
    }
    for package_id, expected in expected_extended.items():
        package_path = root / "docs/zero-trust/packages" / f"{package_id.lower()}-package.yaml"
        package = load(package_path)
        if (package.get("implementation_status"), package.get("validation_status")) != expected:
            result.fail("status.extended", f"{package_id}: package authority changed")
        snapshot = records[package_id]
        if (snapshot["implementation_status"], snapshot["runtime_validation_status"]) != (expected[0], "PARTIALLY_VALIDATED"):
            result.fail("status.extended", f"{package_id}: snapshot does not preserve partial runtime status")
    if any(record["maturity_status"] != "UNASSESSED" or record["compliance_status"] != "NOT_ASSESSED" for record in records.values()):
        result.fail("status.claim", "Planning action must leave every package maturity UNASSESSED and compliance NOT_ASSESSED.")
    tracked = subprocess.run(["git", "ls-files", ".runtime"], cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if tracked.returncode != 0:
        result.fail("status.git", "Unable to inspect tracked runtime.", integrity=True)
    elif tracked.stdout.strip():
        result.fail("status.runtime", "Tracked .runtime files are prohibited.")
    if not any(item.level == "FAIL" and item.category.startswith("status.") for item in result.findings):
        result.passed("status", "Package implementation, local/runtime validation, acceptance, maturity and compliance truth is preserved.")


def validate_repository_safety(root: Path, result: Result) -> None:
    paths = [path for pair in AUTHORITIES.values() for path in pair] + [
        Path("README.md"), Path("docs/project-definition.md"), Path("docs/project-methodology.md"),
        Path("docs/control-validation-lifecycle.md"), Path("docs/references/kisa-2026-critical-infrastructure-guide.yaml")
    ]
    private_path = re.compile(r"(?i)[A-Z]:\\Users\\|/Users/|/home/[A-Za-z0-9._-]+/")
    secret_assignment = re.compile(r"(?i)(password|passwd|token|private[_-]?key|mfa[_-]?seed|recovery[_-]?code)\s*[:=]\s*[^<\s][^\s]*")
    for relative in paths:
        path = root / relative
        if not path.is_file():
            result.fail("safety.files", f"missing {relative}", integrity=True)
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if private_path.search(text):
            result.fail("safety.privacy", f"{relative}: private absolute path detected")
        if secret_assignment.search(text):
            result.fail("safety.secret", f"{relative}: secret-like assignment detected")
    if not any(item.level == "FAIL" and item.category.startswith("safety.") for item in result.findings):
        result.passed("safety", "Planning authorities contain no private absolute path or secret assignment.")


VALIDATORS: dict[str, Callable[[Path, Result], None]] = {
    "project_definition": validate_project_definition,
    "roadmap": validate_roadmap,
    "execution_plan": validate_execution_plan,
    "dependency_graph": lambda root, result: validate_execution_plan(root, result, dependencies_only=True),
    "milestones": validate_milestones,
    "risk_register": validate_risk_register,
    "evidence_plan": validate_evidence_plan,
    "maturity_target": validate_maturity_target,
    "kisa_mapping": validate_kisa_mapping,
    "acceptance_cases": validate_acceptance_cases,
    "status_truth": validate_status_truth,
}


def run(component: str, root: Path = ROOT, strict: bool = False) -> Result:
    result = Result()
    VALIDATORS[component](root, result)
    validate_repository_safety(root, result)
    if strict:
        # No warning level is emitted; strict is explicit for a stable CLI contract.
        pass
    return result


def cli(component: str, argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=f"Validate Zero Trust project-plan component: {component}")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    result = run(component, args.root.resolve(), args.strict)
    if args.format == "json":
        print(json.dumps({"component": component, "findings": [asdict(item) for item in result.findings], "summary": {"passed": sum(item.level == "PASS" for item in result.findings), "failed": result.failed}, "exit_status": 2 if result.integrity_error else (1 if result.failed else 0)}, ensure_ascii=False, indent=2))
    else:
        for item in result.findings:
            if args.verbose or item.level != "PASS":
                print(f"[{item.level}] {item.category}: {item.message}")
        print(f"{component} summary: passed={sum(item.level == 'PASS' for item in result.findings)}, failed={result.failed}")
    if result.integrity_error:
        return 2
    return 1 if result.failed else 0
