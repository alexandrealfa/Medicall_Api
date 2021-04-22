from http import HTTPStatus

from flask_jwt_extended import jwt_required
from flask_restful import reqparse, request
from sqlalchemy.exc import IntegrityError

from . import BaseView, DoctorModel, db_manager, doctor_schema, is_bad_request


class Doctor(BaseView):
    @jwt_required()
    def get(self):
        if self.get_type() == "patient":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE
        doctor_id = self.get_id()
        doctor: DoctorModel = DoctorModel.query.get_or_404(doctor_id)

        if doctor.disabled:
            return {"message": "your account is disabled"}, HTTPStatus.UNAUTHORIZED

        serializer = doctor_schema.dump(doctor)

        return {"message": "success", "data": serializer}, HTTPStatus.OK

    def post(self):
        body = request.get_json()
        parse = reqparse.RequestParser()

        parse.add_argument("specialty", type=str, required=True)
        parse.add_argument("crm", type=str, required=True)
        parse.add_argument("firstname", type=str, required=True)
        parse.add_argument("lastname", type=str, required=True)
        parse.add_argument("phone", type=str, required=True)
        parse.add_argument("email", type=str, required=True)
        parse.add_argument("password", type=str, required=True)

        kwargs = parse.parse_args()
        if is_bad_request(body, kwargs.keys()):
            return {"message": "invalid values"}, HTTPStatus.BAD_REQUEST

        new_doctor = DoctorModel(
            specialty=kwargs.specialty,
            crm=kwargs.crm,
            firstname=kwargs.firstname,
            lastname=kwargs.lastname,
            phone=kwargs.phone,
            email=kwargs.email,
        )
        new_doctor.password = kwargs.password

        try:
            db_manager(new_doctor)
        except IntegrityError:
            return {"message": "email already in use"}, HTTPStatus.NOT_ACCEPTABLE

        serializer = doctor_schema.dump(new_doctor)

        return {"message": "success created", "data": serializer}, HTTPStatus.OK

    @jwt_required()
    def patch(self):
        if self.get_type() == "patient":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE

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
        doctor_id = self.get_id()
        doctor = DoctorModel.query.get_or_404(doctor_id)

        if doctor.disabled:
            return {"message": "your account is disabled"}, HTTPStatus.UNAUTHORIZED

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
        if self.get_type() == "patient":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE

        doctor_id = self.get_id()
        doctor: DoctorModel = DoctorModel.query.get_or_404(doctor_id)

        if doctor.disabled:
            return {"message": "your account is disabled"}, HTTPStatus.UNAUTHORIZED

        doctor.disabled = True        

        db_manager(doctor)

        return {
                   "data": f"doctor {doctor_id} was disabled"
               }, HTTPStatus.OK
