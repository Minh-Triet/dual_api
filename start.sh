#!/bin/sh
gunicorn -w 4 -b 0.0.0.0:5000 api_request.app:app &
gunicorn -w 1 -b 0.0.0.0:8000 api_scheduler.app:app