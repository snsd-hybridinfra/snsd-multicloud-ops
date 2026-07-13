# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Security header baseline | Baseline exists. | generated log and summary |
| V002 | Security header rule matrix | Matrix exists. | generated log and summary |
| V003 | Nginx example config | Marked example exists. | generated log and summary |
| V004 | Server token reduction | `server_tokens off` exists. | generated log and summary |
| V005 | Required security headers | Six headers exist. | generated log and summary |
| V006 | Required header values | Exact values/placeholders exist. | generated log and summary |
| V007 | Always directive | Every header uses `always`. | generated log and summary |
| V008 | Baseline and matrix completeness | Required entries, guidance, and limits exist. | generated log and summary |
| V009 | TLS material safety | No TLS path or private material. | generated log and summary |
| V010 | Address and domain safety | No numeric address or real domain. | generated log and summary |
| V011 | Credential and account safety | No credential or identifier. | generated log and summary |
| V012 | Execution safety boundary | No Nginx, curl, host, or network command. | generated log and summary |

Every check maps by ID to `logs/nginx-security-header-validation.log` and `configs/nginx-security-header-summary.md`.
