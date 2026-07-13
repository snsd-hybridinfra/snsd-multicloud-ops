# Load Balancer Failure Command Reference

```text
curl -I http://<load-balancer-url-placeholder>
curl -I http://<backend-a-url-placeholder>
curl -I http://<backend-b-url-placeholder>
systemctl status <load-balancer-service-placeholder>
```

## MANUAL FAULT INJECTION ONLY
`systemctl stop <load-balancer-service-placeholder>`

## MANUAL RECOVERY ACTION ONLY
`systemctl start <load-balancer-service-placeholder>`

The validator never executes stop/start. Production, configuration changes, DNS/routing changes, credentials, cookies, authorization headers, API keys, payloads, response bodies, URLs, domains, IPs, and TLS material are out of scope.
