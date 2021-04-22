from environs import Env
from flask import Flask

from app.configurations import (authentication, database, migration,
                                serializer, views_config)
from app.views.bp_download_pdf import bild_app
from config import config_selector

env = Env()
env.read_env()


def create_app():
    app = Flask(__name__)
    config_type = env("FLASK_ENV")
    app.config.from_object(config_selector[config_type])

    database.init_app(app)
    authentication.init_app(app)
    migration.init_app(app)
    serializer.init_app(app)
    views_config.init_app(app)
    bild_app(app)

    return app
