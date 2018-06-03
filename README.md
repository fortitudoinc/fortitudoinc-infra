# Fortitudo OpenMRS Infrastructure

[![Build Status](https://travis-ci.org/fortitudoinc/fortitudoinc-infra.svg?branch=master)](https://travis-ci.org/fortitudoinc/fortitudoinc-infra)

This repo contains the Fortitudo OpenMRS docker deployment

## Overview

The software stack consists of three docker containers: an nginx TLS proxy (with TLS certificates managed by letsencypt), a tomcat server with OpenMRS reference application installed, and a MySLQ 5.6 database backend.

![software stack](stack.png)

## Requirements
- docker
- docker-compose

## Usage

Testing:
```bash
cd fortitudoinc-infra
source example.env
docker-compose up -d
```

## Options

See `example-new-db.env` or `example-saved-db.env` for an example configuration for a new database or a saved database, respectively.

### MySQL Options
- MYSQL_ROOT_PASSWORD: password for the root user of the mysql 5.6 database
- MYSQL_DATABASE: A database to setup when creating the mysql container

### OpenMRS Options
- DB_DATABASE: The database used
- DB_USERNAME: The username used to connect to the database container
- DB_PASSWORD: The password used  to connect to the database container
- DB_CREATE_TABLES: (`true`/`false`) Whether new tables should be created or existing ones used
- MODULE_WEB_ADMIN: (`true`/`false`) Whether to allow modules to be uploaded via the web interface
- OPENMRS_ADMIN_PASSWORD: Administrative password (must be a combination of upper case, lower case, and digits)

### Nginx Options
- URL: The FQDN to use for the TLS certificate
- STAGING: (`true`/`false`)
    - If true: will use a non-valid certificate, but will not be rate-limited by letsencrypt service (use this option for testing)
    - If false: will use a valid certificate, but will be rate-limited by letsencrypt (use this option for production deployments)
- TZ: optional time zone
- EMAIL: an email address for the server administrator (for letsencrypt security notices, etc.)