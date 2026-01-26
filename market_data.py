import yfinance as yf

def fetch_stock_data(ticker: str):
    ticker = ticker.upper()
    stock = yf.Ticker(ticker)
    info = stock.info

    if not info or "shortName" not in info:
        raise ValueError("Invalid ticker")

    return {
        "ticker": ticker,
        "name": info.get("shortName"),
        "price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "sector": info.get("sector"),
        "summary": info.get("longBusinessSummary")
    }
