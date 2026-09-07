#!/usr/bin/env python3
"""Validate the historical P1-ACC denial and its scoped superseding exception."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/continuous_verification"))

from rv_common import assess, campaign_records, parse_time  # noqa: E402
from validate_zero_trust import validate_schema_instance  # noqa: E402

BLOCKED_DECISION = Path("docs/zero-trust/recovery/P1-ACC-001/acceptance-decision.yaml")
BLOCKED_SCHEMA = Path("schemas/phase-1-acceptance-decision.schema.json")
DECISION = Path("docs/zero-trust/recovery/P1-ACC-001/acceptance-decision-with-gaps.yaml")
EXCEPTION = Path("docs/zero-trust/exceptions/p1-rv-freshness-001.yaml")
REFRESH_PROGRESS = Path("docs/zero-trust/recovery/P1-ACC-001/rv-refresh-progress.yaml")
REFRESH_SCHEMA = Path("schemas/phase-1-rv-refresh-progress.schema.json")
EVIDENCE_INDEX = Path("docs/zero-trust/recovery/P1-ACC-001/evidence-index.yaml")
SCHEMA = Path("schemas/phase-1-accepted-with-gaps-decision.schema.json")
CAMPAIGN = Path("docs/zero-trust/repeatable-validation-campaign.yaml")
POLICY = Path("docs/zero-trust/repeatability-acceptance-policy.yaml")
HISTORY = Path("docs/zero-trust/verification-history.yaml")
FLOW = Path("docs/zero-trust/package-flow.yaml")
PACKAGE_STATUS = Path("docs/zero-trust/package-status.yaml")
EXECUTION_PLAN = Path("docs/zero-trust/final-execution-plan.yaml")
ROADMAP = Path("docs/zero-trust/final-roadmap.yaml")
MILESTONES = Path("docs/zero-trust/milestones-and-gates.yaml")
PACKAGE_FILES = {
    "ZT-FND-001": Path("docs/zero-trust/packages/zt-fnd-001-package.yaml"),
    "ZT-NET-001": Path("docs/zero-trust/packages/zt-net-001-package.yaml"),
    "ZT-VIS-001": Path("docs/zero-trust/packages/zt-vis-001-package.yaml"),
    "ZT-ID-001": Path("docs/zero-trust/packages/zt-id-001-package.yaml"),
    "ZT-CV-001": Path("docs/zero-trust/packages/zt-cv-001-package.yaml"),
    "ZT-RV-001": Path("docs/zero-trust/packages/zt-rv-001-package.yaml"),
}
REQUIRED_PATHS = (
    BLOCKED_DECISION, BLOCKED_SCHEMA, DECISION, EXCEPTION, REFRESH_PROGRESS,
    REFRESH_SCHEMA, EVIDENCE_INDEX, SCHEMA,
    CAMPAIGN, POLICY, HISTORY, FLOW, PACKAGE_STATUS,
    EXECUTION_PLAN, ROADMAP, MILESTONES, *PACKAGE_FILES.values(),
)


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain an object")
    return value


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    missing = [str(path) for path in REQUIRED_PATHS if not (root / path).is_file()]
    if missing:
        return [f"required authority is missing: {path}" for path in missing]

    try:
        blocked_decision = load(root / BLOCKED_DECISION)
        decision = load(root / DECISION)
        exception = load(root / EXCEPTION)
        refresh_progress = load(root / REFRESH_PROGRESS)
        evidence_index = load(root / EVIDENCE_INDEX)
        blocked_schema = load(root / BLOCKED_SCHEMA)
        schema = load(root / SCHEMA)
        refresh_schema = load(root / REFRESH_SCHEMA)
        campaign = load(root / CAMPAIGN)
        policy = load(root / POLICY)
        history = load(root / HISTORY)
        flow = load(root / FLOW)
        package_status = load(root / PACKAGE_STATUS)
        execution_plan = load(root / EXECUTION_PLAN)
        roadmap = load(root / ROADMAP)
        milestones = load(root / MILESTONES)
        packages = {package_id: load(root / path) for package_id, path in PACKAGE_FILES.items()}
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return [str(exc)]

    errors.extend(f"historical schema: {item}" for item in validate_schema_instance(blocked_decision, blocked_schema))
    errors.extend(f"superseding schema: {item}" for item in validate_schema_instance(decision, schema))
    errors.extend(f"refresh schema: {item}" for item in validate_schema_instance(refresh_progress, refresh_schema))
    if blocked_decision.get("evidence_index") != EVIDENCE_INDEX.as_posix():
        errors.append("historical acceptance decision must reference the authoritative evidence index")
    if decision.get("supersedes") != BLOCKED_DECISION.as_posix() or decision.get("exception") != EXCEPTION.as_posix():
        errors.append("superseding decision must reference the historical denial and accepted exception")
    evidence_entries = evidence_index.get("entries", [])
    expected_package_ids = list(PACKAGE_FILES)
    if [item.get("package_id") for item in evidence_entries] != expected_package_ids:
        errors.append("evidence index must cover the six ordered Phase 1 predecessor packages")
    for item in evidence_entries:
        references = [item.get("decision_authority"), *item.get("evidence_authorities", [])]
        for reference in references:
            if not isinstance(reference, str) or not (root / reference).is_file():
                errors.append(f"evidence index reference is missing: {reference}")
    if evidence_index.get("gap_authority") != "docs/zero-trust/gap-register.md#zg-016":
        errors.append("evidence index must reference the ZG-016 freshness blocker")
    if evidence_index.get("sanitization_status") != "PASS" or evidence_index.get("raw_runtime_included") is not False or evidence_index.get("secret_findings") != 0 or evidence_index.get("privacy_findings") != 0:
        errors.append("evidence index must remain sanitized and contain no raw runtime, secret, or privacy finding")
    assessed_at = parse_time(str(blocked_decision.get("assessed_at", "")))
    records = campaign_records(history)
    historical_records = [item for item in records if parse_time(str(item["execution_timestamp"])) <= assessed_at]
    if len(historical_records) != 3:
        errors.append(f"expected three RV records at the historical denial time, got {len(historical_records)}")
        return errors

    current = assess(historical_records, campaign, assessed_at)
    freshness = blocked_decision.get("freshness_gate", {})
    newest = max(historical_records, key=lambda item: parse_time(str(item["execution_timestamp"])))
    age_seconds = (assessed_at - parse_time(str(newest["execution_timestamp"]))).total_seconds()
    maximum_age = policy.get("criteria", {}).get("maximum_evidence_age")
    if maximum_age != "P7D" or freshness.get("maximum_age_seconds") != 604800:
        errors.append("P1-ACC-001 freshness boundary must remain P7D / 604800 seconds")
    if age_seconds <= 604800 or abs(float(freshness.get("newest_evidence_age_seconds", -1)) - age_seconds) > 0.001:
        errors.append("recorded newest evidence age does not prove the P7D expiration")
    if freshness.get("newest_execution_id") != newest.get("execution_id") or freshness.get("newest_execution_timestamp") != newest.get("execution_timestamp"):
        errors.append("recorded newest RV execution differs from verification history")
    if (
        current.get("freshness", {}).get("status") != "STALE"
        or current.get("execution_history", {}).get("accepted") != 0
        or current.get("current_continuity") != "EC3_ONE_TIME_RUNTIME"
        or current.get("acceptance", {}).get("result") != "NOT_STARTED"
    ):
        errors.append("recorded assessment time must reproduce STALE / 0 accepted / EC3 / NOT_STARTED")

    refresh_time = parse_time(str(refresh_progress.get("assessment_time", "")))
    refresh_assessment = assess(records, campaign, refresh_time)
    if (
        refresh_assessment.get("freshness", {}).get("status") != "STALE"
        or refresh_assessment.get("execution_history", {}).get("accepted") != 1
        or refresh_assessment.get("execution_history", {}).get("rejected") != 3
        or refresh_assessment.get("execution_history", {}).get("consecutive_successes") != 1
        or refresh_assessment.get("current_continuity") != "EC3_ONE_TIME_RUNTIME"
        or refresh_assessment.get("acceptance", {}).get("result") != "IN_PROGRESS"
    ):
        errors.append("RV refresh progress must reproduce STALE / 1 accepted / 3 expired / EC3 / IN_PROGRESS")
    latest = max(records, key=lambda item: parse_time(str(item["execution_timestamp"])))
    progress_latest = refresh_progress.get("latest_execution", {})
    if (
        progress_latest.get("execution_id") != latest.get("execution_id")
        or progress_latest.get("execution_timestamp") != latest.get("execution_timestamp")
        or progress_latest.get("evidence_reference") != latest.get("sanitized_evidence_reference")
    ):
        errors.append("RV refresh progress latest execution differs from verification history")
    if (
        latest.get("execution_authority") != "CODEX_EXECUTED_LIVE_RUNTIME"
        or latest.get("execution_mode") != "EXECUTE_READ_ONLY"
        or latest.get("fail") != 0
        or latest.get("exit_code") != 0
        or latest.get("sanitization_status") != "PASS"
        or latest.get("security_boundary", {}).get("status") != "PASS"
    ):
        errors.append("latest RV refresh execution must remain an eligible sanitized read-only success")
    expected_next = parse_time(str(latest["execution_timestamp"])) + timedelta(hours=24)
    if parse_time(str(refresh_progress.get("next_execution_not_before", ""))) != expected_next:
        errors.append("RV refresh next execution must preserve PT24H separation")
    if (
        refresh_progress.get("scheduler_used") is not False
        or refresh_progress.get("automatic_retry_used") is not False
        or refresh_progress.get("live_target_changed") is not False
        or refresh_progress.get("history_appended") is not True
        or refresh_progress.get("package_status_promoted") is not False
        or refresh_progress.get("phase_2_continues") is not True
    ):
        errors.append("RV refresh must remain manual, read-only, explicitly appended, and parallel with Phase 2")

    expected_acceptance = {
        "ZT-FND-001": "BOUNDED_ACCEPTED",
        "ZT-NET-001": "ACCEPTED",
        "ZT-VIS-001": "ACCEPTED",
        "ZT-ID-001": "ACCEPTED",
        "ZT-CV-001": "PARTIALLY_ACCEPTED",
        "ZT-RV-001": "ACCEPTED",
    }
    status_records = {item.get("package_id"): item for item in package_status.get("packages", [])}
    for package_id, expected in expected_acceptance.items():
        actual = status_records.get(package_id, {}).get("runtime_acceptance_status")
        if actual != expected:
            errors.append(f"{package_id} package-status acceptance differs: {actual}")
    if packages["ZT-CV-001"].get("latest_execution", {}).get("decision") != "PASS_WITH_OPEN_GAPS":
        errors.append("ZT-CV-001 must retain the reviewed PASS_WITH_OPEN_GAPS decision")
    if packages["ZT-RV-001"].get("acceptance_state") != "REPEATABILITY_ACCEPTED":
        errors.append("historical ZT-RV-001 acceptance must remain preserved")

    action = next((item for item in execution_plan.get("actions", []) if item.get("action_id") == "P1-ACC-001"), {})
    phase2_action = next((item for item in execution_plan.get("actions", []) if item.get("action_id") == "P2-VIS-001"), {})
    phase = next((item for item in roadmap.get("phases", []) if item.get("id") == "PHASE_1"), {})
    phase2 = next((item for item in roadmap.get("phases", []) if item.get("id") == "PHASE_2"), {})
    milestone = next((item for item in milestones.get("milestones", []) if item.get("milestone_id") == "M2"), {})
    phase_acceptance = flow.get("phase_1_acceptance", {})
    deferred = flow.get("deferred_final_work", {})
    if blocked_decision.get("decision") != "BLOCKED_STALE_EVIDENCE":
        errors.append("historical default-deny decision must remain preserved")
    historical = decision.get("historical_freshness_state", {})
    if (
        historical.get("status") != "STALE"
        or historical.get("accepted_current_records") != 0
        or historical.get("current_continuity") != "EC3_ONE_TIME_RUNTIME"
        or historical.get("reclassified_as_fresh") is not False
    ):
        errors.append("superseding decision must preserve STALE / 0 accepted / EC3 without freshness reclassification")
    phase2_entry = decision.get("phase_2_entry", {})
    if (
        decision.get("decision") != "ACCEPTED_WITH_GAPS"
        or phase2_entry.get("status") != "AUTHORIZED_WITH_GAPS"
        or phase2_entry.get("first_action") != "P2-VIS-001"
        or phase2_entry.get("live_mutation_authorized") is not False
        or phase2_entry.get("live_validator_authorized") is not False
    ):
        errors.append("superseding decision must authorize only bounded Phase 2 local preparation")
    if (
        exception.get("exception_id") != "P1-RV-FRESHNESS-001"
        or exception.get("status") != "ACCEPTED_TEMPORARY"
        or exception.get("scope") != "PHASE_2_ENTRY_ONLY"
        or exception.get("review_trigger") != "BEFORE_ZT_SCH_001_REENABLE_OR_P5_ACC_001"
        or exception.get("scheduler_state_required") != "DISABLED"
    ):
        errors.append("RV freshness exception must remain temporary, Phase-2-entry-only, and final-gate bound")
    if action.get("current_status") != "COMPLETED":
        errors.append("P1-ACC-001 execution action must be COMPLETED by the superseding decision")
    if phase2_action.get("current_status") != "IN_PROGRESS":
        errors.append("P2-VIS-001 must be the single in-progress Phase 2 action")
    if phase.get("current_status") != "COMPLETED_WITH_GAPS" or phase_acceptance.get("completion_status") != "COMPLETED_WITH_GAPS":
        errors.append("Phase 1 must be COMPLETED_WITH_GAPS")
    if phase2.get("current_status") != "IN_PROGRESS":
        errors.append("Phase 2 must be IN_PROGRESS")
    expected_flow = {
        "decision_status": "ACCEPTED_WITH_GAPS",
        "accepted_exception": "P1-RV-FRESHNESS-001",
        "deferred_final_risk": "STALE_RV_EVIDENCE",
        "decision_record": DECISION.as_posix(),
    }
    for key, expected in expected_flow.items():
        if phase_acceptance.get(key) != expected:
            errors.append(f"Phase 1 acceptance {key} must be {expected}")
    if milestone.get("approval_decision") != "APPROVED" or milestone.get("blocking_gaps"):
        errors.append("M2 must be APPROVED without an active blocking gap under the reviewed exception")
    if deferred.get("package_id") != "ZT-SCH-001" or deferred.get("schedule_state") != "DISABLED" or deferred.get("execution_phase") != "PHASE_5":
        errors.append("ZT-SCH-001 must remain disabled and deferred to Phase 5")
    if any(decision.get(field) is not False for field in ("runtime_executed", "live_target_changed", "scheduler_changed", "package_status_promoted", "maturity_assessed", "compliance_assessed")):
        errors.append("superseding acceptance decision must not claim runtime, mutation, promotion, maturity, or compliance")
    next_action = blocked_decision.get("next_action", {})
    if next_action.get("package_id") != "ZT-RV-001" or next_action.get("minimum_new_eligible_executions") != 3 or next_action.get("minimum_separation") != "PT24H" or next_action.get("scheduler_required") is not False:
        errors.append("recovery must remain the three-run manual ZT-RV-001 path without SCH")
    return errors


def main() -> int:
    errors = validate()
    for error in errors:
        print(f"[FAIL] {error}")
    if errors:
        print(f"Phase 1 acceptance summary: passed=0, failed={len(errors)}")
        return 1
    print("[PASS] P1-ACC-001 preserves the historical stale-evidence denial, applies the scoped Phase 2 exception, and records manual RV freshness progress at 1/3 without scheduler or status promotion.")
    print("Phase 1 acceptance summary: passed=1, failed=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
