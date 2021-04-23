from app.models.doctor_model import DoctorModel
from app.schema.episodes_schema import episodes_schema

from . import ma


class DoctorSchema(ma.Schema):
    class Meta:
        model = DoctorModel

    id = ma.Integer()
    specialty = ma.String()
    crm = ma.String()
    firstname = ma.String()
    lastname = ma.String()
    phone = ma.String()
    email = ma.String()
    created_at = ma.String()
    episodes_list = ma.Nested(episodes_schema)


doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)