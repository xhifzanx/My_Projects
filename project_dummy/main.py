import smtplib

my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="someemail", msg="hello")
connection.close()
