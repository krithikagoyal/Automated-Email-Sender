import smtplib

myEmail = "codetesting010@gmail.com"
myPassword = "testing12345@"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.ehlo()
connection.starttls() 
connection.login(user=myEmail, password=myPassword)
connection.sendmail(
    from_addr = myEmail,
    to_addrs = "goyalkrithika7@gmail.com",
    msg = "hello",
)
connection.close()