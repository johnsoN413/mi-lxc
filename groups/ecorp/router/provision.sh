#!/bin/sh

set -e
if [ -z $MILXCGUARD ] ; then exit 1; fi
DIR=`dirname $0`
cd `dirname $0`

cat unbound.conf >> /etc/unbound/unbound.conf

