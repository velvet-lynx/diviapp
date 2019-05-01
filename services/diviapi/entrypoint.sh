#!/bin/sh
echo "Waiting for redis..."

while ! nc -z redis 6379; do
    sleep 0.1
done

echo "redis started"

python manage.py run -h 0.0.0.0