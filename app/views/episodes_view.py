from flask_restful import Resource, reqparse, current_app
from http import HTTPStatus

from app.models.episode_model import EpisodeModel
from app.schema.episodes_schema import episode_schema, episodes_schema


class AllEpisodes(Resource):
    def get(self):
        all_episodes: EpisodeModel = EpisodeModel.query.order_by(EpisodeModel.id).all()
        serializer = episodes_schema.dump(all_episodes)

        return {"data": serializer}, HTTPStatus.OK


class Episode(Resource):
    def get(self, episode_id):
        episode = EpisodeModel.query.get(episode_id)
        serializer = episode_schema.dump(episode)

        return {"data": serializer}, HTTPStatus.OK

    def post(self):
        parse = reqparse.RequestParser()

        parse.add_argument("description", type=str, required=True)
        parse.add_argument("urgency", type=int, required=True)
        parse.add_argument("doctor_id", type=int, required=True)
        parse.add_argument("patient_id", type=int, required=True)

        kwargs = parse.parse_args()

        new_episode = EpisodeModel(
            description=kwargs.description,
            urgency=kwargs.urgency,
            doctor_id=kwargs.doctor_id,
            patient_id=kwargs.patient_id,
        )

        session = current_app.db.session
        session.add(new_episode)
        session.commit()

        serializer = episode_schema.dump(new_episode)

        return {"data": serializer}, HTTPStatus.OK