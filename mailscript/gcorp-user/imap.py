#!/usr/bin/python3

import os
from mail import receive_mails

token =  os.environ.get('MAILTOKEN')

user_messages = [[token+' Test 2 from hacker','Email usuel : doit être reçu\nFrom : hacker@isp-a.milxc\nTo : user@gcorp.milxc\nServeur utilisé : isp-a.milxc\nMachine : isp-a.hacker',False],
[token+' Test 2 from admin','Email usuel : doit être reçu\nFrom : admin@target.milxc\nTo : user@gcorp.milxc\nServeur utilisé : target.milxc\nMachine : target.admin',False]]


mails = receive_mails("imap.gcorp.milxc", "user", "user", user_messages, "gcorp-user")
