#!/bin/sh
python manage.py makemigrations
python manage.py migrate --no-input
gunicorn abu_task.wsgi:application --0.0.0.0:8000 & 
unlink /etc/nginx/sites-enabled/default
nginx -g 'daemon off;'