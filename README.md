# IBKR Portfolio Backend

Backend-sovellus Interactive Brokers (IBKR) portfolion hallintaan ja analysointiin. Sovellus tarjoaa API:n portfolion tietojen hakemiseen, osinkojen seurantaan ja osaketietojen analysointiin.

## Ominaisuudet

- Portfolio-analyysi ja -seuranta
- Osinkojen seuranta ja ennusteet
- Osaketietojen analyysi
- REST API rajapinta
- Docker-tuki
- Mock API kehitystä varten

## Teknologiat

- Python 3.11
- FastAPI
- Jinja2
- Tailwind CSS
- Docker
- DuckDB (suunnitteilla)

## Asennus

### Vaatimukset

- Python 3.11 tai uudempi
- Docker ja Docker Compose
- Git

### Kehitysympäristö

1. Kloonaa repository:
```bash
git clone https://github.com/yourusername/ibkr-portfolio-backend.git
cd ibkr-portfolio-backend
```

2. Luo virtuaaliympäristö ja asenna riippuvuudet:
```bash
python -m venv .venv
source .venv/bin/activate  # Unix/macOS
# tai
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

3. Käynnistä sovellus:
```bash
uvicorn app:app --reload
```

### Docker

1. Rakenna ja käynnistä Docker-kontti:
```bash
docker compose up --build
```

Sovellus on saatavilla osoitteessa http://localhost:8000

## API Dokumentaatio

API dokumentaatio on saatavilla osoitteessa:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Kehitys

### Projektin rakenne

```
backend/
├── app.py              # Pääsovellus
├── mock_api.py         # Mock API kehitystä varten
├── requirements.txt    # Python riippuvuudet
├── Dockerfile         # Docker konfiguraatio
├── docker-compose.yml # Docker Compose konfiguraatio
├── conf.yaml          # IBKR Gateway konfiguraatio
├── start.sh           # Käynnistysskripti
├── static/            # Staattiset tiedostot
└── templates/         # Jinja2 templatet
```

### Kehitysympäristön asetukset

1. VS Code asetukset:
   - Python extension
   - Docker extension
   - Remote Development extension

2. Hot reload:
   - Sovellus käynnistyy automaattisesti muutosten yhteydessä
   - Docker Compose käyttää volyymimounttausta kehitystä varten

### Testaus

```bash
# Yksikkötestit
pytest

# API testit
pytest tests/api/

# Kattavuusraportti
pytest --cov=app tests/
```

## Tuotantoon vienti

1. Rakenna Docker-kuva:
```bash
docker build -t ibkr-portfolio-backend .
```

2. Vie kuva rekisteriin:
```bash
docker tag ibkr-portfolio-backend your-registry.com/ibkr-portfolio-backend:latest
docker push your-registry.com/ibkr-portfolio-backend:latest
```

## Lisenssi

MIT

## Yhteystiedot

- GitHub: [yourusername](https://github.com/yourusername)
- Email: your.email@example.com 