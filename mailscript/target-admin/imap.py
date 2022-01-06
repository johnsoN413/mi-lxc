#!/usr/bin/python3

import os
from mail import receive_mails

token =  os.environ.get('MAILTOKEN')

admin_subjects = [token+' Test 3 source = hacker', token+' Test 3 source = user']

mails = receive_mails("imap.target.milxc", "admin", "admin", admin_subjects, "isp-a-admin")
