from flask_restful import Resource, reqparse
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from . import patients_schema, patient_schema, PatientModel, DoctorModel, doctor_schema, doctors_schema


class SignIn(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("nickname", type=str, required=True)
        parse.add_argument("email", type=str, required=True)
        parse.add_argument("password", type=str, required=True)
        kwargs = parse.parse_args()

        