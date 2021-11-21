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

echo -e "\$TTL	86400
\$ORIGIN milxc.
@  1D  IN  SOA ns.milxc. hostmaster.milxc. (
			      2002022401 ; serial
			      3H ; refresh
			      15 ; retry
			      1w ; expire
			      3h ; nxdomain ttl
			     )
       IN  NS     ns.milxc.
ns    IN  A      100.100.20.10  ;name server definition
ns	IN	AAAA	2001:db8:a020::10
target.milxc.		IN	NS	ns.target.milxc.
ns.target.milxc.	IN	A 100.80.1.2
ns.target.milxc.	IN	AAAA 2001:db8:80::1:2
isp-a.milxc.	IN	NS	ns.isp-a.milxc.
ns.isp-a.milxc.	IN	A 100.120.1.2
ns.isp-a.milxc.	IN	AAAA 2001:db8:120:1::2
mica.milxc.	IN	NS	ns.mica.milxc.
ns.mica.milxc.	IN	A 100.82.0.2
ns.mica.milxc.	IN	AAAA 2001:db8:82::2
ecorp.milxc.	IN	NS	ns.ecorp.milxc.
ns.ecorp.milxc.	IN	A 100.81.0.2
ns.ecorp.milxc.	IN	AAAA 2001:db8:81::2
gozilla.milxc.	IN	NS	ns.gozilla.milxc.
ns.gozilla.milxc.	IN	A 100.83.0.2
ns.gozilla.milxc.	IN	AAAA 2001:db8:83::2
gcorp.milxc.		IN	NS	ns.gcorp.milxc.
ns.gcorp.milxc.	IN	A 100.84.1.2
ns.gcorp.milxc.	IN	AAAA 2001:db8:84:1::2
" >> /etc/nsd/milxc.zone
