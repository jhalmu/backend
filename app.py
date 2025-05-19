import csv
import os
import time
from datetime import datetime
from decimal import Decimal
from functools import lru_cache
from typing import Dict, List, Optional

import duckdb
import requests
import urllib3
import uvicorn
from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from requests.adapters import HTTPAdapter
from urllib3.exceptions import InsecureRequestWarning
from urllib3.util.retry import Retry

from db_config import get_db

# Import local modules
from mock_api import get_mock_response

# Disable SSL warnings for local development
urllib3.disable_warnings(InsecureRequestWarning)

# Configuration
BASE_API_URL = "https://localhost:5055/v1/api"
ACCOUNT_ID = os.getenv("IBKR_ACCOUNT_ID")
USE_MOCK = os.getenv("USE_MOCK", "true").lower() == "true"  # Use mock data by default
REQUEST_TIMEOUT = 30  # Increased timeout for local development
MAX_RETRIES = 5  # Increased retries for local development

app = FastAPI(title="IBKR REST API")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Tietokanta (myöhemmin siirretään omaan moduuliin)
DIVIDEND_HISTORY: List[Dict] = []


# Configure requests session with retries and timeouts
@lru_cache()
def get_session():
    session = requests.Session()
    retry_strategy = Retry(
        total=MAX_RETRIES,
        backoff_factor=1,  # Increased backoff for local development
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET", "POST", "PUT", "DELETE"],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


# Template filter
def timectime(s):
    return time.ctime(s / 1000)


# Add filter to template context
templates.env.filters["ctime"] = timectime


async def make_api_request(endpoint: str, method: str = "GET", **kwargs) -> dict:
    """Make an API request with proper error handling and retries."""
    if USE_MOCK:
        print(f"Using mock data for endpoint: {endpoint}")  # Debug logging
        return get_mock_response(endpoint)

    session = get_session()
    try:
        response = session.request(
            method,
            f"{BASE_API_URL}/{endpoint}",
            verify=False,  # Disable SSL verification for local development
            timeout=REQUEST_TIMEOUT,
            **kwargs,
        )
        response.raise_for_status()
        return response.json() if response.content else {}
    except requests.exceptions.RequestException as e:
        print(f"Error making request to {endpoint}: {str(e)}")  # Debug logging
        raise HTTPException(
            status_code=500, detail=f"Error communicating with IBKR Gateway: {str(e)}"
        )


def calculate_dividend_totals(dividends: List[Dict]) -> Dict:
    """Calculate total dividend income for different time periods."""
    monthly_total = Decimal("0")
    yearly_total = Decimal("0")
    five_year_total = Decimal("0")

    for div in dividends:
        # Laske vuosittainen osinkotulo
        yearly = Decimal(str(div.get("annualDividend", 0))) * Decimal(
            str(div.get("position", 0))
        )
        monthly = yearly / Decimal("12")
        five_year = yearly * Decimal("5")

        monthly_total += monthly
        yearly_total += yearly
        five_year_total += five_year

    # Oletetaan EUR/USD kurssiksi 1.08 (myöhemmin haetaan reaaliajassa)
    eur_rate = Decimal("1.08")

    return {
        "monthly_dividend": float(monthly_total),
        "monthly_dividend_eur": float(monthly_total / eur_rate),
        "yearly_dividend": float(yearly_total),
        "yearly_dividend_eur": float(yearly_total / eur_rate),
        "five_year_dividend": float(five_year_total),
        "five_year_dividend_eur": float(five_year_total / eur_rate),
    }


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    try:
        accounts = await make_api_request("portfolio/accounts")
        if not accounts and not USE_MOCK:  # Tarkista mock-tila
            return HTMLResponse(
                'Make sure you authenticate first then visit this page. <a href="https://localhost:5055">Log in</a>'
            )

        account = accounts[0]
        account_id = account["id"]
        summary = await make_api_request(f"portfolio/{account_id}/summary")
        positions = await make_api_request(f"portfolio/{account_id}/positions/0")

        return templates.TemplateResponse(
            "dashboard.html",
            {
                "request": request,
                "account": account,
                "summary": summary,
                "positions": positions,
            },
        )
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})


@app.get("/lookup", response_class=HTMLResponse)
async def lookup(request: Request, symbol: Optional[str] = None):
    stocks = []
    if symbol:
        try:
            stocks = await make_api_request(
                f"iserver/secdef/search?symbol={symbol}&name=true"
            )
        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"detail": e.detail})

    return templates.TemplateResponse(
        "lookup.html", {"request": request, "stocks": stocks}
    )


@app.get("/dividends", response_class=HTMLResponse)
async def dividends(request: Request):
    try:
        dividends_data = await make_api_request("portfolio/dividends")
        dividends_list = dividends_data.get("dividends", [])

        # Laske yhteenvedot
        totals = calculate_dividend_totals(dividends_list)

        return templates.TemplateResponse(
            "dividends.html",
            {
                "request": request,
                "dividends": dividends_list,
                **totals,
            },
        )
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})


@app.post("/dividends/upload")
async def upload_dividend_history(file: UploadFile = File(...)):
    """Handle CSV file upload for dividend history."""
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")

    try:
        contents = await file.read()
        decoded = contents.decode()
        csv_reader = csv.DictReader(decoded.splitlines())

        # Tyhjennä vanha historia
        DIVIDEND_HISTORY.clear()

        # Lisää uudet rivit
        for row in csv_reader:
            DIVIDEND_HISTORY.append({
                "date": row.get("date", ""),
                "symbol": row.get("symbol", ""),
                "amount": float(row.get("amount", 0)),
                "currency": row.get("currency", "USD"),
                "description": row.get("description", ""),
            })

        return {
            "message": f"Successfully imported {len(DIVIDEND_HISTORY)} dividend records"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error processing CSV file: {str(e)}"
        )


@app.get("/stock/{symbol}", response_class=HTMLResponse)
async def stock_details(request: Request, symbol: str):
    """Show detailed information about a specific stock."""
    try:
        # Hae osakkeen tiedot IBKR:sta
        stock_info = await make_api_request(
            f"iserver/secdef/search?symbol={symbol}&name=true"
        )
        if not stock_info:
            raise HTTPException(status_code=404, detail=f"Stock {symbol} not found")

        # Hae osakkeen position tiedot
        positions = await make_api_request(f"portfolio/{ACCOUNT_ID}/positions/0")
        position = next((p for p in positions if p["name"] == symbol), None)

        # Hae osakkeen osinkohistoria
        dividend_history = [d for d in DIVIDEND_HISTORY if d["symbol"] == symbol]

        return templates.TemplateResponse(
            "stock.html",
            {
                "request": request,
                "stock": stock_info[0] if stock_info else None,
                "position": position,
                "dividend_history": dividend_history,
            },
        )
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})


# Health check endpoint
@app.get("/health")
async def health_check():
    try:
        # Tarkista DuckDB yhteys
        conn = get_db()
        conn.execute("SELECT 1")
        conn.close()

        return JSONResponse(
            status_code=200,
            content={
                "status": "healthy",
                "timestamp": datetime.utcnow().isoformat(),
                "version": "1.0.0",
                "environment": os.getenv("ENVIRONMENT", "development"),
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat(),
                "environment": os.getenv("ENVIRONMENT", "development"),
            },
        )
