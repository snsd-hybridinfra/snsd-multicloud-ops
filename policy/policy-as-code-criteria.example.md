# Policy as Code Criteria

| Policy Domain | Policy Rule | Evaluation Input | Expected Condition | Violation Condition | Required Evidence | Related Scenario | Final Judgment |
|---|---|---|---|---|---|---|---|
| Terraform drift governance | Detection mapping | Sanitized input | retired-numbered-case present | Missing retired-numbered-case | Detection evidence | retired-numbered-case | POLICY_PASS |
| Terraform remediation governance | Remediation mapping | Sanitized input | retired-numbered-case present | Missing approval/rollback | Remediation evidence | retired-numbered-case | POLICY_FAIL |
| Security rule governance | Least privilege | Sanitized input | Restricted placeholders | Broad exposure | Baseline evidence | retired-numbered-case/retired-numbered-case/retired-numbered-case/retired-numbered-case | POLICY_FAIL |
| Backup evidence governance | No real artifact | Sanitized input | Metadata only | Real artifact | retired-numbered-case evidence | retired-numbered-case | POLICY_PASS |
| Restore evidence governance | No real restored data | Sanitized input | Metadata only | Real data | retired-numbered-case evidence | retired-numbered-case | POLICY_PASS |
| Cost governance | Cost mapping | Sanitized input | retired-numbered-case/retired-numbered-case mapping | Mapping absent | Cost/cleanup evidence | retired-numbered-case/retired-numbered-case | POLICY_REVIEW_REQUIRED |
| Kubernetes manifest governance placeholder | Delegated detail | Sanitized input | retired-numbered-case mapping | Detail duplicated | retired-numbered-case evidence | retired-numbered-case | POLICY_PASS |

Exceptions require owner, reason, expiry, approval, rollback condition, and evidence reference. Policy validation maps to retired-numbered-case.
