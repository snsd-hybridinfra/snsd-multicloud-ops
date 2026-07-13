# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-nginx-reverse-proxy.ps1`.
2. Confirm the baseline, config, matrix, command reference, and three samples exist.
3. Validate proxy routing, forwarded headers, timeouts, and rule-matrix coverage.
4. Parse the marked config-test, HTTP-response, and access-log samples.
5. Reject numeric addresses, real domains, non-placeholder URLs, TLS material, credentials, tokens, cookies, authorization values, and unsafe proxying.
6. Confirm Static mode invoked neither Nginx, curl, nor the network.
7. Review the generated aggregate log and summary.
8. Run optional LiveHttp only through `-LiveHttp -TargetUrl "http://<reverse-proxy-host-placeholder>/"` after explicit approval.

## Execution Boundaries

LiveHttp sends one cookie-free HEAD request and retains only its sanitized status and timestamp. It does not send credentials, save response content, run curl, or start/reload/modify Nginx. The optional live check remains `NOT_RUN` in this static validation record.
