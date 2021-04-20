from http import HTTPStatus

from flask import request
from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError

from . import (DoctorModel, EpisodeModel, PatientModel, db_manager,
               episode_schema, episodes_schema, is_bad_request)


class DoctorEpisodes(Resource):
    def get(self, doctor_id):

        DoctorModel.query.get_or_404(doctor_id)
        all_episodes: EpisodeModel = EpisodeModel.query.filter(
            EpisodeModel.doctor_id == doctor_id
        ).all()

        serializer = episodes_schema.dump(all_episodes)

        return {"message": "success", "data": serializer}, HTTPStatus.OK


class PatientEpisodes(Resource):
    def get(self, patient_id):

        PatientModel.query.get_or_404(patient_id)
        all_episodes: EpisodeModel = EpisodeModel.query.filter(
            EpisodeModel.patient_id == patient_id
        ).all()

        serializer = episodes_schema.dump(all_episodes)

        return {"message": "success", "data": serializer}, HTTPStatus.OK


class Episode(Resource):
    def get(self, episode_id):

        episode: EpisodeModel = EpisodeModel.query.get_or_404(episode_id)

        serializer = episode_schema.dump(episode)
        return {"message": "success", "data": serializer}, HTTPStatus.OK

    def post(self):
        body = request.get_json()

        parse = reqparse.RequestParser()
        parse.add_argument("description", type=str, required=True)
        parse.add_argument("emergency_status", type=str, required=True)
        parse.add_argument("doctor_id", type=int, required=True)
        parse.add_argument("patient_id", type=int, required=True)

        kwargs = parse.parse_args()

        if is_bad_request(body, kwargs.keys()):
            return {"message": "invalid values"}, HTTPStatus.BAD_REQUEST

        new_episode = EpisodeModel(**kwargs)

        try:
            db_manager(new_episode)
        except IntegrityError:
            return {"message": "doctor or patient not found"}, HTTPStatus.NOT_FOUND

        serializer = episode_schema.dump(new_episode)

        return {"message": "success created", "data": serializer}, HTTPStatus.OK

    def patch(self, episode_id):
        body = request.get_json()

        parse = reqparse.RequestParser()
        parse.add_argument("description", type=str)
        parse.add_argument("emergency_status", type=str)
        parse.add_argument("doctor_id", type=int)
        parse.add_argument("patient_id", type=int)
        parse.add_argument("created_at", type=str)

        kwargs = parse.parse_args()

        if is_bad_request(body, kwargs.keys()):
            return {"message": "invalid values"}, HTTPStatus.BAD_REQUEST

        current_episode = EpisodeModel.query.get_or_404(episode_id)

        [
            setattr(current_episode, key, value)
            for key, value in kwargs.items()
            if value is not None
        ]

        db_manager(current_episode)
        serializer = episode_schema.dump(current_episode)

        return {"message": "success updated", "data": serializer}, HTTPStatus.OK

    def delete(self, episode_id):
        current_episode = EpisodeModel.query.get_or_404(episode_id)
        db_manager(current_episode, True)

        return {"message": f"patient {episode_id} has been deleted"}, HTTPStatus.OK