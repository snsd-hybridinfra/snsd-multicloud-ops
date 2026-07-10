# Commands

Scenario: S037-security-rule-misconfiguration-validation
Level: L4-failure-recovery
Capability: Security Rule Misconfiguration Validation

Record approved commands or manual actions used during validation. Do not include real command output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Command Records

| Check ID | Purpose | Planned Command Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Capture pre-change security rule baseline | `<approved-rule-read-command-placeholder>` | `<security-group-id>` / `<nsg-name>` / `<openstack-security-group>` / `<firewall-rule>` | TODO: `screenshots/security-rule-before-change.png` |
| V002 | Inject controlled misconfiguration | `<approved-rule-change-placeholder>` | `<firewall-rule>` | TODO: `logs/security-rule-misconfiguration-validation.log` |
| V003 | Detect public SSH exposure | Manual rule review for `<service-port>` and `<unauthorized-cidr>` | SSH rule placeholder | TODO: `configs/security-rule-misconfiguration-summary.md` |
| V004 | Detect public DB exposure | Manual rule review for `<service-port>` and `<unauthorized-cidr>` | DB rule placeholder | TODO: `configs/security-rule-misconfiguration-summary.md` |
| V005 | Detect overly broad inbound CIDR | Manual rule review for `<unauthorized-cidr>` | inbound rule placeholder | TODO: `screenshots/security-rule-during-misconfiguration.png` |
| V006 | Detect required service access breakage | `<approved-service-reachability-check-placeholder>` | required service rule placeholder | TODO: `logs/security-rule-misconfiguration-validation.log` |
| V007 | Test unauthorized source access | `<approved-access-test-placeholder>` from `<unauthorized-cidr>` | `<service-port>` | TODO: `configs/security-rule-misconfiguration-summary.md` |
| V008 | Test authorized source access | `<approved-access-test-placeholder>` from `<allowed-cidr>` | `<service-port>` | TODO: `configs/security-rule-misconfiguration-summary.md` |
| V009 | Record manual rollback decision points | Manual review of rollback decision checklist | manual rollback | TODO: `configs/security-rule-rollback-decision-points.md` |
| V010 | Validate post-rollback security rule | `<approved-rule-read-command-placeholder>` | selected rule placeholder | TODO: `screenshots/security-rule-after-rollback.png` |
| V011 | Validate post-rollback service reachability | `<approved-service-reachability-check-placeholder>` | required service rule placeholder | TODO: `logs/security-rule-misconfiguration-validation.log` |
| V012 | Measure detection and rollback time | Manual timestamp comparison between misconfiguration, detection, rollback, and restored state | `<recovery-threshold-seconds>` | TODO: `configs/security-rule-recovery-threshold.md` |

## Manual Rollback Decision Point Placeholder

```text
Confirm selected security control area: TODO
Confirm misconfiguration type: TODO
Confirm unauthorized exposure or required access impact: TODO
Choose rollback to approved baseline: TODO
Validate post-rollback rule state: TODO
Validate post-rollback service reachability: TODO
Record evidence and incident notes: TODO
```

## Output Placeholder

```text
Execution timestamp: TODO
Operator: TODO
Security control area: TODO
Rule placeholder: <firewall-rule>
Allowed CIDR: <allowed-cidr>
Unauthorized CIDR: <unauthorized-cidr>
Service port: <service-port>
Command or manual review: TODO
Expected purpose: TODO
Sanitized output summary: TODO
```
