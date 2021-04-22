from .base_view import BaseView
from flask_jwt_extended import jwt_required
from . import EpisodeModel, DoctorModel, PatientModel


class PrintEpisode(BaseView):
    @jwt_required()
    def get(self, episode_id):
        id_user = self.get_id()
        type_request = self.get_type()
        episode: EpisodeModel = EpisodeModel.query.get_or_404(episode_id)
        doctor = DoctorModel.query.get_or_404(episode.doctor_id)
        patient = PatientModel.query.get_or_404(episode.patient_id)

        if type_request == "doctor" and episode.doctor_id == id_user:
            self.pdf_template(patient.name,
                              patient.email,
                              patient.phone,
                              doctor.name,
                              doctor.email,
                              episode.description,
                              episode.emergency_status,
                              episode.created_at
                              )

        elif type_request == "patient" and episode.patient_id == id_user:
            self.pdf_template(patient.name,
                              patient.email,
                              patient.phone,
                              doctor.name,
                              doctor.email,
                              episode.description,
                              episode.emergency_status,
                              episode.created_at
                              )
