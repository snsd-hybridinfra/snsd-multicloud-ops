# Security Rule Misconfiguration Command Reference

The following are read-only documentation examples with placeholders:

```text
aws ec2 describe-security-groups --group-ids <security-group-id-placeholder>
az network nsg rule list --nsg-name <nsg-placeholder> --resource-group <resource-group-placeholder>
openstack security group rule list <openstack-security-group-placeholder>
kubectl get networkpolicy -n <namespace-placeholder>
kubectl describe networkpolicy <network-policy-placeholder> -n <namespace-placeholder>
git diff -- <security-rule-file-placeholder>
git checkout -- <security-rule-file-placeholder>
```

Cloud modification commands are **OUT OF SCOPE**. Firewall modification commands are **OUT OF SCOPE**. `kubectl apply`, `kubectl delete`, and `kubectl patch` are **OUT OF SCOPE**. Rollback is represented by sanitized evidence and a manual runbook only.

Do not use real account/project/resource identifiers, CLI profiles, resource groups, security-group IDs, NSG names, IPs, CIDRs, credentials, or secrets.
