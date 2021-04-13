from app.models.patient_model import PatientModel
from app.schema.patient_schema import patients_schema, patient_schema
from app.models.doctor_model import DoctorModel
from app.schema.doctor_schema import doctor_schema, doctors_schema
from flask import current_app


def db_manager(available_patient: object, deleted: bool = False):
    session = current_app.db.session
    if deleted:
        session.delete(available_patient)
        session.commit()
    else:
        session.add(available_patient)
        session.commit()