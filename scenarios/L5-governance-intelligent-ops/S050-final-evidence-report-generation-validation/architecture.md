# Architecture

Implemented flow: canonical local docs and mirrored S001-S050 directories -> Markdown/JSON generator -> static report validator -> S050 evidence log/summary.

## Relevant Components

- Tracking inputs: progress tracker, scenario status matrix, and evidence status matrix.
- Review inputs: validation checklist, implementation log, and risk register.
- Scenario inputs: each scenario `README.md` and `evidence-map.md`.
- Evidence inputs: each scenario's `commands.md`, `validation.md`, and approved supporting artifacts.
- Aggregation model: coverage, status, completeness, exception, and level summaries.
- Judgment model: one supported `FINAL_REPORT_*` state with a documented reason.
- Report output: `<final-report-file>` placeholder plus reviewer and next-phase placeholders.

## Logical Flow

1. Confirm required inputs exist and are internally consistent.
2. Aggregate scenario and evidence state by scenario and level.
3. Identify missing evidence and failed or blocked scenarios.
4. Build the required report sections from sanitized references.
5. Assign a supported final judgment.
6. Review the report schema and record validation evidence.

No live systems, cloud accounts, compliance platforms, or real report-generation tooling are part of this architecture.
