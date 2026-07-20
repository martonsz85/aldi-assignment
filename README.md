# DevOps Engineer Homework

## Overview

This repository contains a small, containerized Python REST-only application (i.e. no UI) that acts as a configuration manager. The application is designed to be deployed on a Kubernetes cluster using a Helm chart. When run by the accompanying CI/CD pipeline, the Helm chart deployment is orchestrated by Terraform.

## Changes

### Terraform

* Variables *were* defined, but were left unused in many cases
* Pinned provider versions at the current major version (could have been more granular)
* Updated resource definitions to reflect changed behavior introduced since v2.x (e.g. `set` blocks)
* Added support for Helm chart and container image to be stored in a repository (variables: `image_repo` and `chart_repo`)

### Helm

* Variables *were* defined, but were left unused in many cases (replica count and container port, hard-coded port numbers were sometimes incorrect)
* Added labels to resources, so that selectors would work
* Application version is taken from the build number (`APPVERSION` variable)
* Ingress is made optional

## Assumptions

* Container image and Helm chart will be stored in GitLab repo
* Vanilla Kubernetes will be used, if not, Terraform provider should be updated
* Terraform state file location will be fixed (haven't included it in .gitignore)
## Known Limitations

* The application's data store is ephemeral
* Current setup uses a single local state file, so it effectively supports only one environment
* Helm chart version and application version are kept in sync (both use `$CI_PIPELINE_ID`)

## Production Improvements

### Application and Containerization

* INFRA: Python package and base image versions could be frozen
* INFRA: If staying with Python, pip `requirements.txt` could be used
* SECURITY: Hardening the container image
	* Don't use Python, but rather a compiled code (e.g. Go, Java, .NET)
	* Run as a non-root user
* FEATURE: Use persistent store for configuration data
### Helm chart / Kubernetes manifest

* INFRA: Liveness / readiness check
* INFRA: Ingress needs to be enabled and configured once it is finalized
* INFRA: imagePullSecrets need to be set in the deployment template

### Terraform

* SECURITY: Store Terraform state in a central location (e.g. Azure Storage, S3 bucket, Kubernetes Secret)
* INFRA: Update main.tf to create a `regcred` imagePullSecret before helm_release (explicit dependency)

### GitLab CI

* FEATURE: Add unit tests, and have the pipeline break if the tests fail