import requests
import os

api_key = os.environ.get("OWM_API_KEY")
# api_key = "752e3cc0ad49059cd471c30285620744"
#'coord': {'lon': 81.85, 'lat': 25.45}
parameters = {
    "lat": 25.45,
    "lon": 81.85,
    "appid": api_key,
    "exclude": "current,daily,minutely,daily"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
weather_slice = weather_data["hourly"][:12]
weather_hourly_data = []
will_rain = False
for i in range(12):
    hourly_data = weather_data["hourly"][i]["weather"][0]["id"]
    if hourly_data < 700:
        weather_hourly_data.append(hourly_data)
        will_rain = True

if will_rain:
    print("Please bring an umbrella")





