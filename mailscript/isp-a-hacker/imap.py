#!/usr/bin/python3

import os
from mail import receive_mails

token =  os.environ.get('MAILTOKEN')

hacker_messages = [[token+' Test 2 from user','Email usuel : doit être reçu\nFrom : user@gcorp.milxc\nTo : hacker@isp-a.milxc\nServeur : gcorp.milxc\nPort : 587\nMachine : gcorp.user',False],
[token+' Test 1 from admin','Email usuel : doit être reçu\nFrom : admin@target.milxc\nTo : hacker@isp-a.milxc\nServeur: target.milxc\nPort : 587\nMachine : target.admin',False]]

mails = receive_mails("imap.isp-a.milxc", "hacker", "hacker", hacker_messages, "isp-a-hacker")
