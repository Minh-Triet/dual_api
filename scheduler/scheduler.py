import atexit
import os
import signal
import sys

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_restful import Api
from loguru import logger

from development_config import check_scheduler
from model.apscheduler import create_apscheduler

thread = None
generating_data = False
connected = []


def create_app():
    _app_ = Flask(__name__)
    load_dotenv('../.env', verbose=True)
    _app_.config.from_object('development_config')  # load default configs from development_config.py
    _app_.config.from_envvar(
        'APPLICATION_SETTING')  # override with config.py (APPLICATION_SETTINGS points to config.py)
    api = Api(_app_)
    SECRET_KEY = os.urandom(32)
    _app_.config['SECRET_KEY'] = SECRET_KEY

    @_app_.route('/')
    def home():
        return render_template('index.html'), 200

    return _app_


def run_scheduler(app_object):
    if not check_scheduler:
        check_scheduler.append('EXIST')

        create_apscheduler()

    def cleanup():
        check_scheduler.clear()
        logger.debug('Scheduler cleared.')

    def handle_exit(signum, frame):
        sys.exit(0)

    atexit.register(cleanup)
    signal.signal(signal.SIGTERM, handle_exit)
    signal.signal(signal.SIGINT, handle_exit)


app = create_app()
run_scheduler(app)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)