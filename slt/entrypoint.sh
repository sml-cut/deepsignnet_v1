#!/bin/sh

python -m django startproject config .
python manage.py startapp slt
python manage.py migrate

exec "$@"
