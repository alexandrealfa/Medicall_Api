from flask_restful import Resource, reqparse
from flask import request
from flask_jwt_extended import create_access_token
from . import patients_schema, patient_schema, PatientModel, DoctorModel, doctor_schema, doctors_schema
from datetime import timedelta
from http import HTTPStatus


class SignIn(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("email", type=str, required=True)
        parse.add_argument("password", type=str, required=True)
        kwargs = parse.parse_args()
        email = [value for key, value in kwargs.items() if key == "email"][0]
        found_user = DoctorModel.query.filter_by(email=email).first()
        if not found_user:
            found_user = PatientModel.query.filter_by(email=email).first()
        access_token = create_access_token(identity=found_user.id, expires_delta=timedelta(days=7))
        serializer = doctor_schema.dump(found_user)
        return {"msg": "created", "data": serializer, "access_token": access_token}, HTTPStatus.OK