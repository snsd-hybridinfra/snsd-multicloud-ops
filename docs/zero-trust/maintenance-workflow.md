# Zero Trust Maintenance Workflow

1. Review the external source and relevant package authority.
2. Update the highest machine-readable authority first.
3. Validate schemas, capability references, package IDs, predecessor rules, evidence links, and status separation.
4. Update reviewed presentation views only after authority is correct.
5. Run Zero Trust validation, synchronization, report check, package-flow validation, architecture and runbook validation, repository structure, and unit tests.
6. Confirm repository immutability, tracked runtime, secret, privacy, and overclaim gates.
7. Inspect the diff and explicit staging allowlist.
8. Commit only when the action authorizes publication and all checks pass.

The retired numbered scenario framework is never recreated or used for progress. New work belongs to a package, capability, technical target, validator, and sanitized evidence path.

Live infrastructure execution remains a separately approved workflow.
