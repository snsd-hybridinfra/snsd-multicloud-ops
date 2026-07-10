# Commands and Planned Actions

Scenario: `S050-final-evidence-report-generation-validation`

Execution status: `NOT_RUN`

No real final evidence report or command output has been generated. Replace each TODO only after an authorized, sanitized review.

| Check ID | Planned Input or Action | Purpose | Planned Evidence | Output |
| --- | --- | --- | --- | --- |
| V001 | Review `docs/progress-tracker.md` | Confirm level and total progress inputs | `configs/final-evidence-report-generation-summary.md` | TODO |
| V002 | Review `docs/scenario-status-matrix.md` | Confirm S001 through S050 status inputs | `configs/final-evidence-report-generation-summary.md` | TODO |
| V003 | Review `docs/evidence-status-matrix.md` | Confirm evidence status inputs | `configs/final-evidence-completeness-matrix.md` | TODO |
| V004 | Review `docs/validation-checklist.md` | Confirm checklist input | `configs/final-evidence-report-schema.md` | TODO |
| V005 | Reference `docs/implementation-log.md` | Preserve implementation history traceability | `validation.md` | TODO |
| V006 | Reference `docs/risk-register.md` | Preserve open risk traceability | `validation.md` | TODO |
| V007 | Inspect `scenarios/<level>/<scenario-id>/README.md` | Aggregate scenario coverage | `configs/final-evidence-report-generation-summary.md` | TODO |
| V008 | Inspect `evidence/<level>/<scenario-id>/` | Aggregate evidence completeness | `configs/final-evidence-completeness-matrix.md` | TODO |
| V009 | Aggregate L1 through L5 records | Produce level coverage summary | `screenshots/final-evidence-coverage-summary.png` | TODO |
| V010 | Identify missing required evidence | Produce missing evidence summary | `configs/final-evidence-completeness-matrix.md` | TODO |
| V011 | Identify failed or blocked scenarios | Produce exception summary | `validation.md` | TODO |
| V012 | Compare report draft with schema | Confirm required report sections | `configs/final-evidence-report-schema.md` | TODO |
| V013 | Apply final judgment model | Select one supported judgment | `configs/final-report-judgment-model.md` | TODO |
| V014 | Review consistency and prohibited claims | Confirm report boundary compliance | `logs/final-evidence-report-generation-validation.log` | TODO |

## Final Report Placeholder

```text
Final report file: <final-report-file>
Scenario ID: <scenario-id>
Evidence status: <evidence-status>
Validation result: <validation-result>
Coverage rate: <coverage-rate>
Reviewer note: <reviewer-note>
Final judgment: TODO
```

Allowed judgment values are `FINAL_REPORT_READY`, `FINAL_REPORT_PARTIAL`, `FINAL_REPORT_INVALID`, `FINAL_REPORT_INCONCLUSIVE`, and `FINAL_REPORT_OUT_OF_SCOPE`.
