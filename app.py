import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_restful import Api
from loguru import logger


def create_app():
    _app_ = Flask(__name__)
    load_dotenv('.env', verbose=True)
    _app_.config.from_object('development_config')  # load default configs from development_config.py
    _app_.config.from_envvar(
        'APPLICATION_SETTING')  # override with config.py (APPLICATION_SETTINGS points to config.py)
    api = Api(_app_)
    SECRET_KEY = os.urandom(32)
    _app_.config['SECRET_KEY'] = SECRET_KEY

    @_app_.route('/')
    def home():
        return render_template('index.html'), 200

    @_app_.route('/api', methods=['GET', 'POST'])
    def api():
        if request.method == 'GET':
            # Xử lý request GET
            logger.debug('GET request received')
            return 'GET request received'
        elif request.method == 'POST':
            # Xử lý request POST
            logger.debug('GET request received')
            return 'POST request received'

    return _app_


app = create_app()
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
