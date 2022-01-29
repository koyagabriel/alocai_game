#!/usr/bin/env bash
echo "Starting up server..."
export FLASK_APP=manage.py
flask run --host=0.0.0.0