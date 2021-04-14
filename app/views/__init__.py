from app.models.patient_model import PatientModel
from app.schema.patient_schema import patients_schema, patient_schema
from app.models.doctor_model import DoctorModel
from app.schema.doctor_schema import doctor_schema, doctors_schema
from app.models.episode_model import EpisodeModel
from app.schema.episodes_schema import episode_schema, episodes_schema
from flask import current_app


def db_manager(available_patient: object, deleted: bool = False):
    session = current_app.db.session
    if deleted:
        session.delete(available_patient)
        session.commit()
    else:
        session.add(available_patient)
        session.commit()

def is_bad_request(request):
    is_bad = False

    body_keys = [k for k in request.keys()]
    reference = ['description', 'urgency', 'doctor_id', 'patient_id', 'created_at']

    for k in body_keys:
        if k not in reference:
            is_bad = True

    return is_bad
