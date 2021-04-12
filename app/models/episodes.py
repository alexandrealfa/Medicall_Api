from . import db
import datetime


class EpisodesModel(db.Model):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    urgency = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())


# 1- Baixa
# 2- Média
# 3- Alta
