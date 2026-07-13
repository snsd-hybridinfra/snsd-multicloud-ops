# Prometheus Target Down Command Reference

```text
curl http://<prometheus-server-placeholder>/api/v1/targets
curl "http://<prometheus-server-placeholder>/api/v1/query?query=up"
curl "http://<prometheus-server-placeholder>/api/v1/query?query=up{job='<scrape-job-name-placeholder>'}"
curl http://<prometheus-server-placeholder>/api/v1/rules
curl http://<prometheus-server-placeholder>/api/v1/alerts
```

## MANUAL FAULT INJECTION ONLY
`systemctl stop <exporter-service-placeholder>`

## MANUAL RECOVERY ACTION ONLY
`systemctl start <exporter-service-placeholder>`

The validator never executes curl or stop/start in Static mode and never performs service/rule/reload changes. Use disposable lab exporters only; production, credentials, cookies, authorization headers, webhooks, real URLs/domains/IPs/scrape targets, and TLS keys are excluded.
