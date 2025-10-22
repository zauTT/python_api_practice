import requests

def get_coordinates(city_name):
    """Get latitude and longitude for a city."""
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
    res = requests.get(geo_url)
    if res.status_code == 200 and res.json().get("results"):
        city_info = res.json()["results"][0]
        return city_info["latitude"], city_info["longitude"], city_info["name"]
    else:
        print("❌ City not found.")
        return None, None, None
    
def get_weather(lat, lon, city):
    """Fetch and display current weather for the city."""
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    res = requests.get(weather_url)
    if res.status_code == 200:
        data = res.json()
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
        print("❌ Failed to get weather data:", res.status_code)

city = input("Enter city name: ").strip()

lat, lon, name = get_coordinates(city)
if lat and lon:
    get_weather(lat, lon, name)

