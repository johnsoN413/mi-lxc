#!/usr/bin/python3

from mail import receive_mails

user_subjects = ['Test 1 source = user', 'Test 2 source = user', 'Test 4 source = user', 'Test 5 source = user']

print("-----------------------------")
print("Mails received to gcorp-user :")

mails = receive_mails("imap.gcorp.milxc", "user", "user", user_subjects)
