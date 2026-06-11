"""FastAPI web dashboard for Crypto Portfolio Monitor."""
import json
import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Crypto Portfolio Monitor")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

DATA_FILE = "data/portfolio_snapshot.json"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Crypto Portfolio Monitor</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Inter', -apple-system, sans-serif; background: #0a0a0f; color: #e0e0e0; min-height: 100vh; }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 40px 20px; }}
        h1 {{ font-size: 28px; margin-bottom: 8px; color: #fff; }}
        .subtitle {{ color: #888; margin-bottom: 30px; }}
        .card {{ background: #13131a; border: 1px solid #1e1e2a; border-radius: 12px; padding: 20px; margin-bottom: 16px; }}
        .card h2 {{ font-size: 16px; color: #888; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 1px; }}
        .balance {{ font-size: 36px; font-weight: 700; color: #fff; }}
        .balance.usd {{ color: #4ade80; }}
        .asset-row {{ display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid #1e1e2a; }}
        .asset-row:last-child {{ border-bottom: none; }}
        .asset-name {{ font-weight: 600; font-size: 18px; }}
        .asset-details {{ text-align: right; }}
        .asset-price {{ color: #888; font-size: 14px; }}
        .status {{ display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 8px; }}
        .status.online {{ background: #4ade80; }}
        .timestamp {{ color: #555; font-size: 12px; margin-top: 20px; text-align: center; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Crypto Portfolio Monitor</h1>
        <p class="subtitle">Real-time balance tracking and price alerts</p>
        <div class="card">
            <h2>Total Portfolio Value</h2>
            <div class="balance usd">${total_value}</div>
        </div>
        <div class="card">
            <h2>Assets</h2>
            {assets_html}
        </div>
        <div class="card">
            <h2>System Status</h2>
            <div style="margin-top: 8px;"><span class="status online"></span> Monitoring Active</div>
            <div style="margin-top: 8px; color: #888; font-size: 14px;">Alerts via email - 5-min check interval - 2% price alert threshold</div>
        </div>
        <div class="timestamp">Last updated: {timestamp} - Data refreshes every 5 minutes</div>
    </div>
</body>
</html>
"""

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {"total_value_usd": 0, "assets": {}}

@app.get("/")
async def root():
    data = load_data()
    assets = data.get("assets", {})
    total = data.get("total_value_usd", 0)
    asset_rows = ""
    coin_icons = {"ETH": "ETH", "BTC": "BTC", "SOL": "SOL"}
    for name, info in assets.items():
        bal = info.get("balance", 0)
        price = info.get("price_usd", 0)
        value = bal * price
        asset_rows += f"""
        <div class="asset-row">
            <div><span class="asset-name">{name}</span></div>
            <div class="asset-details">
                <div>{bal:.6f} {name}</div>
                <div class="asset-price">${price:,.2f} - ${value:,.2f}</div>
            </div>
        </div>"""
    timestamp = data.get("timestamp", "N/A")
    html = HTML_TEMPLATE.format(
        total_value=f"{total:,.2f}",
        assets_html=asset_rows,
        timestamp=timestamp
    )
    return HTMLResponse(html)

@app.get("/api/portfolio")
async def api_portfolio():
    return load_data()

@app.get("/api/health")
async def health():
    return {"status": "ok", "service": "crypto-portfolio-monitor", "version": "1.0.0"}
