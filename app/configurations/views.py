from flask import Flask
from flask_restful import Api


def init_app(app: Flask):
    api = Api(app)

    # Import views, and builds and resources
    from app.views.patient_view import Patients, AllPatients
    from app.views.doctor_view import Doctor, AllDoctors
    from app.views.episodes_view import Episode, AllEpisodes, DoctorEpisodes, PatientEpisodes

    api.add_resource(AllDoctors, "/api/doctors", endpoint="/api/doctors")
    api.add_resource(Doctor, "/api/doctors", endpoint="/api/doctor", methods=["POST"])
    api.add_resource(Doctor, "/api/doctors", endpoint="/api/doctor/<int:doctor_id>", methods=["GET", "PATCH", "DELETE"])

    api.add_resource(AllEpisodes, "/api/episodes", endpoint="api/episodes", methods=["GET"])
    api.add_resource(Episode, "/api/episode", endpoint="api/episode", methods=["POST"])
    api.add_resource(Episode, "/api/episode/<int:episode_id>", endpoint="api/episode/<int:episode_id>", methods=["GET", "DELETE", "PATCH"])
    api.add_resource(DoctorEpisodes, "/api/episodes/doctor/<int:doctor_id>", endpoint="/api/episodes/doctor/<int:doctor_id>", methods=["GET"])
    api.add_resource(PatientEpisodes, "/api/episodes/patient/<int:patient_id>", endpoint="/api/episodes/patient/<int:patient_id>", methods=["GET"])


    api.add_resource(AllPatients, "/api/patients", endpoint="/api/patients", methods=["GET"])
    api.add_resource(Patients, "/api/patient", endpoint="/api/patient/", methods=["POST"])
    api.add_resource(Patients, "/api/patient/<int:patient_id>", endpoint="/api/patient/<int:patient_id>", methods=[
        "GET", "PATCH", "DELETE"])

