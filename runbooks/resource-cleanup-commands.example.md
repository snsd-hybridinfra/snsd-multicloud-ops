# Resource Cleanup Commands — Examples Only

Run `powershell -ExecutionPolicy Bypass -File tools/validate-resource-cleanup.ps1`; local reviews use `git diff -- terraform/`, `git diff -- cost-governance/`, and `git diff -- policy/`.

Terraform plan/show are MANUAL LAB EVIDENCE CONVERSION ONLY. `aws ec2 describe-instances --filters <filter-placeholder>`, `az resource list --tag <tag-placeholder>`, `openstack server list --long`, and `kubectl get all -n <namespace-placeholder>` are MANUAL LAB INVENTORY EXAMPLES ONLY.

`terraform destroy -target=<resource-address-placeholder>`, `terraform apply`, `terraform state rm`, `aws ec2 terminate-instances --instance-ids <instance-id-placeholder>`, `az resource delete --ids <resource-id-placeholder>`, `openstack server delete <server-id-placeholder>`, and `kubectl delete <resource-kind-placeholder> <resource-name-placeholder> -n <namespace-placeholder>` are OUT OF SCOPE.

The validator does not run Terraform/cloud CLIs/kubectl or delete resources; no external cleanup tool is required. Production cleanup is OUT OF SCOPE.
