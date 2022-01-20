#!/usr/bin/python3

import time
import json
import sys

dic_ip = {"100.120.1.2":"smtp.isp-a.milxc", "100.84.1.2":"smtp.gcorp.milxc","100.80.1.2":"smtp.target.milxc","100.120.0.4":"isp-a-hacker","100.84.0.2":"gcorp-user","100.80.0.4":"target-admin"}

def parse_log(log) :
    message = " ".join(log.split(" ")[4:])
    adfrom = ""
    adto = ""
    server = ""
    if message.split(": ")[1] == "NOQUEUE" :
        adfrom = message.split("from=")[1].split(" ")[0]
        adto = message.split("to=")[1].split(" ")[0]
        server = dic_ip[message.split("RCPT from unknown[")[1].split("]")[0]]
    if len(message.split(" Please see"))==2 :
        message = message.split(" Please see")[0]
    return [message, adfrom, adto, server]

def is_log_error(mail) :
    with open("/var/log/mail.log", "r") as f :
        logs = f.readlines()[-50 : ]
        for log in logs :
            log = parse_log(log)
            if "<"+mail["From"].split("<")[1] == log[1] and "<"+mail["To"]+">"==log[2] and (mail["Server"]==log[3] or mail["Container"]==log[3]) :
                return [True, log[0]]
        return [False, ""]

mails = json.loads(sys.argv[1])
t = time.time()
dic_mails = {}
for mail in mails :
    dic_mails[mail["Subject"]] = False

while (time.time()-t)<30 :
    for mail in mails :
        if not dic_mails[mail["Subject"]] :
            er = is_log_error(mail)
            if er[0] :
                print("----------------------\n\033[30;41mRéception du mail {} pour {} refusée\033[0m".format(mail["Subject"], mail["To"]))
                print(er[1])
                dic_mails[mail["Subject"]] = True
