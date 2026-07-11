# S002-eve-ng-on-prem-routing-validation

| Field | Value |
|---|---|
| Scenario ID | S002 |
| Scenario Name | EVE-NG On-Prem Routing Validation |
| Level | L1 Foundation Validation |
| Category | Foundation |
| Primary Domain | Repository-side on-prem routing baseline |
| Related Components | EVE-NG topology documentation, four router example configs, five logical zones |
| Validation Type | Infrastructure Validation |
| Evidence Directory | evidence/L1-foundation/S002-eve-ng-on-prem-routing-validation/ |
| Status | VALIDATED |

## Objective Summary

Validate that the repository contains a complete, placeholder-only EVE-NG on-prem routing baseline without requiring a live lab or network credentials.

## Scope Summary

S002 checks one topology document and four non-production router examples. It does not authenticate to EVE-NG, connect to routers, validate live reachability, or test cloud connectivity.

## Related Components

- `eve-ng/topology/on-prem-routing-topology.md`
- `eve-ng/router-configs/*.example.cfg`
- `tools/validate-eve-ng-routing-baseline.ps1`

## Validation Summary

The script checks required files, zones, devices, CIDR placeholder tokens, example structure, secret-like assignments, and literal IPv4 addresses.

## Evidence Output Summary

- `logs/eve-ng-routing-baseline-validation.log`
- `configs/eve-ng-routing-baseline-summary.md`
- `commands.md`
- `validation.md`
