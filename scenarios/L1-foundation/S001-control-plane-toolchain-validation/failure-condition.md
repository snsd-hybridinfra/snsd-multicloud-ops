# Failure Condition

## Failure Conditions

- One or more required tools cannot be invoked.
- A version command requires authentication or access to sensitive files.
- Command output cannot be captured in a reviewable form.
- Evidence is missing for any validation check.
- Real credentials, private keys, tfstate, kubeconfig content, account IDs, subscription IDs, tenant IDs, project IDs, or unsanitized environment details are captured.

## Evidence of Failure

Record the failed or blocked check in `validation.md` with the related check ID and sanitized details.

## Follow-Up Requirement

Create a follow-up task to install, repair, or document the missing tool before dependent scenarios proceed.
