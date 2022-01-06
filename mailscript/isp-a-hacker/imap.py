#!/usr/bin/python3

import os
from mail import receive_mails

token =  os.environ.get('MAILTOKEN')

hacker_subjects = [token+' Test 1 source = hacker', token+' Test 2 source = hacker', token+' Test 4 source = hacker', token+' Test 5 source = hacker']

mails = receive_mails("imap.isp-a.milxc", "hacker", "hacker", hacker_subjects, "isp-a-hacker")
