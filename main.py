import pandas as pd
from datetime import datetime
import random as rn
import smtplib

myEmail = "codetesting010@gmail.com"
myPassword = "testing12345@"

today = datetime.now()
today = (today.month, today.day)

data = pd.read_csv("dates.csv")

datesDict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in datesDict:
    emailPerson = datesDict[today]
    templatePath = "emailTemplates/email1.txt"
    with open(templatePath) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", emailPerson["name"])

    #smtp.gmail.com -> location of email provider smtp server
    #connection is an object
    with smtplib.SMTP("smtp.gmail.com", 587) as connection: #connect our email providers with smtp email server
        connection.starttls() #securing our connection to email server
        connection.ehlo() #identify computer
        #tls stands for transport layer security -> encrypt our email
        connection.login(user=myEmail, password=myPassword)
        connection.sendmail(
            from_addr = myEmail,
            to_addrs = emailPerson["email"],
            msg = f"Subject:Happy Birthday!\n\n{contents}"
        )