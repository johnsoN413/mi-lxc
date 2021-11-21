#!usr/bin/python3

from mail import send_mail

send_mail('smtp.isp-a.milxc', 'Hacker<hacker@isp-a.milxc>', ['hacker@isp-a.milxc'],'Test 1 source = hacker','SMTP : isp-a. hacker to hacker')
send_mail('smtp.target.milxc', 'Hacker<hacker@isp-a.milxc>', ['hacker@isp-a.milxc'],'Test 2 source = hacker','SMTP : target. hacker to hacker')
send_mail('smtp.isp-a.milxc', 'Hacker<hacker@isp-a.milxc>', ['commercial@target.milxc'],'Test 3 source = hacker','SMTP : isp-a. hacker to commercial')
send_mail('smtp.isp-a.milxc', 'Commercial<commercial@target.milxc>', ['hacker@isp-a.milxc'],'Test 4 source = hacker','SMTP : isp-a. commercial to hacker')
