#import smtplib

#my_email = "dummyacounhotmail@gmail.com"
#password = "hifzan1234"
#connection = smtplib.SMTP("smtp.gmail.com")
#connection.starttls()
#connection.login(user=my_email, password=password)
#connection.sendmail(from_addr=my_email, to_addrs="misterj435@gmail.com", msg="hello")
#connection.close()
#print("dkfjkfj")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
if year > 2020:
    print("You are 20 year old")
print(f"{year}//{month}//{day_of_week+1}")

date_of_birth = dt.datetime(year=2000, month=3, day=27)
print(date_of_birth)