# Helm chart

## Overview

This Helm chart deploys the Python application into Kubernetes.
It provides a configurable Deployment and Service, optionally an Ingress, and exposes environment-specific settings through chart values.

## Installation

Install the chart locally:

```bash
helm install myapp ./helm \
  --set image.repository=myrepo/myapp \
  --set image.tag=v1 \
  --set environment=prod
```

Upgrade:

```bash
helm upgrade myapp ./helm
```

Uninstall:

```bash
helm uninstall myapp
```

## Values

The following values can be configured in values.yaml or via `--set`.

| Key                | Description                        | Default  |
| ------------------ | ---------------------------------- | -------- |
| `environment`      | Environment name passed to the app | "dev"    |
| `image.repository` | Container image repository         | "myapp"  |
| `image.tag`        | Image tag                          | "latest" |
| `service.port`     | Service port                       | 8000     |
| `replicaCount`     | Number of replicas                 | 1        |

