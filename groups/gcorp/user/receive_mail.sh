#!/bin/sh


###Can(should ?) be improved !  The path is the one in the lxc container

echo "------------------------------"
echo "Mails received to gcorp-user :"
python3 /mnt/lxc/mailscript/user/imap.py

