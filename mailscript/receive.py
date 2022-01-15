#!/usr/bin/python3

import imaplib
import smtplib
import email
from email.parser import BytesParser, Parser
from email.policy import default
from email.utils import formatdate
from email.mime.text import MIMEText
import time
import sys
import json

def render_dic(dic) :
    res = ""
    for key in dic.keys() :
        res = res+key+" : "+str(dic[key])+"\n"
    return res[:-1]

mailSent = json.loads(sys.argv[1])

received = False

dic_logs = {
    "admin@target.milxc":["admin","admin"],
    "hacker@isp-a.milxc":["hacker","hacker"], 
    "user@gcorp.milxc":["user","user"]
}

try:
    imap = imaplib.IMAP4(host="imap."+mailSent["To"].split("@")[1], port=143)
except Exception as e:
    print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
    imap = None

imap.login(dic_logs[mailSent["To"]][0], dic_logs[mailSent["To"]][1])
imap.select('INBOX')
t = time.time()

while (not received) and (time.time()-t)<30 :
        
    status, messages = imap.search(None, "ALL")
    messages = messages[0].split(b' ')
    
    for mail in messages:
        try :
            _, msg = imap.fetch(mail, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject = Parser(policy=default).parsestr(str(msg))["subject"]
                    if subject == mailSent["Subject"] :
                        received = True
                        imap.store(mail, "+FLAGS", "\\Deleted")
        except imaplib.IMAP4.error:
            pass
imap.expunge()
# close the mailbox
imap.close()
# logout from the account
imap.logout()
test_succeded = received == mailSent["ShouldPass"]
if test_succeded :
    res = "V"
else :
    res = "X"
if received :
    print("----------------------\n"+res+" RECU :\n{}".format(render_dic(mailSent)))
else :
    print("----------------------\n"+res+" NON RECU :\n{}".format(render_dic(mailSent)))


			
