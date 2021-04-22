from flask import Flask
from flask_restful import Api


def init_app(app: Flask):
    api = Api(app)

    # Import views, and builds and resources
    from app.views.print_episode_view import PrintEpisode
    from app.views.access_view import SignIn
    from app.views.doctor_view import Doctor
    from app.views.episodes_view import (DoctorEpisodes, Episode,
                                         PatientEpisodes)
    from app.views.patient_view import Patients
    from app.views.super_user_view import AllDoctors, AllEpisodes, AllPatients, SuperUser, AllSuperUsers

    api.add_resource(SignIn, "/login", endpoint="/login",
                     methods=["POST"])

    api.add_resource(SuperUser, "/root", endpoint="/root",
                     methods=["POST", "PATCH", "DELETE", "GET"])
    api.add_resource(AllSuperUsers, "/all_superusers", endpoint="/all_superusers",
                     methods=["GET"])
    api.add_resource(AllDoctors, "/all_doctors", endpoint="/all_doctors",
                     methods=["GET"])
    api.add_resource(AllEpisodes, "/all_episodes", endpoint="/all_episodes",
                     methods=["GET"])
    api.add_resource(AllPatients, "/all_patients", endpoint="/all_patients",
                     methods=["GET"])

    api.add_resource(Doctor, "/doctor", endpoint="/doctor",
                     methods=["GET", "PATCH", "DELETE", "POST"],)

    api.add_resource(Patients, "/patient", endpoint="/patient",
                     methods=["GET", "POST", "PATCH", "DELETE"],)

    api.add_resource(Episode, "/episode", endpoint="/episode",
                     methods=["POST"])
    api.add_resource(Episode, "/episode/<int:episode_id>", endpoint="/episode/<int:episode_id>",
                     methods=["GET", "DELETE", "PATCH"],)
    api.add_resource(DoctorEpisodes, "/episodes/doctor/<int:doctor_id>", endpoint="/episodes/doctor/<int:doctor_id>",
                     methods=["GET"])
    api.add_resource(PatientEpisodes, "/episodes/patient/<int:patient_id>",
                     endpoint="/episodes/patient/<int:patient_id>",
                     methods=["GET"])
    api.add_resource(Episode, "/episode/print/<int:episode_id>",
                     endpoint="/episode/print/<int:episode_id>",
                     methods=["GET"])