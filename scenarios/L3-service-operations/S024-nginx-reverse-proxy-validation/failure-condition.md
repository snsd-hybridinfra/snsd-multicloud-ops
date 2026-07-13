# Failure Condition

S024 fails when any of these conditions occurs:

- A required baseline or sample file is missing.
- Upstream, server, listener, symbolic server name, location, or `proxy_pass` is missing.
- A required forwarded header or timeout is absent or incorrect.
- The config-test sample lacks either success indicator or the HTTP sample lacks 200 OK.
- A sample is not marked and sanitized as non-production.
- A real domain, numeric address, concrete URL, key/certificate path or material, credential, token, cookie, authorization value, or secret-like assignment is detected.
- Broad dynamic proxying, a resolver, or an out-of-scope TLS listener appears in the example.
- LiveHttp is requested without a valid TargetUrl, cannot connect, times out, returns 5xx, or returns another unaccepted status.
- The validator runs Nginx/curl, modifies Nginx, or persists a live target or response content.

HTTP 401 or 403 in LiveHttp is a warning because authentication may be expected; it does not prove routing failure.
