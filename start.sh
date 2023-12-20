#!/bin/bash

# Install modules
# python3 -m pip install -r requirements.txt

# Initialize database or reset
# python3 -m flask --app board init-db

# For development use (simple logging, etc):
# python3 -m flask --app board run --port 8000 --debug

# For production use: 
python3 -m gunicorn "board:create_app()" -w 1 --log-file -