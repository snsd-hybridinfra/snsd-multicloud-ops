# Scope

## Included

- Scenario and evidence status aggregation.
- Validation result and L1 through L5 coverage summaries.
- Evidence completeness and missing evidence summaries.
- Failed or blocked scenario summary.
- References to the implementation log, risk register, and validation checklist.
- Final report schema, review checklist, and judgment model.
- Placeholder final report output and reviewer notes.
- Evidence mapping for the report-generation validation process.

## Target Report Inputs

- `docs/progress-tracker.md`
- `docs/scenario-status-matrix.md`
- `docs/evidence-status-matrix.md`
- `docs/validation-checklist.md`
- `docs/implementation-log.md`
- `docs/risk-register.md`
- Scenario `README.md` and `evidence-map.md` files.
- Evidence `commands.md`, `validation.md`, and scenario-specific placeholder artifacts.

## Required Report Sections

- Report title, generation timestamp, repository name, and project title.
- Validation scope and scenario coverage summaries.
- Separate L1, L2, L3, L4, and L5 summaries.
- Scenario status and evidence status summaries.
- Failed or blocked scenario and missing evidence summaries.
- Risk register and implementation log references.
- Final judgment, `<reviewer-note>`, and next implementation phase recommendation placeholder.

## Final Judgment Model

- `FINAL_REPORT_READY`
- `FINAL_REPORT_PARTIAL`
- `FINAL_REPORT_INVALID`
- `FINAL_REPORT_INCONCLUSIVE`
- `FINAL_REPORT_OUT_OF_SCOPE`

## Excluded

- Generation of a real final audit or compliance report.
- Claims of ISO 27001, ISMS-P, SOC 2, CSA STAR, PCI-DSS, or legal compliance certification.
- Claims of production-grade audit readiness.
- Automated compliance enforcement or enterprise GRC integration.
- Replacement of individual scenario validation with aggregate reporting.
- New tools, infrastructure, cloud resources, or implementation code.
- Credentials, secrets, private keys, tfstate, kubeconfig, account identifiers, billing identifiers, or account-specific data.
