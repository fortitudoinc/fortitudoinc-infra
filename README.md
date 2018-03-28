# Fortitudo OpenMRS Infrastructure

[![Build Status](https://travis-ci.org/fortitudoinc/fortitudoinc-ansible.svg?branch=master)](https://travis-ci.org/fortitudoinc/fortitudoinc-ansible)

This repo documents the Fortitudo OpenMRS infrastructure as an ansible playbook testable against docker containers. The playbook may also be used to configure arbitrary Ubuntu servers as Fortitudo OpenMRS servers by changing the inventory.

## Dependencies
- Docker (for testing only)
- Ansible

## Setup

For the testing build, docker and ansible will attempt to use keys in the `ssh-keys/` directory. Before testing, generate keys with the following command:

```bash
ssh-keygen -f ssh-keys/id_rsa -t rsa -N ''
```

## Usage

If testing, first start the docker containers:
```bash
docker-compose up --build
```
Then run ansible:
```bash
ansible-playbook playbook.yml -i inventory-local.ini
```
