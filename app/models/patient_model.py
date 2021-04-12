from . import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


class PatientModel(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    @property
    def password(self):
        raise TypeError("Password cannot be accessed")

    @password.setter
    def password(self, new_password):
        new_password_hash = generate_password_hash(new_password)
        self.password_hash = new_password_hash

    def check_password(self, password_to_check):
        return check_password_hash(self.password_hash, password_to_check)