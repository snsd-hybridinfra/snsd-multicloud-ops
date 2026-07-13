# Objective

## Objective Statement

Validate that MariaDB access-control definitions follow least privilege and keep application, replication, monitoring, administration, and root responsibilities separated.

## Success Measures

- Required policy, matrix, and non-production SQL example exist.
- Application grants contain only required DML on the application database placeholder.
- Replication and monitoring grants are narrowly scoped.
- Application and monitoring identities receive no dangerous privilege.
- Root application use, remote root login, wildcard hosts, and repository password storage are prohibited.
- No real credentials, connection strings, dumps, addresses, or account-specific content are present.
