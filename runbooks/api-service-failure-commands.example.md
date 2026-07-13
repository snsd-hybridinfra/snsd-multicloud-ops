# API Service Failure Command Reference

All values are placeholders and all live work is restricted to a disposable non-production lab.

## Read-only collection

```text
kubectl get deployment <api-deployment-name> -n <namespace>
kubectl get pods -n <namespace> -l app=<api-app-label-placeholder>
kubectl get service <api-service-name> -n <namespace>
kubectl get endpoints <api-service-name> -n <namespace>
kubectl describe deployment <api-deployment-name> -n <namespace>
kubectl describe service <api-service-name> -n <namespace>
kubectl rollout status deployment/<api-deployment-name> -n <namespace>
curl -I http://<api-url-placeholder>/<api-health-endpoint-placeholder>
```

## MANUAL FAULT INJECTION ONLY

These commands are references for a separately approved disposable lab exercise. They are never executed by the validator and production execution is out of scope.

```text
kubectl delete pod <api-pod-name> -n <namespace>
kubectl scale deployment/<api-deployment-name> --replicas=0 -n <namespace>
```

Do not automate these destructive commands. Do not record kubeconfig paths, cluster endpoints, API URLs, tokens, certificates, authorization headers, cookies, or payloads.
