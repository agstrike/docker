#!/bin/sh

python manage.py migrate --noinput
python manage.py createtestdata --prune
uwsgi

