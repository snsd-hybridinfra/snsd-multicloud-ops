# S005 OpenStack AIO Validation Summary

## Provenance

- Validation date: 2026-07-16
- Environment: non-production single-node AIO lab
- Evidence source: user-executed OpenStack AIO and EVE-NG runtime results
- Initial Codex action: local normalization, sanitization, cross-checking, and repository updates
- Later corroboration: forced-command read-only `validate-all` executed by Codex
- Raw runtime output: not committed

## Result Summary

| Area | Result | Basis |
|---|---|---|
| Kolla deployment | PASS | Required deployment stages reported complete |
| Authentication/control plane | PASS | Token issuance, services, endpoints, Nova, hypervisor, and Neutron agent results agree |
| Provider network | PASS | ACTIVE flat external network on `physnet1` |
| Tenant network | PASS | ACTIVE tenant subnet, DHCP, namespaces, and router |
| Instance/Floating IP | PASS | Active resources with association and data-plane probes |
| Open vSwitch mapping | PASS | Required bridges, patch ports, provider NIC state, and positive ofport |
| EVE-NG integration | PASS | External-router reachability after ARP convergence and five successful Floating IP probes |
| Instance egress | PASS | Tenant gateway and public IPv4 probes succeeded |
| Cloud-init | PASS | Start, end, and completion markers present |
| Sensitive-data review | PASS | Prohibited values omitted or represented by placeholders |

## False-Negative Analysis

`LOCAL(br-ex)` reported `PORT_DOWN` and `LINK_DOWN`. This isolated control-plane
indicator is not treated as a forwarding failure because the provider NIC was
link-up/admin-up, mapped to `br-ex` with a positive OpenFlow port, the patch
path existed, the Neutron router and Floating IP were reachable, and the tenant
instance reached the public IPv4 network. No manual bridge link-state change is
recommended.

## Troubleshooting Record

| Issue | Cause | Corrective Action | Verification | Operational Lesson |
|---|---|---|---|---|
| Non-interactive sudo failure | Required privilege escalation was unavailable | Configure lab-only passwordless sudo for the Kolla execution account | Bootstrap rerun completed | Validate become behavior before bootstrap |
| Docker SDK import failure | SDK absent from the Kolla virtual environment | Install and import-test it in `/opt/kolla-venv` | Precheck passed | Install dependencies in the interpreter Kolla actually uses |
| dbus import failure | Module absent from the Kolla virtual environment | Install required build dependencies and module in `/opt/kolla-venv` | Precheck passed | Host Python packages do not satisfy a separate venv |
| Test-image guard | Lab image namespace required explicit acknowledgement | Apply the supported precheck acknowledgement only where valid | Precheck/pull/deploy completed | Check action-specific CLI help before reusing options |
| Unsupported image option | Option was not accepted by pull/deploy actions | Remove the unsupported option from those actions | Pull/deploy completed | Kolla options are action-specific |
| Post-deploy inventory mismatch | Default inventory path differed from actual path | Supply `<AIO_INVENTORY>` explicitly | Client configuration generated | Treat inventory path as an explicit input |
| Cloud profile name mismatch | Generated profiles differed from assumption | Select `<ADMIN_CLOUD_PROFILE>` from generated profiles | Authentication succeeded | Inspect generated profile names; do not assume one |
| CLI field-name false failure | Incorrect field names were queried | Use actual colon-delimited provider fields | Attributes returned correctly | Validate field names against real CLI output |
| OVS lookup in wrong container | Agent container did not own the queried OVS DB context | Query `<OVS_DB_CONTAINER>` / `<OVS_VSWITCHD_CONTAINER>` | Bridge and port mapping returned | Inspect OVS in its owning container context |
| `LOCAL(br-ex)` false negative | Local port state did not represent the functional physical path | Correlate physical, OVS, router, Floating IP, and guest results | End-to-end path passed | Never judge the data plane from one interface flag |
| Initial probe loss | ARP convergence | Repeat bounded probe after neighbor learning | Following probes succeeded | Preserve convergence context without hiding it |
| Mistyped external address | Operator input did not target the validated range | Exclude the result and rerun against the correct placeholder target | Correct-target probes passed | Separate test-input error from platform failure |

## Validation Authority

The deployment workflow and original data-plane evidence were executed by the
operator. Codex initially verified repository consistency and sanitized the
supplied evidence locally. Codex later connected only through a forced-command
endpoint and executed the fixed read-only `validate-all` operation. That run
returned 50 PASS, 0 FAIL, and exit status 0. It did not grant direct shell,
credential, arbitrary sudo, or mutation access.

## Final Judgment

- OpenStack AIO deployment: `VALIDATED FROM USER-EXECUTED RESULT`
- Core control plane: `VALIDATED FROM USER-EXECUTED RESULT`
- Provider/tenant/Floating-IP path: `VALIDATED FROM USER-EXECUTED RESULT`
- Evidence readiness: `READY`
- Restricted current-state corroboration: `PASS (50/50, exit 0)`
- Production readiness: not claimed
