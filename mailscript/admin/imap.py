#!/usr/bin/python3

from mail import receive_mails

admin_subjects = ['Test 3 source = hacker', 'Test 3 source = user','Test 6 source = hacker']

mails = receive_mails("imap.target.milxc", "admin", "admin", admin_subjects)
