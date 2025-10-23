import requests
import datetime

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
except requests.RequestException as e:
    print("❌ API request failed:", e)
    data = {}
    
bitcoin_price = data.get("bitcoin", {}).get("usd")
ethereum_price = data.get("ethereum", {}).get("usd")

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if bitcoin_price is not None:
    if bitcoin_price > 50000:
        print("🚀 Bitcoin is soaring high!")
    elif bitcoin_price < 30000:
        print("📉 Bitcoin is dipping low.")
    else:
        print("🔄 Bitcoin is stable.")

if ethereum_price is not None:
    if ethereum_price > 4000:
        print("🚀 Ethereum is soaring high!")
    elif ethereum_price < 2000:
        print("📉 Ethereum is dipping low.")
    else:
        print("🔄 Ethereum is stable.")

with open("crypto_prices.txt", "a") as f:
    f.write(f"{current_time} - BTC: {bitcoin_price}, ETH: {ethereum_price}\n")
