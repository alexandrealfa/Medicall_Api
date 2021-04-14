from . import db
import datetime
import enum


class EnumEmergency(enum.Enum):
    EMERGENCY = "emergency"
    VERY_URGENT = "very urgent"
    URGENT = "urgent"
    LESS_URGENT = "less urgent"
    NOT_URGENT = "not urgent"


class EpisodeModel(db.Model):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    emergency_status = db.Column(
        db.Enum(EnumEmergency, values_callable=lambda obj: [enum.value for enum in obj]),
        nullable=False,
        default=EnumEmergency.NOT_URGENT.value,
        server_default=EnumEmergency.NOT_URGENT.value,
    )
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
