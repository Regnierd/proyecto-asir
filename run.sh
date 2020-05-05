#!/bin/bash

cd "$(dirname "$0")"
PYTHON_VENV=$(pipenv --venv)
uwsgi --socket :8080 --home $PYTHON_VENV -w main:app
