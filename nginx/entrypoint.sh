#!/bin/bash
set -eu

envsubst '${SERVER_NAME} ${SERVER_PORT}' < /etc/nginx/conf.d/local.conf.template > /etc/nginx/conf.d/default.conf

exec "$@"