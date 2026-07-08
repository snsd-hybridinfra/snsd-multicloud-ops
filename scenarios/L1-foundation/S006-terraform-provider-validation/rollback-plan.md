# Rollback Plan

## Stop Condition

Stop immediately if validation activity creates tfstate, downloads providers into a committed path, exposes credentials, writes backend configuration, or adds account-specific provider data.

## Rollback Steps

1. Stop the validation activity.
2. Remove unsafe evidence content.
3. Replace sensitive values with placeholders such as `<aws-region>`, `<azure-subscription-id-redacted>`, or `<openstack-cloud-name>`.
4. Confirm no tfstate, `.terraform/`, credential, backend, private key, or account-specific file is staged or committed.
5. Mark the affected validation item as `BLOCKED` or `FAIL` in `validation.md`.
6. Record the blocked condition in the implementation log if scenario progress is affected.

## Recovery Validation

Confirm S006 remains documentation and evidence planning only, with provider roles separated and no real credentials, tfstate, private keys, or account-specific values added.
