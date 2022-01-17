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

dic_logs = {
    "admin@target.milxc":["admin","admin"],
    "hacker@isp-a.milxc":["hacker","hacker"], 
    "user@gcorp.milxc":["user","user"]
}

mailsSent = json.loads(sys.argv[1])

for mailSent in mailsSent :

    received = False

    try:
        imap = imaplib.IMAP4(host="imap."+mailSent["To"].split("@")[1], port=143)
    except Exception :
        print("\033[30;41mFailure, maybe wait a few seconds and retry while the mailservers are starting.\033[0m")
        imap = None
        exit(1)

    try :
        imap.login(dic_logs[mailSent["To"]][0], dic_logs[mailSent["To"]][1])
    except imaplib.IMAP4.error :
        print("\033[30;41mCould not login to {}.\033[0m".format(mailSent["To"]))
        exit(1)
    
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
        color = "\033[92m"
    else :
        res = "X"
        color = "\033[31m"
    if received :
        print("----------------------\n"+color+res+" RECU :\n{}\033[0m".format(render_dic(mailSent)))
    else :
        print("----------------------\n"+color+res+" NON RECU :\n{}\033[0m".format(render_dic(mailSent)))


			
