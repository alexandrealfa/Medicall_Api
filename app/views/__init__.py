from flask import current_app
from marshmallow_enum import EnumField

from app.configurations.serializer import ma
from app.models.doctor_model import DoctorModel
from app.models.enum_model import EnumType
from app.models.superuser_model import SuperuserModel
from app.models.episode_model import EpisodeModel
from app.models.patient_model import PatientModel
from app.schema.doctor_schema import (doctor_schema, doctors_schema,
                                      episodes_schema)
from app.schema.episodes_schema import episode_schema
from app.schema.patient_schema import patient_schema, patients_schema
from app.views.base_view import BaseView


def db_manager(available_patient: object, deleted: bool = False):
    session = current_app.db.session
    if deleted:
        session.delete(available_patient)
        session.commit()
    else:
        session.add(available_patient)
        session.commit()


def is_bad_request(body, valid_keys):
    is_bad = False

    body_keys = [k for k in body.keys()]
    reference = [k for k in valid_keys]

    for k in body_keys:
        if k not in reference:
            is_bad = True

    return is_bad
