from flask_restful import Resource, reqparse
from flask import request
from flask_jwt_extended import create_access_token
from . import patients_schema, patient_schema, PatientModel, DoctorModel, doctor_schema, doctors_schema, is_bad_request
from datetime import timedelta
from http import HTTPStatus
from flask import request


class SignIn(Resource):
    def post(self):
        body = request.get_json()

        parse = reqparse.RequestParser()
        parse.add_argument("email", type=str, required=True)
        parse.add_argument("password", type=str, required=True)
        kwargs = parse.parse_args()

        if is_bad_request(body, kwargs.keys()):
                    return {"message": "invalid values"}, HTTPStatus.BAD_REQUEST

        email = [value for key, value in kwargs.items() if key == "email"][0]
        password = [value for key, value in kwargs.items() if key == "password"][0]

        found_user: DoctorModel = DoctorModel.query.filter_by(email=email).first()

        if not found_user:
            found_user: PatientModel = PatientModel.query.filter_by(email=email).first()


        if not found_user.check_password(password):
            return {"message": "unauthorized"}, HTTPStatus.UNAUTHORIZED    

        access_token = create_access_token(identity=found_user.id, expires_delta=timedelta(days=7))
        serializer = doctor_schema.dump(found_user)
        
        return {"message": "sucess", "data": serializer, "access_token": access_token}, HTTPStatus.OK