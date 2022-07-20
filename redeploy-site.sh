#!/bin/bash

# change to project folder
cd ~/Fellowship-Portfolio
# git update
git fetch && git reset origin/main --hard
# spin containers down
docker compose -f docker-compose.prod.yml down
# spin containers up
docker compose -f docker-compose.prod.yml up -d --build
