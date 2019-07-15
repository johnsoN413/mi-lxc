#!/bin/bash
# ldapclient template
set -e
if [ -z $MILXCGUARD ] ; then exit 1; fi
DIR=`dirname $0`
cd `dirname $0`

IFS='.'
dn=""
for i in $domain; do
  dn="$dn, dc=$i"
done
dn=`echo $dn | cut -c3- -`
#echo $dn


# LDAP client
apt-get update
#cp ldap.seed /tmp/
#sed -i -e "s/\$server/$server/" /tmp/ldap.seed

echo -e "libnss-ldap	shared/ldapns/base-dn	string	$dn
libpam-ldap	shared/ldapns/base-dn	string	$dn
libnss-ldap	shared/ldapns/ldap-server	string	ldap://$server/
libpam-ldap	shared/ldapns/ldap-server	string	ldap://$server/" | debconf-set-selections

DEBIAN_FRONTEND=noninteractive apt-get install -y libnss-ldap libpam-ldap
sed -i -e 's/compat/compat ldap/' /etc/nsswitch.conf
