from marshmallow_enum import EnumField

from app.models.episode_model import EpisodeModel

from . import EnumEmergency, ma


class EpisodeSchema(ma.Schema):
    class Meta:
        model = EpisodeModel

    id = ma.Integer()
    description = ma.String()
    emergency_status = EnumField(EnumEmergency, by_value=True)
    doctor_id = ma.Integer()
    patient_id = ma.Integer()
    created_at = ma.String()


episode_schema = EpisodeSchema()
episodes_schema = EpisodeSchema(many=True)