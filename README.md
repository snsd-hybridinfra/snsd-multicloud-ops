# SNSD Zero Trust Package Validation Platform

This repository implements and validates bounded Zero Trust controls in a non-production EVE-NG and OpenStack laboratory. It is organized around capabilities, packages, validators, sanitized evidence, and explicit status decisions.

It is not a scenario catalog, a simple infrastructure build, a product-installation exercise, or proof of complete compliance or maturity.

## Authoritative model

```text
ZT-ARC-001 surrounds
ZT-FND-001 -> ZT-NET-001 -> ZT-VIS-001 -> ZT-ID-001
           -> ZT-CV-001 -> ZT-RV-001 -> ZT-SCH-001
           -> PHASE_1_ACCEPTANCE
```

- `ZT-ARC-001`: cross-phase architecture authority
- `ZT-FND-001`: validation and evidence foundation
- `ZT-NET-001`: bounded network-control validation
- `ZT-VIS-001`: bounded visibility and evidence integrity
- `ZT-ID-001`: bounded identity-control validation
- `ZT-CV-001`: cross-capability validation
- `ZT-RV-001`: repeatability and deterministic-result validation
- `ZT-SCH-001`: scheduled execution, freshness, failure detection, and automated evidence production

The canonical machine-readable flow is [docs/zero-trust/package-flow.yaml](docs/zero-trust/package-flow.yaml).

## External authorities

1. **제로트러스트 가이드라인 2.0** defines capability, architecture, and maturity semantics.
2. The **2026 KISA critical-infrastructure technical vulnerability guide** is intended as a secondary asset-specific inspection and hardening reference after ZT-GOV-MAP-001 authenticates and maps it.
3. Package metadata and evidence establish repository implementation truth.

No mapping alone establishes implementation, validation, compliance, certification, production readiness, or maturity.

## Scenario retirement

The former numbered scenario framework and its dedicated evidence placeholders and aggregate tools were removed by ZT-SCN-RETIRE-001. Git history is the recovery authority. No successor numbered scenario series was created.

## Current boundary

- Current infrastructure: bounded EVE-NG and OpenStack non-production laboratory
- Live target mutation in this change: none
- Tracked runtime: prohibited
- Phase 1: PARTIAL / PARTIALLY_VALIDATED / NOT_COMPLETE
- Scope boundary: ZT-SCH-001

## Key documents

- [Scope lock](docs/scope-lock.md)
- [Excluded scope](docs/excluded-scope.md)
- [Package flow](docs/zero-trust/package-flow.yaml)
- [Progress](docs/progress-tracker.md)
- [Evidence model](docs/evidence-model.md)
- [Zero Trust governance](docs/zero-trust/governance.md)
- [Scenario retirement decision](docs/zero-trust/governance/scenario-framework-retirement.md)
- [Phase 1 runbooks](docs/runbooks/README.md)

## Read-only validation

```powershell
python tools/validate_scenario_retirement.py --verbose --strict
python tools/validate_zero_trust.py --verbose
python tools/check_zero_trust_sync.py
python tools/generate_zero_trust_reports.py --check
python tools/validate_phase1_runbook_baseline.py --strict
python tools/validate_advanced_target_architecture.py --strict
powershell -NoProfile -ExecutionPolicy Bypass -File tools/validate-repo-structure.ps1
python -m unittest discover -s tests
```
