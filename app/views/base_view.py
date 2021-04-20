from flask_jwt_extended import get_jwt_identity
from flask_restful import Resource


class BaseView(Resource):
    __abstract__ = True

    def get_id(self):
        user_id = int(tuple(get_jwt_identity().split(" "))[0])
        return user_id

    def get_type(self):
        user_type = tuple(get_jwt_identity().split(" "))[1]
        return user_type