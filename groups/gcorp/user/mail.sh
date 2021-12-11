#!/bin/sh

if [ "$#" -ne 1 ]
then
    echo "Illegal number of parameters" >&2
    exit 2
fi

if [ "$1" = "send" ]
then
    python3 /root/Documents/mi-lxc/mailscript/user/smtp.py
    exit 0
fi
if [ "$1" = "receive" ]
then
    python3 /root/Documents/mi-lxc/mailscript/user/imap.py
    exit 0
else
    echo "Expect send or receive as parameter" >&2
    exit 2
fi

