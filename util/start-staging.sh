#!/bin/bash
# Runs all services but 

# replace this .env with a path to your .env
source environments/staging-reuse-db.env

# replace with the appropriate .yml if not using load-db configuration
docker-compose up --build -d db refapp