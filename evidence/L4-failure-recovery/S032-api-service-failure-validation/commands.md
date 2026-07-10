# Commands

Scenario: S032-api-service-failure-validation
Level: L4-failure-recovery
Capability: Api Service Failure Validation

Record approved commands or manual actions used during validation. Do not include real command output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Command Records

| Check ID | Purpose | Planned Command Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Capture pre-failure API Deployment status | `kubectl get deployment <api-deployment> -n <namespace>` | `<api-deployment>` | TODO: `logs/api-service-failure-validation.log` |
| V002 | Capture pre-failure API Pod Ready status | `kubectl get pods -n <namespace> -l app=<api-deployment>` | `<api-pod>` | TODO: `screenshots/api-service-before-failure.png` |
| V003 | Capture pre-failure API Service endpoint status | `kubectl get endpoints <api-service> -n <namespace>` | `<api-service>` | TODO: `configs/api-service-failure-summary.md` |
| V004 | Inject API workload failure | `kubectl scale deployment <api-deployment> --replicas=0 -n <namespace>` or approved equivalent | `<api-deployment>` | TODO: `logs/api-service-failure-validation.log` |
| V005 | Validate API route failure response | `curl <ingress-host><api-path>` or approved equivalent | `<ingress-host><api-path>` | TODO: `screenshots/api-service-during-failure.png` |
| V006 | Validate API health endpoint failure | `curl <api-health-endpoint>` or approved equivalent | `<api-health-endpoint>` | TODO: `logs/api-service-failure-validation.log` |
| V007 | Reference Ingress API path failure | Manual review of S023-related API path behavior | `<api-path>` | TODO: `configs/api-service-failure-summary.md` |
| V008 | Reference Blackbox API probe failure | Manual review of S030-related API probe behavior | `<api-health-endpoint>` | TODO: `configs/api-service-failure-summary.md` |
| V009 | Restore API workload | `kubectl scale deployment <api-deployment> --replicas=<expected-api-replicas> -n <namespace>` or approved rollback equivalent | `<api-deployment>` | TODO: `logs/api-service-failure-validation.log` |
| V010 | Validate API health recovery | `curl <api-health-endpoint>` or approved equivalent | `<api-health-endpoint>` | TODO: `screenshots/api-service-after-recovery.png` |
| V011 | Measure detection and recovery time | Manual timestamp comparison between failure action, detected failure, and recovered healthy state | `<recovery-threshold-seconds>` | TODO: `configs/api-service-recovery-threshold.md` |

## Output Placeholder

```text
Execution timestamp: TODO
Operator: TODO
Namespace: <namespace>
Target API Deployment: <api-deployment>
Target API Pod: <api-pod>
API path: <api-path>
Command or manual review: TODO
Expected purpose: TODO
Sanitized output summary: TODO
```
