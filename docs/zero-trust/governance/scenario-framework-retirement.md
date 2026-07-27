# Numbered Scenario Framework Retirement

## 1. Decision

The numbered S001-S050 framework is no longer an active project authority.

## 2. Scope

ZT-SCN-RETIRE-001 removes the active numbered definitions, dedicated evidence tree, status and capability matrices, aggregate runner, scenario-only validators, and scenario-only tests.

## 3. Removed authorities

- Numbered scenario definitions and registry assumptions
- Dedicated scenario evidence paths and parity checks
- Scenario status and completion count
- Aggregate PASS/WARN/FAIL interpretation
- Successor scenario planning

## 4. Replacement model

Zero Trust packages, capability mappings, implementation actions, validators, and sanitized evidence are the active authorities.

ZT-ARC-001 surrounds:

```text
ZT-FND-001 -> ZT-NET-001 -> ZT-VIS-001 -> ZT-ID-001
           -> ZT-CV-001 -> ZT-RV-001 -> ZT-SCH-001
           -> P1-ACC-001
```

## 5. Package flow

The machine-readable authority is `docs/zero-trust/package-flow.yaml`. Package order does not imply implementation or acceptance.

## 6. Status migration

Implementation, local validation, runtime validation, runtime acceptance, evidence, and maturity remain separate. No status is promoted by retirement.

## 7. Evidence migration

Dedicated scenario evidence was removed. Package and recovery evidence under `docs/evidence/zero-trust/` and `docs/zero-trust/recovery/` remains protected. Git history preserves deleted material.

## 8. Validator migration

Package, capability, architecture, runbook, repository-safety, synchronization, and report-check validators remain. Scenario aggregate and scenario-count checks are removed.

## 9. Git-history recovery

No tracked archive, backup, legacy, or deprecated copy is created. Historical recovery uses Git history.

## 10. Explicit non-claims

This decision does not establish implementation, runtime validation, Phase 1 completion, production readiness, compliance, certification, or maturity.

## 11. Known limitations

Existing reusable configuration examples may retain general test-case language, but they have no numbered-scenario authority. Package-owned acceptance cases replace numbered-scenario execution authority. The authenticated KISA seed map is planning-only; complete technical-control review and acceptance remain ZT-GOV-MAP-001 work.

## 12. Next action

ZT-GOV-MAP-001 is the next separately authorized action. It may complete and accept the integrated Zero Trust Guideline 2.0 and authenticated KISA 2026 technical-control mapping framework; this retirement record does not execute it.
