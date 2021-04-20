from http import HTTPStatus

from flask_jwt_extended import jwt_required

from . import (BaseView, DoctorModel, EpisodeModel, PatientModel,
               doctors_schema, episodes_schema, patients_schema)


class SuperUser(BaseView):
    def post(self):
        ...


class AllDoctors(BaseView):
    @jwt_required()
    def get(self):
        if self.get_type() != "superuser":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE

        all_doctors: DoctorModel = DoctorModel.query\
            .order_by(DoctorModel.id)\
            .paginate(page=self.page_pagination(),
                      per_page=self.per_page_pagination(),
                      error_out=False).items

        serializer = doctors_schema.dump(all_doctors)

        return {"message": "success", "data": serializer}, HTTPStatus.OK


class AllPatients(BaseView):
    @jwt_required()
    def get(self):
        if self.get_type() != "superuser":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE
        all_patients = PatientModel.query.\
            paginate(page=self.page_pagination(),
                     per_page=self.per_page_pagination(),
                     error_out=False).items

        serializer = patients_schema.dump(all_patients)
        return {"message": "success", "data": serializer}, HTTPStatus.OK


class AllEpisodes(BaseView):
    @jwt_required()
    def get(self):
        if self.get_type() != "superuser":
            return {"message": "Not Access"}, HTTPStatus.NOT_ACCEPTABLE
        all_episodes: EpisodeModel = EpisodeModel.query\
            .order_by(EpisodeModel.id)\
            .paginate(page=self.page_pagination(),
                      per_page=self.per_page_pagination,
                      error_out=False).items

        serializer = episodes_schema.dump(all_episodes)
        return {"message": "success", "data": serializer}, HTTPStatus.OK