from flask.globals import session
from flask_restful import Resource, reqparse
from http import HTTPStatus
from . import DoctorModel, doctor_schema, doctors_schema, db_manager


class AllDoctors(Resource):
    def get(self):
        all_doctors: DoctorModel = DoctorModel.query.order_by(DoctorModel.id).all()
        serializer = doctors_schema.dump(all_doctors)

        return {"data": serializer}, HTTPStatus.OK


class Doctor(Resource):
    def get(self, doctor_id):
        doctor = DoctorModel.query.get(doctor_id)
        serializer = doctor_schema.dump(doctor)

        return {"data": serializer}, HTTPStatus.OK

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

        return {"data": serializer}, HTTPStatus.OK

    def patch(self, doctor_id):
        parse = reqparse.RequestParser()

        parse.add_argument("specialty", type=str)
        parse.add_argument("crm", type=str)
        parse.add_argument("firstname", type=str)
        parse.add_argument("lastname", type=str)
        parse.add_argument("phone", type=str)
        parse.add_argument("email", type=str)
        parse.add_argument("password", type=str)

        kwargs = parse.parse_args()

        doctor = DoctorModel.query.get_or_404(doctor_id)

        for key, value in kwargs.items():
            if value:
                if key != "password":
                    setattr(doctor, key, value)

        if kwargs.password:
            setattr(doctor, "password", kwargs.password)

        db_manager(doctor)
        serializer = doctor_schema.dump(doctor)

        return {"data": serializer}, HTTPStatus.OK

    def delete(self, doctor_id):
        doctor = DoctorModel.query.get_or_404(doctor_id)
        db_manager(doctor)

        return {"data": f"Doctor {doctor_id} has successfully been deleted"}, HTTPStatus.OK