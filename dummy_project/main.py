import smtplib

my_email = "someemail"
my_password = "password"

connection = smtplib.SMTP("smtp.mail.yahoo.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="email", msg="Hello")
connection.close()
