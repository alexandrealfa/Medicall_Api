from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.address_model import AddressModel
    from app.models.doctor_model import DoctorModel
    from app.models.enum_model import EnumEmergency, EnumType
    from app.models.episode_model import EpisodeModel
    from app.models.patient_model import PatientModel
    from app.models.superuser_model import SuperuserModel
