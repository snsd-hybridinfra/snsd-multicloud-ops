# Policy as Code Criteria

| Policy Domain | Policy Rule | Evaluation Input | Expected Condition | Violation Condition | Required Evidence | Related Scenario | Final Judgment |
|---|---|---|---|---|---|---|---|
| Terraform drift governance | Detection mapping | Sanitized input | S041 present | Missing S041 | Detection evidence | S041 | POLICY_PASS |
| Terraform remediation governance | Remediation mapping | Sanitized input | S042 present | Missing approval/rollback | Remediation evidence | S042 | POLICY_FAIL |
| Security rule governance | Least privilege | Sanitized input | Restricted placeholders | Broad exposure | Baseline evidence | S014/S015/S016/S037 | POLICY_FAIL |
| Backup evidence governance | No real artifact | Sanitized input | Metadata only | Real artifact | S038 evidence | S038 | POLICY_PASS |
| Restore evidence governance | No real restored data | Sanitized input | Metadata only | Real data | S039 evidence | S039 | POLICY_PASS |
| Cost governance | Cost mapping | Sanitized input | S045/S046 mapping | Mapping absent | Cost/cleanup evidence | S045/S046 | POLICY_REVIEW_REQUIRED |
| Kubernetes manifest governance placeholder | Delegated detail | Sanitized input | S044 mapping | Detail duplicated | S044 evidence | S044 | POLICY_PASS |

Exceptions require owner, reason, expiry, approval, rollback condition, and evidence reference. Policy validation maps to S043.
