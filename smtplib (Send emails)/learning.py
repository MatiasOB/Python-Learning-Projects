import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")
# my_email = ""
# password = ""
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=my_email,
#                         msg="Subject:Hello\n\nThis is the body of my email!")

now = dt.datetime.now()
year = now.year
month= now.month
day_of_week = now.weekday()
date_of_birth = dt.datetime(year=1994,month=10,day=11, hour=9)

#if day_of_week == 4:
if True:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    message = quote
    my_email = os.getenv("myemail")
    password = os.getenv("mypass")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivation\n\nDear Matias,\n\n{message}")






