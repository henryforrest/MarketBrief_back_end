import yfinance as yf


def fetch_stock_data(ticker, start_date="2015-01-01"):
    ticker = ticker.upper()
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date)

    if df.empty:
        raise ValueError(f"No data found for ticker: {ticker}")

    return df

def get_prices(df):
    if "Adj Close" in df.columns:
        return df["Adj Close"]
    elif "Close" in df.columns:
        return df["Close"]
    else:
        raise KeyError("Price column not found in data")



def get_volume(df):
    return df["Volume"]
