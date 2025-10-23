import pandas as pd
import matplotlib.pyplot as plt

data = []

with open("crypto_prices.txt", "r") as file:
    for line in file:
        # print(f"RAW LINE: {reprcl(line)}")
        parts = line.strip().split(" - ")
        if len(parts) == 2:
            date = parts[0]
            btc_part, eth_part = parts[1].split(", ")
            btc = float(btc_part.split(": ")[1])
            eth = float(eth_part.split(": ")[1])
            data.append({"date": date, "BTC": btc, "ETH": eth})

# print(data)
df = pd.DataFrame(data)
df.to_csv("crypto_prices.csv", index=False)
print("✅ Saved crypto_prices.csv")

plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["BTC"], label="Bitcoin (BTC)", color="orange")
plt.plot(df["date"], df["ETH"], label="Ethereum (ETH)", color="blue")
plt.xticks(rotation=45)
plt.xlabel("Time")
plt.ylabel("Price in (USD)")
plt.title("Crypto price tracker")
plt.legend()
plt.tight_layout()
plt.show()
