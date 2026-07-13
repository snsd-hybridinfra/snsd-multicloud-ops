# Architecture

```text
Prometheus scrape placeholder
  -> <blackbox-exporter>
  -> HTTP/TCP module
  -> <endpoint-url-placeholder>
  -> probe_success/status/duration
  -> sanitized judgment
```

Static validation parses artifacts and fixtures. LiveBlackbox validates two explicit HTTP(S) URLs, URL-encodes the target in memory, sends no credentials/cookies/authorization, and retains only probe metrics and timestamp.

Warning and failure files are classification fixtures, not live service claims.
