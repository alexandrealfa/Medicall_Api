from .base_view import BaseView
from flask_jwt_extended import jwt_required
from . import EpisodeModel


class PrintEpisode(BaseView):
    @jwt_required()
    def get(self, episode_id):
        id_user = self.get_id()
        type_request = self.get_type()
        episode: EpisodeModel = EpisodeModel.query.get_or_404(episode_id)
        if type_request == "Doctor":
            if episode.doctor_id == id_user:
                ...
