#import smtplib



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
