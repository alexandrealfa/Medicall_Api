from .base_model import db, BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from app.models.enum_model import EnumType


class AddressModel(BaseModel):
    zip_code = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    address_complement = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey("episodes.id"), nullable=False)
