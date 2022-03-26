import pandas as pd
import smtplib as s
import datetime as dt
from random import choice

BIRTHDAY_CSV = "birthdays.csv"
PLACEHOLDER = "[NAME]"
MY_EMAIL = "xxxxxxxxx"
SMTP_SERVER = "smtp.gmail.com"
PASSWORD = "jxxxxxxxx"
SMTP_PORT = 587

data = pd.read_csv(BIRTHDAY_CSV)
bday = data.to_dict(orient='records')
letter_templates = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt",
                    "./letter_templates/letter_3.txt"]

random_letter = choice((letter_templates))


for entry in bday:
    if entry['month'] == dt.datetime.now().month and entry['day'] == dt.datetime.now().day:
        with open(random_letter) as f:
            letter = f.read()
            new_letter = letter.replace(PLACEHOLDER, entry['name'])
            with s.SMTP(SMTP_SERVER, SMTP_PORT) as c:
                c.starttls()
                c.login(MY_EMAIL, PASSWORD)
                c.sendmail(from_addr=MY_EMAIL, to_addrs=entry['email'], msg=f"Subject: HAPPY BIRTHDAY!\n\n {new_letter}")
