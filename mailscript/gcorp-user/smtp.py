#!usr/bin/python3

import os
from mail import send_mail

token =  os.environ.get('MAILTOKEN')
send_mail('smtp.gcorp.milxc', 587, 'User<user@gcorp.milxc>', ['admin@target.milxc'],token+' Test 1 from user','Email usuel : doit être reçu\nFrom : user@gcorp.milxc\nTo : admin@target.milxc\nServeur : gcorp.milxc\nPort : 587\nMachine : gcorp.user')
send_mail('smtp.gcorp.milxc', 587, 'User<user@gcorp.milxc>', ['hacker@isp-a.milxc'],token+' Test 2 from user','Email usuel : doit être reçu\nFrom : user@gcorp.milxc\nTo : hacker@isp-a.milxc\nServeur : gcorp.milxc\nPort : 587\nMachine : gcorp.user')

print("Mails sent from gcorp-user")
