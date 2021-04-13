from flask import Flask
from flask_restful import Api


def init_app(app: Flask):
    api = Api(app)

    # Import views, and builds and resources
    from app.views.patient_view import Patients, AllPatients
    from app.views.doctor_view import Doctor, AllDoctors

    api.add_resource(AllDoctors, "/api/doctors", endpoint="/api/doctors")
    api.add_resource(Doctor, "/api/doctors", endpoint="/api/doctor", methods=["POST"])
    api.add_resource(Doctor, "/api/doctors", endpoint="/api/doctor/<int:doctor_id>", methods=["GET", "PATCH", "DELETE"])

    api.add_resource(AllPatients, "/api/patients", endpoint="/api/patients", methods=["GET"])
    api.add_resource(Patients, "/api/patients", endpoint="/api/patient/", methods=["POST"])
    api.add_resource(Patients, "/api/patients", endpoint="api/patient/<int:patient_id>", methods=["GET", "PATCH", "DELETE"])