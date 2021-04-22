from http import HTTPStatus

from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import reqparse
from sqlalchemy.exc import IntegrityError

from . import (BaseView, PatientModel, db_manager, is_bad_request,
               patient_schema)


class Patients(BaseView):
    @jwt_required()
    def get(self):
        if self.get_type() == "doctor":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE
        patient_id = self.get_id()
        current_patient: PatientModel = PatientModel.query.get_or_404(patient_id)

        if current_patient.disabled:
            return {"message": "your account is disabled"}, HTTPStatus.UNAUTHORIZED

        serializer = patient_schema.dump(current_patient)

        return {"message": "success", "data": serializer}, HTTPStatus.OK

    def post(self):
        body = request.get_json()

        parse = reqparse.RequestParser()
        parse.add_argument("firstname", type=str, required=True)
        parse.add_argument("lastname", type=str, required=True)
        parse.add_argument("phone", type=str, required=True)
        parse.add_argument("email", type=str, required=True)
        parse.add_argument("password", type=str, required=True)
        kwargs = parse.parse_args()

        if is_bad_request(body, kwargs.keys()):
            return {"message": "invalid values"}, HTTPStatus.BAD_REQUEST

        new_patient = PatientModel(**kwargs)

        try:
            db_manager(new_patient)
        except IntegrityError:
            return {"message": "email already in use"}, HTTPStatus.NOT_ACCEPTABLE

        serializer = patient_schema.dump(new_patient)

        return {"message": "success created", "data": serializer}, HTTPStatus.OK

    @jwt_required()
    def patch(self):
        if self.get_type() == "":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE
        body = request.get_json()

        parse = reqparse.RequestParser()
        parse.add_argument("firstname", type=str)
        parse.add_argument("lastname", type=str)
        parse.add_argument("phone", type=str)
        parse.add_argument("email", type=str)
        parse.add_argument("password", type=str)

        patient_id = self.get_id()
        current_patient = PatientModel.query.get_or_404(patient_id)

        if current_patient.disabled:
            return {"message": "your account is disabled"}, HTTPStatus.UNAUTHORIZED

        kwargs = parse.parse_args()

        if is_bad_request(body, kwargs.keys()):
            return {"message": "invalid values"}, HTTPStatus.BAD_REQUEST

        [
            setattr(current_patient, key, value)
            for key, value in kwargs.items()
            if key != "password" and value is not None
        ]
        if kwargs.password:
            setattr(current_patient, "password", kwargs.password)

        db_manager(current_patient)
        serializer = patient_schema.dump(current_patient)

        return {"message": "success updated", "data": serializer}, HTTPStatus.OK

    @jwt_required()
    def delete(self):
        if self.get_type() == "doctor":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE
        patient_id = self.get_id()
        current_patient: PatientModel = PatientModel.query.get_or_404(patient_id)

        if current_patient.disabled:
            return {"message": "your account is disabled"}, HTTPStatus.UNAUTHORIZED
            
        current_patient.disabled = True
        db_manager(current_patient)

        return {"message": f"patient {patient_id} patient was disabled"}, HTTPStatus.OK
