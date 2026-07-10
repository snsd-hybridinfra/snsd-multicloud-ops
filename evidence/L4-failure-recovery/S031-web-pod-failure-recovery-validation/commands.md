# Commands

Scenario: S031-web-pod-failure-recovery-validation
Level: L4-failure-recovery
Capability: Web Pod Failure Recovery Validation

Record approved commands or manual actions used during validation. Do not include real command output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Command Records

| Check ID | Purpose | Planned Command Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Capture pre-failure Web Deployment status | `kubectl get deployment <web-deployment> -n <namespace>` | `<web-deployment>` | TODO: `logs/web-pod-failure-recovery-validation.log` |
| V002 | Capture pre-failure Web Pod Ready status | `kubectl get pods -n <namespace> -l app=<web-deployment>` | `<web-pod>` | TODO: `screenshots/web-pod-before-failure.png` |
| V003 | Capture pre-failure Web Service endpoint status | `kubectl get endpoints <web-service> -n <namespace>` | `<web-service>` | TODO: `configs/web-pod-failure-recovery-summary.md` |
| V004 | Inject controlled Web Pod failure | `kubectl delete pod <web-pod> -n <namespace>` | `<web-pod>` | TODO: `logs/web-pod-failure-recovery-validation.log` |
| V005 | Observe replacement Pod creation | `kubectl get pods -n <namespace> -w` or approved equivalent | `<web-deployment>` | TODO: `logs/web-pod-failure-recovery-validation.log` |
| V006 | Confirm replacement Pod Ready state | `kubectl wait --for=condition=Ready pod/<replacement-web-pod> -n <namespace> --timeout=<recovery-threshold-seconds>s` | `<replacement-web-pod>` | TODO: `screenshots/web-pod-after-recovery.png` |
| V007 | Confirm Web Service endpoint recovery | `kubectl get endpoints <web-service> -n <namespace>` | `<web-service>` | TODO: `configs/web-pod-failure-recovery-summary.md` |
| V008 | Confirm HTTP health endpoint recovery | `curl <health-endpoint>` or approved equivalent | `<health-endpoint>` | TODO: `logs/web-pod-failure-recovery-validation.log` |
| V009 | Measure recovery time | Manual timestamp comparison between delete action and Ready/healthy state | `<recovery-threshold-seconds>` | TODO: `configs/web-pod-recovery-threshold.md` |
| V010 | Capture post-recovery workload status | `kubectl get deployment,pods,endpoints -n <namespace>` | `<namespace>` | TODO: `logs/web-pod-failure-recovery-validation.log` |

## Output Placeholder

```text
Execution timestamp: TODO
Operator: TODO
Namespace: <namespace>
Target Web Deployment: <web-deployment>
Target Web Pod: <web-pod>
Command or manual review: TODO
Expected purpose: TODO
Sanitized output summary: TODO
```
