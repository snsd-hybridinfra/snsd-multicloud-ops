# Resource Cleanup Validation

> SAMPLE / NON-PRODUCTION — static governance evidence only.

S046 validates cleanup candidates, ownership, lifecycle/retention, cost classification, approval/exception, dependency risk, cleanup plan, rollback/recovery note, and final judgment for `<cloud-provider-placeholder>`, `<terraform-environment-placeholder>`, `<resource-type-placeholder>`, `<resource-address-placeholder>`, `<resource-id-placeholder>`, and `<cleanup-candidate-id-placeholder>`. Orphaned means no valid owner/dependency evidence; unused means no approved workload; cost-bearing idle means retained cost without approved use. Evidence uses `<owner-placeholder>`, `<retention-class-placeholder>`, `<cleanup-change-id-placeholder>`, `<approval-id-placeholder>`, `<exception-id-placeholder>`, `<rollback-change-id-placeholder>`, `<estimated-monthly-cost-placeholder>`, `<cleanup-risk-level-placeholder>`, and `<evidence-path>`.

S045 owns cost guardrails, S041/S042 drift, and S050 final reporting. Real deletion, Terraform apply/destroy/state removal, cloud/kubectl delete, storage/database/volume/network/security-group deletion, automatic cleanup/shutdown, and production execution are OUT OF SCOPE.
