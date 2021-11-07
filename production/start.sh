#!/bin/sh

python manage.py migrate --noinput
uwsgi

