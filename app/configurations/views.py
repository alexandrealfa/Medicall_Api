from flask import Flask
from flask_restful import Api


def init_app(app: Flask):
    api = Api(app)

    # Import views, and builds and resources
    from app.views.patient_view import Patients, AllPatients
    from app.views.doctor_view import Doctor, AllDoctors
    from app.views.episodes_view import (
        Episode,
        AllEpisodes,
        DoctorEpisodes,
        PatientEpisodes,
    )
    from app.views.access_view import SignIn

    api.add_resource(AllDoctors, "/doctors", endpoint="/doctors", methods=["GET"],)
    api.add_resource(Doctor, "/doctor", endpoint="/doctor", methods=["GET", "PATCH", "DELETE", "POST"],)

    api.add_resource(AllEpisodes, "/episodes", endpoint="/episodes", methods=["GET"],)
    api.add_resource(Episode, "/episode", endpoint="/episode", methods=["POST"],)
    api.add_resource(Episode,"/episode/<int:episode_id>",endpoint="/episode/<int:episode_id>",methods=["GET", "DELETE", "PATCH"],)
    api.add_resource(DoctorEpisodes, "/episodes/doctor/<int:doctor_id>", endpoint="/episodes/doctor/<int:doctor_id>", methods=["GET"],)
    api.add_resource(PatientEpisodes, "/episodes/patient/<int:patient_id>", endpoint="/episodes/patient/<int:patient_id>", methods=["GET"],)

    api.add_resource(AllPatients, "/patients", endpoint="/patients", methods=["GET"],)
    api.add_resource(Patients, "/patient", endpoint="/patient", methods=["GET", "POST", "PATCH", "DELETE"],)

    api.add_resource(SignIn, "/login", endpoint="/login", methods=["POST"],)