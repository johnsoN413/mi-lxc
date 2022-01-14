#!/usr/bin/python3

import os
from mail import receive_mails

token =  os.environ.get('MAILTOKEN')

user_messages = [[token+' Test 2 from hacker','Email usuel : doit être reçu\nFrom : hacker@isp-a.milxc\nTo : user@gcorp.milxc\nServeur : isp-a.milxc\nPort : 587\nMachine : isp-a.hacker',False],
                [token+' Test 2 from admin','Email usuel : doit être reçu\nFrom : admin@target.milxc\nTo : user@gcorp.milxc\nServeur : target.milxc\nPort : 587\nMachine : target.admin',False],
                [token+' Test 3 from admin','Email problématique car on essaye d\'envoyer un mail depuis l\'extérieur de target.milxc en passant par ce serveur. Ne doit pas être reçu.\nFrom : hacker@isp-a.milxc\nTo : user@gcorp.milxc\nServeur : target.milxc\nPort : 587\nMachine : target.admin',True],
                [token+' Test 3 from hacker','Email problématique car on essaye d\'envoyer un mail depuis target.milxc avec une adresse interne mais sur une machine externe au réseau de ce serveur. Ne doit pas être reçu.\nFrom : admin@target.milxc\nTo : user@gcorp.milxc\nServeur : target.milxc\nPort : 587\nMachine : isp-a.hacker',True],
                [token+ " Test 4 from hacker","Email problématique car on essaye d'usurper l'adresse d'Admin. Ne doit pas être reçu.\nFrom : admin@target.milxc\nTo : user@gcorp.milxc\nServeur : isp-a.milxc\nPort : 587\nMachine : isp-a.hacker", True],
                [token+" Test 5 from hacker","Email problématique car on essaye de se connecter directement depuis Hacker sur le port 25 du serveur smtp de target. Ne doit pas être reçu.\nFrom : admin@target.milxc\nTo : user@gcorp.milxc\nServeur : isp-a.milxc\nPort : 587\nMachine : isp-a.hacker", True]
                ]

mails = receive_mails("imap.gcorp.milxc", "user", "user", user_messages, "gcorp-user")
