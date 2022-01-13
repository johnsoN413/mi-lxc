#!/usr/bin/python3

import os
from mail import receive_mails

token =  os.environ.get('MAILTOKEN')

admin_messages = [[token+' Test 1 from hacker','Email usuel : doit être reçu\nFrom : hacker@isp-a.milxc\nTo : admin@target.milxc\nServeur: isp-a.milxc\nMachine : isp-a.hacker',False],
[token+' Test 1 from user','Email usuel : doit être reçu\nFrom : user@gcorp.milxc\nTo : admin@target.milxc\nServeur : gcorp.milxc\nMachine : gcorp.user',False]]

mails = receive_mails("imap.target.milxc", "admin", "admin", admin_messages, "isp-a-admin")
