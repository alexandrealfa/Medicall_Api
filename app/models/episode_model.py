from . import db
import datetime


# VERMLHO = EMERGENCIA
# LARANJA = MUITO URGENTE
# AMARELO = URGENTE
# VERDE = POUCO URGENTE
# AZUL = NAO URGENTE


class EpisodeModel(db.Model):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    urgency = db.Column(db.Integer, nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
