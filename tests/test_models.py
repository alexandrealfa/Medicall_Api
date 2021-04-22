# import pytest
# from app import create_app


# @pytest.fixture()
# def app():
#     return create_app()


# @pytest.fixture()
# def db(app):
#     from app import database

#     with app.app_context():
#         database.create_all()
#         yield database
#         database.drop_all()
#         database.session.commit()


# @pytest.fixture()
# def data():
#     return {}
