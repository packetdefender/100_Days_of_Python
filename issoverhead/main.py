import requests
from datetime import datetime
import smtplib as s


MY_EMAIL = "xxxxxxx
SMTP_SERVER = "smtp.gmail.com"
PASSWORD = "xxxxxxxx"
SMTP_PORT = 587
MY_LAT = 29.917817 # Your latitude
MY_LONG = -81.413552 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

def is_iss_overhead(my_lat, my_lng, iss_lat, iss_lng):
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_dark(my_time, sr, ss):
    if my_time >= ss or my_time <= sr:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

iss_over_me = is_iss_overhead(MY_LAT, MY_LONG, iss_latitude, iss_longitude)
is_night = is_dark(time_now, sunrise, sunset)
if iss_over_me and is_night:
    with s.SMTP(SMTP_SERVER, SMTP_PORT) as c:
        c.starttls()
        c.login(MY_EMAIL, PASSWORD)
        c.sendmail(from_addr=MY_EMAIL, to_addrs="mike@mikelossmann.me", msg="Subject: LOOKUP!\n\n The ISS is overhead!")
else:
    print("Nothing!")


