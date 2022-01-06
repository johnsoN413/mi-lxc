#!/usr/bin/python3

import os
from mail import receive_mails

token =  os.environ.get('MAILTOKEN')

user_subjects = [token+' Test 1 source = user', token+' Test 2 source = user', token+' Test 4 source = user', token+' Test 5 source = user']


mails = receive_mails("imap.gcorp.milxc", "user", "user", user_subjects, "gcorp-user")
