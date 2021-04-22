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
        page = 1 if not request.args.get("page") else int(request.args.get("page"))
        return page

    def per_page_pagination(self):
        per_page = 15 if not request.args.get("per_page") else int(request.args.get("per_page"))
        return per_page

    def pdf_template(self, name, email, phone, doctor_name, doctor_email, description, emergency_status, created_at):
        html = render_template("pdf_template.html",
                               name=name, email=email, phone=phone,
                               doctor_name=doctor_name, doctor_email=doctor_email,
                               description=description, emergency_status=emergency_status,
                               created_at=created_at)
        pdf = pdfkit.from_string(html, False)

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

        return response
