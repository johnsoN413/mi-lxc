#!usr/bin/python3

import os
from mail import send_mail

token =  os.environ.get('MAILTOKEN')

send_mail('smtp.target.milxc', 587, 'Admin<admin@target.milxc>', ['hacker@isp-a.milxc'],token+' Test 1 from admin','Email usuel : doit être reçu\nFrom : admin@target.milxc\nTo : hacker@isp-a.milxc\nServeur: target.milxc\nMachine : target.admin')
send_mail('smtp.target.milxc', 587, 'Admin<admin@target.milxc>', ['user@gcorp.milxc'],token+' Test 2 from admin','Email usuel : doit être reçu\nFrom : admin@target.milxc\nTo : user@gcorp.milxc\nServeur utilisé : target.milxc\nMachine : target.admin')

print("Mails sent from target-admin")
