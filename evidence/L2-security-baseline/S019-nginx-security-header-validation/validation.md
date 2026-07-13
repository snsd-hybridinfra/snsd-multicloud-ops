# Validation

Scenario: S019-nginx-security-header-validation

Level: L2-security-baseline

Date: 2026-07-13

Overall status: PASS

| Check ID | Validation Item | Expected Condition | Actual Result | Evidence File | Status |
|---|---|---|---|---|---|
| V001 | Security header baseline | File exists. | Baseline exists. | generated log and summary | PASS |
| V002 | Security header rule matrix | File exists. | Matrix exists. | generated log and summary | PASS |
| V003 | Nginx example config | File exists. | Marked example exists. | generated log and summary | PASS |
| V004 | Server token reduction | `server_tokens off` exists. | Directive found. | generated log and summary | PASS |
| V005 | Required security headers | Six headers exist. | All found. | generated log and summary | PASS |
| V006 | Required header values | Exact values exist. | All values match. | generated log and summary | PASS |
| V007 | Always directive | Every header uses `always`. | All six pass. | generated log and summary | PASS |
| V008 | Baseline and matrix completeness | Required documentation exists. | All content found. | generated log and summary | PASS |
| V009 | TLS material safety | No TLS path or private material. | None detected. | generated log and summary | PASS |
| V010 | Address and domain safety | No address or real domain. | None detected. | generated log and summary | PASS |
| V011 | Credential and account safety | No credential or identifier. | None detected. | generated log and summary | PASS |
| V012 | Execution safety boundary | No live process, host, or network command. | None detected. | generated log and summary | PASS |

## Generated Result

All twelve checks passed using repository files only. Evidence is recorded in `logs/nginx-security-header-validation.log` and `configs/nginx-security-header-summary.md`.
