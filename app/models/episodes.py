from . import db
import datetime


class EpisodesModel(db.Model):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    category = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date, default=datetime.datetime.utcnow)
