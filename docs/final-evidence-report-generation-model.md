# Final Evidence Report Generation Model

Inputs: `docs/progress-tracker.md`, `docs/scenario-status-matrix.md`, `docs/evidence-status-matrix.md`, `docs/implementation-log.md`, `docs/risk-register.md`, `docs/scope-lock.md`, `docs/excluded-scope.md`, `scenarios/`, and `evidence/`.

Outputs: S050 `configs/final-evidence-report.sample.md`, `configs/final-evidence-report-summary.sample.json`, generated Markdown/JSON equivalents, `logs/final-evidence-report-generation.log`, and `configs/final-evidence-report-validation-summary.md`.

Aggregation counts S001-S050, confirms 11 scenario docs and evidence docs, known statuses, level/evidence totals, partial/blocked scenarios, risks, exclusions, and absence of secrets/real identifiers.

Judgments: `FINAL_REPORT_READY` when coverage/sections/matrices/safety pass; `FINAL_REPORT_WARNING` for complete but partial/placeholder evidence; `FINAL_REPORT_INCOMPLETE` for missing coverage; `FINAL_REPORT_BLOCKED` for a critical blocker; `FINAL_REPORT_INVALID` for secrets, real identifiers, or unsafe claims.
