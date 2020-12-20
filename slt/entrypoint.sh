#!/bin/sh

python -m django startproject config .

python manage.py migrate

exec "$@"
