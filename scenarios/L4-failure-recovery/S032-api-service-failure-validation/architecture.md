# Architecture

```text
healthy API Pod + endpoint + HTTP
  -> separately authorized manual disposable-lab fault
  -> Pod/endpoint/HTTP failure evidence
  -> manual recovery placeholder
  -> replacement Ready Pod + endpoint + HTTP 200 + rollout success
```

Static mode parses samples. LiveKubectl performs only get/status queries, and LiveHttp sends only an unauthenticated HEAD request. Raw live output and response bodies are not retained.
