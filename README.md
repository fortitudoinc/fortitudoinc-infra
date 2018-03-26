# Fortitudo OpenMRS Infrastructure

This repo documents the Fortitudo OpenMRS infrastructure as an ansible playbook tested against docker containers. The playbook may also be used to configure arbitrary Ubuntu servers as Fortitudo OpenMRS servers

## Dependencies
- Docker (for testing only)
- Ansible

## Usage

```bash
ansible-playbook playbook.yml --extra-vars "testing=true"
```
