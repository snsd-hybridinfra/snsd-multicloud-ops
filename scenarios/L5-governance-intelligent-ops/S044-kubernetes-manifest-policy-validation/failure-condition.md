# Failure Condition

This scenario fails if any of the following occur:

- The operational capability cannot be validated against the objective.
- Required evidence is missing or not traceable.
- Excluded implementation code or real environment changes are introduced.
- Secrets, credentials, tfstate, kubeconfig files, private keys, or account-specific values are captured.
- Rollback or recovery steps are undefined for future execution.