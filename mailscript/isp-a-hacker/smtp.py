#!usr/bin/python3

import os
from mail import send_mail

token =  os.environ.get('MAILTOKEN')

send_mail('smtp.isp-a.milxc', 'Hacker<hacker@isp-a.milxc>', ['hacker@isp-a.milxc'],token+' Test 1 source = hacker','SMTP : isp-a. hacker to hacker')
send_mail('smtp.target.milxc', 'Hacker<hacker@isp-a.milxc>', ['hacker@isp-a.milxc'],token+' Test 2 source = hacker','SMTP : target. hacker to hacker')
send_mail('smtp.isp-a.milxc', 'Hacker<hacker@isp-a.milxc>', ['admin@target.milxc'],token+' Test 3 source = hacker','SMTP : isp-a. hacker to admin')
send_mail('smtp.isp-a.milxc', 'Admin<admin@target.milxc>', ['hacker@isp-a.milxc'],token+' Test 4 source = hacker','SMTP : isp-a. admin to hacker')
send_mail('smtp.target.milxc', 'Admin<admin@target.milxc>', ['hacker@isp-a.milxc'],token+' Test 5 source = hacker','SMTP : target. admin to hacker')

print("Mails sent from isp-a-hacker")
