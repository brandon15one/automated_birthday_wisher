import pandas
import datetime as dt
import random
import smtplib

my_email = "@gmail.com"
password = ""
dates = pandas.read_csv("birthdays.csv")
date = dt.datetime.now()
today = (date.month, date.day)
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in dates.iterrows()}


if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as template:
        contents = template.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday! \n\n{contents}")
