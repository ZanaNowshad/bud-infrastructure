"""Crypto Portfolio Monitor v1 - track balances and send price alerts via AgentMail."""
import os
import time
import json
import requests
from datetime import datetime

WALLETS = {
    "ETH": "0xC18F96f597a58e6816A46D4E06BFfA237bc34A19",
    "BTC": "1FHwbig4wbNZwkQJB5SkbPRSHuoTquAcPa",
    "SOL": "An2dZzMcCY1NJgsr1Vqoq8aAU2zuGxSePUwLSaeXFNyo",
}
CHECK_INTERVAL = 300
PRICE_CHANGE_THRESHOLD = 2.0
_price_cache = {}
_balance_cache = {}

def get_eth_balance(address):
    try:
        url = f"https://api.blockcypher.com/v1/eth/main/addrs/{address}/balance"
        r = requests.get(url, timeout=10)
        data = r.json()
        return data.get("balance", 0) / 1e18
    except:
        return 0

def get_btc_balance(address):
    try:
        url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance"
        r = requests.get(url, timeout=10)
        data = r.json()
        return data.get("balance", 0) / 1e8
    except:
        return 0

def get_sol_balance(address):
    try:
        url = "https://api.mainnet-beta.solana.com"
        payload = {"jsonrpc": "2.0", "id": 1, "method": "getBalance", "params": [address]}
        r = requests.post(url, json=payload, timeout=10)
        data = r.json()
        if "result" in data:
            return data["result"]["value"] / 1e9
        return 0
    except:
        return 0

def get_price(asset):
    asset_map = {"ETH": "ethereum", "BTC": "bitcoin", "SOL": "solana"}
    coin_id = asset_map.get(asset)
    if not coin_id:
        return 0
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
        r = requests.get(url, timeout=10)
        data = r.json()
        return data.get(coin_id, {}).get("usd", 0)
    except:
        return _price_cache.get(asset, 0)

def send_alert(asset, balance, price, change_pct):
    try:
        from agentmail import AgentMail
        client = AgentMail()
        inbox = "muhamed-6323@agentmail.to"
        action = "UP" if change_pct > 0 else "DOWN"
        emoji = chr(128200) if change_pct > 0 else chr(128203)
        value_usd = balance * price
        client.inboxes.messages.send(
            inbox_id=inbox, to=inbox,
            subject=f"{emoji} {asset} Price Alert: {action} {abs(change_pct):.1f}%",
            text=f"Price Alert - {asset}\n\nCurrent Price: ${price:,.2f}\nYour Balance: {balance:.6f} {asset}\nPortfolio Value: ${value_usd:,.2f}\nChange: {action} {abs(change_pct):.1f}%\n\nTimestamp: {datetime.now().isoformat()}",
            labels=["crypto", "alerts"]
        )
        return True
    except Exception as e:
        print(f"Alert send failed: {e}")
        return False

def check_all():
    print(f"Portfolio Check: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    total_value = 0
    for asset, address in WALLETS.items():
        if asset == "ETH":
            balance = get_eth_balance(address)
        elif asset == "BTC":
            balance = get_btc_balance(address)
        elif asset == "SOL":
            balance = get_sol_balance(address)
        else:
            balance = 0
        price = get_price(asset)
        value = balance * price
        total_value += value
        prev_price = _price_cache.get(asset, price)
        _price_cache[asset] = price
        _balance_cache[asset] = balance
        change_pct = ((price - prev_price) / prev_price) * 100 if prev_price > 0 else 0
        print(f"  {asset}: {balance:.6f} x ${price:,.2f} = ${value:,.2f} ({change_pct:+.1f}%)")
        if abs(change_pct) >= PRICE_CHANGE_THRESHOLD:
            send_alert(asset, balance, price, change_pct)
    print(f"  TOTAL: ${total_value:,.2f}")
    report = {"timestamp": datetime.now().isoformat(), "total_value_usd": round(total_value, 2),
              "assets": {a: {"balance": _balance_cache.get(a, 0), "price_usd": _price_cache.get(a, 0)} for a in WALLETS}}
    os.makedirs("data", exist_ok=True)
    with open("data/portfolio_snapshot.json", "w") as f:
        json.dump(report, f, indent=2)
    return total_value

def run_loop():
    print("Crypto Portfolio Monitor started")
    check_all()
    while True:
        time.sleep(CHECK_INTERVAL)
        try:
            check_all()
        except Exception as e:
            print(f"Check failed: {e}")

if __name__ == "__main__":
    check_all()
