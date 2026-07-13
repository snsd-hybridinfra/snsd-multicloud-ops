# Architecture

```text
healthy LB + two healthy backends
 -> manual disposable-lab LB stop
 -> LB/client failure while direct backends remain healthy
 -> manual LB start
 -> LB/client path restored
 -> bypass rollback documented
```

Static samples are authoritative; optional LiveHttp is status-only and read-only.
