#!/bin/sh

###Can(should ?) be improved !  The path is the one in the lxc container
python3 /mnt/lxc/mailscript/user/smtp.py
echo "Mails sent from gcorp-user"
