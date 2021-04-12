from . import ma
from app.models.doctor_model import DoctorModel


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


doctor_schema = DoctorSchema()
doctors_schema = DoctorSchema(many=True)