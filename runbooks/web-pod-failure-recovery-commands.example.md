# Web Pod Failure Recovery Command Examples

NON-PRODUCTION EXAMPLES.

```text
kubectl get deployment <deployment-name> -n <namespace>
kubectl get pods -n <namespace> -l app=<app-label-placeholder>
kubectl describe pod <pod-name> -n <namespace>
kubectl rollout status deployment/<deployment-name> -n <namespace>
kubectl get endpoints <service-name> -n <namespace>
```

## MANUAL FAULT INJECTION ONLY

```text
kubectl delete pod <pod-name> -n <namespace>
```

The delete command is never executed by the validator. Destructive testing requires separate approval and a disposable lab namespace. Production execution is out of scope. Do not add kubeconfig paths, cluster endpoints, tokens, certificates, or real namespace values.
