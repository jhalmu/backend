# IBKR Portfolio

Web-sovellus Interactive Brokers (IBKR) portfolion hallintaan ja analysointiin.

## Features

- Portfolio overview and analysis
- Stock details and historical data
- Dividend tracking
- Real-time market data (when connected to IBKR)
- Mock data support for development

## Security & Environment

- Älä koskaan jaa .env-tiedostoa tai IBKR_ACCOUNT_ID:tä julkisesti.
- Kaikki salaisuudet ja tunnukset tulee säilyttää .env-tiedostossa, joka on .gitignore:ssa.
- Kehitysympäristössä käytetään mock-dataa (USE_MOCK=true), tuotannossa oikeaa IBKR-yhteyttä (USE_MOCK=false).
- Varmista, että ENVIRONMENT on production tuotantokäytössä.
- Suojaa palvelin palomuurilla ja käytä HTTPS:ää tuotannossa.
- Katso myös SECURITY.md (tulossa) ja .github/workflows/security.yml.
- The project relies on GitHub Dependabot for security updates and vulnerability checks.
- The Safety tool will be used for security checks once it is updated to be compatible with the latest pydantic version.

## Development Setup

### Prerequisites

- Docker and Docker Compose
- Python 3.12+
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
# - USE_MOCK: true/false
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
| USE_MOCK | Use mock data (true/false) | true |

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

Lue myös: [CONTRIBUTING.md](CONTRIBUTING.md)

## License

This project is licensed under the MIT License - see the LICENSE file for details. 