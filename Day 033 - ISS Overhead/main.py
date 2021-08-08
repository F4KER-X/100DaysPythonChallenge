import time

import requests
from datetime import datetime
import smtplib

MY_LAT = 45.583729  # Your latitude
MY_LONG = -73.750069  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def near_me():
    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True
    return False


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


def is_dark():
    if sunset <= time_now <= sunrise:
        return True


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
MY_EMAIL = ''  # Email
MY_PASSWORD = ''  # Password


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connections:
        connections.starttls()
        connections.login(user=MY_EMAIL, password=MY_PASSWORD)
        connections.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="LOOK UP")


while True:
    time.sleep(60)
    if near_me() and is_dark():
        send_email()
        break
# BONUS: run the code every 60 seconds.
