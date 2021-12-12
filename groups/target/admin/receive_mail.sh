#!/bin/sh


###Can(should ?) be improved !  The path is the one in the lxc container

echo "------------------------------"
echo "Mails received to isp-a-admin"
python3 /mnt/lxc/mailscript/admin/imap.py


