#!/bin/bash
# .milxc registry

set -e
if [ -z $MILXCGUARD ] ; then exit 1; fi
DIR=`dirname $0`
cd `dirname $0`

# disable systemd-resolved which conflicts with nsd
echo "DNSStubListener=no" >> /etc/systemd/resolved.conf
systemctl stop systemd-resolved

apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y nsd

echo -e "zone:
	name: \"milxc.\"
	zonefile: \"milxc.zone\"
" > /etc/nsd/nsd.conf

cp dns.conf /etc/nsd/milxc.zone
