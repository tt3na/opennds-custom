#!/bin/bash

crond -n 2>&1 >/dev/null &

sed -i 's/User apache/User pi/g' /etc/httpd/conf/httpd.conf
sed -i 's/Group apache/Group pi/g' /etc/httpd/conf/httpd.conf

cat << FIN >> /etc/httpd/conf/httpd.conf

<Directory "/home/pi/web">
        Options +Indexes +FollowSymLinks +ExecCGI
	    AddHandler cgi-script .cgi 
        AllowOverride All
        Require all granted
</Directory>

NameVirtualHost *:80
<VirtualHost *:80>
    DocumentRoot /home/pi/web
</VirtualHost>
FIN

cat << FIN > /home/pi/web/.htaccess
SetEnv LDAP_SERVER $LDAP_SERVER
FIN

exec /usr/sbin/httpd -DFOREGROUND

exit 0
