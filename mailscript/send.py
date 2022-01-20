#!/usr/bin/python3

import imaplib
import smtplib
import email
from email.parser import BytesParser, Parser
from email.policy import default
from email.utils import formatdate
from email.mime.text import MIMEText
import sys 
import json

server = smtplib.SMTP()
mails = json.loads(sys.argv[1])

for mail in mails :
    try :
        server.connect(mail["Server"], mail["ServerPort"])
    except ConnectionRefusedError :
        if mail["ServerPort"]==587 :
            print("----------------------\n\033[30;41mConnexion à {} refusée, avez-vous activé le port 587 ?\033[0m".format(mail["Server"]))
            exit(0)
        print("----------------------\n\033[30;41mConnexion à {} refusée.\033[0m".format(mail["Server"]))
        exit(1)

    server.helo() 
    msg = MIMEText(mail["Body"])
    msg['Subject'] = mail["Subject"]
    msg['From'] = mail["From"]
    msg['To'] = mail["To"]

    try:
        server.sendmail(mail["From"], mail["To"], msg.as_string())
    except smtplib.SMTPException as e:
        print("----------------------\n\033[30;41mEnvoi du mail '{}' refusé depuis {}\033[0m".format(mail["Subject"], mail["Container"]))
        print(e)

server.quit()
