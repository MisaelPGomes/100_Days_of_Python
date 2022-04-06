import smtplib
import datetime as dt
import random

MY_EMAIL = "my_email@gmail.com"
PASSWORD = "mypassword"

today = dt.datetime.now()
weekday = today.weekday()
if weekday == 0 :
    with open("quotes.txt") as quotes:
        motivation_quotes = quotes.readlines()
        monday_quote = random.choice(motivation_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="devmisael@yahoo.com",
                            msg=f"Subject: Motivational Monday\n\n{monday_quote}."
                            )




