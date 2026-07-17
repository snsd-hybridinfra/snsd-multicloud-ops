# Validation

- Scenario: S005-openstack-network-provisioning-validation
- Validation date: 2026-07-16
- Environment: non-production single-node OpenStack AIO lab
- Runtime authority: user-executed original validation plus Codex-executed restricted read-only corroboration
- Evidence treatment: supplied results normalized and sanitized; restricted validator output recorded separately
- Overall Validation Result Status: `PASS`
- Evidence Readiness Status: `READY`

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Kolla deployment workflow | Required stages complete | Operator reported bootstrap, prechecks, pull, deploy, and post-deploy completion | PASS | sanitized log |
| V002 | Keystone authentication | Token issuance succeeds | User-executed token issuance succeeded; value omitted | PASS | sanitized log |
| V003 | Core services and endpoints | Required services/endpoints registered | Identity, compute, placement, image, and network services/endpoints observed | PASS | sanitized log |
| V004 | Nova services | Scheduler, conductor, compute enabled/up | All three reported enabled/up | PASS | sanitized log |
| V005 | Hypervisor | Hypervisor up | `<OPENSTACK_AIO_HOST>` reported up with QEMU type | PASS | sanitized log |
| V006 | Neutron agents | OVS, L3, DHCP, metadata alive/up | All required agents reported alive/up | PASS | sanitized log |
| V007 | Provider network | ACTIVE flat `physnet1`, external=true | Required state and attributes observed | PASS | sanitized log |
| V008 | Tenant network and DHCP | ACTIVE; DHCP assignment present | Tenant network active and fixed address assigned | PASS | sanitized log |
| V009 | Router | ACTIVE with external port | Router active and provider-side port allocated | PASS | sanitized log |
| V010 | Image | Active | Image active | PASS | sanitized log |
| V011 | Instance | ACTIVE with fixed address | Instance active with masked fixed address | PASS | sanitized log |
| V012 | Floating IP | Associated and ACTIVE | Masked Floating IP active and associated | PASS | sanitized log |
| V013 | Neutron namespaces | Router and DHCP namespaces exist | Both namespace categories observed | PASS | sanitized log |
| V014 | OVS provider mapping | Bridges/patches/provider NIC valid | `br-tun`, `br-int`, `br-ex`, patch path, provider NIC mapping, link/admin state, and positive ofport observed | PASS | sanitized log |
| V015 | EVE external-router reachability | Probe succeeds after convergence | First probe lost during ARP learning; following four succeeded | PASS | sanitized log |
| V016 | EVE Floating IP reachability | Recorded probes succeed | Five of five probes succeeded | PASS | sanitized log |
| V017 | Instance gateway reachability | Tenant gateway reachable | Cloud-init probe succeeded | PASS | sanitized log |
| V018 | Instance Internet reachability | Public IPv4 reachable | Cloud-init public IPv4 probe succeeded | PASS | sanitized log |
| V019 | Cloud-init completion | Start/end/completion markers present | All markers observed | PASS | sanitized log |
| V020 | False-negative analysis | Functional path overrides isolated local-port indicator | `LOCAL(br-ex)` DOWN did not contradict link, mapping, router, Floating IP, or egress results | PASS | summary |
| V021 | Evidence sanitization | No prohibited runtime value retained | IDs, tokens, MACs, auth files, keys, management/dynamic addresses, and raw output omitted/masked | PASS | summary |

## Validation Authority

The original deployment workflow and EVE-NG data-plane probes remain
user-executed evidence. Codex normalized and sanitized those supplied results.
After a dedicated restricted endpoint was installed, Codex independently ran
only `validate-all` through its forced-command SSH alias. That live read-only
run produced 50 PASS, 0 FAIL, and exit status 0, corroborating the current
control-plane, resource, OVS, console-marker, instance-connectivity, and API
state. Codex was not granted a general shell, direct credentials, arbitrary
sudo, or mutation commands.

Security-boundary tests also confirmed that interactive access, a harmless
arbitrary command, and a direct credential-file read request were rejected.
The obsolete unrestricted bootstrap validation key was removed after success,
and the restricted endpoint still passed afterward.

## Codex-Executed Restricted Validation

| Item | Actual Result | Status | Evidence |
|---|---|---|---|
| Forced `validate-all` execution | 50 PASS, 0 FAIL, exit 0 | PASS | restricted live validation log |
| Interactive shell request | Rejected with non-zero exit | PASS | restricted endpoint security summary |
| Arbitrary command request | Rejected with non-zero exit | PASS | restricted endpoint security summary |
| Credential-file read request | Rejected with non-zero exit | PASS | restricted endpoint security summary |
| Direct bootstrap login with validator keys | Both dedicated and obsolete validator keys rejected | PASS | restricted endpoint security summary |
| Post-cleanup endpoint check | 50 PASS, 0 FAIL, exit 0 | PASS | restricted live validation log |

## Excluded Observations

- A mistyped address outside the validated provider range was excluded as operator input error.
- Raw output is not committed.
- Terraform, Security Group policy, HA, storage, backup, monitoring, hardening,
  AWS/Azure, and Kubernetes results are not inferred.
