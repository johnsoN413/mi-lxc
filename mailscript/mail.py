import imaplib
import smtplib
from email.utils import formatdate

def send_mail(smtpServ, fromaddr, toaddrs, subject, body):
    server = smtplib.SMTP()
    server.connect(smtpServ)
    server.helo() 
    msg = """\
    From: %s\r\n\
    To: %s\r\n\
    Subject: %s\r\n\
    Date: %s\r\n\
    \r\n\
    %s
    """ % (fromaddr, ", ".join(toaddrs), subject, formatdate(localtime=True), body)
    try:
        server.sendmail(fromaddr, toaddrs, msg)
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

    imap.login("hacker", "hacker")
    imap.select()
    typ, data = imap.search(None, 'ALL')
    data_idx=data[0].split()
    num=data_idx[-1];
    typ, data = imap.fetch(num, '(RFC822)')
    imap.close()
    imap.logout()
    return(data)

