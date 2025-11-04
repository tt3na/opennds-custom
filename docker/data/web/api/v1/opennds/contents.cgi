#!/bin/bash -vx
#
# contents.cgi
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

if [ -n "$QUERY_STRING" ];then
	sed 's/&/\n/g' <<< $QUERY_STRING	| 
	sed 's/=/ /g'				|
	nkf -w --url-input > $tmp-name
else
	: > $tmp-name
fi

case=$(awk '$1=="case"{print $2}' $tmp-name)

echo "Content-type: text/html; charset=UTF-8"
echo ""
case "$case" in
	"0")
		cat <<- FIN
		<div class="rules">
			<ul style="margin-top:10px;margin-bottom:20px;">
				<li>12時間ごとにログインし直す必要があります</li>
				<li>いたずらしないこと</li>
			</ul>
		</div>
		FIN
	;;
	"1")
		cat <<- FIN
		<p style="text-align:center;">おめでとうございます！ <br/> インターネットに接続されました！</p>
		FIN
	;;
	"2")
		cat <<- FIN
		<p style="text-align:center;color:deeppink;">認証に失敗しました</p>
		FIN
	;;
esac

rm -rf $tmp-name
exit 0
