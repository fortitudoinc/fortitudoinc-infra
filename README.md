# Fortitudo OpenMRS Infrastructure

This repo documents the Fortitudo OpenMRS infrastructure as an ansible playbook tested on a vagrant vm. The playbook may also be used to configure arbitrary Ubuntu servers as Fortitudo OpenMRS servers

## Dependencies
- Vagrant
- Ansible

## Usage

First-time:
```bash
vagant up --provision
```

To reset and test from a clean state:
```bash
vagrant destroy
vagrant up --provision
```