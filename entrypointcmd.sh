#!/bin/bash

#RUN_PORT=${PORT:-80}

#/usr/local/bin/gunicorn --worker-tmp-dir /dev/shm -k uvicorn.workers.UvicornWorker main:app --bind "0.0.0.0:${RUN_PORT}"

#uvicorn main:app --proxy-headers --port 80

gunicorn --worker-tmp-dir /dev/shm --config gunicorn.config.py main:app --port 80
