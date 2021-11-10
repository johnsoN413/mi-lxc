#!/bin/bash
# Ecorp infra
set -e
if [ -z $MILXCGUARD ] ; then exit 1; fi
DIR=`dirname $0`
cd `dirname $0`

DEBIAN_FRONTEND=noninteractive apt-get install -y certbot python3-certbot-apache

# Hacker's mail account hacker@isp-a.milxc
useradd -m -s "/bin/bash" -p `mkpasswd --method=sha-512 admin` admin || true
addgroup admin mail
#mkdir /home/hacker/mail
#touch /home/hacker/mail/Drafts /home/hacker/mail/Queue /home/hacker/mail/Sent /home/hacker/mail/Trash

# disable systemd-resolved which conflicts with nsd
echo "DNSStubListener=no" >> /etc/systemd/resolved.conf
systemctl stop systemd-resolved

# manage isp-a.milxc zone
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y nsd

# DNS server
echo -e "zone:
	name: \"ecorp.milxc.\"
	zonefile: \"ecorp.milxc.zone\"
" > /etc/nsd/nsd.conf

cp dns.conf /etc/nsd/ecorp.milxc.zone


cp index.html /var/www/html/
ln -s /var/www/html/index.html /var/www/html/doku.php
a2enmod headers
echo "RequestHeader unset If-Modified-Since" >> /etc/apache2/apache2.conf

# preconfig TLS and certbot
a2enmod ssl
a2ensite default-ssl.conf
echo -e "
email=admin@target.milxc
agree-tos=1
no-verify-ssl=1
" >> /etc/letsencrypt/cli.ini
