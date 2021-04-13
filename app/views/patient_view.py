from . import patient_schema, patients_schema, PatientModel
from flask_restful import Resource, reqparse, current_app
from http import HTTPStatus


class AllPatients(Resource):
    def get(self):
        all_patients = PatientModel.query.all()
        serializer = patients_schema(all_patients)

        return {
            "msg": "success",
            "data": serializer
        }, HTTPStatus.OK


class Patients(Resource):

    @staticmethod
    def save_db(available_patient: object, deleted: bool = False):
        session = current_app.db.session
        if bool:
            session.remove(available_patient)
            session.commit()
        else:
            session.add(available_patient)
            session.commit()

    def get(self, patient_id):
        current_patient = PatientModel.query.get_or_404(patient_id)
        serializer = patient_schema.dump(current_patient)

        return {
            "msg": "success",
            "data": serializer
        }, HTTPStatus.OK

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("firstname", type="str", required=True)
        parse.add_argument("lastname", type="str", required=True)
        parse.add_argument("phone", type="str", required=True)
        parse.add_argument("email", type="str", required=True)
        parse.add_argument("password", type="str", required=True)
        kwargs = parse.parse_args()

        new_patient = PatientModel(**kwargs)
        Patients.save_db(new_patient)
        serializer = patient_schema(new_patient)

        return {
            "msg": "success created",
            "data": serializer
        }, HTTPStatus.OK

    def patch(self, patient_id):
        parse = reqparse.RequestParser()
        parse.add_argument("firstname", type="str")
        parse.add_argument("lastname", type="str")
        parse.add_argument("phone", type="str")
        parse.add_argument("email", type="str")
        parse.add_argument("password", type="str")

        current_patient = PatientModel.query.get_or_404(patient_id)
        kwargs = parse.parse_args()
        [setattr(current_patient, key, value) for key, value in kwargs.itmes()]
        Patients.save_db(kwargs)
        serializer = patient_schema(current_patient)

        return {
            "msg": "success updated",
            "data": serializer
        }

    def delete(self, patient_id):
        current_patient = PatientModel.query.get_or_404(patient_id)
        Patients.save_db(current_patient, True)