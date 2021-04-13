from flask import Flask
from flask_restful import Api


def init_app(app: Flask):
    api = Api(app)

    # Import views, and builds and resources

    from app.views.doctor_view import Doctor, AllDoctors
    from app.views.episodes_view import Episode, AllEpisodes

    api.add_resource(AllDoctors, "/api/doctors", endpoint="/api/doctors")
    api.add_resource(Doctor, "/api/doctors", endpoint="/api/doctor", methods=["POST"])
    api.add_resource(Doctor, "/api/doctors", endpoint="/api/doctor/<int:doctor_id>", methods=["GET", "PATCH", "DELETE"])
    api.add_resource(AllEpisodes, "/api/episodes", endpoint="api/episodes")
    api.add_resource(Episode, "/api/episodes", endpoint="api/episode", methods=["POST"])