from flask.globals import session
from flask_restful import Resource, reqparse
from http import HTTPStatus
from . import DoctorModel, doctor_schema, doctors_schema, db_manager, is_bad_request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request


class AllDoctors(Resource):
    @jwt_required()
    def get(self):
        all_doctors: DoctorModel = DoctorModel.query.order_by(DoctorModel.id).all()
        serializer = doctors_schema.dump(all_doctors)

        return {"message": "success", "data": serializer}, HTTPStatus.OK


class Doctor(Resource):
    @jwt_required()
    def get(self):
        doctor_id = get_jwt_identity()
        doctor = DoctorModel.query.get(doctor_id)
        serializer = doctor_schema.dump(doctor)

        return {"message": "success", "data": serializer}, HTTPStatus.OK

    def post(self):
        parse = reqparse.RequestParser()

        parse.add_argument("specialty", type=str, required=True)
        parse.add_argument("crm", type=str, required=True)
        parse.add_argument("firstname", type=str, required=True)
        parse.add_argument("lastname", type=str, required=True)
        parse.add_argument("phone", type=str, required=True)
        parse.add_argument("email", type=str, required=True)
        parse.add_argument("password", type=str, required=True)

        kwargs = parse.parse_args()

        new_doctor = DoctorModel(
            specialty=kwargs.specialty,
            crm=kwargs.crm,
            firstname=kwargs.firstname,
            lastname=kwargs.lastname,
            phone=kwargs.phone,
            email=kwargs.email,
        )

        new_doctor.password = kwargs.password

        db_manager(new_doctor)

        serializer = doctor_schema.dump(new_doctor)

        return {"message": "success created", "data": serializer}, HTTPStatus.OK

    @jwt_required()
    def patch(self):
        body = request.get_json()

        parse = reqparse.RequestParser()
        parse.add_argument("specialty", type=str)
        parse.add_argument("crm", type=str)
        parse.add_argument("firstname", type=str)
        parse.add_argument("lastname", type=str)
        parse.add_argument("phone", type=str)
        parse.add_argument("email", type=str)
        parse.add_argument("password", type=str)

        kwargs = parse.parse_args()

        doctor_id = get_jwt_identity()
        doctor = DoctorModel.query.get_or_404(doctor_id)

        if is_bad_request(body, kwargs.keys()):
            return {"message": "invalid values"}, HTTPStatus.BAD_REQUEST

        for key, value in kwargs.items():
            if key != "password" and value is not None:
                setattr(doctor, key, value)

        if kwargs.password:
            setattr(doctor, "password", kwargs.password)

        db_manager(doctor)
        serializer = doctor_schema.dump(doctor)

        return {"message": "success updated", "data": serializer}, HTTPStatus.OK

    @jwt_required()
    def delete(self):
        doctor_id = get_jwt_identity()
        doctor = DoctorModel.query.get_or_404(doctor_id)
        db_manager(doctor, True)

        return {
            "data": f"doctor {doctor_id} has successfully been deleted"
        }, HTTPStatus.OK
