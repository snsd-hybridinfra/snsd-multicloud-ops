# Failure Condition

## Failure Conditions

- A required module or environment file is missing.
- A required AWS network resource type is absent.
- A real tfvars, tfstate, or backend block exists.
- Credential, private-key, account-ID, or unexpected CIDR content is detected.
- Execution attempts Terraform initialization, validation requiring providers, planning, apply, destroy, AWS authentication, or a cloud API call.

Terraform CLI absence or a formatting difference is a warning, not a required-definition failure.

## Evidence of Failure

The generated log and summary identify the failed local check without exposing sensitive content.

## Follow-Up Requirement

Correct the repository definition or remove the unsafe file, then rerun S003. Do not authenticate to AWS as remediation.
