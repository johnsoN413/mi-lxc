#!usr/bin/python3

from mail import send_mail

send_mail('smtp.isp-a.milxc', 'Hacker<hacker@isp-a.milxc>', ['hacker@isp-a.milxc'],'Test 1 source = hacker','SMTP : isp-a. hacker to hacker')
send_mail('smtp.target.milxc', 'Hacker<hacker@isp-a.milxc>', ['hacker@isp-a.milxc'],'Test 2 source = hacker','SMTP : target. hacker to hacker')
send_mail('smtp.isp-a.milxc', 'Hacker<hacker@isp-a.milxc>', ['admin@target.milxc'],'Test 3 source = hacker','SMTP : isp-a. hacker to admin')
send_mail('smtp.isp-a.milxc', 'Admin<admin@target.milxc>', ['hacker@isp-a.milxc'],'Test 4 source = hacker','SMTP : isp-a. admin to hacker')
send_mail('smtp.target.milxc', 'Admin<admin@target.milxc>', ['hacker@isp-a.milxc'],'Test 5 source = hacker','SMTP : target. admin to hacker')

print("Mails sent from isp-a-hacker")
