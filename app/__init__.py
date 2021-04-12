from flask import Flask
from environs import Env
from config import config_selector

from app.configurations import database
from app.configurations import serializer
from app.configurations import migration
from app.configurations import views

env = Env()
env.read_env()


def create_app():
    app = Flask(__name__)
    config_type = env("FLASK_ENV")
    app.config.from_object(config_selector[config_type])

    database.init_app(app)
    migration.init_app(app)
    serializer.init_app(app)
    views.init_app(app)

    return app