# Cost Impact Classification Matrix

| Resource Category | Cost Signal | Risk Level | Required Evidence | Cleanup Mapping | Related Scenario | Final Judgment |
|---|---|---|---|---|---|---|
| Compute instance placeholder | monthly estimate | Medium | owner | S046 | S045/S046 | COST_REVIEW_REQUIRED |
| Persistent volume placeholder | retained capacity | Medium | owner/retention | S046 | S045/S046 | COST_REVIEW_REQUIRED |
| Public IP placeholder | allocated address | Medium | owner/exposure review | S046 | S045/S046 | COST_REVIEW_REQUIRED |
| Load balancer placeholder | hourly estimate | Medium | owner | S046 | S045/S046 | COST_REVIEW_REQUIRED |
| Object storage placeholder | growth/retention | Medium | owner/retention | S046 | S045/S046 | COST_REVIEW_REQUIRED |
| NAT gateway placeholder | usage estimate | High | owner/approval | S046 | S045/S046 | COST_REVIEW_REQUIRED |
| Managed database placeholder | capacity estimate | High | owner/retention | S046 | S045/S046 | COST_REVIEW_REQUIRED |
| Kubernetes node placeholder | node count | Medium | owner | S046 | S045/S046 | COST_REVIEW_REQUIRED |
| Monitoring storage placeholder | retention growth | Medium | owner/retention | S046 | S045/S046 | COST_REVIEW_REQUIRED |
| Orphaned resource placeholder | cost without owner | High | cleanup evidence | S046 required | S046 | COST_GUARDRAIL_FAIL |

Critical spikes require approval. Missing estimates are `COST_EVIDENCE_INCOMPLETE`.
