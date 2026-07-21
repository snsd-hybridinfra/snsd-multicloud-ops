# Authoritative Operational Runbook Index

## Authority and status summary

| Collection | Count | Authority | Current meaning |
|---|---:|---|---|
| Phase 1 baseline | 7 | Authoritative for bounded Phase 1 operator procedure | Two repository procedures implemented, four package/evidence procedures partial, one design specification |
| Future-phase numbered designs | 29 | Architecture design authority only | `DESIGN_SPECIFICATION`; no executable implementation is implied |
| Root `runbooks/` references | 53 Markdown files | Secondary reference only | Scenario-specific material; never overrides this index or the Phase 1 manifest |

`VALIDATED_LOCAL` means the runbook structure and repository-local procedure
were validated. `PARTIALLY_RUNTIME_VALIDATED` reflects only the bounded package
evidence cited by the runbook. Neither status establishes Phase 1 completion,
capability-wide validation, compliance, certification, or maturity.

## Phase 1 authoritative baseline

| ID | Runbook | Procedure | Validation | Related packages/actions |
|---|---|---|---|---|
| RB-P1-001 | [`phase-1/01-phase-1-entry-and-preflight.md`](phase-1/01-phase-1-entry-and-preflight.md) | IMPLEMENTED | VALIDATED_LOCAL | P1-REC-002, P1-HYG-001, P1-RUN-BASE |
| RB-P1-002 | [`phase-1/02-repository-safe-validation.md`](phase-1/02-repository-safe-validation.md) | IMPLEMENTED | VALIDATED_LOCAL | P1-HYG-001 |
| RB-P1-003 | [`phase-1/03-evidence-handling-and-sanitization.md`](phase-1/03-evidence-handling-and-sanitization.md) | PARTIALLY_IMPLEMENTED | VALIDATED_LOCAL | ZT-FND-001, ZT-NET-001, ZT-VIS-001 |
| RB-P1-004 | [`phase-1/04-network-validation-and-gap-management.md`](phase-1/04-network-validation-and-gap-management.md) | PARTIALLY_IMPLEMENTED | PARTIALLY_RUNTIME_VALIDATED | ZT-NET-001 |
| RB-P1-005 | [`phase-1/05-visibility-validation-and-gap-management.md`](phase-1/05-visibility-validation-and-gap-management.md) | PARTIALLY_IMPLEMENTED | PARTIALLY_RUNTIME_VALIDATED | ZT-VIS-001, ZT-VIS-002 |
| RB-P1-006 | [`phase-1/06-identity-validation-readiness.md`](phase-1/06-identity-validation-readiness.md) | IMPLEMENTED | VALIDATED_RUNTIME | ZT-ID-001 |
| RB-P1-007 | [`phase-1/07-repeatable-and-scheduled-validation.md`](phase-1/07-repeatable-and-scheduled-validation.md) | DESIGN_SPECIFICATION | VALIDATED_LOCAL | ZT-CV-001, ZT-RV-001, ZT-SCH-001 |

## Future-phase design specifications

| Runbook | Purpose | Procedure | Validation | Architecture package |
|---|---|---|---|---|
| `00-platform-overview.md` | Understand platform boundaries and the Golden Path | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-ARC-001 |
| `01-prerequisites.md` | Prepare physical and manual prerequisites | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-ONB-001 |
| `02-target-selection.md` | Select a target type | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-ONB-001 |
| `03-openstack-vm-onboarding.md` | Plan OpenStack VM onboarding | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-IAC-001 |
| `04-existing-vm-onboarding.md` | Plan existing VM onboarding | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-IAC-002 |
| `05-physical-server-onboarding.md` | Plan physical server onboarding | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-IAC-002 |
| `06-environment-profile.md` | Plan a secret-free target profile | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-PLT-001 |
| `07-secret-preparation.md` | Plan external secret preparation | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-CFG-001 |
| `08-preflight-validation.md` | Plan profile and host readiness | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-ONB-001 |
| `09-iac-plan.md` | Plan infrastructure or registration changes | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-PLN-001 |
| `10-policy-evaluation.md` | Plan policy evaluation | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-PAC-001 |
| `11-deployment-approval.md` | Plan approval binding | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-DEP-001 |
| `12-platform-deployment.md` | Plan approved deployment | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-DEP-001 |
| `13-runtime-validation.md` | Plan capability and service validation | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-PAC-003 |
| `14-platform-status.md` | Plan state reporting | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-PLT-001 |
| `15-drift-detection.md` | Plan drift detection | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-DRIFT-001 |
| `16-reconciliation.md` | Plan approved reconciliation | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-PAC-004 |
| `17-backup.md` | Plan backup | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-REC-001 |
| `18-restore.md` | Plan restore | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-REC-001 |
| `19-rollback.md` | Plan rollback | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-REC-001 |
| `20-upgrade.md` | Plan upgrade | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-CFG-001 |
| `21-secret-rotation.md` | Plan secret rotation | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-CFG-001 |
| `22-certificate-rotation.md` | Plan certificate rotation | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-CFG-001 |
| `23-incident-response.md` | Plan incident response | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-INC-001 |
| `24-target-replacement.md` | Plan target replacement | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-PLT-001 |
| `25-decommission.md` | Plan decommission | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-PLT-001 |
| `26-evidence-handling.md` | Plan future evidence operations | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-EFF-001 |
| `27-operator-handoff.md` | Plan clean-operator acceptance | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-HOF-001 |
| `28-troubleshooting.md` | Plan failure-boundary diagnosis | DESIGN_SPECIFICATION | NOT_IMPLEMENTED | ZT-RUN-001 |
