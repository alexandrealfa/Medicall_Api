from flask_restful import Resource, reqparse
from . import DoctorModel, doctors_schema, PatientModel, patients_schema, EpisodeModel, episodes_schema
from flask_jwt_extended import jwt_required
from http import HTTPStatus


class AllDoctors(Resource):
    @jwt_required()
    def get(self):
        all_doctors: DoctorModel = DoctorModel.query.order_by(DoctorModel.id).all()
        serializer = doctors_schema.dump(all_doctors)

        return {"message": "success", "data": serializer}, HTTPStatus.OK


class AllPatients(Resource):
    @jwt_required()
    def get(self):
        all_patients = PatientModel.query.all()
        serializer = patients_schema.dump(all_patients)
        return {"message": "success", "data": serializer}, HTTPStatus.OK


class AllEpisodes(Resource):
    @jwt_required()
    def get(self):
        all_episodes: EpisodeModel = EpisodeModel.query.order_by(EpisodeModel.id).all()
        serializer = episodes_schema.dump(all_episodes)
        return {"message": "success", "data": serializer}, HTTPStatus.OK