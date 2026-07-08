# S002-eve-ng-onprem-routing-validation

| Field | Value |
|---|---|
| Scenario ID | S002 |
| Scenario Name | EVE-NG On-Prem Routing Validation |
| Level | L1 Foundation Validation |
| Category | Foundation |
| Primary Domain | On-prem network routing readiness |
| Related Components | EVE-NG topology, routers, Management Zone, Bastion Zone, Transit Zone, Internal Server Zone, Monitoring Zone |
| Validation Type | Infrastructure Validation |
| Evidence Directory | evidence/L1-foundation/S002-eve-ng-onprem-routing-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate the baseline EVE-NG on-prem routing structure used by the SNSD Multi-Cloud Ops project.

## Scope Summary

This scenario validates planned routing evidence for the Management, Bastion, Transit, Internal Server, and Monitoring zones. It checks topology and routing readiness only.

## Related Components

- EVE-NG topology definition
- Router configuration snapshots
- Zone gateways
- Route tables
- Firewall boundaries as awareness points only

## Validation Summary

Validation confirms that topology files, router configuration snapshots, gateway reachability checks, inter-zone ping plans, route capture plans, and missing-route failure conditions are documented and mapped to evidence.

## Evidence Output Summary

Evidence must be recorded under `evidence/L1-foundation/S002-eve-ng-onprem-routing-validation/`, with command plans in `commands.md` and validation results in `validation.md`.
