from http import HTTPStatus

from flask_jwt_extended import jwt_required

from . import (BaseView, DoctorModel, EpisodeModel, PatientModel,
               doctors_schema, episodes_schema, patients_schema)


class AllDoctors(BaseView):
    @jwt_required()
    def get(self):
        if self.get_type() != "superuser":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE

        all_doctors: DoctorModel = DoctorModel.query.order_by(DoctorModel.id).all()
        serializer = doctors_schema.dump(all_doctors)

        return {"message": "success", "data": serializer}, HTTPStatus.OK


class AllPatients(BaseView):
    @jwt_required()
    def get(self):
        if self.get_type() != "superuser":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE
        all_patients = PatientModel.query.all()
        serializer = patients_schema.dump(all_patients)
        return {"message": "success", "data": serializer}, HTTPStatus.OK


class AllEpisodes(BaseView):
    @jwt_required()
    def get(self):
        if self.get_type() != "superuser":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE
        all_episodes: EpisodeModel = EpisodeModel.query.order_by(EpisodeModel.id).all()
        serializer = episodes_schema.dump(all_episodes)
        return {"message": "success", "data": serializer}, HTTPStatus.OK