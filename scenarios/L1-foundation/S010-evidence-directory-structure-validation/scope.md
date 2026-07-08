# Scope

## Included

- Scenario directory count validation plan.
- Evidence directory count validation plan.
- Scenario-to-evidence path matching validation plan.
- Required evidence file validation plan.
- Required evidence subdirectory validation plan.
- Evidence filename convention validation plan.
- Sensitive file exclusion validation plan.
- Evidence status matrix consistency validation plan.
- Repository validation script execution plan.
- Failure condition for missing evidence directory, missing required file, inconsistent path, or sensitive file exposure.

## Excluded

- Terraform, Ansible, Kubernetes, cloud, monitoring, ML, or backup implementation logic.
- Real evidence collection from live systems.
- Real public IPs, credentials, private keys, tfstate, kubeconfig files, or account-specific files.
- Binary evidence creation for this skeleton.
- Modifying other scenario or evidence directories.

## Assumptions

- The expected repository model contains 50 scenario directories and 50 matching evidence directories.
- Evidence status values are `NOT_READY`, `PARTIAL`, `READY`, and `REVIEWED`.
- The repository validation script is `tools/validate-repo-structure.ps1`.
