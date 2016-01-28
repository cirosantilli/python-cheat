#!/usr/bin/env python

"""
Before running, setup credentials (of a throw-away test email) with:

    cp smtplib_cheat_local.py.sample smtplib_cheat_local.py

- http://stackoverflow.com/questions/6270782/sending-email-with-python
- http://stackoverflow.com/questions/10147455/trying-to-send-email-gmail-as-mail-provider-using-python
"""

import email.mime.text
import smtplib
import smtplib_cheat_local

def send_email(server_url, user, password, recipient, subject, body):
    to = recipient if type(recipient) is list else [recipient]
    tos = ', '.join(to)
    server = smtplib.SMTP(server_url, 587)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(user, password)

    #message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (user, tos, subject, body)

    msg = email.mime.text.MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = tos
    message = msg.as_string()

    server.sendmail(user, to, message)
    server.quit()

send_email(
        smtplib_cheat_local.server,
        smtplib_cheat_local.user,
        smtplib_cheat_local.password,
        smtplib_cheat_local.recipient,
        'subject0',
        'body0')
