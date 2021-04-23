import pytest
from app import create_app
from flask import current_app
from app.models.doctor_model import DoctorModel
from flask_sqlalchemy import SQLAlchemy

import app

database = SQLAlchemy()


@pytest.fixture()
def app():
    return create_app()


@pytest.fixture()
def db(app):
    from app import database

    context = app.app_context()
    with context:
        context.push()
        database.db.create_all()
        database.db.session.commit()
        context.pop()

        yield database.db
        database.db.drop_all()
        database.db.session.commit()



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
    doctor = DoctorModel(**doctor_data)
    db.session.add(doctor)
    db.session.commit()
    doctors = DoctorModel.query.all()
    assert len(doctors) == 1
