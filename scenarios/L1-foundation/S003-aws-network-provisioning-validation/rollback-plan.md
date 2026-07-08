# Rollback Plan

## Stop Condition

Stop immediately if validation activity attempts to create real AWS resources, writes tfstate, reads credentials, exposes account-specific data, or executes Terraform against a real AWS account.

## Rollback Steps

1. Stop the activity.
2. Remove any unsafe output from evidence files.
3. Replace sensitive values with placeholders such as `<aws-vpc-id>` or `<aws-account-id-redacted>`.
4. Mark the affected validation item as `BLOCKED` or `FAIL` in `validation.md`.
5. Record the blocked condition in the implementation log if scenario progress is affected.

## Future Terraform Destroy Checklist

For a future approved lab execution, rollback must include:

1. Confirm the target workspace and account are approved.
2. Capture planned resources for teardown.
3. Run `terraform destroy` only after explicit approval.
4. Confirm VPC, subnets, route tables, internet gateway, and security groups are removed.
5. Capture sanitized destroy output and final AWS CLI listing evidence.

This checklist is documentation only and must not be executed during the S003 skeleton phase.
