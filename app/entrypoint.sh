#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py makemigrations api
python manage.py migrate

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

exec "$@"