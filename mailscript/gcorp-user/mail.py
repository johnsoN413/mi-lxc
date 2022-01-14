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
        if not value[1] :
            return False
    return True


def send_mail(smtpServ, port, fromaddr, toaddrs, subject, body):
    server = smtplib.SMTP()
    server.connect(smtpServ, port)
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
        dic_received[key[0]] = [key[1], False, key[2]]
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
                        dic_received[headers][1] = True
            imap.store(mail, "+FLAGS", "\\Deleted")
    imap.expunge()
    # close the mailbox
    imap.close()
    # logout from the account
    imap.logout()
    for key in dic_received.keys() :
        dic_received[key][2] = dic_received[key][1] ^ dic_received[key][2]
        res = ""
        if dic_received[key][2] :
            res = "V"
        else :
            res = "X"
        if dic_received[key][1] :
            print("----------------------\n"+res+" RECU :\n{}".format(dic_received[key][0]))
        else :
            print("----------------------\n"+res+" NON RECU :\n{}".format(dic_received[key][0]))
			
