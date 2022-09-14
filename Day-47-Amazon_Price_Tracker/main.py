from bs4 import BeautifulSoup as bs
import requests
import smtplib
import os

URL = "https://www.amazon.com/Anker-PowerCore-Portable-Charger-Compatible/dp/B09VPHVT2Z/ref=sr_1_3?keywords=anker+737+power+bank&qid=1663116501&sprefix=anker+737+%2Caps%2C91&sr=8-3"
SMTP_USERNAME = os.environ["SMTP_USERNAME"]
SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]
SMTP_SERVER = "smtp.xxx.xxx"
SMTP_PORT = 587
TARGET_PRICE = 100.00


#Get Page
response = requests.get(URL, headers={"Accept-Language": "en-US", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15"})
website = response.text

soup = bs(website, 'html.parser')
dollar_amount = soup.find(name='span', class_="a-price-whole").getText()
change_amount = soup.find(name='span', class_="a-price-fraction").getText()
total_amount = float(f"{dollar_amount}{change_amount}")


#Setup and send Email
if total_amount <= TARGET_PRICE:
    FROM = "xxxx@xxxx.com"
    TO = "xxxx@xxxx.com"
    MSG = f"subject: Anker PowerCore is now {total_amount}, buy now! \n\nThe anker powercore 737 you are a looking at" \
          f" is below the threshold amount of ${TARGET_PRICE}!  Click here to buy it now {URL}"
    mail = smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(FROM, TO, MSG)
else:
    FROM = "xxxx@xxxx.com"
    TO = "xxxx@xxxx.com"
    MSG = f"subject: Anker PowerCore price is {total_amount}. \n\nThe price of the anker powercore 737 you are a looking " \
          f"at is ${TARGET_PRICE}.  No need to purchase yet"
    mail = smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(FROM, TO, MSG)


