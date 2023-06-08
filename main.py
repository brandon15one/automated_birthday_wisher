import smtplib


my_email = "siddhantb151@gmail.com"
password = "wyjiuyfuvbbuwtzh"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="siddhantb151@yahoo.com",
        msg="Subject: hello\n\nthis is the body og my email")

