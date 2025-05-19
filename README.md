# IBKR Portfolio

A web application for managing and analyzing Interactive Brokers portfolios.

## Features

- Portfolio overview and analysis
- Stock details and historical data
- Dividend tracking and analysis
- Real-time market data (when connected to IBKR)
- Mock data support for development

## Development Setup

### Prerequisites

- Docker
- Docker Compose
- Python 3.11+

### Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd backend
```

2. Start the development environment:
```bash
docker-compose up --build
```

3. Access the application:
- Web interface: http://localhost:5055
- API documentation: http://localhost:5055/docs

### Development Mode

The application runs in development mode by default with:
- Hot-reload for Python files
- DuckDB database with 1GB cache
- Mock API support

### Environment Variables

- `ENVIRONMENT`: Set to "development" for hot-reload
- `DUCKDB_PATH`: Path to DuckDB database
- `DUCKDB_CACHE_SIZE`: Cache size for DuckDB

## Project Structure

```
backend/
├── app.py              # Main FastAPI application
├── mock_api.py         # Mock API implementation
├── db_config.py        # Database configuration
├── start.sh           # Startup script
├── conf.yaml          # IBKR Gateway configuration
├── data/              # Data directory
├── static/            # Static files
└── templates/         # HTML templates
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 