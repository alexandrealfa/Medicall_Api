from app.models.patient_model import PatientModel
from app.schema.episodes_schema import episodes_schema

from . import ma


class PatientSchema(ma.Schema):
    class Meta:
        model = PatientModel

    id = ma.Integer()
    firstname = ma.String()
    lastname = ma.String()
    phone = ma.String()
    email = ma.String()
    created_at = ma.String()
    episodes_list = ma.Nested(episodes_schema)


patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)
