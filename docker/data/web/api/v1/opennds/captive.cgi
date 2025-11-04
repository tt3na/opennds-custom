#!/bin/bash -vx
#
# captive.cgi
#
########################################

export LANG=ja_JP.UTF-8
export PATH=/usr/local/bin:/opt/TOOL:$PATH

homd=/home/pi
tmp=/tmp/tmp_$$

ERROR_HANDLER(){
    echo "Status: 403"
    echo "Content-type: text/html; charset=UTF-8"
    echo ""
    rm -rf $tmp-name
    exit 0
}

trap ERROR_HANDLER err
set -o pipefail

if [ -n "$QUERY_STRING" ];then
	sed 's/&/\n/g' <<< $QUERY_STRING	| 
	sed 's/=/ /g'				|
	nkf -w --url-input > $tmp-name
else
	: > $tmp-name
fi

token=$(awk '$1=="token"{print $2}' $tmp-name)

if [ "$token" == "$(date +%Y%m%d370)" -o "$token" == "$(cat $homd/.appass)" ];then
	echo "Status: 200"
	echo "Content-type: text/html; charset=UTF-8"
	echo ""
else
	false
fi

rm -rf $tmp-name
exit 0
