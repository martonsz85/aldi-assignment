# Application

## Overview

This directory contains a minimal Python web application used for the DevOps homework assignment.
The application exposes several endpoints that return health information, version metadata, environment configuration, and simple key/value storage.

The app is intentionally lightweight to keep the focus on containerization, Kubernetes deployment, Helm templating, Terraform provisioning, and CI/CD automation.

## Endpoints

### `GET /health`

Returns a static health status.
Useful for readiness/liveness probes.

**Response:**

```json
{
    "status": "ok"
}
```

### `GET /version`

Returns the application version.
The version is injected via the APPVERSION environment variable, which is set by the Helm chart using .Chart.AppVersion.

**Sample response:**

```json
{
    "version": "1.0.0"
}
```

### `GET /env`

Returns the current environment (e.g., dev, test, prod).
The value comes from the ENVIRONMENT environment variable, configured through Helm values.

**Sample response:**

```json
{
    "environment": "production"
}
```

### `POST /config`

Stores a key/value pair in memory.

**Sample request:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

**Sample response:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

### `GET /config/{name}`

Retrieves a previously stored configuration value.

**Sample request:**

```bash
GET /config/database_url
```

**Sample response:**

```json
{
    "name": "database_url",
    "value": "postgres://example"
}
```

### `DELETE /config/{name}`

Deletes a configuration entry.

**Response:**

```json
{
    "deleted": true
}
```

## Running Locally

Install the prerequisites and run using uvicorn:

```bash
RUN pip install fastapi uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
```

Test endpoints:

```bash
curl localhost:8000/health
curl localhost:8000/version
curl localhost:8000/env
```

## Implementation Notes

The application has been implemented using FastAPI in order to keep development effort low.

## Known Limitations

* In-memory config store (not persistent)
* No authentication
* Not production-grade -- intentionally simple for the assignment

## Future Improvements

* Add persistent storage
* Add unit tests
