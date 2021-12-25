import datetime as dt
import smtplib
import random

MY_EMAIL = "akileshpython@gmail.com"
PASSWORD = "Thilagu@123"
quotes = []

with open("quotes.txt") as quotes_file:
    for line in quotes_file:
        new_line = line.rstrip()
        quotes.append(new_line)

random_quote = random.choice(quotes)

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="akileshakileshs1234@gmail.com",
                        msg=f"Subject: Monday Motivation\n\n{random_quote}")
    connection.close()

