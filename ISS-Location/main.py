import requests
from datetime import datetime
#
URL = "https://api.sunrise-sunset.org/json"
PARAMETERS = {
      'lat': 29.917817,
      "lng": -81.413552,
      "formatted": 0
}

#
# response = requests.get(URL)
# response.raise_for_status()
# iss_location = response.json()['iss_position']
#
# print(f"The location of the ISS is:\n\t Longitude: {iss_location['longitude']}\n\t "
#       f"Latitude: {iss_location['latitude']}")


response = requests.get(URL, params=PARAMETERS)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")
sunset = data['results']['sunset'].split("T")[1].split(":")
time_now = datetime.now()
print(time_now.hour)
print(sunrise[0])
print(sunset[0])