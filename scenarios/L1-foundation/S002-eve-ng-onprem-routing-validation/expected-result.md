# Expected Result

## Success Conditions

- The EVE-NG topology evidence path is defined.
- The router configuration snapshot evidence path is defined.
- Gateway reachability checks are planned for Management, Bastion, Internal Server, and Monitoring zones.
- Transit Zone route existence and default route checks are planned where applicable.
- Inter-zone routing checks are defined for approved paths.
- Missing route or unreachable gateway failure conditions are explicit.
- Firewall rule implementation remains excluded.

## Required Evidence

- `commands.md`
- `validation.md`
- `configs/router-config-snapshot.md`
- `configs/topology-summary.md`
- `logs/routing-validation.log`
- `screenshots/eve-ng-topology.png`

## Completion Criteria

The scenario can move from `PLANNED` to `VALIDATED` only after sanitized routing evidence is collected and all validation checks have final statuses.
