from flask import Blueprint, Flask, render_template, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.episode_model import EpisodeModel
from app.models.doctor_model import DoctorModel
from app.models.patient_model import PatientModel
import pdfkit

bp_download = Blueprint("bp_download", __name__)


@bp_download.route("/episode/print/<int:episode_id>", methods=["GET"])
@jwt_required()
def download(episode_id):
    id_user = int(tuple(get_jwt_identity().split(" "))[0])
    type_request = tuple(get_jwt_identity().split(" "))[1]
    episode: EpisodeModel = EpisodeModel.query.get_or_404(episode_id)
    doctor = DoctorModel.query.get_or_404(episode.doctor_id)
    patient = PatientModel.query.get_or_404(episode.patient_id)

    if type_request == "doctor" and episode.doctor_id == id_user:
        html = render_template("pdf_template.html",
                               name=patient.firstname,
                               email=patient.email,
                               phone=patient.phone,
                               doctor_name=doctor.firstname,
                               doctor_email=doctor.email,
                               description=episode.description,
                               emergency_status=episode.emergency_status.value,
                               created_at=episode.created_at
                               )

        pdf = pdfkit.from_string(html, False)

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

        return response

    elif type_request == "patient" and episode.patient_id == id_user:
        html = render_template("pdf_template.html",
                               name=patient.firstname,
                               email=patient.email,
                               phone=patient.phone,
                               doctor_name=doctor.firstname,
                               doctor_email=doctor.email,
                               description=episode.description,
                               emergency_status=episode.emergency_status.value,
                               created_at=episode.created_at
                               )

        pdf = pdfkit.from_string(html, False)

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

        return response


def bild_app(app: Flask):
    app.register_blueprint(bp_download)