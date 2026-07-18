# Korean Zero Trust Guideline 2.0 Alignment

## Purpose

This framework maps the SNSD lab and its locked S001-S050 validation model to selected capabilities from the Korean Zero Trust Guideline 2.0.

Repository positioning: **Hybrid and Multicloud Secure Operations Platform aligned with the Korean Zero Trust Guideline 2.0.** Alignment means traceable mapping and evidence-based assessment. It does not mean full compliance, complete implementation, certification, or organization-wide maturity.

The post-Phase-1 target positioning is **IaC, Configuration as Code, and Policy
as Code-driven Advanced Zero Trust Secure Operations Platform with an
Optimal-Ready Extension Architecture**. The conservative public title is
**Hybrid and Multicloud-Ready Secure Operations Platform**. Configuration as
Code is the meaning of CaC throughout the target architecture; CaC does not
mean Compliance as Code here.

## Scope and Boundaries

- The authoritative source defines terminology, architecture, maturity, capabilities, adoption, and assessment concepts.
- Repository scenario status, capability implementation status, evidence level, validation result, and maturity are separate dimensions.
- S002 and S005 have scenario-level runtime validation. That fact does not make any complete Zero Trust capability validated or establish a maturity level.
- All capability maturity values remain `UNASSESSED` until capability-specific evidence is evaluated.
- Planned AWS, Azure, Kubernetes, database, observability, recovery, ML, and policy scenarios remain unimplemented unless their existing tracking records say otherwise.

## Document Index

- [Authoritative source](authoritative-source.md)
- [Reference architecture](zero-trust-reference-architecture.md)
- [Capability taxonomy](capability-taxonomy.md)
- [Machine-readable capability catalog](capability-catalog.yaml)
- [Maturity model](maturity-model.md)
- [Adoption lifecycle](adoption-lifecycle.md)
- [Scenario-capability matrix](scenario-capability-matrix.md)
- [Control coverage matrix](control-coverage-matrix.md)
- [Evidence coverage matrix](evidence-coverage-matrix.md)
- [Maturity assessment method](maturity-assessment-method.md)
- [Gap register](gap-register.md)
- [Implementation roadmap](implementation-roadmap.md)
- [Validation checklist](validation-checklist.md)
- [Current baseline assessment](current-baseline-assessment.md)
- [Machine-readable current baseline](current-baseline-assessment.yaml)
- [Machine-readable implementation backlog](capability-implementation-backlog.yaml)
- [Laboratory implementation blueprint](implementation-blueprint.md)
- [Control-pattern catalog](control-pattern-catalog.md)
- [Reference laboratory architecture](reference-lab-architecture.md)
- [Capability verification plan](capability-verification-plan.md)
- [Phase gates](phase-gates.md)
- [Prioritized implementation queue](prioritized-implementation-queue.md)
- [Future scenario governance](future-scenario-governance.md)
- [Governance rules](governance.md)
- [Maintenance workflow](maintenance-workflow.md)
- [ZT-ARC-001 target architecture](target-architecture/README.md)
- [Advanced target selection](target-architecture/capability-selection.yaml)
- [Advanced acceptance model](target-architecture/advanced-maturity-acceptance-model.yaml)
- [Target phase roadmap](target-architecture/phase-roadmap.md)
- [Authoritative operational runbook index](../runbooks/RUNBOOK_INDEX.md)
- [ZT-FND-001 package](packages/zt-fnd-001-restricted-validation-foundation.md)
- [ZT-FND-001 rollback](packages/zt-fnd-001-rollback.md)
- [ZT-ARC-001 package](packages/zt-arc-001-advanced-target-architecture.md)

## Machine Validation

The catalog, baseline, and capability backlog YAML files are the repository machine-readable taxonomy, current-assessment, and planning authorities respectively. Markdown matrices are presentation views and must remain synchronized. The backlog cannot promote current implementation, validation, evidence, or maturity state.

```powershell
python tools/validate_zero_trust.py --verbose
python tools/check_zero_trust_sync.py
python tools/generate_zero_trust_reports.py --check
python tools/validate_advanced_target_architecture.py --verbose
powershell -ExecutionPolicy Bypass -File tools/validate-zero-trust.ps1
python -m unittest discover -s tests -v
```

Validation is read-only by default. Only `generate_zero_trust_reports.py --write` can write, and it is restricted to reviewed generated markers.

## Current Boundary

Current runtime evidence supports a limited network foundation, one OpenStack AIO provider/tenant path, and a restricted read-only validation workflow. It does not prove micro-segmentation, continuous identity verification, endpoint compliance, PAM, EDR/XDR, DLP, complete DevSecOps, AI-driven policy, full data governance, or Optimal maturity.

The second-pass baseline records 0 fully validated capabilities, 6 partially
validated capabilities within the bounded lab scope, 7 mapped-only
capabilities, and 39 identified capability gaps. All 52 maturity values remain
`UNASSESSED`.

ZT-ARC-001 classifies 21 capabilities as Advanced primary targets, 15 as
Advanced supporting targets, 4 as Initial targets, 5 as design-only, and 7 as
future Optimal-roadmap items. These are target-selection judgments only. The
architecture package does not change the current counts above.
