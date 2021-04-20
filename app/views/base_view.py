from flask_jwt_extended import get_jwt_identity
from flask_restful import Resource, request


class BaseView(Resource):
    __abstract__ = True

    def get_id(self):
        user_id = int(tuple(get_jwt_identity().split(" "))[0])
        return user_id

    def get_type(self):
        user_type = tuple(get_jwt_identity().split(" "))[1]
        return user_type

    def page_pagination(self):
        page = int(request.args.get("page")) if request.args.get("page") else 1
        return page

    def per_page_pagination(self):
        per_page = int(request.args.get("per_page")) if request.args.get("per_page") else 15
        return per_page