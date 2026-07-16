# Commands

Scenario: S002-eve-ng-on-prem-routing-validation

Level: L1-foundation

Repository truth state: `VALIDATED`

Real lab output was collected for the EVE-NG host bridge and route bootstrap.
The raw terminal output is not committed; only the sanitized record is stored.

## Observed Read-Only Command Categories

```text
ip -br link
ip -br addr
ip route
brctl show
```

These commands inventory local EVE-NG interfaces, addresses, routes, and bridge
membership. They do not configure an interface or change a route.

## Evidence

- Sanitized output: `logs/20260715-S002-eve-uplink-bootstrap.sanitized.txt`
- Review summary: `configs/20260715-S002-eve-uplink-bootstrap-summary.md`

## Management Readiness Completion

HTTP execution status: `PASS`

Gateway/public connectivity, host-only ping, SSH/22, and HTTP/80 results are
represented. HTTPS/443 failed and is retained as an accurate negative result;
HTTP/80 is the validated management web path in this evidence set.

No router, ACL, firewall, zone-to-zone route, OpenStack path, or service VM
command was executed for this evidence package.

## Planned Recapture Reference

The following read-only command categories describe the evidence collection
surface used for S002. These are planned reference commands for any future
recapture, not unrecorded substitutes for the completed evidence. A recapture
must be executed by the operator and sanitized before commit.

```text
# EVE-NG host
ip -br link
ip -br addr
ip route
brctl show
<kvm-capability-read-only-command>

# Router
show version
show ip interface brief
show ip route
show interfaces trunk
show ip nat translations
show ip nat statistics
show access-lists
show running-config | include interface|encapsulation|ip address|ip nat|access-group
show startup-config | include config-register|interface|encapsulation|ip address

# Switch
show version
show vlan brief
show interfaces trunk
show interfaces status

# Sanitized connectivity tests
ping <zone-gateway-placeholder>
ping <vmware-nat-gateway-masked>
ping <public-connectivity-test-address>
ping <opposite-zone-endpoint-masked>
```

Do not commit raw console transcripts, device serial numbers, MAC addresses,
runtime WAN/management addresses, public test addresses, image filenames,
checksums, binaries, credentials, or proprietary image-acquisition details.

Current gap matrix:
`configs/20260716-S002-required-evidence-gap-matrix.md`.
