from flask_jwt_extended import get_jwt_identity
from flask_restful import Resource, request
from flask import render_template, make_response
import pdfkit


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

    def pdf_template(self, name, email, phone):
        render = render_template("pdf_template.html", name=name, email=email, phone=phone)
        pdf = pdfkit.from_string(render, False)

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=template.pdf'

        return response