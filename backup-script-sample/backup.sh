#!/usr/bin/env bash

var=$(date +"%FORMAT_STRING")
now=$(date +"%m_%d_%Y")
today=$(date +"%Y-%m-%d")
mysqldump --add-drop-table -u mysqluser -p mysqldb > /backups/${today}-name-db.sql
tar -czvf /backups/${today}-name-db.tar.gz /backups/${today}-name-db.sql
python /backups/send.py