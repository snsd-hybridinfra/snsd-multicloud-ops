# Failure Condition

## Failure Conditions

- The topology document or a required router example is missing.
- A required zone, device, or CIDR token is absent.
- An example lacks the required placeholder structure.
- A private-key marker, credential assignment, or IPv4 literal is detected.
- Validation attempts a router connection, EVE-NG API call, credential read, cloud access, kubeconfig read, or tfstate access.

## Evidence of Failure

The generated log and summary identify the failed check and sanitized reason.

## Follow-Up Requirement

Correct only the repository topology or example config, then rerun S002. Live network remediation remains outside this scenario.
