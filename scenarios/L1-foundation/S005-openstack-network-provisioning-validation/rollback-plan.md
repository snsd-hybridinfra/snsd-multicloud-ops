# Rollback Plan

## Stop Condition

Stop immediately if validation activity attempts to create real OpenStack resources, writes tfstate, reads credentials, creates `openrc` or `clouds.yaml`, exposes project-specific data, or executes Terraform or OpenStack CLI against a real environment.

## Rollback Steps

1. Stop the activity.
2. Remove any unsafe output from evidence files.
3. Replace sensitive values with placeholders such as `<openstack-tenant-network-name>` or `<openstack-project-id-redacted>`.
4. Mark the affected validation item as `BLOCKED` or `FAIL` in `validation.md`.
5. Record the blocked condition in the implementation log if scenario progress is affected.

## Future Terraform Destroy or OpenStack CLI Cleanup Checklist

For a future approved lab execution, rollback must include:

1. Confirm the target workspace and OpenStack project are approved.
2. Capture planned tenant-owned resources for teardown.
3. Run `terraform destroy` or approved OpenStack CLI cleanup only after explicit approval.
4. Confirm Tenant Network, Tenant Subnet, Router, Router Interface, Security Group baseline, Floating IP allocation, and Keypair placeholder resources are removed or returned to baseline.
5. Do not remove provider networks unless they are explicitly owned by the approved lab scope.
6. Capture sanitized cleanup output and final OpenStack CLI listing evidence.

This checklist is documentation only and must not be executed during the S005 skeleton phase.
