# Rollback Plan

## Stop Condition

Stop immediately if validation activity attempts to create real Azure resources, writes tfstate, reads credentials, exposes subscription or tenant data, or executes Terraform against a real Azure subscription.

## Rollback Steps

1. Stop the activity.
2. Remove any unsafe output from evidence files.
3. Replace sensitive values with placeholders such as `<azure-vnet-name>` or `<azure-subscription-id-redacted>`.
4. Mark the affected validation item as `BLOCKED` or `FAIL` in `validation.md`.
5. Record the blocked condition in the implementation log if scenario progress is affected.

## Future Terraform Destroy Checklist

For a future approved lab execution, rollback must include:

1. Confirm the target workspace and subscription are approved.
2. Capture planned resources for teardown.
3. Run `terraform destroy` only after explicit approval.
4. Confirm Resource Group, VNet, subnets, NSG, route table, public IP placeholder, and management entry point resources are removed or returned to baseline.
5. Capture sanitized destroy output and final Azure CLI listing evidence.

This checklist is documentation only and must not be executed during the S004 skeleton phase.
