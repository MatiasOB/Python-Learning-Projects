# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
df = pd.read_csv("letter_templates/birthdays.csv")

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

for index, row in df.iterrows():
    birthday_month = row["month"]
    birthday_day = row["day"]
    birthday_name = row["name"]

    if birthday_month == month and birthday_day == day:
        print(f"Happy birthday!, {birthday_name}!")
        birthday_email = row["email"]

        random_number = random.randint(1,3)
        with open(f"letter_templates/letter_{random_number}.txt") as file:
            message = file.read()
            message = message.replace("[NAME]",birthday_name)

        my_email = os.getenv("myemail")
        password = os.getenv("mypass")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:Happy Birthday! {birthday_name}!\n\n{message}")

        #Check pythonanywhere to run this in the cloud so it checks everyday.
