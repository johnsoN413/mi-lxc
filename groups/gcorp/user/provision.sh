#!/bin/bash
# Gcorp user
set -e
if [ -z $MILXCGUARD ] ; then exit 1; fi
DIR=`dirname $0`
cd `dirname $0`

# systemctl set-default graphical.target

apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y python3
DEBIAN_FRONTEND=noninteractive apt-get install -y python3-requests


#cp -ar homedir/* /home/debian/
#ln -sf /home/debian/background.jpg /usr/share/images/desktop-base/default
#ln -sf /home/debian/background.jpg /etc/alternatives/desktop-background


