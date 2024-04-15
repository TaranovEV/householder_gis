#!/bin/bash


docker compose -f ./docker-compose-dev.yml build drf-test
docker compose -f ./docker-compose-dev.yml run drf-test pytest
