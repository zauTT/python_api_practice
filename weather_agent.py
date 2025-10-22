import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=41.7151&longitude=44.8271&current_weather=true"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data["current_weather"]

    temp = weather["temperature"]
    wind = weather["windspeed"]

    print(f"🌍 Tbilisi Weather Report:")
    print(f"Temperature: {temp}°C")
    print(f"Wind Speed: {wind} km/h")

    if temp > 25:
        print("☀️ It's warm today — maybe go outside for a walk!")
    elif temp < 15:
        print("🌤️ Nice and mild, perfect coffee weather.")
    else:
        print("🥶 Cold day — don’t forget your jacket!")

else:
    print("❌ Failed to get weather data:", response.status_code)

