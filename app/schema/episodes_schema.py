from . import ma
from app.models.episode_model import EpisodeModel


class EpisodeSchema(ma.Schema):
    class Meta:
        model = EpisodeModel

    id = ma.Integer()
    description = ma.String()
    urgency = ma.Integer()
    doctor_id = ma.Integer()
    patient_id = ma.Integer()
    created_at = ma.String()


episode_schema = EpisodeSchema()
episodes_schema = EpisodeSchema(many=True)