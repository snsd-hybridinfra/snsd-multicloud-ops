# Validation

Scenario: S019-nginx-security-header-validation
Level: L2-security-baseline
Capability: Nginx Security Header Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real Nginx output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Nginx configuration syntax validation plan | Nginx syntax validation can be performed before service exposure. | TODO | NOT_RUN | `commands.md`; `configs/nginx-security-header-summary.md` |
| V002 | server_tokens off validation plan | Nginx server version exposure is reduced. | TODO | NOT_RUN | `commands.md`; `configs/nginx-security-policy.md` |
| V003 | X-Content-Type-Options header validation plan | Header is present with an approved value. | TODO | NOT_RUN | `commands.md`; `configs/nginx-security-policy.md` |
| V004 | X-Frame-Options header validation plan | Header is present with an approved value. | TODO | NOT_RUN | `commands.md`; `configs/nginx-security-policy.md` |
| V005 | Referrer-Policy header validation plan | Header is present with an approved value. | TODO | NOT_RUN | `commands.md`; `configs/nginx-security-policy.md` |
| V006 | Content-Security-Policy placeholder validation plan | CSP placeholder is documented until service-specific directives are approved. | TODO | NOT_RUN | `commands.md`; `configs/nginx-security-policy.md` |
| V007 | HTTP response header capture using curl -I plan | Response headers can be captured and reviewed. | TODO | NOT_RUN | `commands.md`; `logs/nginx-security-header-validation.log`; `screenshots/nginx-security-header-test.png` |
| V008 | Access log capture plan | Access logs can be reviewed without sensitive values. | TODO | NOT_RUN | `commands.md`; `logs/nginx-security-header-validation.log` |
| V009 | Error log capture plan | Error logs can be reviewed for configuration or response issues. | TODO | NOT_RUN | `commands.md`; `logs/nginx-security-header-validation.log` |
| V010 | Failure condition for missing security header, exposed server version, invalid Nginx configuration, or unexplained response behavior | Unsafe or unexplained response patterns produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Nginx security header summary is captured: NOT_READY
- Nginx security policy is captured: NOT_READY
- Nginx security header validation log is captured: NOT_READY
- Nginx security header screenshot is captured: NOT_READY

## Notes

This scenario validates Nginx security header design only. Real TLS implementation is excluded. Ingress routing validation is handled in S023, and load balancing validation is handled in S025.
