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
           -> ZT-CV-001 -> ZT-RV-001 -> P1-ACC-001
```

`ZT-SCH-001` is preserved outside this sequence as the disabled final Phase 5
project gate immediately before `P5-ACC-001`.

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

## Subsequent closure

`ZT-GOV-MAP-001` was later completed as a separate action. Its current authority is `docs/zero-trust/mappings/zt-kisa-technical-control-map.yaml`; `P0-ACC-001` is the next execution-plan action. This note does not rewrite the retirement action's historical scope or evidence.

## Subsequent scheduled-validation rebaseline

ADR 0013 later removed `ZT-SCH-001` from the sequential Phase 1 predecessor
chain, retained it as a disabled final Phase 5 gate, and set `P1-ACC-001` as the
current Phase 1 action. The historical RV campaign and integrated assessment
snapshots remain unchanged; `docs/zero-trust/package-flow.yaml` is the current
flow authority.

## Subsequent Phase 1 acceptance preflight

P1-ACC-001 first recorded `BLOCKED_STALE_EVIDENCE` because every reviewed RV
record exceeded P7D at the acceptance assessment time. ADR 0014 later preserved
that historical result and accepted the scoped `P1-RV-FRESHNESS-001` residual
risk for Phase 2 local entry. The stale finding remains mandatory final-gate
work and is not reclassified as fresh evidence.
