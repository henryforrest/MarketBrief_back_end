import os
import requests
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

HF_TOKEN = os.environ["HF_TOKEN"]

def generate_ai_summary(ticker: str, stock_data: dict) -> str:
    prompt = f"""
Give a concise, investor-friendly overview of {ticker}.
Key data:
Price: {stock_data['price']}
Market Cap: {stock_data['market_cap']}
PE Ratio: {stock_data['pe_ratio']}
Sector: {stock_data['sector']}
"""

    response = requests.post(
        "https://router.huggingface.co/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {HF_TOKEN}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/Llama-3.1-8B-Instruct",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 200
        },
        timeout=30
    )

    return response.json()["choices"][0]["message"]["content"]
