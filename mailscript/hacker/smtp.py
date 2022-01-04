#!usr/bin/python3

from mail import send_mail

send_mail('smtp.isp-a.milxc', 'Hacker<hacker@isp-a.milxc>', ['hacker@isp-a.milxc'],'Test 1 source = hacker','SMTP : isp-a. hacker to hacker')
send_mail('smtp.target.milxc', 'Hacker<hacker@isp-a.milxc>', ['hacker@isp-a.milxc'],'Test 2 source = hacker','SMTP : target. hacker to hacker')
send_mail('smtp.isp-a.milxc', 'Hacker<hacker@isp-a.milxc>', ['admin@target.milxc'],'Test 3 source = hacker','SMTP : isp-a. hacker to admin')
send_mail('smtp.isp-a.milxc', 'Hacker<admin@target.milxc>', ['hacker@isp-a.milxc'],'Test 4 source = hacker','SMTP : isp-a. admin to hacker')
send_mail('smtp.target.milxc', 'Hacker<admin@target.milxc>', ['hacker@isp-a.milxc'],'Test 5 source = hacker','SMTP : target. admin to hacker')
send_mail('smtp.target.milxc', 'Hacker<admin@target.milxc>', ['admin@target.milxc'],'Test 6 source = hacker','SMTP : target. admin to admin')
send_mail('smtp.isp-a.milxc', 'Hacker<admin@target.milxc>', ['user@gcorp.milxc'],'Test 7 source = hacker','SMTP : target. admin to user')

