#!/bin/sh
. venv/bin/activate
venv/bin/gunicorn -b 0.0.0.0:8080 --log-level=debug threescale-auth0-wrapper:app -k gevent