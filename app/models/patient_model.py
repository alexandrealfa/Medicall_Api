import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from app.models.enum_model import EnumType

from .base_model import BaseModel, db


class PatientModel(BaseModel):
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    user_type = db.Column(
        db.Enum(EnumType, values_callable=lambda obj: [enum.value for enum in obj]),
        nullable=False,
        default=EnumType.PATIENT.value,
        server_default=EnumType.PATIENT.value,
    )
    episodes_list = db.relationship("EpisodeModel", backref=db.backref("patient_list", lazy="joined"), lazy="joined")
    disabled = db.Column(db.Boolean, default=False, nullable=True)

    @property
    def password(self):
        raise TypeError("Password cannot be accessed")

    @password.setter
    def password(self, new_password):
        new_password_hash = generate_password_hash(new_password)
        self.password_hash = new_password_hash

    def check_password(self, password_to_check):
        return check_password_hash(self.password_hash, password_to_check)