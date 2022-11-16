import requests
from datetime import datetime
import smtplib
MY_LAT = 17.644022 # Your latitude
MY_LONG = -66.425653 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


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

time_now = datetime.now()
hour = time_now.hour

def proximity_check():
    if hour > 20:
        if iss_latitude > MY_LAT-5 and iss_latitude < MY_LAT + 5:
            if iss_longitude > MY_LONG-5 and iss_longitude < MY_LONG + 5:
                return True
        else:
            return False
    else:
        return False

if proximity_check():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login("foo", "foo")
        connection.sendmail(from_addr="foo",
                            to_addrs="foo",
                            msg="Subject: Look up"
                            )
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



