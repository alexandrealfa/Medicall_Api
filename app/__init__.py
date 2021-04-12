from flask import Flask
from environs import Env
from config import config_selector

from app.configurations import database
from app.configurations import serializer
from app.configurations import migration

env = Env()
env.read_env()


def create_app():
    app = Flask(__name__)
    config_type = env("FLASK_ENV")
    app.config.from_object(config_selector[config_type])

    # app.config['SQLALCHEMY_DATABASE_URI'] = env('DB_URI_DEV')

    # app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://alexandre:123456@localhost:5432/medicall"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    database.init_app(app)
    migration.init_app(app)
    serializer.init_app(app)

    return app