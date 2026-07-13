# Failure Condition

## Critical Failure Conditions

- Scenario or evidence count, ID coverage, or uniqueness is invalid.
- A scenario lacks a mirrored evidence path or an orphan evidence path exists.
- A required evidence file or subdirectory is missing.
- A forbidden state, real tfvars, key, credential, kubeconfig, cloud config, database dump, certificate with private material, or archive file is detected.
- The evidence status matrix is missing S001-S050, contains duplicates, or uses a non-readiness status.

Any critical failure produces a non-zero exit. S010 does not reinterpret an individual scenario validation result.
