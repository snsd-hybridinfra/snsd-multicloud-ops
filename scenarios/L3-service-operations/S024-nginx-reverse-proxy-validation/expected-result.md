# Expected Result

S024 is validated when all required artifacts exist, the example contains the approved proxy and timeout directives, all four forwarding headers use approved variables, samples parse successfully, and safety scans find no concrete endpoint or sensitive content.

Static mode must finish without running Nginx, curl, or a network request. An explicitly requested LiveHttp run passes for 200, 204, 301, or 302; warns for 401 or 403; and fails for connection/timeout errors, 5xx, or another unaccepted status.

The generated log and summary record aggregate judgments only. They never contain the live target, response body, response headers, credentials, cookies, tokens, TLS material, domains, or numeric addresses.
