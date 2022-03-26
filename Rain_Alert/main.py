import requests
import os
from twilio.rest import Client

API_KEY = os.environ.get("API_KEY_OWM")
LAT = 30.035639
LON = -81.56947
URL = "https://api.openweathermap.org/data/2.5/onecall"

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

PARAMETERS = {
    'lat': LAT,
    "lon": LON,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(URL, PARAMETERS)
response.raise_for_status()

weather_data = response.json()["hourly"]
will_rain = False
for hour in weather_data[:12]:
    if int(hour["weather"][0]['id']) < 600:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body="It is going to 🌧 today, bring a ☔️️",
            from_='+yyyyy',
            to='xxxxxx'
        )
else:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body="No rain today, you are good!",
            from_='+xxxxxx',
            to='+yyyyyy'
        )

print(message.status)
