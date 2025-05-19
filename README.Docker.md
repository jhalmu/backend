# Docker Setup for IBKR Portfolio

This document describes how to run the IBKR Portfolio application using Docker.

## Prerequisites

- Docker
- Docker Compose
- IBKR Account (for production use)

## Quick Start

1. Create `.env` file:
```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your settings
# Required variables:
# - IBKR_ACCOUNT_ID: Your IBKR account ID
# - ENVIRONMENT: development/production
# - DUCKDB_PATH: Path to DuckDB database file
# - DUCKDB_CACHE_SIZE: Cache size for DuckDB
```

2. Create data directory:
```bash
mkdir -p data
```

3. Start the application:
```bash
docker-compose up --build
```

## Accessing the Application

- Main application: http://localhost:5055
- API documentation: http://localhost:5055/docs

## Development Mode

The application runs in development mode by default with:
- Hot-reload for Python files
- DuckDB database with 1GB cache
- Mock API support

## Environment Variables

The application uses the following environment variables (configured in `.env`):

| Variable | Description | Default |
|----------|-------------|---------|
| IBKR_ACCOUNT_ID | Your IBKR account ID | - |
| ENVIRONMENT | development/production | development |
| DUCKDB_PATH | Path to DuckDB database | data/portfolio.duckdb |
| DUCKDB_CACHE_SIZE | DuckDB cache size | 1GB |

## Ports

- 5055: Main application
- 5056: IBKR Gateway (if available)

## Data Persistence

The application uses Docker volumes to persist data:
- `./data:/app/data`: Database and other persistent data

## Health Check

The application includes a health check endpoint at `/health` that monitors:
- Application status
- Database connection
- IBKR Gateway connection (if available)

## Troubleshooting

1. If the application fails to start:
   - Check Docker logs: `docker-compose logs`
   - Verify environment variables in `.env`
   - Ensure data directory exists and has correct permissions

2. If IBKR Gateway is not connecting:
   - Verify IBKR Gateway is running
   - Check IBKR Gateway logs
   - Verify account credentials in `.env`

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