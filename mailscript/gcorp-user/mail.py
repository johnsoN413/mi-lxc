import imaplib
import smtplib
import email
from email.parser import BytesParser, Parser
from email.policy import default
from email.utils import formatdate
from email.mime.text import MIMEText
import time



def checked(dic) :
    for value in dic.values() :
        if not value :
            return False
    return True


def send_mail(smtpServ, fromaddr, toaddrs, subject, body):
    server = smtplib.SMTP()
    server.connect(smtpServ)
    server.helo() 
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = fromaddr
    msg['To'] = ", ".join(toaddrs)
    try:
        server.sendmail(fromaddr, toaddrs, msg.as_string())
    except smtplib.SMTPException as e:
        print(e)
    server.quit()
    return


def receive_mails(smtpServ, login, password, list_received, dst):
    dic_received = {}
    for key in list_received :
        dic_received[key] = False
    try:
        imap = imaplib.IMAP4(host=smtpServ, port=143)
    except Exception as e:
        print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
        imap = None

    imap.login(login, password)
    imap.select('INBOX')
    t = time.time()
    while (not checked(dic_received)) and (time.time()-t)<30 :
        
        status, messages = imap.search(None, "ALL")
        messages = messages[0].split(b' ')
        
        for mail in messages:
            _, msg = imap.fetch(mail, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    headers = Parser(policy=default).parsestr(str(msg))["subject"]
                    if headers in dic_received :
                        dic_received[headers] = True
            imap.store(mail, "+FLAGS", "\\Deleted")
    imap.expunge()
    # close the mailbox
    imap.close()
    # logout from the account
    imap.logout()
    res = "----------------------\nMails received by {} :\n".format(dst)
    for key in dic_received.keys() :
        if dic_received[key] :
            res += "{} : reçu\n".format(key)
        else :
            res += "{} : non reçu\n".format(key)
    print(res)
			
