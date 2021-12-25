import datetime as dt
import smtplib
import random

my_email = "akileshpython@gmail.com"
password = "Thilagu@123"
quotes = []

with open("quotes.txt") as quotes_file:
    for line in quotes_file:
        new_line = line.rstrip()
        quotes.append(new_line)

random_quote = random.choice(quotes)

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 5:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="akileshakileshs1234@gmail.com",
                        msg=f"Subject: Monday Motivation\n\n{random_quote}")
    connection.close()

