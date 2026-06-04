#!/bin/bash
set -e

export POSTGRES_USER=$(cat /run/secrets/db_user)
export POSTGRES_PASSWORD=$(cat /run/secrets/db_password)
export POSTGRES_DB=$(cat /run/secrets/db_name)

exec docker-entrypoint.sh postgres