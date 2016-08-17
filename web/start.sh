#!/bin/bash

echo "Waiting for postgres container to be available"
dockerize -wait tcp://postgres:5432

echo "Mezzanine microservice executing: createdb/migrate ..."
python3 manage.py createdb --noinput

echo "Mezzanine microservice executing: collectstatic ..."
python3 manage.py collectstatic --noinput

echo "Starting WSGI ..."
/usr/local/bin/gunicorn docker_mezzanine.wsgi:application -w 2 -b :8000
