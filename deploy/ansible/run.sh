#!/usr/bin/env bash

ansible-galaxy role install -r requirements.yml
ansible-playbook pb_deploy.yml --ask-vault-pass