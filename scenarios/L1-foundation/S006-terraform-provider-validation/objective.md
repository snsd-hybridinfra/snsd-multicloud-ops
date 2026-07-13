# Objective

Validate the static Terraform provider baseline for AWS, AzureRM, and OpenStack. Each provider must have an expected source, an explicit version constraint, and a non-authenticating provider block.

Success means the repository-side declarations pass all required safety checks without real provider credentials, account identifiers, backend configuration, initialization, provider download, state creation, or cloud interaction.

AWS, Azure, and OpenStack network definitions are handled in S003, S004, and S005. Terraform drift detection and remediation are handled in S041 and S042.
