# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
| --- | --- | --- | --- | --- |
| V001 | Progress tracker input | Review required level and total rows | L1 through L5 and total progress are available | `configs/final-evidence-report-generation-summary.md` |
| V002 | Scenario status matrix input | Inspect S001 through S050 rows | Every scenario has a recognized status | `configs/final-evidence-report-generation-summary.md` |
| V003 | Evidence status matrix input | Inspect S001 through S050 rows | Every scenario has a recognized evidence status | `configs/final-evidence-completeness-matrix.md` |
| V004 | Validation checklist input | Review checklist sections | Repository, scenario, evidence, security, and readiness checks are referenceable | `configs/final-evidence-report-schema.md` |
| V005 | Implementation log reference | Verify report reference plan | Relevant implementation history can be cited without duplication | `validation.md` |
| V006 | Risk register reference | Verify report reference plan | Open and relevant risks remain visible | `validation.md` |
| V007 | Scenario coverage aggregation | Compare scenario directories and matrix rows | S001 through S050 are represented once | `configs/final-evidence-report-generation-summary.md` |
| V008 | Evidence completeness aggregation | Compare required evidence paths and statuses | Completeness and gaps are summarized consistently | `configs/final-evidence-completeness-matrix.md` |
| V009 | L1 through L5 coverage summary | Aggregate by level | Each level has an explicit `<coverage-rate>` | `screenshots/final-evidence-coverage-summary.png` |
| V010 | Missing evidence summary | Filter incomplete evidence records | Every known gap is listed or explicitly absent | `configs/final-evidence-completeness-matrix.md` |
| V011 | Failed or blocked scenario summary | Filter scenario validation states | Failed or blocked work is visible and traceable | `validation.md` |
| V012 | Final report section completeness | Compare draft schema with required sections | All required sections are present | `configs/final-evidence-report-schema.md` |
| V013 | Final judgment state | Validate selected state against allowed values | Exactly one supported judgment is used with a reason | `configs/final-report-judgment-model.md` |
| V014 | Boundary and consistency review | Inspect claims, totals, statuses, and evidence references | No unsupported compliance claim, inconsistent summary, or sensitive value is present | `logs/final-evidence-report-generation-validation.log` |
