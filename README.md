# Fortitudo OpenMRS Infrastructure

[![Build Status](https://travis-ci.org/fortitudoinc/fortitudoinc-ansible.svg?branch=master)](https://travis-ci.org/fortitudoinc/fortitudoinc-ansible)

This repo documents the Fortitudo OpenMRS infrastructure as an ansible playbook testable against vagrant vms. The playbook may also be used to configure arbitrary Ubuntu servers as Fortitudo OpenMRS servers by changing the inventory.

## Requirements
- Vagrant w/4GB RAM allocatable to VMs (for testing only)
- Ansible

## Usage (local testing)

First run:
```bash
vagrant up --provision
```

Reset:
```bash
vagrant destroy
vagrant up --provision
```

## Usage (remote deployment)

Create an inventory file (use inventory-example.yml as a guide) and run:

```bash
ansible-playbook playbook.yml -i your-inventory.yml
```

Or use an encrypted inventory:

```bash
ansible-playbook playbook.yml -i inventory-staging.yml --ask-vault-pass
```

