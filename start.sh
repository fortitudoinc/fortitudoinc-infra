#!/bin/bash
# A sample startup script

# replace this .env with a path to your .env
source environments/production.env

# replace with the appropriate .yml if not using load-db configuration
docker-compose -f load-db.yml up -d --build