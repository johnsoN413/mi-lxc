#!/usr/bin/python3

from mail import receive_mails

hacker_subjects = ['Test 1 source = hacker', 'Test 2 source = hacker', 'Test 4 source = hacker', 'Test 5 source = hacker']

mails = receive_mails("imap.isp-a.milxc", "hacker", "hacker", hacker_subjects)
