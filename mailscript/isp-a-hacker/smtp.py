#!usr/bin/python3

import os
from mail import send_mail

token =  os.environ.get('MAILTOKEN')
"""
send_mail('smtp.isp-a.milxc', 587, 'Hacker<hacker@isp-a.milxc>', ['admin@target.milxc'],token+' Test 1 from hacker','Email usuel : doit être reçu\nFrom : hacker@isp-a.milxc\nTo : admin@target.milxc\nServeur : isp-a.milxc\nPort : 587\nMachine : isp-a.hacker')
send_mail('smtp.isp-a.milxc', 587, 'Hacker<hacker@isp-a.milxc>', ['user@gcorp.milxc'],token+' Test 2 from hacker','Email usuel : doit être reçu\nFrom : hacker@isp-a.milxc\nTo : user@gcorp.milxc\nServeur : isp-a.milxc\nPort : 587\nMachine : isp-a.hacker')
send_mail('smtp.target.milxc', 587, 'Admin<admin@target.milxc>', ['user@gcorp.milxc'],token+' Test 3 from hacker','Email problématique car on essaye d\'envoyer un mail depuis target.milxc avec une adresse interne mais sur une machine externe au réseau de ce serveur. Ne doit pas être reçu.\nFrom : admin@target.milxc\nTo : user@gcorp.milxc\nServeur : target.milxc\nPort : 587\nMachine : isp-a.hacker')
"""
print("Mails sent from isp-a-hacker")
