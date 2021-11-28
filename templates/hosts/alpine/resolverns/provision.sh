#!/bin/sh
# Root NS template
set -e
if [ -z $MILXCGUARD ] ; then exit 1; fi
DIR=`dirname $0`
cd `dirname $0`

apk update
apk add unbound bind-tools

# get root hints
#wget "http://www.internic.net/domain/named.root" -O /etc/unbound/root.hints
echo -e ".                        3600000      NS    O.ROOT-SERVERS.NET.
O.ROOT-SERVERS.NET.      3600000      A     100.100.0.10
O.ROOT-SERVERS.NET.      3600000      AAAA     2001:db8:a000::10
.												3600000      NS    P.ROOT-SERVERS.NET.
P.ROOT-SERVERS.NET.      3600000      A     100.100.1.10
P.ROOT-SERVERS.NET.      3600000      AAAA     2001:db8:a001::10
" > /etc/unbound/root.hints

# customize unbound config
#echo -e "server:
#	ip-address: 127.0.0.1
echo -e "server:
	root-hints: /etc/unbound/root.hints
	interface: 0.0.0.0
    access-control: 0.0.0.0/0 allow
	cache-max-ttl: 20
	cache-max-negative-ttl: 20
" > /etc/unbound/unbound.conf

service unbound restart
