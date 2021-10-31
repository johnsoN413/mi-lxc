#!/bin/bash
# Gozilla infra
set -e
if [ -z $MILXCGUARD ] ; then exit 1; fi
DIR=`dirname $0`
cd `dirname $0`

# disable systemd-resolved which conflicts with nsd
echo "DNSStubListener=no" >> /etc/systemd/resolved.conf
systemctl stop systemd-resolved

# manage gozilla.milxc zone
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y nsd 

# DNS server
echo -e "zone:
	name: \"gozilla.milxc.\"
	zonefile: \"gozilla.milxc.zone\"
" > /etc/nsd/nsd.conf

# cp dns.conf /etc/unbound/unbound.conf.d/
cp dns.conf /etc/nsd/gozilla.milxc.zone


# Script to add a cert to the CA/Browser consortium
cp addcatofox.sh /usr/local/bin
chmod a+x /usr/local/bin/addcatofox.sh
