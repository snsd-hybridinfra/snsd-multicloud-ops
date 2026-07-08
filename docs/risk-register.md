# Risk Register

Track risks that may affect scenario quality, evidence integrity, cost, safety, or repository consistency.

| Risk ID | Risk | Impact | Mitigation | Status |
|---|---|---|---|---|
| R001 | Scope expansion | Repository may drift beyond locked validation scope. | Require scope review and ADR before expanding technologies or implementation boundaries. | Open |
| R002 | Cloud cost increase | Future validation could create billable resources unexpectedly. | Require explicit approval, cost guardrails, and teardown evidence before real cloud execution. | Open |
| R003 | Evidence missing | Scenarios may be difficult to review or reproduce. | Require evidence status updates and validation table completion for every scenario. | Open |
| R004 | Secret leakage | Sensitive material could be committed to the repository. | Enforce `.gitignore`, evidence sanitization, and review checklist before commits. | Open |
| R005 | OneDrive sync conflict | Local sync behavior may create conflicts or partial file updates. | Check working tree status before and after large edits; avoid simultaneous edits. | Open |
| R006 | Codex modifying unrelated files | Automation may change files outside the requested scope. | Require scope confirmation and final status review for every task. | Open |
| R007 | Scenario implementation inconsistency | Scenarios may use different structures or criteria. | Use `docs/scenario-template.md` and update tracking matrices consistently. | Open |
