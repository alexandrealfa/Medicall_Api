from marshmallow_enum import EnumField

from app.models.address_model import AddressModel

from . import EnumState, ma


class AddressSchema(ma.Schema):
    class Meta:
        model = AddressModel
    
    zip_code = ma.String()
    address = ma.String()
    complement = ma.String()
    city = ma.String()
    state = EnumField(EnumState, by_value=True)
    country = ma.String()
    patient_id = ma.Integer()


address_schema = AddressSchema()
