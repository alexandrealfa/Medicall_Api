from .base_model import db, BaseModel
from app.models.enum_model import EnumState

class AddressModel(BaseModel):
    zip_code = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    complement = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    state = db.Column(
        db.Enum(EnumState, values_callable=lambda obj: [enum.value for enum in obj]),
        nullable=False,
        default=EnumState.PR.value,
        server_default=EnumState.PR.value,
    )
