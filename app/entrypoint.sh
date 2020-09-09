#!/bin/bash

# Wait postgres load
RETRIES=15
until python manage.py makemigrations > /dev/null 2>&1 || [ $RETRIES -eq 0 ]; do
  echo "Waiting for postgres server, $((RETRIES--)) remaining attempts..."
  sleep 3
done

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py makemigrations api
python manage.py migrate

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

exec "$@"