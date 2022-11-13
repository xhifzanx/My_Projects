##################### Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib


data = pandas.read_csv("birthdays.csv")
birthdays_data = data.to_dict(orient="records")



now = dt.datetime.now()
year = now.year
month = now.month
day = now.day


for i in range(4):
    if month == birthdays_data[i]["month"] and day == birthdays_data[i]["day"]:

            x = random.randint(1, 3)
            location = f"./letter_templates/letter_{x}.txt"
            with open(location, "r") as data:
                content = data.read()
                new_content = content.replace("[NAME]", f"{birthdays_data[i]['name']}")
            my_email = "YOUREMAIL"
            password = "YOURPASSWORD"
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=my_email, password=password)
            print(birthdays_data[i]['email'])
            connection.sendmail(from_addr=my_email, to_addrs=f"{birthdays_data[i]['email']}", msg=new_content)
            connection.close()
