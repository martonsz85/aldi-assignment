# Terraform

## Overview

This directory contains the Terraform configuration used to deploy the application into Kubernetes.

Terraform manages:
* Namespace creation
* Helm deployment
* Environment-specific configuration
* Image and chart version injection

## Requirements

* Kubernetes cluster
* `kubectl` configured
* Terraform >= 1.5

## Variables


| Variable      | Description                            | Example                                   |
| ------------- | -------------------------------------- | ----------------------------------------- |
| namespace     | Kubernetes namespace to deploy into    | production                                |
| environment   | Logical environment passed to the app  | prod                                      |
| chart_repo    | OCI registry containing the Helm chart | `oci://registry.gitlab.com/group/project` |
| chart_version | Helm chart version (from CI)           | 1.0.0                                     |
| image_repo    | Docker image repository                | `registry.gitlab.com/group/project/myapp` |
| image_tag     | Docker image tag                       | 1.0.0                                     |

These variables are passed by the CI/CD pipeline.

## Multi-Environment Usage

Terraform should be run with separate state files per environment.
Recommended structure:

```bash
terraform/
  envs/
    production/
    test/
    dev/
```

Note: Changing namespace inside a single state will cause Terraform to destroy the old namespace and deployment. This behavior is expected.

## Running Terraform Manually

### Initialize

```bash
terraform init
```

### Apply

```bash
terraform apply \
  -var="namespace=production" \
  -var="environment=prod" \
  -var="chart_repo=oci://registry.gitlab.com/group/project" \
  -var="chart_version=1.0.0" \
  -var="image_repo=registry.gitlab.com/group/project/myapp" \
  -var="image_tag=1.0.0"
```

## Known Limitations

* No remote backend (local state only) - *must be fixed before going live*
* No secret creation (registry credentials must exist beforehand)
