##################### Extra Hard Starting Project ######################
import pandas
import random
import smtplib
import datetime as dt

MY_EMAIL = "devmisaelpeixoto@gmail.com"
PASSWORD = "246gvdne"

# 1. Update the birthdays.csv
df = pandas.read_csv("birthdays.csv")
birthday_dates = df.to_dict(orient="records")

print(birthday_dates)

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
month = today.month
day = today.month


for index in birthday_dates:
    if index["month"] == month:
        if index["day"] == day:


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

            letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
            letter_chosen = random.choice(letters)
            with open(f"letter_templates/{letter_chosen}", "r") as letter:
                filedata = letter.read()
                filedata = filedata.replace("[NAME]", index["name"])
                print(filedata)
            with open(f"send_letters/birthday_{index['name']}.txt", "w") as letter:
                letter.write(filedata)
                print(type(filedata))


# 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=index['email'],
                                    msg=f"Subject: Happy Birthday\n\n"
                                        f"{filedata}"
                                    )



