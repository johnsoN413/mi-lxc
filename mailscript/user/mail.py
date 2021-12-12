import imaplib
import smtplib
import email
from email.parser import BytesParser, Parser
from email.policy import default
from email.utils import formatdate
from email.mime.text import MIMEText


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


def receive_mails(smtpServ, login, password, list_received):
    try:
        imap = imaplib.IMAP4(host=smtpServ, port=143)
    except Exception as e:
        print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
        imap = None

    imap.login(login, password)
    imap.select('INBOX')
    status, messages = imap.search(None, "ALL")
    if messages==[b'']:
        exit()
    messages = messages[0].split(b' ')
    headers = []
    for mail in messages:
        _, msg = imap.fetch(mail, "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                headers.append(Parser(policy=default).parsestr(str(msg))["subject"])
        imap.store(mail, "+FLAGS", "\\Deleted")

    imap.expunge()
    # close the mailbox
    imap.close()
    # logout from the account
    imap.logout()
    res = ""
    for subject in list_received :
        if subject in headers :
            res += "{} : reçu\n".format(subject)
        else :
            res += "{} : non reçu\n".format(subject)
    print(res)
			
