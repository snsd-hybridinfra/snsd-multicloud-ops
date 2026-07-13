# Service Health After Recovery Command Reference

Read-only documentation placeholders:

```text
curl -I http://<web-service-url-placeholder>/health
curl -I http://<api-health-url-placeholder>/health
curl -I http://<load-balancer-url-placeholder>/health
kubectl get deployment -n <namespace-placeholder>
kubectl get pods -n <namespace-placeholder>
kubectl get service -n <namespace-placeholder>
kubectl get endpoints -n <namespace-placeholder>
kubectl rollout status deployment/<deployment-name-placeholder> -n <namespace-placeholder>
curl http://<prometheus-server-placeholder>/api/v1/query?query=up
curl http://<prometheus-server-placeholder>/api/v1/query?query=probe_success
curl http://<prometheus-server-placeholder>/api/v1/targets
curl http://<prometheus-server-placeholder>/api/v1/alerts
```

Recovery, backup, restore, SQL, service/configuration change, kubectl apply/delete/patch/edit/scale/restart/cordon/drain/taint, and infrastructure mutation are **OUT OF SCOPE**. Credentials, cookies, authorization headers, API keys, response bodies, raw Prometheus responses, kubeconfig details, and database output are never stored.
