#!/bin/bash

echo -n "DB root password:"
read -s password

timestamp=$(date +%Y-%m-%d_%H:%M:%S)
docker exec $1 /usr/bin/mysqldump -u root --password=$password openmrs > $timestamp.sql
