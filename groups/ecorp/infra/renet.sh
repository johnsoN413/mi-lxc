#!/bin/bash
# Target DMZ
set -e
if [ -z $MILXCGUARD ] ; then exit 1; fi
DIR=`dirname $0`
cd `dirname $0`

cp dns-ecorp.conf /etc/nsd/ecorp.milxc.zone
cp dns-target.conf /etc/nsd/target.milxc.zone
