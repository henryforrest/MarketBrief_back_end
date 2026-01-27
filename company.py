import yfinance as yf

def get_company_summary(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    return {
        "name": info.get("shortName", "N/A"),
        "sector": info.get("sector", "N/A"),
        "industry": info.get("industry", "N/A"),
        "summary": info.get("longBusinessSummary", "N/A"),
        "website": info.get("website", "N/A"),
        "market_cap": info.get("marketCap", "N/A")
    }


def truncate_text(text, max_chars=300):
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "…"
