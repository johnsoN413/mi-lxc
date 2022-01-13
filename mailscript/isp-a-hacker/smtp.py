#!usr/bin/python3

import os
from mail import send_mail

token =  os.environ.get('MAILTOKEN')

send_mail('smtp.isp-a.milxc', 587, 'Hacker<hacker@isp-a.milxc>', ['admin@target.milxc'],token+' Test 1 from hacker','Email usuel : doit être reçu\nFrom : hacker@isp-a.milxc\nTo : admin@target.milxc\nServeur: isp-a.milxc\nMachine : isp-a.hacker')
send_mail('smtp.isp-a.milxc', 587, 'Hacker<hacker@isp-a.milxc>', ['user@gcorp.milxc'],token+' Test 2 from hacker','Email usuel : doit être reçu\nFrom : hacker@isp-a.milxc\nTo : user@gcorp.milxc\nServeur utilisé : isp-a.milxc\nMachine : isp-a.hacker')

print("Mails sent from isp-a-hacker")
