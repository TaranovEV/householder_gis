#!/bin/bash

docker compose -f ./docker-compose-dev.yml build
docker compose -f ./docker-compose-dev.yml up -d --remove-orphans

#docker exec -it geo_backend python ./manage.py collectstatic --noinput --clear
