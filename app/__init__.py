__version__ = '0.1.0'
from flask import Flask
from os import getenv
from app.configurations import database
from config import config_selector


def create_app():
    app = Flask(__name__)
    config_type = getenv("FLASK_ENV")
    app.config.from_object(config_selector[config_type])
    database.init_app(app)

    return app