import smtplib
import datetime as dt
import random as rndm

my_email = "@gmail.com"
password = ""

today = dt.datetime.now()
day = today.weekday()


def new_quote():
    with open("quotes.txt", mode="r") as qt:
        qt_list = qt.readlines()
        quote = rndm.choice(qt_list)
        return quote


if day == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="1@yahoo.com",
            msg=f"Subject: MONDAY MOTIVATION \n\n{new_quote()}")
