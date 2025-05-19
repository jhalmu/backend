# Docker Development Environment

This document describes how to run the application using Docker in development mode.

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Build and start the containers:
```bash
docker-compose up --build
```

2. Access the application:
- FastAPI application: http://localhost:5055
- IBKR Gateway: http://localhost:5056

## Development Mode

The application runs in development mode by default with the following features:
- Hot-reload enabled for Python files
- DuckDB database with 1GB cache
- Mock API mode if IBKR Gateway is not available

## Environment Variables

- `ENVIRONMENT`: Set to "development" for hot-reload and debug features
- `DUCKDB_PATH`: Path to DuckDB database file (default: /app/data/portfolio.db)
- `DUCKDB_CACHE_SIZE`: Cache size for DuckDB (default: 1GB)

## Ports

- 5055: FastAPI application
- 5056: IBKR Gateway (if available)

## Data Persistence

The application data is stored in the `data` directory, which is mounted as a volume in the container.

### Building and running your application

When you're ready, start your application by running:
`docker compose up --build`.

Your application will be available at http://localhost:8000.

### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References
* [Docker's Python guide](https://docs.docker.com/language/python/)