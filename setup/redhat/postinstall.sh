#!/bin/sh

set -e

izi_CONFIGURATION_DIR=/etc/izi
izi_CONFIGURATION_FILE=$izi_CONFIGURATION_DIR/izi.conf
izi_DATA_DIR=/var/lib/izi
izi_GROUP="izi"
izi_LOG_DIR=/var/log/izi
izi_LOG_FILE=$izi_LOG_DIR/izi-server.log
izi_USER="izi"

if ! getent passwd | grep -q "^izi:"; then
    groupadd $izi_GROUP
    adduser --system --no-create-home $izi_USER -g $izi_GROUP
fi
# Register "$izi_USER" as a postgres user with "Create DB" role attribute
su - postgres -c "createuser -d -R -S $izi_USER" 2> /dev/null || true
# Configuration file
mkdir -p $izi_CONFIGURATION_DIR
# can't copy debian config-file as addons_path is not the same
if [ ! -f $izi_CONFIGURATION_FILE ]
then
    echo "[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = False
db_port = False
db_user = $izi_USER
db_password = False
addons_path = /usr/lib/python3.6/site-packages/izi/addons
" > $izi_CONFIGURATION_FILE
    chown $izi_USER:$izi_GROUP $izi_CONFIGURATION_FILE
    chmod 0640 $izi_CONFIGURATION_FILE
fi
# Log
mkdir -p $izi_LOG_DIR
chown $izi_USER:$izi_GROUP $izi_LOG_DIR
chmod 0750 $izi_LOG_DIR
# Data dir
mkdir -p $izi_DATA_DIR
chown $izi_USER:$izi_GROUP $izi_DATA_DIR

INIT_FILE=/lib/systemd/system/izi.service
touch $INIT_FILE
chmod 0700 $INIT_FILE
cat << EOF > $INIT_FILE
[Unit]
Description=izi Open Source ERP and CRM
After=network.target

[Service]
Type=simple
User=izi
Group=izi
ExecStart=/usr/bin/izi --config $izi_CONFIGURATION_FILE --logfile $izi_LOG_FILE
KillMode=mixed

[Install]
WantedBy=multi-user.target
EOF
