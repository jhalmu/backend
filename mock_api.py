"""
Mock data for IBKR API responses during development.
"""

MOCK_ACCOUNTS = [
    {
        "id": "MOCK_ACCOUNT_ID",
        "accountId": "MOCK_ACCOUNT_ID",
        "accountVan": "MOCK_ACCOUNT_ID",
        "accountTitle": "Individual",
        "displayName": "Individual",
        "accountAlias": "Individual",
        "accountStatus": 1,
        "currency": "USD",
        "type": "INDIVIDUAL",
        "faclient": False,
        "parent": "",
        "desc": "",
        "covestor": False,
        "masterAccountId": "",
        "tradingType": "CASH",
        "firmType": "INDIVIDUAL",
        "clearingStatus": "PAPER",
        "businessType": "INDIVIDUAL",
    }
]

MOCK_SUMMARY = {
    "totalcashvalue": {"amount": 100000.00, "currency": "USD"},
    "netliquidationvalue": {"amount": 150000.00, "currency": "USD"},
    "buyingpower": {"amount": 200000.00, "currency": "USD"},
    "equitywithloanvalue": {"amount": 150000.00, "currency": "USD"},
    "previousdayequitywithloanvalue": {"amount": 145000.00, "currency": "USD"},
    "regtequity": {"amount": 150000.00, "currency": "USD"},
    "regtmargin": {"amount": 200000.00, "currency": "USD"},
    "sma": {"amount": 50000.00, "currency": "USD"},
}

# Lista suosittuja osakkeita eri sektoreista
POPULAR_STOCKS = [
    # Tech
    ("AAPL", "Apple Inc", 175.50),
    ("MSFT", "Microsoft Corporation", 275.75),
    ("GOOGL", "Alphabet Inc Class A", 115.25),
    ("AMZN", "Amazon.com Inc", 145.24),
    ("META", "Meta Platforms Inc", 310.15),
    ("NVDA", "NVIDIA Corporation", 450.00),
    ("TSLA", "Tesla Inc", 180.50),
    ("AMD", "Advanced Micro Devices Inc", 125.75),
    ("INTC", "Intel Corporation", 35.25),
    ("CRM", "Salesforce Inc", 210.50),
    # Finance
    ("JPM", "JPMorgan Chase & Co", 150.25),
    ("BAC", "Bank of America Corp", 35.75),
    ("GS", "The Goldman Sachs Group Inc", 380.50),
    ("V", "Visa Inc", 250.75),
    ("MA", "Mastercard Inc", 380.25),
    # Healthcare
    ("JNJ", "Johnson & Johnson", 155.75),
    ("PFE", "Pfizer Inc", 28.50),
    ("MRK", "Merck & Co Inc", 105.25),
    ("UNH", "UnitedHealth Group Inc", 450.75),
    ("ABBV", "AbbVie Inc", 145.50),
    # Consumer
    ("KO", "Coca-Cola Co", 60.25),
    ("PEP", "PepsiCo Inc", 165.75),
    ("MCD", "McDonald's Corp", 280.50),
    ("SBUX", "Starbucks Corp", 95.25),
    ("NKE", "Nike Inc", 100.75),
    # Industrial
    ("BA", "Boeing Co", 180.50),
    ("CAT", "Caterpillar Inc", 325.75),
    ("GE", "General Electric Co", 125.25),
    ("MMM", "3M Co", 95.50),
    ("HON", "Honeywell International Inc", 195.75),
    # Energy
    ("XOM", "Exxon Mobil Corporation", 105.25),
    ("CVX", "Chevron Corporation", 150.75),
    ("COP", "ConocoPhillips", 115.50),
    ("SLB", "Schlumberger Ltd", 45.25),
    ("EOG", "EOG Resources Inc", 120.75),
    # Materials
    ("BHP", "BHP Group Ltd", 60.25),
    ("RIO", "Rio Tinto Plc", 65.75),
    ("VALE", "Vale SA", 12.50),
    ("FCX", "Freeport-McMoRan Inc", 38.25),
    ("NEM", "Newmont Corporation", 35.75),
    # Telecom
    ("T", "AT&T Inc", 16.75),
    ("VZ", "Verizon Communications Inc", 40.25),
    ("TMUS", "T-Mobile US Inc", 145.50),
    ("CMCSA", "Comcast Corporation", 40.75),
    ("CHTR", "Charter Communications Inc", 280.25),
    # Real Estate
    ("AMT", "American Tower Corp", 195.50),
    ("PLD", "Prologis Inc", 125.75),
    ("CCI", "Crown Castle Inc", 105.25),
    ("WELL", "Welltower Inc", 85.50),
    ("EQR", "Equity Residential", 60.75),
    # Utilities
    ("NEE", "NextEra Energy Inc", 60.25),
    ("DUK", "Duke Energy Corp", 95.75),
    ("SO", "Southern Co", 70.50),
    ("D", "Dominion Energy Inc", 45.25),
    ("AEP", "American Electric Power Co Inc", 80.75),
]

# Luo positionit suosituista osakkeista
MOCK_POSITIONS = []
for i, (symbol, name, price) in enumerate(POPULAR_STOCKS):
    position = {
        "conid": 1000000 + i,
        "name": symbol,
        "contractDesc": name,
        "position": 100,  # Oletuspositio 100 osaketta
        "avgCost": round(price * 0.9, 2),  # Osto 10% alle nykyisen hinnan
        "mktPrice": price,
        "mktValue": round(100 * price, 2),
        "unrealizedPnl": round(100 * (price - price * 0.9), 2),
        "currency": "USD",
    }
    MOCK_POSITIONS.append(position)

# Luo osakkeiden tiedot hakua varten
MOCK_STOCKS = []
for i, (symbol, name, price) in enumerate(POPULAR_STOCKS):
    # Generoidaan CUSIP (9 merkkiä) ja ISIN (12 merkkiä) mock-datana
    cusip = f"{symbol:6}{i:03d}".replace(" ", "0")  # 6 merkkiä symbolista + 3 numeroa
    isin = f"US{cusip}0"  # US + CUSIP + check digit (0 mock-datassa)

    stock = {
        "conid": 1000000 + i,
        "symbol": symbol,
        "name": name,
        "exchange": "NASDAQ"
        if symbol
        in [
            "AAPL",
            "MSFT",
            "GOOGL",
            "AMZN",
            "META",
            "NVDA",
            "TSLA",
            "AMD",
            "INTC",
            "CRM",
        ]
        else "NYSE",
        "type": "STK",
        "currency": "USD",
        "cusip": cusip,
        "isin": isin,
        "country": "US",  # Liikkeellelaskijamaa
    }
    MOCK_STOCKS.append(stock)

# Lisätään osinkotiedot osakkeille
DIVIDEND_DATA = {
    "AAPL": {"dividend": 0.24, "yield": 0.55, "next_ex_date": "2024-05-10"},
    "MSFT": {"dividend": 0.75, "yield": 0.73, "next_ex_date": "2024-05-15"},
    "JNJ": {"dividend": 1.19, "yield": 3.05, "next_ex_date": "2024-05-28"},
    "PFE": {"dividend": 0.42, "yield": 5.89, "next_ex_date": "2024-05-09"},
    "KO": {"dividend": 0.46, "yield": 3.05, "next_ex_date": "2024-05-31"},
    "PEP": {"dividend": 1.15, "yield": 2.77, "next_ex_date": "2024-05-31"},
    "JPM": {"dividend": 1.05, "yield": 2.79, "next_ex_date": "2024-07-31"},
    "V": {"dividend": 0.52, "yield": 0.83, "next_ex_date": "2024-06-06"},
    "MA": {"dividend": 0.66, "yield": 0.69, "next_ex_date": "2024-06-07"},
    "XOM": {"dividend": 0.95, "yield": 3.61, "next_ex_date": "2024-05-14"},
    "CVX": {"dividend": 1.63, "yield": 4.32, "next_ex_date": "2024-05-17"},
    "T": {"dividend": 0.28, "yield": 6.69, "next_ex_date": "2024-07-10"},
    "VZ": {"dividend": 0.67, "yield": 6.67, "next_ex_date": "2024-07-10"},
    "DUK": {"dividend": 1.02, "yield": 4.26, "next_ex_date": "2024-06-17"},
    "NEE": {"dividend": 0.51, "yield": 3.38, "next_ex_date": "2024-05-31"},
}

# Päivitetään MOCK_POSITIONS lisäämällä osinkotiedot
for position in MOCK_POSITIONS:
    symbol = position["name"]
    if symbol in DIVIDEND_DATA:
        position.update({
            "dividend": DIVIDEND_DATA[symbol]["dividend"],
            "dividendYield": DIVIDEND_DATA[symbol]["yield"],
            "nextExDate": DIVIDEND_DATA[symbol]["next_ex_date"],
            "annualDividend": round(
                DIVIDEND_DATA[symbol]["dividend"] * 4, 2
            ),  # Vuosittainen osinko
            "dividendIncome": round(
                position["position"] * DIVIDEND_DATA[symbol]["dividend"] * 4, 2
            ),  # Vuosittainen osinkotulo
        })


def get_mock_response(endpoint: str) -> dict:
    """Return mock data based on the endpoint."""
    if endpoint == "portfolio/accounts":
        return MOCK_ACCOUNTS
    elif endpoint.startswith("portfolio/") and "/summary" in endpoint:
        return MOCK_SUMMARY
    elif endpoint.startswith("portfolio/") and "/positions" in endpoint:
        return MOCK_POSITIONS
    elif endpoint.startswith("iserver/secdef/search"):
        return MOCK_STOCKS
    elif endpoint.startswith("portfolio/dividends"):
        # Palautetaan osinkotiedot kaikille osakkeille
        return {
            "dividends": [
                {
                    "symbol": symbol,
                    "name": next(
                        (
                            p["contractDesc"]
                            for p in MOCK_POSITIONS
                            if p["name"] == symbol
                        ),
                        "",
                    ),
                    "position": next(
                        (p["position"] for p in MOCK_POSITIONS if p["name"] == symbol),
                        0,
                    ),
                    "cusip": next(
                        (s["cusip"] for s in MOCK_STOCKS if s["symbol"] == symbol),
                        "",
                    ),
                    "isin": next(
                        (s["isin"] for s in MOCK_STOCKS if s["symbol"] == symbol),
                        "",
                    ),
                    "dividend": data["dividend"],
                    "yield": data["yield"],
                    "next_ex_date": data["next_ex_date"],
                    "annualDividend": round(data["dividend"] * 4, 2),
                    "dividendIncome": round(
                        next(
                            (
                                p["position"]
                                for p in MOCK_POSITIONS
                                if p["name"] == symbol
                            ),
                            0,
                        )
                        * data["dividend"]
                        * 4,
                        2,
                    ),
                }
                for symbol, data in DIVIDEND_DATA.items()
            ]
        }
    return {}
