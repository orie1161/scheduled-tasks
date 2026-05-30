import os
import smtplib
import pandas
from random import randint
import datetime as dt


MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

today = (dt.datetime.now().month, dt.datetime.now().day)
birthdays_df = pandas.read_csv("birthdays.csv")
print(birthdays_df)
birthday_dict = birthdays_df.to_dict(orient="records")
print(birthday_dict)

for person in birthday_dict:
    birthday = (person["month"],person["day"])
    name = person["name"]
    email = person["email"]
    if birthday == today:
        with open(f"letter_templates/letter_{randint(1,3)}.txt") as letter:
            letter_contents = letter.read()
            new_letter_contents = letter_contents.replace("[NAME]", person["name"])
        print(new_letter_contents)
        print(email)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject: Happy Birthday!\n\n{new_letter_contents}")



