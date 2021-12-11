import imaplib
import smtplib
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


def receive_mails(smtpServ, login, password):
    try:
        imap = imaplib.IMAP4(host="imap.isp-a.milxc", port=143)
    except Exception as e:
        print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
        imap = None

    imap.login("user", "user")
    imap.select()
    typ, data = imap.search(None, 'ALL')
    data_idx=data[0].split()
    num=data_idx[-1];
    typ, data = imap.fetch(num, '(RFC822)')
    imap.close()
    imap.logout()
    return(data)

