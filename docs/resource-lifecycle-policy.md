# Resource Lifecycle and Cleanup Policy

**Status: ACTIVE POLICY — OpenStack apply/validate evidence exists, while
destroy and cleanup verification remain unvalidated.**

## Required Lifecycle

Every infrastructure-bearing lab change follows:

`Plan -> Apply -> Validate -> Collect sanitized evidence -> Destroy -> Verify cleanup`

| Stage | Required Record | Prohibited Shortcut |
|---|---|---|
| Plan | Purpose, owner, provider, resource count, cost guardrail, TTL, rollback, evidence owner | Applying from an unreviewed configuration |
| Apply | Approved change identifier and bounded resource list | Untracked manual expansion |
| Validate | Owning scenario, expected result, and actual judgment | Treating apply success as validation |
| Collect | Minimum sanitized evidence mapped to the scenario | Committing raw IDs, addresses, credentials, state, or kubeconfig |
| Destroy | Terraform destroy/manual cleanup plan as applicable | Leaving temporary compute/public addresses running |
| Verify cleanup | Post-destroy inventory and unresolved-resource decision | Assuming command success means cleanup is complete |

## Ownership

- Resource owner: accountable for purpose and runtime window.
- Evidence owner: sanitizes and maps validation artifacts.
- Cleanup owner: confirms destroy and post-cleanup inventory.
- Reviewer: verifies limits, tags, sensitive-data safety, and scenario boundary.

One person may hold multiple roles in the portfolio lab, but every role must be
explicit in the change record.

## Cleanup Rules

- AWS EC2, Azure VM, OpenStack instances, and public/Floating IPs are temporary
  unless a documented exception exists.
- Compute creation defaults to disabled where practical.
- Expired resources become cleanup candidates and cannot be silently retained.
- Cleanup evidence records aggregate results and masked identifiers only.
- Terraform state, provider credentials, billing values, and account IDs never
  enter evidence.

## Failure Handling

If validation fails, preserve only sanitized failure evidence, execute the
documented rollback, destroy temporary resources, and verify cleanup. A failed
validation does not justify extending public exposure or bypassing cost limits.

## Relationship to Governance Scenarios

S041-S046 own drift, remediation decisions, policy, cost, and cleanup validation.
This policy defines the lab lifecycle but does not automatically change their
statuses or claim automated enforcement.

## Non-Production Disclaimer

This is a manual portfolio-lab lifecycle policy, not an enterprise ITSM,
Terraform Cloud, GitOps, FinOps automation, or production lifecycle service.
