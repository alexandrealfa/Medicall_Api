from . import ma
from app.models.patient_model import PatientModel


class PatientSchema(ma.Schema):
    class Meta:
        model = PatientModel

    id = ma.Integer()
    firstname = ma.String()
    lastname = ma.String()
    phone = ma.Column()
    email = ma.String()
    created_at = ma.Datetime()


patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)
