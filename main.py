from fastapi import FastAPI, HTTPException
from market_data import fetch_stock_data
from ai_summary import generate_ai_summary


app = FastAPI()

@app.get("/stock/{ticker}")
def get_stock(ticker: str):
    try:
        stock_data = fetch_stock_data(ticker)
        ai_summary = generate_ai_summary(ticker, stock_data)

        return {
            **stock_data,
            "ai_summary": ai_summary
        }

    except Exception as e:
        print("ERROR:", repr(e))
        raise HTTPException(status_code=500, detail=str(e))

