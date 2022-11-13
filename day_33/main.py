import requests
import datetime as dt
import smtplib


MY_LAT = 25.473034
MY_LONG = 81.878357

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}



def function():
    response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(f"sunrise: {sunrise}")
    print(f"sunset: {sunset}")

    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    iss_data = response_iss.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["latitude"])
    print(iss_latitude)
    print(iss_longitude)

    now = dt.datetime
    now_hour = now.now().hour
    print(f"now in hours: {now_hour}")

    sunset_time = 18
    sunrise_time = 5
    if (now_hour > sunset_time or now_hour<sunrise_time) and ((iss_latitude >= MY_LAT-5 or iss_latitude <= MY_LAT+5) and (iss_longitude >= MY_LONG-5 or iss_longitude <= MY_LONG+5)):
        print("look up")
        my_email = "YOUR EMAIL"
        my_password = "YOUR PASSWORD"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="YOUR EMAIL", msg="Lookup")
        connection.close()
    else:
        print("wait sometime")


while True:
    condition = dt.datetime.now().second
    if condition == 59:
        function()

