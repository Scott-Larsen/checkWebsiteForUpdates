import smtplib

from config import USER, PASS, FROM_EMAIL


def sendEMail(body, email):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(USER, PASS)

    subject = f"Changes to a watched website."

    msg = f"From: {FROM_EMAIL}\r\nTo: {email}\r\nSubject: {subject}\n\n{body}"
    server.sendmail(FROM_EMAIL, email, msg)

    server.quit()