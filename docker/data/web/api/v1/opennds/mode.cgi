#!/bin/bash -vx
#
# mode.cgi
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
    exit 0
}

trap ERROR_HANDLER err
set -o pipefail

mode=$(cat $homd/.apmode)

if [ -n "$QUERY_STRING" ];then
	sed 's/&/\n/g' <<< $QUERY_STRING	| 
	sed 's/=/ /g'				|
	nkf -w --url-input > $tmp-name
else
	: > $tmp-name
fi

echo "Status: 200"
echo "Content-type: text/html; charset=UTF-8"
echo ""
echo "$mode"

rm -rf $tmp-name
exit 0
