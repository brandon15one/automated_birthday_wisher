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


