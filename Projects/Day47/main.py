
from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

#Misael Peixoto

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            "Accept-Language": 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7'}

amazon_url = "https://www.amazon.com/KLIEGOU-Hipster-Longline-Crewneck-T-Shirt/dp/B098Q74F7K/ref=sr_1_4_sspa?crid=18AMD1YSBWD1X&keywords=t-shirt&qid=1664412544&qu=eyJxc2MiOiIxMS42MiIsInFzYSI6IjExLjAxIiwicXNwIjoiMTAuMTkifQ%3D%3D&sprefix=t-shir%2Caps%2C219&sr=8-4-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFHRjBSUlVLQ0hQMEomZW5jcnlwdGVkSWQ9QTA0ODQzODIxSFBEQk5YQUM4VDFVJmVuY3J5cHRlZEFkSWQ9QTAxOTcxNzRIR0FCTEpIV09ESTcmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
r = requests.get(url=amazon_url, headers=headers)
amazon_page_deal = r.content

soup = BeautifulSoup(amazon_page_deal, "lxml")

price = soup.find(name = "span", class_="a-offscreen").getText()

print(price)
price_without_currency = price.split("$")[1]
price_as_afloat = float(price_without_currency)
print(price_as_afloat)

## Send e-mail ##

def send_email():
    smtp_server = "smtp@gmail.com"
    sender_email = "youremail@gmail.com"
    receiver_email = "receiver@something.com"
    #password = input("Type your password and press enter: ")
    password = "yourpassword"
    message = f"Subject: Amazon Webscraping\n\nThe product you wan to buy is {price_as_afloat}. Buy it at: {amazon_url}"

    with smtplib.SMTP("64.233.184.108", 587) as connection:
        connection.starttls()
        connection.login(user= sender_email, password= password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=receiver_email,
                            msg=message)

if price_as_afloat <= 22:
    send_email()
else:
    print("Price is higher than budget")