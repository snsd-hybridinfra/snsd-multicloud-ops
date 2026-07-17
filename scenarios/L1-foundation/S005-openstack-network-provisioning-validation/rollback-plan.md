# Rollback Plan

## Stop Condition

Stop validation if credentials or raw authentication material could be captured,
if provider routing affects an unintended network, or if host-capacity limits
are exceeded.

## Rollback Steps

1. Stop further lab mutations and preserve only sanitized diagnostic notes.
2. Use the operator-approved Kolla/OpenStack cleanup procedure outside the repository.
3. Remove temporary instance, Floating IP, router, and network resources in dependency order when teardown is authorized.
4. Confirm the provider VLAN and EVE-NG routing baseline remain intact.
5. Record cleanup under its owning validation scenario; do not infer success from this plan.

## Recovery Validation

S005 recovery requires a fresh pass of V001-V021. Automated teardown,
destroy/recreate, backup, and disaster recovery are not validated here.
