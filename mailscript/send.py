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
mail = json.loads(sys.argv[1])


try :
    server.connect(mail["Server"], mail["ServerPort"])
except ConnectionRefusedError :
    print("Connexion refusée, essayez d'activer le port 587")
    exit(1)

server.helo() 
msg = MIMEText(mail["Body"])
msg['Subject'] = mail["Subject"]
msg['From'] = mail["From"]
msg['To'] = mail["To"]

try:
    server.sendmail(mail["From"], mail["To"], msg.as_string())
except smtplib.SMTPException as e:
    print(e)

server.quit()
