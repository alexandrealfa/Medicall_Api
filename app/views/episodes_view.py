from flask_restful import Resource, reqparse
from http import HTTPStatus
from flask import current_app, request

from . import EpisodeModel, episode_schema, episodes_schema, db_manager, is_bad_request


class AllEpisodes(Resource):
    def get(self):
        all_episodes: EpisodeModel = EpisodeModel.query.order_by(EpisodeModel.id).all()
        serializer = episodes_schema.dump(all_episodes)

        return {"data": serializer}, HTTPStatus.OK


class DoctorEpisodes(Resource):
    def get(self, doctor_id):
        session = current_app.db.session
        
        all_episodes: EpisodeModel = session.query(EpisodeModel).filter(EpisodeModel.doctor_id == doctor_id).all()
        
        serializer = episodes_schema.dump(all_episodes)

        return {"data": serializer}, HTTPStatus.OK


class PatientEpisodes(Resource):
    def get(self, patient_id):
        session = current_app.db.session
        
        all_episodes: EpisodeModel = session.query(EpisodeModel).filter(EpisodeModel.patient_id == patient_id).all()
        
        serializer = episodes_schema.dump(all_episodes)

        return {"data": serializer}, HTTPStatus.OK


class Episode(Resource):
    def get(self, episode_id):
        
        episode: EpisodeModel = EpisodeModel.query.get_or_404(episode_id)
        
        serializer = episode_schema.dump(episode)
        return {"data": serializer}, HTTPStatus.OK

    def post(self):
        parse = reqparse.RequestParser()

        parse.add_argument("description", type=str, required=True)
        parse.add_argument("emergency_status", type=int, required=True)
        parse.add_argument("doctor_id", type=int, required=True)
        parse.add_argument("patient_id", type=int, required=True)

        kwargs = parse.parse_args()

        new_episode = EpisodeModel(**kwargs)

        db_manager(new_episode)

        serializer = episode_schema.dump(new_episode)

        return {"data": serializer}, HTTPStatus.OK



    def patch(self, episode_id):
        body = request.get_json()

        parse = reqparse.RequestParser()
        parse.add_argument("description", type=str)
        parse.add_argument("urgency", type=int)
        parse.add_argument("doctor_id", type=int)
        parse.add_argument("patient_id", type=int)
        parse.add_argument("created_at", type=str)

        kwargs = parse.parse_args()

        current_episode = EpisodeModel.query.get_or_404(episode_id)

        if is_bad_request(body):
                return {"msg": "bad request"}, HTTPStatus.BAD_REQUEST
       
        [setattr(current_episode, key, value) for key, value in kwargs.items() if value is not None]

        db_manager(current_episode)
        serializer = episode_schema.dump(current_episode)

        return {"msg": "success updated","data": serializer}, HTTPStatus.OK


    def delete(self, episode_id):
        current_episode = EpisodeModel.query.get_or_404(episode_id)
        db_manager(current_episode, True)

        return {"msg": f"Patient {episode_id} has been deleted"}, HTTPStatus.OK