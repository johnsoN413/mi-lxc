#!usr/bin/python3

import os
from mail import send_mail

token =  os.environ.get('MAILTOKEN')

send_mail('smtp.gcorp.milxc', 'User<user@gcorp.milxc>', ['user@gcorp.milxc'], token+' Test 1 source = user','SMTP : gcorp. user to user')
send_mail('smtp.target.milxc', 'User<user@gcorp.milxc>', ['user@gcorp.milxc'], token+' Test 2 source = user','SMTP : target. user to user')
send_mail('smtp.gcorp.milxc', 'User<user@gcorp.milxc>', ['admin@target.milxc'], token+' Test 3 source = user','SMTP : gcorp. user to admin')
send_mail('smtp.gcorp.milxc', 'Admin<admin@target.milxc>', ['user@gcorp.milxc'], token+' Test 4 source = user','SMTP : gcorp. admin to user')
send_mail('smtp.target.milxc', 'Admin<admin@target.milxc>', ['user@gcorp.milxc'], token+' Test 5 source = user','SMTP : target. admin to user')

print("Mails sent from gcorp-user")
