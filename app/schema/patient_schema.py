from . import ma
from app.models.patient_model import PatientModel


class PatientSchema(ma.Schema):
    class Meta:
        model = PatientModel

    id = ma.Integer()
    firstname = ma.String()
    lastname = ma.String()
    phone = ma.String()
    email = ma.String()
    created_at = ma.String()


patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)
