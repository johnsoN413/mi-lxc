#!/bin/bash
# milxc
set -e
if [ -z $MILXCGUARD ] ; then exit 1; fi
DIR=`dirname $0`
cd `dirname $0`

cp dns.conf /etc/nsd/milxc.zone