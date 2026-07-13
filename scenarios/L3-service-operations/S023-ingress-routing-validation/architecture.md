# Architecture

## Routing Flow

```text
Client
  -> Ingress Controller
  -> host app.example.internal + path /
  -> sample-service-placeholder:80
  -> placeholder endpoint / Pod
```

## Validation Flow

Static mode parses the manifest and three samples. Explicit LiveKubectl mode runs read-only get/describe/get/get queries and stores only routing judgments.

## Trust Boundary

No kubeconfig, token, certificate, TLS key, DNS record, endpoint, numeric address, or raw live resource output is stored. Curl is documentation-only.
