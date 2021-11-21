#!/bin/bash
# Gcorp infra
set -e
if [ -z $MILXCGUARD ] ; then exit 1; fi
DIR=`dirname $0`
cd `dirname $0`

# Home's mail account home@gcorp.milxc
useradd -m -s "/bin/bash" -p `mkpasswd --method=sha-512 home` home || true
addgroup home mail

# disable systemd-resolved which conflicts with nsd
echo "DNSStubListener=no" >> /etc/systemd/resolved.conf
systemctl stop systemd-resolved

# manage gcorp.milxc zone
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y nsd
cp dns.conf /etc/nsd/gcorp.milxc.zone


