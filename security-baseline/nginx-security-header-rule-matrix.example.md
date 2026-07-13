# Nginx Security Header Rule Matrix Example

NON-PRODUCTION EXAMPLE: this matrix documents a static validation baseline and does not configure a server.

| Header / Directive | Required Value Placeholder | Purpose | Required Scope | Validation Method | Risk if Missing | Evidence Reference |
|---|---|---|---|---|---|---|
| server_tokens | off | Reduce version disclosure | reverse proxy baseline | Static directive check | Version information exposure | S019-V004 |
| X-Frame-Options | SAMEORIGIN | Reduce clickjacking risk | all applicable responses | Static header and always check | UI framing attacks | S019-V005 |
| X-Content-Type-Options | nosniff | Disable MIME sniffing | all applicable responses | Static header and always check | Content-type confusion | S019-V005 |
| Referrer-Policy | strict-origin-when-cross-origin | Limit referrer disclosure | all applicable responses | Static header and always check | Information leakage | S019-V005 |
| Content-Security-Policy | `<content-security-policy-placeholder>` | Constrain content sources | service-specific reviewed policy | Static placeholder and always check | Script/content injection impact | S019-V006 |
| Strict-Transport-Security | max-age=31536000; includeSubDomains | Require reviewed HTTPS use | `<tls-termination-point>` only | Static value and always check | HTTPS downgrade risk | S019-V006 |
| Permissions-Policy | `<permissions-policy-placeholder>` | Restrict browser features | service-specific reviewed policy | Static placeholder and always check | Excess browser capability | S019-V006 |

