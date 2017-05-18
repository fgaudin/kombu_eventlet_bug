#!/usr/bin/env bash

gunicorn wsgi:app --workers 1 -k eventlet --timeout=900000 --worker-class=eventlet --reload
