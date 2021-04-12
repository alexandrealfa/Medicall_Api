from flask import Flask
from flask_restful import Api


def init_app(app: Flask):
    api = Api(app)

    # Import views, and builds and resources