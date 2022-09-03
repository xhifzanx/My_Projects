##################### Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

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
            my_email = "dummyacounhotmail@gmail.com"
            password = "hifzan1234"
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=my_email, password=password)
            print(birthdays_data[i]['email'])
            connection.sendmail(from_addr=my_email, to_addrs=f"{birthdays_data[i]['email']}", msg=new_content)
            connection.close()