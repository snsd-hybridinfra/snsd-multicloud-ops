# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| MariaDB bind-address validation plan | `commands.md`; `configs/mariadb-access-control-summary.md`; `validation.md` | command plan, access summary, validation record | yes |
| MariaDB user and host mapping validation plan | `commands.md`; `configs/mariadb-access-control-summary.md`; `validation.md` | command plan, access summary, validation record | yes |
| Application DB user least privilege validation plan | `commands.md`; `configs/mariadb-grant-policy.md`; `validation.md` | command plan, grant policy, validation record | yes |
| Replication DB user separation validation plan | `commands.md`; `configs/mariadb-grant-policy.md`; `validation.md` | command plan, grant policy, validation record | yes |
| Backup DB user separation validation plan | `commands.md`; `configs/mariadb-grant-policy.md`; `validation.md` | command plan, grant policy, validation record | yes |
| Root remote access denial validation plan | `commands.md`; `logs/mariadb-access-control-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| DB port 3306 public exposure denial validation plan | `commands.md`; `logs/mariadb-access-control-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Cloud App/API node to DB access rule validation plan | `commands.md`; `configs/mariadb-access-control-summary.md`; `validation.md` | command plan, access summary, validation record | yes |
| Web node direct DB access denial validation plan | `commands.md`; `logs/mariadb-access-control-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Bastion or management admin access validation plan | `commands.md`; `configs/mariadb-access-control-summary.md`; `screenshots/mariadb-access-control-test.png`; `validation.md` | command plan, access summary, screenshot reference, validation record | yes |
| Failure condition for public DB exposure, root remote access, overly broad grants, missing app user, missing replication user, or direct unauthorized DB access | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real MariaDB access control output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
