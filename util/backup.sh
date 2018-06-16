#!/bin/bash

preserve=30  # By default save last 30 days of daily backups
timestamp=$(date +%Y-%m-%d_%H:%M:%S)
/usr/bin/mysqldump -u root --password=$MYSQL_ROOT_PASSWORD $MYSQL_DATABASE > /backups/$timestamp.sql

while [ $(ls -1q /backups/ | wc -l) -gt $preserve ]; do
    rm /backups/$(ls -t /backups/ | tail -1)
done
