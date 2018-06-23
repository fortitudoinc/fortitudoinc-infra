#!/bin/bash

timestamp=$(date +%Y-%m-%d_%H:%M:%S)
/usr/bin/mysqldump -u root --password=$MYSQL_ROOT_PASSWORD $MYSQL_DATABASE > $timestamp.sql