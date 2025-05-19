# IBKR Portfolio

Web-sovellus Interactive Brokers (IBKR) portfolion hallintaan ja analysointiin.

## Features

- Portfolio overview and analysis
- Stock details and historical data
- Dividend tracking
- Real-time market data (when connected to IBKR)
- Mock data support for development

## Development Setup

### Prerequisites

- Docker and Docker Compose
- Python 3.11+
- IBKR Account (for production use)

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ibkr-portfolio-backend.git
cd ibkr-portfolio-backend
```

2. Create `.env` file:
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

3. Start the development environment:
```bash
docker-compose up --build
```

4. Access the application:
- Main application: http://localhost:5055
- API documentation: http://localhost:5055/docs

### Environment Variables

The application uses the following environment variables (configured in `.env`):

| Variable | Description | Default |
|----------|-------------|---------|
| IBKR_ACCOUNT_ID | Your IBKR account ID | - |
| ENVIRONMENT | development/production | development |
| DUCKDB_PATH | Path to DuckDB database | data/portfolio.duckdb |
| DUCKDB_CACHE_SIZE | DuckDB cache size | 1GB |

## Project Structure

```
.
├── app.py              # Main application
├── mock_api.py         # Mock data for development
├── db_config.py        # Database configuration
├── conf.yaml           # IBKR Gateway configuration
├── docker-compose.yml  # Docker Compose configuration
├── Dockerfile         # Docker configuration
├── requirements.txt    # Python dependencies
├── static/            # Static files
└── templates/         # HTML templates
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 