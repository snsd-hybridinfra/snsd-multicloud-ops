# S041-terraform-drift-detection-validation

| Field | Value |
|---|---|
| Scenario ID | S041 |
| Scenario Name | Terraform Drift Detection Validation |
| Level | L5 Governance and Intelligent Operations Validation |
| Category | Governance Intelligent Ops |
| Primary Domain | Sanitized Terraform drift evidence |
| Related Components | Runbook, criteria/decision matrices, policy, plan JSON examples, manifest, static validator |
| Validation Type | StaticEvidence |
| Evidence Directory | evidence/L5-governance-intelligent-ops/S041-terraform-drift-detection-validation/ |
| Status | VALIDATED |

## Objective Summary

Validate the drift-detection workflow, sanitized plan signals, classification, and final judgment without running Terraform, reading state, querying cloud APIs, or remediating drift.

## Scope Summary

S041 validates detection only. S042 owns remediation, S043 policy validation, S045 cost guardrails, and S046 cleanup.

## Validation Summary

`tools/validate-terraform-drift-detection.ps1` performs local file parsing and safety checks. It never executes Terraform or provider commands.

## Evidence Output Summary

Generated log and summary plus sanitized samples are stored in the matching evidence directory. No tfstate, tfvars, plan binary, backend value, credential, real identifier, network value, or secret is stored.
