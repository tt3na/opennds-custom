#!/bin/bash -vx
#
# ldap.cgi
#
########################################

export LANG=ja_JP.UTF-8
export PATH=/usr/local/bin:/opt/TOOL:$PATH

homd=/home/pi
tmp=/tmp/tmp_$$

# exec 2>log.txt

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

user="$(awk '$1=="USER"{print $2}' $tmp-name)"
user_dec=$(printf '%b\n' "${user//%/\\x}")
pass="$(awk '$1=="PASSWORD"{print $2}' $tmp-name)"
pass_dec=$(printf '%b\n' "${pass//%/\\x}")

# 空判定
if [ "$user" == "" ] || [ "$pass" == "" ]; then
	code=1
else
	# LDAP認証
	ldapwhoami -x -D 'cn='"$user_dec"',ou=people,dc=ldap,dc=com' -w ''"$pass_dec"'' -H ldap://$LDAP_SERVER
	if [ $? -eq 0 ]; then
	    code=0
	else
	    code=1
	fi
fi

if [ $code -eq 0 ];then
	echo "Status: 200"
	echo "Content-type: text/html; charset=UTF-8"
	echo ""
else
	false
fi

rm -rf $tmp-name
exit 0
