from . import patient_schema, patients_schema, PatientModel, db_manager
from flask_restful import Resource, reqparse
from http import HTTPStatus
from flask_jwt_extended import get_jwt_identity, jwt_required


class AllPatients(Resource):
    def get(self):
        all_patients = PatientModel.query.all()
        serializer = patients_schema.dump(all_patients)

        return {
                   "msg": "success",
                   "data": serializer
               }, HTTPStatus.OK


class Patients(Resource):
    @jwt_required()
    def get(self):
        patient_id = get_jwt_identity()
        current_patient = PatientModel.query.get_or_404(patient_id)
        serializer = patient_schema.dump(current_patient)

        return {
                   "msg": "success",
                   "data": serializer
               }, HTTPStatus.OK

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("firstname", type=str, required=True)
        parse.add_argument("lastname", type=str, required=True)
        parse.add_argument("phone", type=str, required=True)
        parse.add_argument("email", type=str, required=True)
        parse.add_argument("password", type=str, required=True)
        kwargs = parse.parse_args()

        new_patient = PatientModel(**kwargs)
        db_manager(new_patient)
        serializer = patient_schema.dump(new_patient)

        return {
                   "msg": "success created",
                   "data": serializer
               }, HTTPStatus.OK

    @jwt_required()
    def patch(self):
        parse = reqparse.RequestParser()
        parse.add_argument("firstname", type=str)
        parse.add_argument("lastname", type=str)
        parse.add_argument("phone", type=str)
        parse.add_argument("email", type=str)
        parse.add_argument("password", type=str)

        patient_id = get_jwt_identity()
        print(patient_id)
        current_patient = PatientModel.query.get_or_404(patient_id)
        kwargs = parse.parse_args()

        [setattr(current_patient, key, value) for key, value in kwargs.items() if key != "password" and value is not None]
        if kwargs.password:
            setattr(current_patient, "password", kwargs.password)

        db_manager(current_patient)
        serializer = patient_schema.dump(current_patient)

        return {
                   "msg": "success updated",
                   "data": serializer
               }, HTTPStatus.OK

    @jwt_required()
    def delete(self):
        patient_id = get_jwt_identity()
        current_patient = PatientModel.query.get_or_404(patient_id)
        db_manager(current_patient, True)

        return {
                   "msg": f"Patient {patient_id} has been deleted"
               }, HTTPStatus.OK