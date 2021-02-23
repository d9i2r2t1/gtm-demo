#!/bin/sh
echo "Waiting for Postgres..."

while ! nc -z $DJANGO_DB_HOST $DJANGO_DB_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

exec "$@"