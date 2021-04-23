import pytest
from app import create_app
from flask import current_app
from app.models.doctor_model import DoctorModel
from flask_sqlalchemy import SQLAlchemy

import app


db = app.database

@pytest.fixture()
def app():
    return create_app()


@pytest.fixture()
def db(app):
    from app import database

    context = app.app_context()
    with context:
        context.push()
        db.create_all()
        db.session.commit()
        context.pop()

        yield db
        db.drop_all()
        db.commit()


@pytest.fixture
def doctor_data():
    return {
    "specialty": "Pediatria",
    "id": 8,
    "firstname": "Max",
    "phone": "41 8888-8888",
    "episodes_list": [],
    "crm": "015432/PR",
    "lastname": "Doe",
    "email": "eae@email.com"
  }

def test_get(db, doctor_data):
    DoctorModel.post(doctor_data)
    
    doctors = DoctorModel.get()
    assert len(doctors) == 1
