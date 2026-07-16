# S037-security-rule-misconfiguration-validation

| Field | Value |
|---|---|
| Scenario ID | S037 |
| Scenario Name | Security Rule Misconfiguration Validation |
| Level | L4 Failure Recovery Validation |
| Category | Failure Recovery |
| Related Components | AWS SG, Azure NSG, OpenStack SG, firewall, NetworkPolicy placeholders, rollback policy |
| Validation Type | StaticEvidence only |
| Evidence Directory | evidence/L4-failure-recovery/S037-security-rule-misconfiguration-validation/ |
| Status | NOT_STARTED |

## Objective Summary

Validate controlled security-rule misconfiguration detection, exposure classification, policy requirements, manual rollback evidence, and safe post-rollback state without changing real infrastructure.

## Scope Summary

Local artifacts only. No cloud CLI, Kubernetes, firewall, Terraform, routing, security-rule mutation, automatic blocking, or SOAR response is performed.

## Validation Summary

Sixteen checks cover artifacts, runbook exclusions, criteria/decision matrices, policy metadata, command boundaries, pre/misconfiguration/detection/impact/rollback/post evidence, expiry maturity, identifier safety, and no execution.

## Evidence Output Summary

Committed samples are non-production. Unsafe placeholders are confined to labeled misconfiguration/detection examples; generated evidence contains judgments only.
