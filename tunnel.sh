#!/usr/bin/env bash

# Tunnel into a remote Postgres instance behind a firewall.

ssh-add ${SSH_CERT_PATH}
ssh -i ${SSH_CERT_PATH} -L 5432:${POSTGRES_HOST} ${JUMP_USER}@${JUMP_SERVER} -N
