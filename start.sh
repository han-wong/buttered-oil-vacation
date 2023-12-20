#!/bin/bash

python3 -m gunicorn "board:create_app()" -w 1 --log-file -