#!/bin/bash

username="admin"
hostname="127.0.0.1"
port="5432"
databases=("geos") # список баз данных для дампа

for dbname in "${databases[@]}"; do
    pg_dump -U "$username" -h "$hostname" -p "$port" "$dbname" > "${dbname}.sql"
done
