from . import db
import datetime
import enum


class UrgencyEnum(enum.Enum):
    low = 1
    medium = 2
    high = 3


class EpisodeModel(db.Model):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    urgency = db.Column(db.Enum(UrgencyEnum), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
